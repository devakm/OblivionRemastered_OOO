#!/usr/bin/env python3
"""
Generate the two SyncMap variants from the Deluxe source-of-truth INI.

The source-of-truth lives outside this repo, in OOO_SyncGen:
    X:\\mod-tools\\OOO_SyncGen\\SyncGen\\Overrides\\Oscuro's_Oblivion_Overhaul_Overrides.ini

It is **the Deluxe Edition variant** — TES4 FormID → UE5 SoftObjectPath
mappings where Deluxe-only items use Deluxe-DLC asset paths. The prefixes
that mark a Deluxe entry are:

  /Game/Forms/items/armor/DEA…
  /Game/Forms/items/armor/DEM…
  /Game/Forms/items/weapons/DEA…
  /Game/Forms/items/weapons/DEM…

For each Deluxe entry, the source contains a commented-out *non-Deluxe*
alternative (typically an `NDArmor…` or vanilla `Weap…` path) directly
above it:

    ; EditorID: OOOMelusPetiliusCuirass | Name: LOC_FN_OOOMelusPetiliusCuirass
    ;0098F4=/Game/Forms/items/armor/NDArmorLightCuirass5.NDArmorLightCuirass5
    0098F4=/Game/Forms/items/armor/DEAHeavyCuirassOrder6.DEAHeavyCuirassOrder6

This script writes two files into a release source folder:

  1. <target>/.../SyncMap/Oscuro's_Oblivion_Overhaul.ini
       — the **default** (non-Deluxe) variant. Each Deluxe pair is swapped
         so the non-Deluxe alternative is active and the Deluxe asset is
         commented out.

  2. <target>/.../OptionalPatches/SyncMap - DeluxeEdition/Oscuro's_Oblivion_Overhaul.ini
       — the **Deluxe** variant. Verbatim copy of the source.

Pair-swap rule:
  Trigger only when the active (uncommented) FormID line uses a path
  starting with one of the Deluxe prefixes (DELUXE_PATH_PREFIXES below)
  AND the immediately-preceding FormID-shaped line (skipping blanks and
  non-FormID header comments) is a commented entry for the same FormID.
  Header comments and other commented prose are left untouched.

Usage:
    py -3 scripts/sync_syncmap.py --target "X:/games/Oscuro/Oscuro's_..._alpha91"
    py -3 scripts/sync_syncmap.py --target work/_test_syncmap --dry-run
    py -3 scripts/sync_syncmap.py --target ... --source <override-source>

The script writes UTF-8 with the source's original line endings preserved.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

# Source-of-truth INI (the Deluxe variant).
DEFAULT_SOURCE = Path(
    r"X:/mod-tools/OOO_SyncGen/SyncGen/Overrides/Oscuro's_Oblivion_Overhaul_Overrides.ini"
)

# Where each variant lands inside a release source folder.
REL_DEFAULT = Path("OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini")
REL_DELUXE = Path("OblivionRemastered/Content/Dev/ObvData/Data/OptionalPatches/SyncMap - DeluxeEdition/Oscuro's_Oblivion_Overhaul.ini")

# Asset-path prefixes that mark an entry as a Deluxe-only mapping. Both the
# armor (DEA = Deluxe Armor, "Order" set; DEM = "Cataclysm" set) and weapons
# variants are covered. Only entries whose ACTIVE line begins with one of
# these prefixes are considered for the comment swap.
DELUXE_PATH_PREFIXES = (
    "/Game/Forms/items/armor/DEA",
    "/Game/Forms/items/armor/DEM",
    "/Game/Forms/items/weapons/DEA",
    "/Game/Forms/items/weapons/DEM",
)

# A FormID line: optional `;` (commented), optional whitespace, 6-8 hex digits,
# `=`, then the asset path. Captures: (semicolon-or-empty, formid, path).
FORMID_LINE_RE = re.compile(r"^(;)?\s*([0-9A-Fa-f]{6,8})\s*=\s*(.+?)\s*$")


@dataclass
class SwapResult:
    pairs_swapped: int
    deluxe_actives_found: int
    deluxe_actives_unmatched: list[tuple[int, str]]  # (line_no, formid) where no preceding alt was found


def _is_deluxe_path(path: str) -> bool:
    return any(path.startswith(p) for p in DELUXE_PATH_PREFIXES)


def swap_deluxe_to_default(deluxe_text: str) -> tuple[str, SwapResult]:
    """Walk the Deluxe ini text and swap each Deluxe/non-Deluxe pair so the
    non-Deluxe alternative becomes the active mapping.

    Returns (transformed_text, swap_result).
    """
    lines = deluxe_text.splitlines(keepends=True)
    pairs_swapped = 0
    deluxe_actives_found = 0
    unmatched: list[tuple[int, str]] = []

    for i, raw in enumerate(lines):
        line = raw.rstrip("\r\n")
        m = FORMID_LINE_RE.match(line)
        if not m or m.group(1):
            # Either not a FormID line, or it's already commented — skip.
            continue
        formid, path = m.group(2), m.group(3)
        if not _is_deluxe_path(path):
            continue
        deluxe_actives_found += 1

        # Walk backwards to find the matching commented alternative.
        # Skip blank lines and non-FormID-shaped lines (header comments etc.);
        # stop at the first FormID-shaped line.
        j = i - 1
        match_idx = None
        while j >= 0:
            prev = lines[j].rstrip("\r\n")
            pm = FORMID_LINE_RE.match(prev)
            if pm:
                if pm.group(1) and pm.group(2) == formid:
                    match_idx = j
                # Whether matched or not, stop at first FormID-shaped neighbour.
                break
            j -= 1

        if match_idx is None:
            unmatched.append((i + 1, formid))
            continue

        # Comment the current Deluxe-active line: prepend ';'.
        lines[i] = ";" + raw

        # Uncomment the previous alternative: strip the FIRST ';' character
        # (preserving whatever leading whitespace + spacing came after it).
        prev_raw = lines[match_idx]
        semi_idx = prev_raw.find(";")
        lines[match_idx] = prev_raw[:semi_idx] + prev_raw[semi_idx + 1:]
        pairs_swapped += 1

    return "".join(lines), SwapResult(
        pairs_swapped=pairs_swapped,
        deluxe_actives_found=deluxe_actives_found,
        deluxe_actives_unmatched=unmatched,
    )


def _read_text_preserving_eol(path: Path) -> str:
    # Read as bytes so we don't normalise line endings, then decode.
    return path.read_bytes().decode("utf-8")


def _write_text_preserving_eol(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode("utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", type=Path, default=DEFAULT_SOURCE,
                    help=f"Deluxe source-of-truth INI (default: {DEFAULT_SOURCE})")
    ap.add_argument("--target", type=Path, required=True,
                    help="Target root — typically a release source folder. "
                         "The two output INIs land at <target>/REL_DEFAULT and <target>/REL_DELUXE.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Show what would be written; do not modify any files.")
    ap.add_argument("--show-unmatched", action="store_true",
                    help="On finish, print FormIDs whose Deluxe-active line had no preceding alternative.")
    args = ap.parse_args()

    if not args.source.is_file():
        raise SystemExit(f"source INI not found: {args.source}")

    deluxe_text = _read_text_preserving_eol(args.source)
    default_text, result = swap_deluxe_to_default(deluxe_text)

    out_default = args.target / REL_DEFAULT
    out_deluxe = args.target / REL_DELUXE

    print(f"[sync_syncmap] source: {args.source}", file=sys.stderr)
    print(f"[sync_syncmap]   {result.deluxe_actives_found} Deluxe-active line(s) found", file=sys.stderr)
    print(f"[sync_syncmap]   {result.pairs_swapped} pair(s) swapped to non-Deluxe", file=sys.stderr)
    if result.deluxe_actives_unmatched:
        print(
            f"[sync_syncmap]   WARN: {len(result.deluxe_actives_unmatched)} Deluxe-active line(s) "
            f"had no preceding alternative — left as-is",
            file=sys.stderr,
        )
        if args.show_unmatched:
            for line_no, formid in result.deluxe_actives_unmatched:
                print(f"[sync_syncmap]     line {line_no}: FormID {formid}", file=sys.stderr)

    if args.dry_run:
        print(f"[sync_syncmap] DRY-RUN: would write\n  - {out_default}\n  - {out_deluxe}",
              file=sys.stderr)
        return 0

    _write_text_preserving_eol(out_default, default_text)
    print(f"[sync_syncmap] wrote default (non-Deluxe): {out_default} ({len(default_text)} bytes)",
          file=sys.stderr)

    # Deluxe variant is verbatim source copy.
    _write_text_preserving_eol(out_deluxe, deluxe_text)
    print(f"[sync_syncmap] wrote Deluxe: {out_deluxe} ({len(deluxe_text)} bytes)",
          file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
