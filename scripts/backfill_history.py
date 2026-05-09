#!/usr/bin/env python3
"""
Walk every release source folder under X:/games/Oscuro/ and ingest each one
in chronological order, producing one commit + one tag per release.

Main-line strategy:
  1. Discover all `Oscuro's_..._alphaXX` directories (skipping `.7z` / `.zip`
     siblings and any non-directory entries).
  2. Sort: alpha00-premerge first, then alpha01, alpha02, ..., alpha90.
     Numeric gaps (alpha55, alpha56, alpha72) are simply absent — that's fine.
  3. For each, if the tag already exists, skip. Otherwise call
     `ingest_release.py` to copy → manifest → commit → tag.

Variants (alpha32nex):
  After the main line is fully ingested, switch to a branch off `alpha32`
  named `alpha32nex` and ingest the variant there, then return to `main`.

Resumability:
  Re-running the script after an interruption skips already-tagged releases
  and continues from where it left off. Use `--force-from <tag>` to re-do
  a contiguous tail of the history (deletes those tags first).

Usage:
    python scripts/backfill_history.py             # ingest everything new
    python scripts/backfill_history.py --dry-run   # show plan, do nothing
    python scripts/backfill_history.py --limit 5   # only ingest first 5 missing
    python scripts/backfill_history.py --skip-variants
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_ROOT = Path(r"X:/games/Oscuro")
SOURCE_PREFIX = "Oscuro's_Oblivion_Remastered_Shivering_Full_"

# alpha00_preMerge → ("alpha", 0, "premerge"); alpha32nex → ("alpha", 32, "nex");
# alpha37 → ("alpha", 37, "")
_FOLDER_RE = re.compile(r"^(alpha)(\d+)(?:_?([A-Za-z][A-Za-z0-9]*))?$")


@dataclass(frozen=True)
class Release:
    folder: Path
    name: str       # tag name, e.g. "alpha00-premerge", "alpha32nex", "alpha37"
    series: str     # "alpha"
    number: int     # 0, 32, 37
    variant: str    # "" for main-line, "premerge"/"nex"/etc. for variants

    @property
    def is_variant(self) -> bool:
        # alpha00-premerge counts as MAIN-LINE because it's the chronological
        # start with no main-line ancestor; only alpha32nex and similar parallel
        # branches count as variants.
        return self.variant != "" and self.variant != "premerge"

    @property
    def parent_tag(self) -> str | None:
        """For variants, the main-line tag this variant should fork from."""
        if not self.is_variant:
            return None
        return f"{self.series}{self.number:02d}"


def parse_release_folder(folder: Path) -> Release | None:
    if not folder.is_dir():
        return None
    if not folder.name.startswith(SOURCE_PREFIX):
        return None
    suffix = folder.name[len(SOURCE_PREFIX):]
    m = _FOLDER_RE.match(suffix)
    if not m:
        return None
    series, num_str, variant = m.group(1), m.group(2), (m.group(3) or "").lower()
    number = int(num_str)
    if variant == "premerge":
        name = f"{series}{number:02d}-premerge"
    elif variant:
        name = f"{series}{number:02d}{variant}"
    else:
        name = f"{series}{number:02d}"
    return Release(folder=folder, name=name, series=series, number=number, variant=variant)


def discover_releases() -> list[Release]:
    out: list[Release] = []
    for child in SOURCE_ROOT.iterdir():
        r = parse_release_folder(child)
        if r is not None:
            out.append(r)
    # Sort: main-line variants by (number, variant); premerge sorts before
    # alphaNN by giving "premerge" an empty variant key trick:
    # main entries get variant_key=0; premerge gets variant_key=-1; other
    # variants get variant_key=1+.
    def key(r: Release):
        if r.variant == "":
            return (r.number, 0, "")
        if r.variant == "premerge":
            return (r.number, -1, r.variant)
        return (r.number, 1, r.variant)
    return sorted(out, key=key)


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT, capture_output=True, text=True, check=check,
    )


def tag_exists(tag: str) -> bool:
    return git("rev-parse", "--verify", "--quiet", f"refs/tags/{tag}", check=False).returncode == 0


def current_branch() -> str:
    return git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()


def ingest_one(folder: Path, force: bool = False) -> int:
    cmd = [sys.executable, "scripts/ingest_release.py", str(folder)]
    if force:
        cmd.append("--force")
    print(f"[backfill] -> {' '.join(cmd)}", flush=True)
    r = subprocess.run(cmd, cwd=REPO_ROOT)
    return r.returncode


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="print the plan, do nothing")
    ap.add_argument("--limit", type=int, default=0, help="ingest at most N missing releases (0 = all)")
    ap.add_argument("--skip-variants", action="store_true", help="skip alpha32nex etc.")
    ap.add_argument("--force-from", help="delete and re-ingest this tag and everything after it")
    args = ap.parse_args()

    if not SOURCE_ROOT.is_dir():
        raise SystemExit(f"source root not found: {SOURCE_ROOT}")

    if current_branch() != "main":
        raise SystemExit(f"refusing to backfill from non-main branch: {current_branch()}")

    all_releases = discover_releases()
    main_line = [r for r in all_releases if not r.is_variant]
    variants = [r for r in all_releases if r.is_variant]

    print(f"[backfill] discovered {len(main_line)} main-line releases, "
          f"{len(variants)} variant(s)", flush=True)

    # --force-from: delete tag and everything after it (main line only)
    if args.force_from:
        from_idx = next((i for i, r in enumerate(main_line) if r.name == args.force_from), None)
        if from_idx is None:
            raise SystemExit(f"--force-from: tag {args.force_from!r} not in discovered main line")
        # Reset main to the parent of the from-tag (or root if it's the first)
        if from_idx == 0:
            raise SystemExit("--force-from on the very first release would orphan the repo. Bailing.")
        parent = main_line[from_idx - 1].name
        print(f"[backfill] --force-from {args.force_from}: resetting main to {parent}", flush=True)
        if not args.dry_run:
            git("reset", "--hard", parent)
            for r in main_line[from_idx:]:
                if tag_exists(r.name):
                    git("tag", "-d", r.name)

    # Plan main-line work
    main_todo = [r for r in main_line if not tag_exists(r.name)]
    if args.limit > 0:
        main_todo = main_todo[: args.limit]

    print(f"[backfill] {len(main_todo)} main-line release(s) to ingest", flush=True)
    for r in main_todo:
        print(f"           - {r.name}", flush=True)

    # Plan variants
    variant_todo: list[Release] = []
    if not args.skip_variants:
        for v in variants:
            if tag_exists(v.name):
                continue
            if v.parent_tag is None or not tag_exists(v.parent_tag):
                # Parent main-line tag doesn't exist yet (it'll be created in this run
                # if v.parent_tag is in main_todo; if it's neither, skip with warning).
                if v.parent_tag and v.parent_tag in {r.name for r in main_todo}:
                    variant_todo.append(v)
                else:
                    print(f"[backfill] WARN: variant {v.name} has no parent {v.parent_tag} — skipping",
                          file=sys.stderr, flush=True)
            else:
                variant_todo.append(v)
        print(f"[backfill] {len(variant_todo)} variant(s) to ingest", flush=True)
        for v in variant_todo:
            print(f"           - {v.name} (off {v.parent_tag})", flush=True)

    if args.dry_run:
        print("[backfill] --dry-run: stopping here", flush=True)
        return 0

    # Execute main-line ingest
    for r in main_todo:
        rc = ingest_one(r.folder)
        if rc != 0:
            print(f"[backfill] ABORT: ingest of {r.name} failed (rc={rc})", file=sys.stderr)
            return rc

    # Execute variant ingest
    for v in variant_todo:
        parent = v.parent_tag
        assert parent is not None
        if not tag_exists(parent):
            print(f"[backfill] WARN: parent tag {parent} missing, skipping variant {v.name}",
                  file=sys.stderr, flush=True)
            continue
        # Branches go under `variants/` so they don't collide with the
        # same-named tag (git emits an "ambiguous refname" warning otherwise).
        branch_name = f"variants/{v.name}"
        # Create branch off the parent tag if it doesn't exist
        r = git("rev-parse", "--verify", "--quiet", f"refs/heads/{branch_name}", check=False)
        if r.returncode != 0:
            print(f"[backfill] creating branch {branch_name} from tag {parent}", flush=True)
            git("checkout", "-b", branch_name, parent)
        else:
            print(f"[backfill] checking out existing branch {branch_name}", flush=True)
            git("checkout", branch_name)
        rc = ingest_one(v.folder)
        if rc != 0:
            print(f"[backfill] ABORT: ingest of variant {v.name} failed (rc={rc})", file=sys.stderr)
            git("checkout", "main")
            return rc
        git("checkout", "main")
        print(f"[backfill] returned to main after variant {v.name}", flush=True)

    print("[backfill] done.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
