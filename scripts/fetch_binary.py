#!/usr/bin/env python3
"""
Fetch a binary that shipped with a historical release, using its `.md`
co-file as the index pointing at the GitHub Release asset.

Workflow per fetch:
  1. Locate the binary's sibling `.md` co-file.
  2. Find the row for the requested tag → pull Download URL + expected
     short SHA-256.
  3. Download the matching `.7z` to `work/_release_cache/<tag>.7z`
     (cached — repeated fetches in the same tag re-use the download).
  4. Extract just the requested file from inside the `.7z` to either:
        - default: `work/historical/<tag>/<original-relative-path>`
        - `--into-place`: overwrite the working-tree binary directly
        - `--out`: explicit destination
  5. Verify the extracted file's SHA-256 starts with the expected
     12-char prefix from the `.md`. Bail loudly on mismatch.

Usage:
    py -3 scripts/fetch_binary.py --tag alpha75 \\
           release/.../Oscuro's_Oblivion_Overhaul.esp

    py -3 scripts/fetch_binary.py --tag alpha75 --all          # every binary
    py -3 scripts/fetch_binary.py --tag alpha75 --all --list   # show plan only
    py -3 scripts/fetch_binary.py --tag alpha75 <bin> --into-place
    py -3 scripts/fetch_binary.py --tag alpha75 <bin> --out <dst>
"""

from __future__ import annotations

import argparse
import hashlib
import io
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RELEASE_DIR = REPO_ROOT / "release"
CACHE_DIR = REPO_ROOT / "work" / "_release_cache"
HISTORICAL_DIR = REPO_ROOT / "work" / "historical"


# Same row regex as update_cofile so we can read the .md table consistently.
ROW_RE = re.compile(
    r"^\|\s*(?P<release>[^|]+?)\s*\|\s*`?(?P<sha>[^|`]+?)`?\s*\|"
    r"\s*(?P<size>[^|]+?)\s*\|\s*(?P<changed>[^|]*?)\s*\|"
    r"\s*(?P<descr>[^|]*?)\s*\|\s*(?P<download>[^|]*?)\s*\|\s*$"
)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def _parse_cofile(cofile: Path) -> list[dict]:
    """Return a list of {tag, sha_short, size_str, descr_url, download_url,
    asset_name} dicts from a .md co-file."""
    rows: list[dict] = []
    if not cofile.is_file():
        return rows
    for line in cofile.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        # Extract the URL from the Download cell (markdown link form).
        dl_md = m.group("download").strip()
        dl_match = LINK_RE.search(dl_md)
        descr_md = m.group("descr").strip()
        descr_match = LINK_RE.search(descr_md)
        if not dl_match:
            continue
        rows.append({
            "tag": m.group("release").strip(),
            "sha_short": m.group("sha").strip("`").strip(),
            "size_str": m.group("size").strip(),
            "asset_name": dl_match.group(1).strip(),
            "download_url": dl_match.group(2).strip(),
            "descr_url": descr_match.group(2).strip() if descr_match else None,
        })
    return rows


def _row_for_tag(cofile: Path, tag: str) -> dict | None:
    for row in _parse_cofile(cofile):
        if row["tag"] == tag:
            return row
    return None


def _ensure_archive(tag: str, download_url: str, dry: bool) -> Path:
    """Download `download_url` to CACHE_DIR/<tag>.7z if not already present."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    archive = CACHE_DIR / f"{tag}.7z"
    if archive.exists() and archive.stat().st_size > 0:
        print(f"  cache hit: {archive} ({archive.stat().st_size // (1024*1024)} MiB)",
              file=sys.stderr, flush=True)
        return archive
    if dry:
        print(f"  DRY: would download {download_url} → {archive}",
              file=sys.stderr, flush=True)
        return archive
    print(f"  downloading {download_url} ...", file=sys.stderr, flush=True)
    with urllib.request.urlopen(download_url) as resp:
        with archive.open("wb") as fh:
            shutil.copyfileobj(resp, fh)
    print(f"  → {archive} ({archive.stat().st_size // (1024*1024)} MiB)",
          file=sys.stderr, flush=True)
    return archive


def _find_7z() -> str:
    exe = shutil.which("7z") or shutil.which("7z.exe")
    if not exe:
        raise SystemExit("7z not on PATH")
    return exe


def _extract_one(archive: Path, inner_path: str, dest: Path, dry: bool) -> Path:
    """Extract `inner_path` from `archive` to `dest`. Returns dest."""
    if dest.exists():
        if not dry:
            dest.unlink()
    dest.parent.mkdir(parents=True, exist_ok=True)
    sevenz = _find_7z()
    # Use 7z's "e" (extract without paths) into a temp staging dir, then move.
    # We use -i to filter to the one path we want.
    import tempfile
    tmp = Path(tempfile.mkdtemp(prefix="fetch7z_"))
    try:
        cmd = [sevenz, "x", "-y",
               f"-o{tmp}",
               str(archive),
               inner_path]
        if dry:
            print(f"  DRY: {' '.join(cmd)}", file=sys.stderr, flush=True)
            print(f"  DRY: would move extracted file → {dest}",
                  file=sys.stderr, flush=True)
            return dest
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            sys.stderr.write(r.stdout + r.stderr)
            raise SystemExit(f"7z extract failed (rc={r.returncode})")
        # Find the extracted file (may be at tmp/<inner_path> or tmp/<basename>
        # depending on 7z's path-mode). Try the full path first.
        candidate = tmp / inner_path
        if not candidate.is_file():
            candidate = tmp / Path(inner_path).name
        if not candidate.is_file():
            raise SystemExit(f"could not find extracted file at {tmp / inner_path}")
        shutil.move(str(candidate), str(dest))
        return dest
    finally:
        if not dry:
            shutil.rmtree(tmp, ignore_errors=True)


def _verify_sha(path: Path, expected_short: str) -> bool:
    """Compute SHA-256 of `path` and check it starts with expected_short."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while chunk := fh.read(1 << 20):
            h.update(chunk)
    actual = h.hexdigest()
    return actual.startswith(expected_short)


def fetch_one(binary_path: Path, tag: str, *, dest: Path | None,
              into_place: bool, list_only: bool, dry: bool) -> Path | None:
    """Fetch a single binary for `tag`. Returns destination path on success
    (or None if list-only / dry / row-missing)."""
    cofile = binary_path.parent / f"{binary_path.name}.md"
    rel = binary_path.relative_to(RELEASE_DIR).as_posix()
    print(f"\n[fetch_binary] {rel} @ {tag}", file=sys.stderr, flush=True)

    if not cofile.is_file():
        print(f"  no co-file at {cofile}, skipping", file=sys.stderr, flush=True)
        return None
    row = _row_for_tag(cofile, tag)
    if row is None:
        print(f"  no row for tag {tag} in {cofile.name}, skipping",
              file=sys.stderr, flush=True)
        return None

    if list_only:
        print(f"  would fetch: {row['download_url']}  (sha~{row['sha_short']})",
              file=sys.stderr, flush=True)
        return None

    archive = _ensure_archive(tag, row["download_url"], dry)
    if dry:
        return None

    # The "inner path" inside the .7z mirrors the binary's path under the
    # release tree (which is what the .7z packager included).
    inner = rel
    if dest is None:
        dest = (binary_path if into_place
                else HISTORICAL_DIR / tag / rel)
    dest = _extract_one(archive, inner, dest, dry)
    if dry:
        return None

    if not _verify_sha(dest, row["sha_short"]):
        raise SystemExit(
            f"SHA mismatch for {dest}: expected starts-with {row['sha_short']}, "
            f"computed full SHA differs. Archive may be corrupted or co-file is stale."
        )
    print(f"  OK → {dest}  (verified sha~{row['sha_short']})",
          file=sys.stderr, flush=True)
    return dest


def find_all_cofiles(root: Path):
    """Yield every <binary>.md co-file in `root` (where the binary itself
    may or may not be present on disk)."""
    for p in root.rglob("*.md"):
        # Skip top-level docs + anything that's clearly not a co-file.
        if not p.is_file():
            continue
        # Heuristic: a co-file's stem ends with a recognized binary extension.
        # e.g. "Foo.esp.md" → stem "Foo.esp"
        stem = p.stem.lower()
        if any(stem.endswith(ext) for ext in
               (".esp", ".esm", ".pak", ".ucas", ".utoc", ".dll", ".exe",
                ".dds", ".tga", ".png", ".jpg", ".jpeg", ".webp",
                ".uasset", ".uexp", ".umap", ".bsa")):
            yield p


def main() -> int:
    # Force UTF-8 on stdout/stderr so docstrings with unicode arrows render
    # correctly when the Windows console default is cp1252.
    for stream in (sys.stdout, sys.stderr):
        if isinstance(stream, io.TextIOWrapper):
            stream.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tag", required=True, help="release tag to fetch from")
    ap.add_argument("binary", type=Path, nargs="?",
                    help="binary path to fetch (path under release/, ignored when --all)")
    ap.add_argument("--all", action="store_true",
                    help="fetch every binary that has a .md co-file at this tag")
    ap.add_argument("--list", action="store_true",
                    help="show what would be fetched; don't download or extract")
    ap.add_argument("--dry-run", action="store_true",
                    help="alias for --list (no FS changes)")
    ap.add_argument("--into-place", action="store_true",
                    help="overwrite the working-tree binary instead of mirroring under work/historical/")
    ap.add_argument("--out", type=Path,
                    help="explicit destination path (single-binary mode only)")
    args = ap.parse_args()

    list_only = args.list or args.dry_run

    if args.all:
        if args.binary or args.out or args.into_place:
            ap.error("--all is incompatible with binary/--out/--into-place")
        cofiles = sorted(find_all_cofiles(RELEASE_DIR))
        if not cofiles:
            print("no co-files found under release/", file=sys.stderr)
            return 1
        print(f"[fetch_binary] {len(cofiles)} co-files; tag={args.tag}",
              file=sys.stderr, flush=True)
        any_failed = False
        for cofile in cofiles:
            # Reconstruct the binary path: strip ".md" from the co-file name.
            binary = cofile.parent / cofile.stem  # cofile.stem already drops .md
            try:
                fetch_one(binary, args.tag, dest=None, into_place=False,
                          list_only=list_only, dry=False)
            except SystemExit as e:
                print(f"  ERR: {e}", file=sys.stderr)
                any_failed = True
        return 1 if any_failed else 0

    if args.binary is None:
        ap.error("specify a binary path or pass --all")

    fetch_one(args.binary, args.tag,
              dest=args.out,
              into_place=args.into_place,
              list_only=list_only,
              dry=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
