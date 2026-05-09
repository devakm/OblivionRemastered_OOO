#!/usr/bin/env python3
"""
Compare two release manifests and emit added / removed / changed file lists.

Usage:
    python scripts/diff_releases.py <prev.json> <curr.json> [--format md|json]
    python scripts/diff_releases.py --no-prev <curr.json> [--format md|json]

`--no-prev` is the "first release" mode: every file in <curr.json> is reported
as added.

The Markdown form is suitable for committing as docs/per-release/<name>.md and
for use as the body of a GitHub Release.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Diff:
    added: list[str]
    removed: list[str]
    changed: list[str]
    unchanged_count: int

    @property
    def total_changes(self) -> int:
        return len(self.added) + len(self.removed) + len(self.changed)


def load_manifest(path: Path) -> dict[str, dict[str, object]]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def diff_manifests(
    prev: dict[str, dict[str, object]] | None,
    curr: dict[str, dict[str, object]],
) -> Diff:
    if prev is None:
        return Diff(added=sorted(curr.keys()), removed=[], changed=[], unchanged_count=0)

    prev_keys = set(prev.keys())
    curr_keys = set(curr.keys())

    added = sorted(curr_keys - prev_keys)
    removed = sorted(prev_keys - curr_keys)

    common = prev_keys & curr_keys
    changed = sorted(k for k in common if prev[k]["sha256"] != curr[k]["sha256"])
    unchanged_count = len(common) - len(changed)

    return Diff(added=added, removed=removed, changed=changed, unchanged_count=unchanged_count)


def _human_size(n: int) -> str:
    for unit in ("B", "KiB", "MiB", "GiB", "TiB"):
        if n < 1024:
            return f"{n:.1f} {unit}" if unit != "B" else f"{n} B"
        n /= 1024  # type: ignore[assignment]
    return f"{n:.1f} PiB"


def _bullet(items: Iterable[str], curr: dict[str, dict[str, object]] | None = None) -> str:
    out: list[str] = []
    for p in items:
        if curr is not None and p in curr:
            size = curr[p]["size"]
            assert isinstance(size, int)
            out.append(f"- `{p}` ({_human_size(size)})")
        else:
            out.append(f"- `{p}`")
    return "\n".join(out) if out else "_none_"


def render_markdown(
    diff: Diff,
    prev_name: str | None,
    curr_name: str,
    curr: dict[str, dict[str, object]],
) -> str:
    if prev_name is None:
        header = f"# {curr_name} — initial release\n\nAll files counted as additions (no prior release for comparison)."
    else:
        header = f"# {curr_name} — changes since {prev_name}"

    summary = (
        f"\n\n## Summary\n\n"
        f"- **Added:** {len(diff.added)}\n"
        f"- **Removed:** {len(diff.removed)}\n"
        f"- **Changed:** {len(diff.changed)}\n"
        f"- **Unchanged:** {diff.unchanged_count}\n"
    )

    sections = [
        ("Added", _bullet(diff.added, curr)),
        ("Removed", _bullet(diff.removed)),
        ("Changed", _bullet(diff.changed, curr)),
    ]
    body = "\n\n".join(f"## {title}\n\n{content}" for title, content in sections)

    return f"{header}{summary}\n{body}\n"


def render_json(diff: Diff, prev_name: str | None, curr_name: str) -> str:
    payload = {
        "previous": prev_name,
        "current": curr_name,
        "added": diff.added,
        "removed": diff.removed,
        "changed": diff.changed,
        "unchanged_count": diff.unchanged_count,
    }
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--no-prev", action="store_true", help="first-release mode")
    ap.add_argument("prev_or_curr", type=Path, nargs="?")
    ap.add_argument("curr", type=Path, nargs="?")
    ap.add_argument("--format", choices=("md", "json"), default="md")
    ap.add_argument("-o", "--output", type=Path, help="write to file (default: stdout)")
    args = ap.parse_args()

    if args.no_prev:
        if args.prev_or_curr is None:
            ap.error("--no-prev requires <curr.json>")
        prev_path = None
        curr_path = args.prev_or_curr
    else:
        if args.prev_or_curr is None or args.curr is None:
            ap.error("need <prev.json> <curr.json> (or --no-prev <curr.json>)")
        prev_path = args.prev_or_curr
        curr_path = args.curr

    curr = load_manifest(curr_path)
    prev = load_manifest(prev_path) if prev_path else None
    diff = diff_manifests(prev, curr)

    prev_name = prev_path.stem if prev_path else None
    curr_name = curr_path.stem

    if args.format == "md":
        out = render_markdown(diff, prev_name, curr_name, curr)
    else:
        out = render_json(diff, prev_name, curr_name)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(out, encoding="utf-8")
        print(
            f"wrote {curr_name} diff (+{len(diff.added)} -{len(diff.removed)} ~{len(diff.changed)}) to {args.output}",
            file=sys.stderr,
        )
    else:
        sys.stdout.write(out)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
