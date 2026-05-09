#!/usr/bin/env python3
"""
7-zip a source directory into dist/<name>.7z. Used to rebuild a release archive
from its source folder without going through the full ingest flow.

For routine release ingestion, use scripts/ingest_release.py — it builds the
archive as part of the ingest. This script is for the case where you've lost
or want to regenerate dist/<name>.7z standalone.

Usage:
    python scripts/package_release.py --source "X:/games/Oscuro/Oscuro's_..._alpha37"
    python scripts/package_release.py --source <path> --name alpha37
    python scripts/package_release.py --source <path> --output some/file.7z
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = REPO_ROOT / "dist"


def find_7z() -> str:
    exe = shutil.which("7z") or shutil.which("7z.exe")
    if not exe:
        raise SystemExit("7z not found on PATH. Install 7-Zip and retry.")
    return exe


def package(source: Path, output: Path) -> int:
    if not source.is_dir():
        raise SystemExit(f"source is not a directory: {source}")
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    if output.exists():
        print(f"[package] removing existing {output}", file=sys.stderr)
        output.unlink()

    cmd = [
        find_7z(), "a", "-t7z", "-mx=9", "-m0=lzma2", "-ms=on", "-mmt=on",
        "-xr!.gitkeep",
        str(output),
        f"{source.as_posix()}/*",
    ]
    print(f"[package] {' '.join(cmd)}", file=sys.stderr)
    r = subprocess.run(cmd, cwd=REPO_ROOT)
    if r.returncode != 0:
        raise SystemExit(f"7z exited {r.returncode}")

    size = output.stat().st_size
    print(f"[package] wrote {output} ({size / (1024*1024):.1f} MiB)", file=sys.stderr)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, required=True, help="directory to archive")
    ap.add_argument("--name", help="archive base name (default: source folder name)")
    ap.add_argument("--output", type=Path, help="explicit output path (overrides --name)")
    args = ap.parse_args()

    name = args.name or args.source.name
    output = args.output or (DIST_DIR / f"{name}.7z")
    return package(args.source, output)


if __name__ == "__main__":
    raise SystemExit(main())
