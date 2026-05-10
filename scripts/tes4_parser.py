"""
Thin adapter around Wrye Bash's TES4 parser. Lets us load an ESP/ESM and
walk parsed records without going through the full Wrye Bash desktop-app
initialization (no bosh init, no game-folder discovery).

Usage:
    from tes4_parser import parse_esp
    mod_file = parse_esp(Path("path/to/Foo.esp"), keep_types=(b"ARMO", b"WEAP"))
    armo_block = mod_file.tops.get(b"ARMO")
    for fid, rec in armo_block.id_records.items():
        print(fid, rec.eid, getattr(rec, "full", None))

The returned ModFile uses Wrye Bash's MreXxx record classes from
`bash.game.oblivion.records`, so parsed records expose typed attributes:
  - rec.eid                # Editor ID (str or None)
  - rec.full               # display-name key (str or None) — for Oblivion
                           #   Remastered this is a localization key like
                           #   `LOC_FN_<EditorID>`, not a literal string
  - rec.model              # Model object with .modPath etc. (some types)
  - rec.entries            # for LVLI/LVLN/LVLC: list of leveled entries
  - rec.flags1             # raw record flags
  - rec.fid                # FormID object: rec.fid.mod_fn, rec.fid.object_dex

See `bash.game.oblivion.records.MreXxx` classes for the per-type attribute
list (each `Mel*` declaration in the class body becomes an attribute).
"""

from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace
from typing import Iterable

# Bootstrap on first import — pulls in Wrye Bash modules.
from _wrye_bootstrap import bootstrap_wrye_bash

bootstrap_wrye_bash()

from bash.bolt import GPath  # noqa: E402
from bash.mod_files import LoadFactory, ModFile  # noqa: E402

# Convenience: every record signature Wrye Bash's Oblivion module knows about.
# Source: AOblivionGameInfo._top_grup_sigs in bash/game/oblivion/__init__.py
ALL_OBLIVION_TOP_SIGS: tuple[bytes, ...] = (
    b"GMST", b"GLOB", b"CLAS", b"FACT", b"HAIR", b"EYES", b"RACE", b"SOUN",
    b"SKIL", b"MGEF", b"SCPT", b"LTEX", b"ENCH", b"SPEL", b"BSGN", b"ACTI",
    b"APPA", b"ARMO", b"BOOK", b"CLOT", b"CONT", b"DOOR", b"INGR", b"LIGH",
    b"MISC", b"STAT", b"GRAS", b"TREE", b"FLOR", b"FURN", b"WEAP", b"AMMO",
    b"NPC_", b"CREA", b"LVLC", b"SLGM", b"KEYM", b"ALCH", b"SBSP", b"SGST",
    b"LVLI", b"WTHR", b"CLMT", b"REGN", b"CELL", b"WRLD", b"DIAL", b"QUST",
    b"IDLE", b"PACK", b"CSTY", b"LSCR", b"LVSP", b"ANIO", b"WATR", b"EFSH",
)


def parse_esp(esp_path: Path, keep_types: Iterable[bytes] = ALL_OBLIVION_TOP_SIGS) -> ModFile:
    """Load an ESP/ESM and return the ModFile with the requested top-level
    record types fully parsed.

    Records of types not in `keep_types` are skipped (the GRUP is read past
    but not unpacked) — keeps memory usage and load time proportional to what
    we actually need.

    Returns a `bash.mod_files.ModFile`. Iterate its `mod_file.tops[<sig>]`
    blocks to get records: `block.id_records.items()` yields (FormID, MreXxx).
    """
    if not esp_path.is_file():
        raise SystemExit(f"ESP not found: {esp_path}")

    # Construct a minimal stand-in for bosh's ModInfo. ModFile/ModReader only
    # need .fn_key (filename string for error messages) and .abs_path (a
    # bolt.Path with .open() method).
    mock_info = SimpleNamespace(
        fn_key=esp_path.name,
        abs_path=GPath(str(esp_path)),
    )

    load_factory = LoadFactory(keepAll=False, by_sig=tuple(keep_types))
    mod_file = ModFile(mock_info, load_factory)
    # loadStrings=False skips the localized-strings table machinery (Oblivion
    # Remastered uses inline string keys like `LOC_FN_<EditorID>`, the actual
    # display strings live in a separate localization file we don't need).
    mod_file.load_plugin(loadStrings=False)
    return mod_file


def main() -> int:
    """CLI smoke test: print top-block sizes for an ESP."""
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("esp", type=Path, help="path to an ESP/ESM")
    ap.add_argument("--types", help="comma-separated 4-char sigs to load (default: all)")
    args = ap.parse_args()

    if args.types:
        keep = tuple(t.strip().encode("ascii") for t in args.types.split(","))
    else:
        keep = ALL_OBLIVION_TOP_SIGS

    mod_file = parse_esp(args.esp, keep)
    print(f"loaded {args.esp.name}")
    print(f"  TES4 v{mod_file.tes4.version}, masters: {[str(m) for m in mod_file.tes4.masters]}")
    print(f"  top blocks loaded: {len(mod_file.tops)}")
    for sig in sorted(mod_file.tops.keys()):
        block = mod_file.tops[sig]
        n = len(getattr(block, "id_records", {}))
        print(f"    {sig.decode():4s}  {n:>6d} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
