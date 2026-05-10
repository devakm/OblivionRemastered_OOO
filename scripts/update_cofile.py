#!/usr/bin/env python3
"""
Maintain the per-binary `.md` co-file that tracks every release a binary
ships in.

Layout of `<binary>.md`:

    # <binary basename>

    [optional free-form prose, hand-authored]

    | Release | SHA-256 | Size | Changed | Description | Download |
    |---------|---------|------|---------|-------------|----------|
    | alpha91 | `abc...` | 16.0 MiB (16,835,508 B) |   | [release alpha91](url) | [alpha91.7z](url) |
    | alpha90 | `abc...` | 16.0 MiB (16,835,508 B) |   | [release alpha90](url) | [alpha90.7z](url) |
    | alpha89 | `def...` | 16.0 MiB (16,800,000 B) | ★ | [release alpha89](url) | [alpha89.7z](url) |

Each invocation appends one row at the top of the table (newest first).

Usage:
    python scripts/update_cofile.py <binary-path> --tag alpha91 \\
           --sha abc123def456...   --size 16835508
    python scripts/update_cofile.py <binary-path> --tag alpha91 \\
           --hash-now            # reads the binary, computes SHA + size
    python scripts/update_cofile.py <binary-path> --tag alpha91 \\
           --repo myuser/myrepo    # override default GitHub repo
    python scripts/update_cofile.py <binary-path> --tag alpha91 \\
           --asset-name custom.7z  # default: <tag>.7z

The co-file is created if it doesn't exist. The H1 header is `# <basename>`.
Free-form prose between the H1 and the table is preserved across updates.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

# Default GitHub repo — change with --repo when invoking elsewhere.
DEFAULT_REPO = "devakm/OblivionRemastered_OOO"

# Marker characters and table headers we use.
CHANGED_MARK = "★"
TABLE_HEADER = (
    "| Release | SHA-256 | Size | Changed | Description | Download |\n"
    "|---------|---------|------|---------|-------------|----------|\n"
)
TABLE_HEADER_SEPARATOR_RE = re.compile(r"^\|[-\|\s]+\|\s*$")
ROW_RE = re.compile(
    r"^\|\s*(?P<release>[^|]+?)\s*\|\s*`?(?P<sha>[^|`]+?)`?\s*\|"
    r"\s*(?P<size>[^|]+?)\s*\|\s*(?P<changed>[^|]*?)\s*\|"
    r"\s*(?P<descr>[^|]*?)\s*\|\s*(?P<download>[^|]*?)\s*\|\s*$"
)


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def _human_size(n: int) -> str:
    f = float(n)
    for unit in ("B", "KiB", "MiB", "GiB"):
        if f < 1024:
            return f"{f:.1f} {unit}" if unit != "B" else f"{int(f)} B"
        f /= 1024
    return f"{f:.1f} TiB"


def _hash_file(path: Path) -> tuple[str, int]:
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as fh:
        while chunk := fh.read(1 << 20):
            h.update(chunk)
            size += len(chunk)
    return h.hexdigest(), size


def _short_sha(sha: str) -> str:
    return sha[:12]


def _release_urls(repo: str, tag: str, asset_name: str) -> tuple[str, str]:
    desc = f"https://github.com/{repo}/releases/tag/{tag}"
    dl = f"https://github.com/{repo}/releases/download/{tag}/{asset_name}"
    return desc, dl


def _row_for(tag: str, sha: str, size: int, changed: bool,
             repo: str, asset_name: str) -> str:
    desc_url, dl_url = _release_urls(repo, tag, asset_name)
    sha_short = _short_sha(sha)
    size_str = f"{_human_size(size)} ({size:,} B)"
    mark = CHANGED_MARK if changed else " "
    return (
        f"| {tag} | `{sha_short}` | {size_str} | {mark} "
        f"| [release {tag}]({desc_url}) | [{asset_name}]({dl_url}) |\n"
    )


# --------------------------------------------------------------------------- #
# Co-file parse + render
# --------------------------------------------------------------------------- #

def _parse_existing(text: str) -> tuple[str, list[str], str | None]:
    """Split the co-file into (prose_block, data_rows, prior_sha_short).

    `prose_block` is everything from start of file through the (last) blank
    line before the table — typically an H1 + optional paragraphs.
    `data_rows` is the existing table data rows (each ending with newline),
    newest-first order preserved.
    `prior_sha_short` is the short SHA from the first existing data row, if
    any (used to set the Changed mark for the new row being inserted).
    """
    lines = text.splitlines(keepends=True)
    # Find the table-header separator line ("|---|---|...").
    sep_idx = None
    for i, line in enumerate(lines):
        if TABLE_HEADER_SEPARATOR_RE.match(line):
            sep_idx = i
            break
    if sep_idx is None:
        # No table yet. Whole file is prose.
        return text, [], None
    # Prose: everything before the table-header line above the separator.
    # Convention: the separator's previous line is the table header. Prose
    # ends just before the table header.
    header_idx = sep_idx - 1
    prose = "".join(lines[:header_idx]).rstrip() + "\n\n"
    # Data rows: everything after the separator, until end-of-data
    data_rows = []
    for line in lines[sep_idx + 1:]:
        stripped = line.strip()
        if not stripped:
            break
        if not stripped.startswith("|"):
            break
        data_rows.append(line if line.endswith("\n") else line + "\n")
    # Detect prior SHA short from the first data row (newest existing entry).
    prior_sha_short = None
    if data_rows:
        m = ROW_RE.match(data_rows[0].rstrip("\n"))
        if m:
            prior_sha_short = m.group("sha").strip("`")
    return prose, data_rows, prior_sha_short


def _render(prose: str, data_rows: list[str]) -> str:
    """Build the final file text from prose + data rows."""
    table = TABLE_HEADER + "".join(data_rows)
    return prose + table


def _row_data_from(row_text: str) -> dict | None:
    """Parse a table row line into {tag, sha_short, size_str, descr, download}."""
    m = ROW_RE.match(row_text.rstrip("\n"))
    if not m:
        return None
    return {
        "tag": m.group("release").strip(),
        "sha_short": m.group("sha").strip("`").strip(),
        "size_str": m.group("size").strip(),
        "descr": m.group("descr").strip(),
        "download": m.group("download").strip(),
    }


def _recompute_markers(data_rows: list[str], repo: str,
                       new_sha_full: dict[str, str]) -> list[str]:
    """Walk rows newest→oldest, set Changed = ★ when this row's SHA differs
    from the row immediately older. Oldest row always gets ★ (first
    appearance). Returns rebuilt rows.

    `new_sha_full` maps tag → full SHA for any row whose full SHA we know
    in this update — so we can write the short form back consistently. Rows
    we didn't author (loaded from disk) keep their existing short SHA.
    """
    rebuilt: list[str] = []
    for i, row in enumerate(data_rows):
        info = _row_data_from(row)
        if info is None:
            # Pass through unparseable rows untouched (shouldn't happen).
            rebuilt.append(row)
            continue
        # Determine Changed by comparing to the row immediately below.
        if i + 1 >= len(data_rows):
            changed = True  # oldest row = first appearance
        else:
            below_info = _row_data_from(data_rows[i + 1])
            changed = (below_info is None
                       or below_info["sha_short"] != info["sha_short"])
        mark = CHANGED_MARK if changed else " "
        new_line = (
            f"| {info['tag']} | `{info['sha_short']}` | {info['size_str']} | {mark} "
            f"| {info['descr']} | {info['download']} |\n"
        )
        rebuilt.append(new_line)
    return rebuilt


def update_cofile(binary_path: Path, tag: str, sha: str, size: int,
                  repo: str = DEFAULT_REPO,
                  asset_name: str | None = None) -> Path:
    """Append (or replace) the row for `tag` in the binary's `.md` co-file.

    If `tag` already has a row in the table, the existing row is replaced
    in place (idempotent re-runs). The Changed (★) marker on every row is
    recomputed pairwise after the update, so it stays correct regardless
    of how rows got into the table.

    Returns the path of the updated `.md`.
    """
    cofile = binary_path.parent / f"{binary_path.name}.md"
    asset_name = asset_name or f"{tag}.7z"

    if cofile.is_file():
        text = cofile.read_text(encoding="utf-8")
        prose, data_rows, _prior_sha_unused = _parse_existing(text)
    else:
        prose = f"# {binary_path.name}\n\n"
        data_rows = []

    # Build the new row with a placeholder Changed mark — _recompute_markers
    # will fix it up after we've inserted/replaced.
    new_row = _row_for(tag, sha, size, False, repo, asset_name)

    # If a row for this tag already exists, replace it. Otherwise prepend.
    replaced = False
    for i, row in enumerate(data_rows):
        info = _row_data_from(row)
        if info and info["tag"] == tag:
            data_rows[i] = new_row
            replaced = True
            break
    if not replaced:
        data_rows.insert(0, new_row)

    # Single source of truth for Changed markers.
    data_rows = _recompute_markers(data_rows, repo, {tag: sha})

    out_text = _render(prose, data_rows)
    cofile.write_text(out_text, encoding="utf-8")
    return cofile


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("binary", type=Path, help="path to the binary file")
    ap.add_argument("--tag", required=True, help="release tag (e.g. alpha91)")
    ap.add_argument("--sha", help="SHA-256 of the binary (full hex)")
    ap.add_argument("--size", type=int, help="size in bytes")
    ap.add_argument("--hash-now", action="store_true",
                    help="open the binary and compute SHA + size now (overrides --sha/--size)")
    ap.add_argument("--repo", default=DEFAULT_REPO,
                    help=f"GitHub owner/repo for URL templates (default: {DEFAULT_REPO})")
    ap.add_argument("--asset-name",
                    help="Release asset filename (default: <tag>.7z)")
    args = ap.parse_args()

    if args.hash_now:
        if not args.binary.is_file():
            raise SystemExit(f"--hash-now requires existing binary: {args.binary}")
        sha, size = _hash_file(args.binary)
    else:
        if not args.sha or args.size is None:
            raise SystemExit("Provide --sha + --size, or pass --hash-now to compute them.")
        sha = args.sha
        size = args.size

    out = update_cofile(args.binary, args.tag, sha, size,
                        repo=args.repo, asset_name=args.asset_name)
    print(f"[update_cofile] updated {out} (tag={args.tag} sha={_short_sha(sha)} size={size})",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
