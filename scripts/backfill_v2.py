#!/usr/bin/env python3
"""
One-shot historical rebuild for the v2 architecture.

Walks every alpha source folder under X:\\games\\Oscuro\\ in chronological
order. For each, it:

  1. Wipes release/ (preserving .gitkeep).
  2. Copies the source folder's content into release/ (text + binaries —
     binaries stay because they're physically present and need to be in
     the manifest, even though they're gitignored from commit).
  3. Hashes release/ → manifests/<tag>.json (excludes co-files + .records/).
  4. Parses every ESP/ESM in release/ → writes .records/ inventory bundles.
  5. Updates each binary's .md co-file with this tag's row (URL points at
     the canonical GitHub Release URL — these archives were published in
     v1 and remain valid).
  6. Diffs vs the prior tag's manifest + ESP inventories → writes
     docs/per-release/<tag>.md.
  7. git add + commit (subject = tag) + git tag <tag>.

NOTE: this script does NOT rebuild dist/<tag>.7z (those already exist
from v1's prebuild; per resolved decision #5 they don't need to be
re-uploaded — the .md tracks per-binary SHAs which are invariant across
packaging). Pass --rebuild-archives to rebuild them anyway.

Variants: after the main line is done, switches to `variants/alpha32nex`
branched off the alpha32 tag, ingests the variant, returns to main.

Usage:
    py -3 scripts/backfill_v2.py             # full backfill
    py -3 scripts/backfill_v2.py --dry-run   # plan only
    py -3 scripts/backfill_v2.py --limit 5   # ingest at most 5 missing tags
    py -3 scripts/backfill_v2.py --skip-variants
    py -3 scripts/backfill_v2.py --rebuild-archives
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RELEASE_DIR = REPO_ROOT / "release"
MANIFEST_DIR = REPO_ROOT / "manifests"
PER_RELEASE_DOC_DIR = REPO_ROOT / "docs" / "per-release"
DIST_DIR = REPO_ROOT / "dist"

SOURCE_ROOT = Path(r"X:/games/Oscuro")
SOURCE_PREFIX = "Oscuro's_Oblivion_Remastered_Shivering_Full_"

# alpha37 → ('alpha', 37, ''), alpha32nex → ('alpha', 32, 'nex'),
# alpha00_preMerge → ('alpha', 0, 'premerge')
_FOLDER_RE = re.compile(r"^(alpha)(\d+)(?:_?([A-Za-z][A-Za-z0-9]*))?$")


@dataclass(frozen=True)
class Release:
    folder: Path
    name: str       # tag, e.g. alpha37 / alpha00-premerge / alpha32nex
    series: str
    number: int
    variant: str    # '' for main-line; 'premerge' is treated as main-line; others are variants

    @property
    def is_variant(self) -> bool:
        return self.variant != "" and self.variant != "premerge"

    @property
    def parent_tag(self) -> str | None:
        if not self.is_variant:
            return None
        return f"{self.series}{self.number:02d}"


# --------------------------------------------------------------------------- #
# Helpers (lifted from release.py / used in-process for speed)
# --------------------------------------------------------------------------- #

sys.path.insert(0, str(REPO_ROOT / "scripts"))
from release import (  # noqa: E402
    BINARY_EXTS,
    iter_release_files,
    iter_release_binaries,
    iter_release_esps,
    git,
    tag_exists,
)


def parse_release_folder(folder: Path) -> Release | None:
    if not folder.is_dir() or not folder.name.startswith(SOURCE_PREFIX):
        return None
    suffix = folder.name[len(SOURCE_PREFIX):]
    m = _FOLDER_RE.match(suffix)
    if not m:
        return None
    series = m.group(1)
    number = int(m.group(2))
    variant = (m.group(3) or "").lower()
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

    def sort_key(r: Release):
        if r.variant == "":
            return (r.number, 0, "")
        if r.variant == "premerge":
            return (r.number, -1, r.variant)
        return (r.number, 1, r.variant)

    return sorted(out, key=sort_key)


# --------------------------------------------------------------------------- #
# Per-release ingest
# --------------------------------------------------------------------------- #

def wipe_release_dir() -> None:
    if not RELEASE_DIR.exists():
        RELEASE_DIR.mkdir(parents=True)
        return
    for child in RELEASE_DIR.iterdir():
        if child.name == ".gitkeep":
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def copy_source_into_release(source: Path) -> int:
    count = 0
    for src in source.rglob("*"):
        if not src.is_file():
            continue
        rel = src.relative_to(source)
        dst = RELEASE_DIR / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        count += 1
    return count


def hash_release_dir() -> dict[str, dict]:
    """Walk release/ excluding co-files + .records/; return {posix_relpath:
    {sha256, size}} sorted by path."""
    manifest: dict[str, dict] = {}
    for p in iter_release_files(RELEASE_DIR):
        rel = p.relative_to(RELEASE_DIR).as_posix()
        sha = hashlib.sha256(p.read_bytes()).hexdigest()
        manifest[rel] = {"sha256": sha, "size": p.stat().st_size}
    return dict(sorted(manifest.items()))


def write_manifest(manifest: dict[str, dict], tag: str) -> Path:
    out = MANIFEST_DIR / f"{tag}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8")
    return out


def build_esp_inventories() -> list[Path]:
    from build_records import write_inventory  # noqa: E402
    esps = list(iter_release_esps(RELEASE_DIR))
    for esp in esps:
        write_inventory(esp)
    return esps


def update_binary_cofiles(tag: str, manifest: dict[str, dict]) -> int:
    from update_cofile import update_cofile  # noqa: E402
    count = 0
    for p in iter_release_binaries(RELEASE_DIR):
        rel = p.relative_to(RELEASE_DIR).as_posix()
        entry = manifest.get(rel)
        if entry is None:
            continue
        update_cofile(p, tag=tag, sha=entry["sha256"], size=entry["size"])
        count += 1
    return count


def write_per_release_doc(tag: str, prev_tag: str | None,
                          manifest: dict[str, dict],
                          esp_paths: list[Path]) -> Path:
    sections: list[str] = [f"# {tag} — release notes\n"]
    if prev_tag is None:
        sections.append("_Initial release in v2 layout._\n")
    else:
        sections.append(f"_Compared against `{prev_tag}`._\n")

    # File-level diff
    if prev_tag:
        prev_path = MANIFEST_DIR / f"{prev_tag}.json"
        if prev_path.exists():
            prev_manifest = json.loads(prev_path.read_text(encoding="utf-8"))
            added = sorted(set(manifest) - set(prev_manifest))
            removed = sorted(set(prev_manifest) - set(manifest))
            changed = sorted(k for k in set(manifest) & set(prev_manifest)
                             if manifest[k]["sha256"] != prev_manifest[k]["sha256"])
            sections.append(f"## File-level changes\n\n"
                            f"- Added: {len(added)}\n- Removed: {len(removed)}\n- Changed: {len(changed)}\n")
            for label, items in (("Added", added), ("Removed", removed), ("Changed", changed)):
                if items:
                    sections.append(f"### {label}\n")
                    for it in items[:50]:
                        sections.append(f"- `{it}`")
                    if len(items) > 50:
                        sections.append(f"_…{len(items) - 50} more {label.lower()} omitted_")
                    sections.append("")

    # Per-ESP content diffs
    if esp_paths:
        from diff_records import render_diff  # noqa: E402
        import tempfile
        for esp in esp_paths:
            curr = esp.parent / f"{esp.name}.records"
            if not curr.is_dir():
                continue
            prev_records: Path | None = None
            if prev_tag:
                rel = curr.relative_to(REPO_ROOT).as_posix()
                ls = git("ls-tree", "-r", prev_tag, rel, check=False)
                if ls.returncode == 0 and ls.stdout.strip():
                    tmp = Path(tempfile.mkdtemp(prefix="prev_records_"))
                    for line in ls.stdout.splitlines():
                        if "\t" not in line:
                            continue
                        _meta, path = line.split("\t", 1)
                        if not path.endswith(".json"):
                            continue
                        sub = path[len(rel) + 1:] if path.startswith(rel + "/") else None
                        if sub is None:
                            continue
                        show = git("show", f"{prev_tag}:{path}", check=False)
                        if show.returncode != 0:
                            continue
                        out_file = tmp / sub
                        out_file.parent.mkdir(parents=True, exist_ok=True)
                        out_file.write_text(show.stdout, encoding="utf-8")
                    if any(tmp.iterdir()):
                        prev_records = tmp
            md = render_diff(prev_records, curr,
                             esp_name=esp.name, max_per_section=20)
            sections.append(md)

    out_text = "\n".join(sections) + "\n"
    out_path = PER_RELEASE_DOC_DIR / f"{tag}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(out_text, encoding="utf-8")
    return out_path


def commit_and_tag(tag: str) -> None:
    subprocess.run(["git", "add", "-A", "release/", "manifests/",
                    "docs/per-release/"],
                   cwd=REPO_ROOT, check=True)
    try:
        subprocess.run(["git", "commit", "-m", tag], cwd=REPO_ROOT,
                       check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        if "nothing to commit" in (e.stdout or "") + (e.stderr or ""):
            pass  # tree identical to prior commit (rare but possible)
        else:
            raise
    subprocess.run(["git", "tag", tag], cwd=REPO_ROOT, check=True)


def rebuild_archive(tag: str) -> Path:
    sevenz = shutil.which("7z") or shutil.which("7z.exe")
    if not sevenz:
        raise SystemExit("7z not on PATH")
    out = DIST_DIR / f"{tag}.7z"
    if out.exists():
        out.unlink()
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    cmd = [sevenz, "a", "-t7z", "-mx=9", "-m0=lzma2", "-ms=on", "-mmt=on",
           "-xr!*.md", "-xr!*.records", "-xr!.gitkeep",
           str(out), f"{RELEASE_DIR.as_posix()}/*"]
    r = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stdout + r.stderr)
        raise SystemExit(f"7z exited {r.returncode}")
    return out


def latest_main_tag(exclude: str) -> str | None:
    r = git("tag", "--merged", "HEAD", "--sort=v:refname", check=False)
    if r.returncode != 0:
        return None
    tags = [t.strip() for t in r.stdout.splitlines()
            if t.strip() and t.strip() != exclude]
    return tags[-1] if tags else None


def ingest_one(release: Release, rebuild_archives: bool) -> None:
    print(f"  [ingest] {release.name} ← {release.folder.name}", flush=True)
    prev_tag = latest_main_tag(exclude=release.name)

    wipe_release_dir()
    n_copied = copy_source_into_release(release.folder)
    print(f"    copied {n_copied} files", flush=True)

    manifest = hash_release_dir()
    write_manifest(manifest, release.name)
    print(f"    manifests/{release.name}.json: {len(manifest)} entries", flush=True)

    esps = build_esp_inventories()
    print(f"    parsed {len(esps)} ESP/ESMs", flush=True)

    n_cofiles = update_binary_cofiles(release.name, manifest)
    print(f"    updated {n_cofiles} co-files", flush=True)

    write_per_release_doc(release.name, prev_tag, manifest, esps)

    if rebuild_archives:
        archive = rebuild_archive(release.name)
        print(f"    archive: {archive}", flush=True)

    commit_and_tag(release.name)
    print(f"    tagged {release.name}", flush=True)


# --------------------------------------------------------------------------- #
# Top-level
# --------------------------------------------------------------------------- #

def current_branch() -> str:
    return git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()


def main() -> int:
    # Force UTF-8 stdout so unicode arrows in our log messages render
    # correctly when the Windows console default is cp1252.
    for stream in (sys.stdout, sys.stderr):
        if isinstance(stream, io.TextIOWrapper):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="print plan, no changes")
    ap.add_argument("--limit", type=int, default=0,
                    help="ingest at most N missing tags (0 = all)")
    ap.add_argument("--skip-variants", action="store_true")
    ap.add_argument("--rebuild-archives", action="store_true",
                    help="rebuild dist/<tag>.7z for each ingested tag (default: skip)")
    args = ap.parse_args()

    if not SOURCE_ROOT.is_dir():
        raise SystemExit(f"source root not found: {SOURCE_ROOT}")
    if current_branch() != "main":
        raise SystemExit(f"refusing to backfill from non-main branch: {current_branch()}")

    all_releases = discover_releases()
    main_line = [r for r in all_releases if not r.is_variant]
    variants = [r for r in all_releases if r.is_variant]

    main_todo = [r for r in main_line if not tag_exists(r.name)]
    if args.limit > 0:
        main_todo = main_todo[: args.limit]

    print(f"[backfill] discovered {len(main_line)} main + {len(variants)} variants")
    print(f"           {len(main_todo)} main-line tags to ingest")
    for r in main_todo:
        print(f"           - {r.name}")
    if not args.skip_variants:
        for v in variants:
            if tag_exists(v.name):
                continue
            print(f"           - {v.name} (variant off {v.parent_tag})")

    if args.dry_run:
        print("[backfill] --dry-run: stopping here")
        return 0

    # Main line
    for r in main_todo:
        ingest_one(r, args.rebuild_archives)

    # Variants
    if not args.skip_variants:
        for v in variants:
            if tag_exists(v.name):
                continue
            parent = v.parent_tag
            if parent is None or not tag_exists(parent):
                print(f"[backfill] WARN: variant {v.name} parent {parent} missing; skip",
                      file=sys.stderr)
                continue
            branch_name = f"variants/{v.name}"
            r = git("rev-parse", "--verify", "--quiet", f"refs/heads/{branch_name}",
                    check=False)
            if r.returncode != 0:
                git("checkout", "-b", branch_name, parent)
            else:
                git("checkout", branch_name)
            ingest_one(v, args.rebuild_archives)
            git("checkout", "main")

    print("[backfill] done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
