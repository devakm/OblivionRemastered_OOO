#!/usr/bin/env python3
"""
Ingest one release source folder into this repo (Releases-for-Assets architecture).

Per release this produces:
  - manifests/<name>.json        — SHA-256 + size for every file in the source
  - docs/per-release/<name>.md   — added/removed/changed vs prior release
  - release/...                  — TEXT files only from the source tree (json/ini/lua/md/txt/etc.)
  - dist/<name>.7z               — full source tree (text + binary), produced once,
                                    NOT committed (gitignored), uploaded as a GitHub Release asset.

The text-only release/ commit gives `git diff alpha75..alpha90 -- release/` line-level
diffs of MagicLoader JSON, SyncMap INI, Lua scripts, etc. The .7z attached to the
matching GitHub Release carries the binaries (paks, ESPs, DLLs).

Steps:
  1. Hash the source folder directly → write manifests/<name>.json.
  2. Diff vs previous tag's manifest → write docs/per-release/<name>.md.
  3. Wipe release/ and copy only text files from source into release/.
  4. Build dist/<name>.7z directly from the source folder.
  5. git add release/ + manifests/ + docs/per-release/, commit, tag.

Idempotency:
  - If the tag already exists, abort unless --force.
  - Re-running with --force deletes the tag and the prior dist archive, then re-creates both.

Usage:
    python scripts/ingest_release.py "X:/games/Oscuro/Oscuro's_..._alpha37"
    python scripts/ingest_release.py <source> --name alpha37
    python scripts/ingest_release.py <source> --force
    python scripts/ingest_release.py <source> --no-commit
    python scripts/ingest_release.py <source> --skip-archive  # don't build .7z
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RELEASE_DIR = REPO_ROOT / "release"
MANIFEST_DIR = REPO_ROOT / "manifests"
PER_RELEASE_DOC_DIR = REPO_ROOT / "docs" / "per-release"
DIST_DIR = REPO_ROOT / "dist"

RELEASE_SOURCE_ROOTS = (
    Path(r"X:/games/Oscuro"),
)

# Files matching these extensions are committed into release/. Everything else
# stays out of git (it lives in the .7z attached to the GitHub Release instead).
TEXT_EXTS = frozenset({
    ".json", ".ini", ".lua", ".md", ".txt",
    ".html", ".css", ".py", ".cfg", ".xml",
    ".csv", ".yaml", ".yml", ".toml",
})

NAME_RE = re.compile(r"_(alpha\d+(?:[a-z][a-z0-9]*)?(?:_[A-Za-z]+)*)$")


def parse_release_name(source: Path) -> str:
    m = NAME_RE.search(source.name)
    if not m:
        raise SystemExit(f"cannot infer release name from folder: {source.name!r}")
    name = m.group(1)
    if "_" in name:
        head, _, tail = name.partition("_")
        name = f"{head}-{tail.lower()}"
    return name


def assert_under_known_source_root(source: Path) -> None:
    s = source.resolve()
    for root in RELEASE_SOURCE_ROOTS:
        try:
            s.relative_to(root.resolve())
            return
        except ValueError:
            continue
    raise SystemExit(
        f"refusing to ingest from unknown source root: {source}\n"
        f"known roots: {', '.join(str(r) for r in RELEASE_SOURCE_ROOTS)}"
    )


def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=True, cwd=REPO_ROOT, capture_output=True, text=True, **kwargs)


def git_tag_exists(tag: str) -> bool:
    r = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"refs/tags/{tag}"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    return r.returncode == 0


def git_working_tree_clean_outside(allowed_prefixes: tuple[str, ...]) -> bool:
    r = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    )
    for line in r.stdout.splitlines():
        if len(line) < 4:
            continue
        path = line[3:].strip().strip('"')
        if not any(path.startswith(p) for p in allowed_prefixes):
            return False
    return True


def wipe_release_dir() -> None:
    if RELEASE_DIR.exists():
        for child in RELEASE_DIR.iterdir():
            if child.name == ".gitkeep":
                continue
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    else:
        RELEASE_DIR.mkdir(parents=True)


def copy_text_files_to_release(source: Path) -> int:
    """Copy only text files (by extension) from source → release/. Returns count."""
    count = 0
    for src in source.rglob("*"):
        if not src.is_file():
            continue
        if src.suffix.lower() not in TEXT_EXTS:
            continue
        rel = src.relative_to(source)
        dst = RELEASE_DIR / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        count += 1
    return count


def find_7z() -> str:
    exe = shutil.which("7z") or shutil.which("7z.exe")
    if not exe:
        raise SystemExit("7z not found on PATH. Install 7-Zip and retry.")
    return exe


def build_archive(source: Path, output: Path) -> None:
    """7zip the full source tree (text + binary) into output, contents at archive root."""
    if output.exists():
        output.unlink()
    output.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        find_7z(), "a", "-t7z", "-mx=9", "-m0=lzma2", "-ms=on", "-mmt=on",
        "-xr!.gitkeep",
        str(output),
        f"{source.as_posix()}/*",
    ]
    r = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stdout + r.stderr)
        raise SystemExit(f"7z exited {r.returncode}")


def find_previous_manifest(curr_name: str) -> Path | None:
    r = subprocess.run(
        ["git", "tag", "--sort=-creatordate", "--merged", "HEAD"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    )
    for tag in r.stdout.splitlines():
        tag = tag.strip()
        if not tag or tag == curr_name:
            continue
        candidate = MANIFEST_DIR / f"{tag}.json"
        if candidate.exists():
            return candidate
    return None


def ingest(source: Path, name: str | None, force: bool, no_commit: bool, skip_archive: bool) -> int:
    assert_under_known_source_root(source)
    if not source.is_dir():
        raise SystemExit(f"source is not a directory: {source}")

    release_name = name or parse_release_name(source)
    print(f"[ingest] release name: {release_name}", file=sys.stderr)

    if not git_working_tree_clean_outside(("release/", "manifests/", "docs/per-release/")):
        raise SystemExit(
            "working tree has uncommitted changes outside release/, manifests/, "
            "docs/per-release/. Commit or stash them first."
        )

    if git_tag_exists(release_name):
        if not force:
            raise SystemExit(
                f"tag {release_name!r} already exists. Pass --force to re-ingest."
            )
        print(f"[ingest] --force: deleting existing tag {release_name}", file=sys.stderr)
        run(["git", "tag", "-d", release_name])

    # Lazy-import sibling scripts.
    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    from build_manifest import build_manifest  # noqa: E402
    from diff_releases import diff_manifests, render_markdown, load_manifest  # noqa: E402

    # 1. Hash the source folder directly into a manifest.
    print(f"[ingest] hashing {source}", file=sys.stderr)
    manifest = build_manifest(source)

    # 2. Write manifest.
    manifest_path = MANIFEST_DIR / f"{release_name}.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"[ingest] wrote {manifest_path} ({len(manifest)} files)", file=sys.stderr)

    # 3. Diff vs previous, write per-release doc.
    prev_manifest_path = find_previous_manifest(release_name)
    prev_manifest = load_manifest(prev_manifest_path) if prev_manifest_path else None
    diff = diff_manifests(prev_manifest, manifest)
    prev_name = prev_manifest_path.stem if prev_manifest_path else None
    doc_md = render_markdown(diff, prev_name, release_name, manifest)
    doc_path = PER_RELEASE_DOC_DIR / f"{release_name}.md"
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    doc_path.write_text(doc_md, encoding="utf-8")
    print(
        f"[ingest] wrote {doc_path} (+{len(diff.added)} -{len(diff.removed)} ~{len(diff.changed)})",
        file=sys.stderr,
    )

    # 4. Wipe release/ and copy text files only.
    wipe_release_dir()
    text_count = copy_text_files_to_release(source)
    print(f"[ingest] copied {text_count} text files to release/", file=sys.stderr)

    # 5. Build dist/<name>.7z from the full source tree.
    if skip_archive:
        print("[ingest] --skip-archive: not building .7z", file=sys.stderr)
    else:
        archive = DIST_DIR / f"{release_name}.7z"
        if archive.exists() and archive.stat().st_size > 0 and not force:
            print(
                f"[ingest] {archive} already exists ({archive.stat().st_size // (1024*1024)} MiB), "
                f"skipping rebuild (pass --force to rebuild)",
                file=sys.stderr,
            )
        else:
            print(f"[ingest] building {archive}", file=sys.stderr)
            build_archive(source, archive)
            print(f"[ingest] archive: {archive.stat().st_size // (1024*1024)} MiB", file=sys.stderr)

    if no_commit:
        print("[ingest] --no-commit: stopping before git commit", file=sys.stderr)
        return 0

    # 6. Commit + tag.
    run(["git", "add", "-A", "release/", "manifests/", "docs/per-release/"])
    body = (
        f"Ingested from: {source}\n\n"
        f"Files in source: {len(manifest)} | "
        f"Text in repo: {text_count} | "
        f"Added: {len(diff.added)} | "
        f"Removed: {len(diff.removed)} | "
        f"Changed: {len(diff.changed)}\n\n"
        f"Per-release diff: docs/per-release/{release_name}.md\n"
        f"Install archive: dist/{release_name}.7z (built locally; "
        f"upload as GitHub Release asset via publish_github.py)"
    )
    commit_msg = f"{release_name}\n\n{body}"
    try:
        run(["git", "commit", "-m", commit_msg])
    except subprocess.CalledProcessError as e:
        if "nothing to commit" in (e.stdout or "") + (e.stderr or ""):
            print("[ingest] tree identical to previous release — no commit", file=sys.stderr)
        else:
            raise
    run(["git", "tag", release_name])
    print(f"[ingest] tagged {release_name}", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source", type=Path, help="path to a release source folder")
    ap.add_argument("--name", help="explicit release name (default: derived from folder)")
    ap.add_argument("--force", action="store_true", help="overwrite existing tag")
    ap.add_argument("--no-commit", action="store_true", help="stage files but don't commit/tag")
    ap.add_argument("--skip-archive", action="store_true", help="don't build dist/<name>.7z")
    args = ap.parse_args()
    return ingest(args.source, args.name, args.force, args.no_commit, args.skip_archive)


if __name__ == "__main__":
    raise SystemExit(main())
