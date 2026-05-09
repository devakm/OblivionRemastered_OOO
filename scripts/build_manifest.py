#!/usr/bin/env python3
"""
Walk a directory and emit a JSON manifest: {posix_relpath: {sha256, size}}.

Manifest format is stable across regenerations and across operating systems:
- Keys use POSIX separators ("/"), even on Windows.
- Keys are sorted alphabetically.
- JSON is pretty-printed with 2-space indent and sorted keys.

Usage:
    python scripts/build_manifest.py <source_dir> [-o <out.json>]

If -o is omitted, JSON is written to stdout.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

CHUNK_SIZE = 1 << 20  # 1 MiB


def hash_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while chunk := fh.read(CHUNK_SIZE):
            h.update(chunk)
    return h.hexdigest()


def build_manifest(root: Path) -> dict[str, dict[str, object]]:
    if not root.is_dir():
        raise SystemExit(f"not a directory: {root}")

    entries: dict[str, dict[str, object]] = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        entries[rel] = {
            "sha256": hash_file(path),
            "size": path.stat().st_size,
        }
    # Re-sort to guarantee stable JSON regardless of FS enumeration order.
    return dict(sorted(entries.items()))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("source", type=Path, help="directory to hash")
    ap.add_argument("-o", "--output", type=Path, help="write JSON here (default: stdout)")
    args = ap.parse_args()

    manifest = build_manifest(args.source)
    blob = json.dumps(manifest, indent=2, sort_keys=True) + "\n"

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(blob, encoding="utf-8")
        print(f"wrote {len(manifest)} entries to {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(blob)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
