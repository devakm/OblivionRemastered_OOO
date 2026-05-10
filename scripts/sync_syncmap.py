#!/usr/bin/env python3
"""
SyncMap drift checker / fixer / diff viewer.

The Deluxe SyncMap source-of-truth lives outside this repo, in OOO_SyncGen:
    X:\\mod-tools\\OOO_SyncGen\\SyncGen\\Overrides\\Oscuro's_Oblivion_Overhaul_Overrides.ini

It is **the Deluxe Edition variant** — TES4 FormID → UE5 SoftObjectPath
mappings where Deluxe-only items use Deluxe-DLC asset paths. The prefixes
that mark a Deluxe entry are:

    /Game/Forms/items/armor/DEA…
    /Game/Forms/items/armor/DEM…
    /Game/Forms/items/weapons/DEA…
    /Game/Forms/items/weapons/DEM…

For each Deluxe entry, the source contains a commented-out non-Deluxe
alternative (typically an `NDArmor…` or vanilla `Weap…` path) directly
above it:

    ; EditorID: OOOMelusPetiliusCuirass | Name: LOC_FN_OOOMelusPetiliusCuirass
    ;0098F4=/Game/Forms/items/armor/NDArmorLightCuirass5.NDArmorLightCuirass5
    0098F4=/Game/Forms/items/armor/DEAHeavyCuirassOrder6.DEAHeavyCuirassOrder6

Two files live in `release/` and are derived from this source:

  Deluxe variant   — verbatim copy of the OOO_SyncGen source.
                     Path: <target>/OblivionRemastered/Content/Dev/ObvData/Data/
                            OptionalPatches/SyncMap - DeluxeEdition/Oscuro's_Oblivion_Overhaul.ini
  default variant  — same file but with each Deluxe pair swapped (the
                     non-Deluxe alternative becomes active; the DEA/DEM
                     line gets commented out).
                     Path: <target>/OblivionRemastered/Content/Dev/ObvData/Data/
                            SyncMap/Oscuro's_Oblivion_Overhaul.ini

Three modes:

  diff-check  (default)
      Read-only. Compares the two files in <target>/ against what they
      SHOULD be (Deluxe == OOO_SyncGen source; default == swap(source)).
      Prints status; exits 0 if both correct, 1 if drift detected.

  diff-fix
      Same checks as diff-check, but if drift is detected, regenerates
      both files in <target>/ to match the expected state. Exits 0 after
      the fix lands (or 0 immediately if nothing was wrong).

  diff-show
      Shows the diff between current standard and current Deluxe in
      <target>/, annotating which differing lines are EXPECTED swap pairs
      (DEA/DEM toggles) vs UNEXPECTED drift (anything else).

Usage:
    py -3 scripts/sync_syncmap.py diff-check               # default mode
    py -3 scripts/sync_syncmap.py diff-check --target release/
    py -3 scripts/sync_syncmap.py diff-fix
    py -3 scripts/sync_syncmap.py diff-show

All modes default --target to the repo's `release/` directory.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Source-of-truth INI (the Deluxe variant).
DEFAULT_SOURCE = Path(
    r"X:/mod-tools/OOO_SyncGen/SyncGen/Overrides/Oscuro's_Oblivion_Overhaul_Overrides.ini"
)

# Where each variant lands inside `release/` (or wherever --target points).
REL_DEFAULT = Path("OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini")
REL_DELUXE = Path("OblivionRemastered/Content/Dev/ObvData/Data/OptionalPatches/SyncMap - DeluxeEdition/Oscuro's_Oblivion_Overhaul.ini")

# Asset-path prefixes that mark an entry as a Deluxe-only mapping. Both armor
# (DEA = "Order" set; DEM = "Cataclysm" set) and weapons variants are covered.
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
    deluxe_actives_unmatched: list[tuple[int, str]]


# --------------------------------------------------------------------------- #
# Pure transformation
# --------------------------------------------------------------------------- #

def _is_deluxe_path(path: str) -> bool:
    return any(path.startswith(p) for p in DELUXE_PATH_PREFIXES)


def swap_deluxe_to_default(deluxe_text: str) -> tuple[str, SwapResult]:
    """Walk the Deluxe ini text and swap each Deluxe/non-Deluxe pair so the
    non-Deluxe alternative becomes the active mapping."""
    lines = deluxe_text.splitlines(keepends=True)
    pairs_swapped = 0
    deluxe_actives_found = 0
    unmatched: list[tuple[int, str]] = []

    for i, raw in enumerate(lines):
        line = raw.rstrip("\r\n")
        m = FORMID_LINE_RE.match(line)
        if not m or m.group(1):
            continue
        formid, path = m.group(2), m.group(3)
        if not _is_deluxe_path(path):
            continue
        deluxe_actives_found += 1

        j = i - 1
        match_idx = None
        while j >= 0:
            prev = lines[j].rstrip("\r\n")
            pm = FORMID_LINE_RE.match(prev)
            if pm:
                if pm.group(1) and pm.group(2) == formid:
                    match_idx = j
                break
            j -= 1

        if match_idx is None:
            unmatched.append((i + 1, formid))
            continue

        lines[i] = ";" + raw
        prev_raw = lines[match_idx]
        semi_idx = prev_raw.find(";")
        lines[match_idx] = prev_raw[:semi_idx] + prev_raw[semi_idx + 1:]
        pairs_swapped += 1

    return "".join(lines), SwapResult(
        pairs_swapped=pairs_swapped,
        deluxe_actives_found=deluxe_actives_found,
        deluxe_actives_unmatched=unmatched,
    )


def _read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


# --------------------------------------------------------------------------- #
# Drift detection
# --------------------------------------------------------------------------- #

@dataclass
class DriftReport:
    source_path: Path
    target_root: Path
    deluxe_target_path: Path
    default_target_path: Path
    expected_deluxe: bytes
    expected_default: bytes
    deluxe_target_exists: bool
    default_target_exists: bool
    deluxe_in_sync: bool
    default_in_sync: bool
    swap_result: SwapResult

    @property
    def has_drift(self) -> bool:
        return not (self.deluxe_in_sync and self.default_in_sync)


def detect_drift(source: Path, target_root: Path) -> DriftReport:
    if not source.is_file():
        raise SystemExit(f"source INI not found: {source}")

    expected_deluxe = _read_bytes(source)
    default_text, swap = swap_deluxe_to_default(expected_deluxe.decode("utf-8"))
    expected_default = default_text.encode("utf-8")

    deluxe_target = target_root / REL_DELUXE
    default_target = target_root / REL_DEFAULT

    deluxe_in_sync = (deluxe_target.is_file()
                      and _read_bytes(deluxe_target) == expected_deluxe)
    default_in_sync = (default_target.is_file()
                       and _read_bytes(default_target) == expected_default)

    return DriftReport(
        source_path=source,
        target_root=target_root,
        deluxe_target_path=deluxe_target,
        default_target_path=default_target,
        expected_deluxe=expected_deluxe,
        expected_default=expected_default,
        deluxe_target_exists=deluxe_target.is_file(),
        default_target_exists=default_target.is_file(),
        deluxe_in_sync=deluxe_in_sync,
        default_in_sync=default_in_sync,
        swap_result=swap,
    )


def _print_report(report: DriftReport, *, header: str) -> None:
    print(f"[sync_syncmap] {header}", file=sys.stderr)
    print(f"  source:  {report.source_path}", file=sys.stderr)
    print(f"  target:  {report.target_root}", file=sys.stderr)
    print(f"  Deluxe-active lines found in source: {report.swap_result.deluxe_actives_found}",
          file=sys.stderr)
    if report.swap_result.deluxe_actives_unmatched:
        print(f"  WARN: {len(report.swap_result.deluxe_actives_unmatched)} "
              f"Deluxe-active line(s) had NO preceding non-Deluxe alternative",
              file=sys.stderr)
        for line_no, formid in report.swap_result.deluxe_actives_unmatched:
            print(f"    line {line_no}: FormID {formid}", file=sys.stderr)
    print(f"  Deluxe target ({report.deluxe_target_path.name}): "
          f"{'matches source' if report.deluxe_in_sync else ('DRIFT' if report.deluxe_target_exists else 'MISSING')}",
          file=sys.stderr)
    print(f"  default target ({report.default_target_path.name}): "
          f"{'matches expected swap' if report.default_in_sync else ('DRIFT' if report.default_target_exists else 'MISSING')}",
          file=sys.stderr)


# --------------------------------------------------------------------------- #
# Annotated diff (for diff-show)
# --------------------------------------------------------------------------- #

def _count_expected_swap_lines(source_path: Path) -> int:
    """Count Deluxe-active lines in OOO_SyncGen source — these are the lines
    that get swap-toggled between standard and Deluxe variants. Each pair
    contributes TWO line-level differences (the Deluxe line + its non-Deluxe
    alternative)."""
    if not source_path.is_file():
        return 0
    text = _read_bytes(source_path).decode("utf-8")
    count = 0
    for line in text.splitlines():
        m = FORMID_LINE_RE.match(line)
        if m and not m.group(1) and _is_deluxe_path(m.group(3)):
            count += 1
    return count


def _swap_pair_formids(source_path: Path) -> set[str]:
    """FormIDs that appear in a Deluxe/non-Deluxe pair in the source — these
    are the FormIDs whose two lines (DEA/DEM + alternative) get toggled
    between standard and Deluxe variants. A FormID is in the set if the
    source has an UNCOMMENTED Deluxe-pathed line for it."""
    out: set[str] = set()
    if not source_path.is_file():
        return out
    text = _read_bytes(source_path).decode("utf-8")
    for line in text.splitlines():
        m = FORMID_LINE_RE.match(line)
        if m and not m.group(1) and _is_deluxe_path(m.group(3)):
            out.add(m.group(2))
    return out


def _annotated_diff(default_path: Path, deluxe_path: Path, source_path: Path) -> str:
    """Diff `default_path` vs `deluxe_path` line-by-line, annotating each
    differing pair as either an EXPECTED swap (DEA/DEM toggle) or
    UNEXPECTED drift. Calls out the byte-identical (broken) case."""
    if not (default_path.is_file() and deluxe_path.is_file()):
        return "[diff-show] one or both files missing — cannot diff"

    default_bytes = _read_bytes(default_path)
    deluxe_bytes = _read_bytes(deluxe_path)
    expected_swap_pairs = _count_expected_swap_lines(source_path)
    expected_diff_lines = expected_swap_pairs * 2  # each pair = 2 line changes

    out: list[str] = ["",
                      "=== Standard vs Deluxe SyncMap ===",
                      f"  standard: {default_path}",
                      f"  Deluxe:   {deluxe_path}",
                      f"  source:   {source_path}",
                      ""]

    if default_bytes == deluxe_bytes:
        out.append("BROKEN: standard and Deluxe files are BYTE-IDENTICAL.")
        out.append("")
        out.append(f"Expected: ~{expected_diff_lines} differing lines "
                   f"({expected_swap_pairs} DEA/DEM pairs × 2 lines per swap).")
        out.append("Actual:   0 differing lines.")
        out.append("")
        out.append("This means the standard variant has NOT had its DEA/DEM pairs swapped.")
        out.append("Run `sync_syncmap.py diff-fix` to regenerate the standard file from")
        out.append("the OOO_SyncGen source with the correct swaps applied.")
        return "\n".join(out)

    default_lines = default_bytes.decode("utf-8").splitlines()
    deluxe_lines = deluxe_bytes.decode("utf-8").splitlines()

    if len(default_lines) != len(deluxe_lines):
        out.append(f"BROKEN: line counts differ — standard={len(default_lines)} "
                   f"Deluxe={len(deluxe_lines)}.")
        out.append("Cannot do pairwise diff with line-count mismatch. Run `diff-fix` to")
        out.append("regenerate both files from the source-of-truth.")
        return "\n".join(out)

    # FormIDs that appear in a swap pair — both the DEA/DEM line AND its
    # NDArmor/Weap/Glass alternative carry this FormID. Either line being a
    # commented-state-only difference for this FormID = expected swap.
    swap_formids = _swap_pair_formids(source_path)

    expected_pairs = 0
    drift_pairs = 0
    for i, (d_line, x_line) in enumerate(zip(default_lines, deluxe_lines), 1):
        if d_line == x_line:
            continue
        d_match = FORMID_LINE_RE.match(d_line)
        x_match = FORMID_LINE_RE.match(x_line)
        is_swap = False
        if (d_match and x_match
                and d_match.group(2) == x_match.group(2)        # same FormID
                and d_match.group(3) == x_match.group(3)        # same path
                and d_match.group(1) != x_match.group(1)        # different commented-state
                and d_match.group(2) in swap_formids):          # FormID is in the swap set
            is_swap = True
        marker = "EXPECTED-SWAP" if is_swap else "DRIFT"
        if is_swap:
            expected_pairs += 1
        else:
            drift_pairs += 1
        out.append(f"  [{marker}] line {i}")
        out.append(f"    standard < {d_line}")
        out.append(f"    Deluxe   > {x_line}")

    out.append("")
    out.append(f"=== Summary ===")
    out.append(f"  EXPECTED-SWAP lines: {expected_pairs}  "
               f"(should be ~{expected_diff_lines}: {expected_swap_pairs} DEA/DEM pairs × 2)")
    out.append(f"  DRIFT lines:         {drift_pairs}  (should be 0)")
    if drift_pairs > 0:
        out.append("")
        out.append("DRIFT lines indicate unexpected differences between standard and Deluxe.")
        out.append("Most likely the OOO_SyncGen source has been edited and one of the targets")
        out.append("hasn't been regenerated. Run `sync_syncmap.py diff-fix` to resync.")
    elif expected_pairs != expected_diff_lines:
        out.append("")
        out.append(f"WARN: only {expected_pairs} DEA/DEM swap lines present, but the source")
        out.append(f"      expects {expected_diff_lines}. Run `diff-fix` to bring the standard")
        out.append("      variant in line with the source.")
    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Mode handlers
# --------------------------------------------------------------------------- #

def cmd_diff_check(source: Path, target_root: Path) -> int:
    report = detect_drift(source, target_root)
    if report.has_drift:
        _print_report(report, header="diff-check: DRIFT DETECTED")
        print(f"  → run `sync_syncmap.py diff-show` to inspect, then "
              f"`sync_syncmap.py diff-fix` to regenerate.", file=sys.stderr)
        return 1
    _print_report(report, header="diff-check: OK (no drift)")
    return 0


def cmd_diff_fix(source: Path, target_root: Path) -> int:
    report = detect_drift(source, target_root)
    if not report.has_drift:
        _print_report(report, header="diff-fix: nothing to fix")
        return 0
    _print_report(report, header="diff-fix: applying corrections")
    if not report.deluxe_in_sync:
        _write_bytes(report.deluxe_target_path, report.expected_deluxe)
        print(f"  WROTE Deluxe → {report.deluxe_target_path}", file=sys.stderr)
    if not report.default_in_sync:
        _write_bytes(report.default_target_path, report.expected_default)
        print(f"  WROTE default → {report.default_target_path}", file=sys.stderr)
    print(f"[sync_syncmap] diff-fix: done", file=sys.stderr)
    return 0


def cmd_diff_show(source: Path, target_root: Path) -> int:
    default_target = target_root / REL_DEFAULT
    deluxe_target = target_root / REL_DELUXE
    print(_annotated_diff(default_target, deluxe_target, source))
    return 0


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="mode", metavar="{diff-check,diff-fix,diff-show}")

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--source", type=Path, default=DEFAULT_SOURCE,
                        help=f"Deluxe source-of-truth INI (default: {DEFAULT_SOURCE})")
    common.add_argument("--target", type=Path, default=REPO_ROOT / "release",
                        help="Target root (default: <repo>/release/)")

    sub.add_parser("diff-check", parents=[common],
                   help="Read-only check: report drift, exit 0 if OK, 1 if drift.")
    sub.add_parser("diff-fix", parents=[common],
                   help="If drift: regenerate both files from source.")

    sub.add_parser("diff-show", parents=[common],
                   help="Show annotated standard-vs-Deluxe diff with EXPECTED-SWAP / DRIFT markers.")

    args = ap.parse_args()

    # Default mode = diff-check
    mode = args.mode or "diff-check"
    if mode == "diff-check":
        source = getattr(args, "source", DEFAULT_SOURCE)
        target = getattr(args, "target", REPO_ROOT / "release")
        return cmd_diff_check(source, target)
    if mode == "diff-fix":
        return cmd_diff_fix(args.source, args.target)
    if mode == "diff-show":
        return cmd_diff_show(args.source, args.target)
    ap.error(f"unknown mode: {mode}")
    return 2  # unreachable


if __name__ == "__main__":
    raise SystemExit(main())
