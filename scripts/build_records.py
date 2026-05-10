#!/usr/bin/env python3
"""
Generate the structured inventory bundle for an ESP/ESM:

    <esp>.records/_meta.json       — TES4 header, masters, list of record types
    <esp>.records/<TYPE>.json      — one file per record type the ESP defines

Each per-type JSON is an array of record entries sorted by FormID for stable
diffs. Most types use the generic {formid, edid, full, modl} schema; per-type
overrides handle records that need richer extraction (LVLI/LVLC/LVLN/LVSP
entries, CELL headers + ref counts, DIAL + INFO summary, QUST stage indices).

Usage:
    python scripts/build_records.py path/to/Foo.esp
    python scripts/build_records.py path/to/Foo.esp --out path/to/somewhere/
    python scripts/build_records.py path/to/Foo.esp --types ARMO,WEAP

If --out is omitted, writes to <esp>.records/ alongside the ESP.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import Any, Callable

from tes4_parser import parse_esp, ALL_OBLIVION_TOP_SIGS


# --------------------------------------------------------------------------- #
# Field-extraction helpers
# --------------------------------------------------------------------------- #

def format_fid(fid: Any) -> str | None:
    """Stable string form of a FormID: 'mod_filename:HEX_object_id'.

    Wrye Bash FormIDs have `mod_fn` (the FName of the master file the ID
    belongs to) and `object_dex` (the 24-bit object index).
    """
    if fid is None:
        return None
    if hasattr(fid, "mod_fn") and hasattr(fid, "object_dex"):
        return f"{fid.mod_fn}:{fid.object_dex:06X}"
    return str(fid)


def get_modl_path(rec: Any) -> str | None:
    """Try several attribute names for the legacy mesh path. Different
    record types use different field names: weapons/etc. use `model`, armor
    uses `maleBody` (with `femaleBody`/`maleWorld`/etc as variants), some
    types have no model at all.
    """
    for attr in ("model", "maleBody", "maleWorld", "femaleBody", "femaleWorld"):
        m = getattr(rec, attr, None)
        if m is not None:
            mp = getattr(m, "modPath", None)
            if mp:
                return mp
    return None


def get_full(rec: Any) -> str | None:
    """The FULL subrecord — for OBR this is typically a localization key like
    `LOC_FN_<EditorID>`. We record it as-is; resolution against a
    localization table is out of scope for the inventory."""
    full = getattr(rec, "full", None)
    if full is None:
        return None
    return str(full)


def get_eid(rec: Any) -> str | None:
    eid = getattr(rec, "eid", None)
    return str(eid) if eid is not None else None


# --------------------------------------------------------------------------- #
# Per-type extractors. Each takes a `bash.brec.record_groups` block and
# returns a list of dicts.
# --------------------------------------------------------------------------- #

def default_extractor(block: Any) -> list[dict]:
    """Generic {formid, edid, full, modl} for any base-object record."""
    out = []
    for fid, rec in block.id_records.items():
        out.append({
            "formid": format_fid(fid),
            "edid": get_eid(rec),
            "full": get_full(rec),
            "modl": get_modl_path(rec),
        })
    return out


def leveled_extractor(block: Any) -> list[dict]:
    """LVLI/LVLN/LVLC/LVSP — leveled lists. Each record has an `entries`
    list of (level, count, listId) tuples."""
    out = []
    for fid, rec in block.id_records.items():
        entries = getattr(rec, "entries", None) or []
        out.append({
            "formid": format_fid(fid),
            "edid": get_eid(rec),
            "entries": [
                {
                    "level": getattr(e, "level", None),
                    "count": getattr(e, "count", None),
                    "ref_formid": format_fid(getattr(e, "listId", None)),
                }
                for e in entries
            ],
        })
    return out


def cell_extractor(block: Any) -> list[dict]:
    """CELL — block.id_records yields MobCell wrappers, not MreCell records.
    Pull the master record + persistent/temp REFR counts.

    Full REFR walk (per the design doc: REFR FormID + base FormID + position
    flag) is a follow-on pass; this MVP captures the cell header + ref
    counts so diffs can detect cell adds/removes and count-level changes.
    """
    out = []
    for fid, mob_cell in block.id_records.items():
        cell_rec = getattr(mob_cell, "master_record", None)
        if cell_rec is None:
            continue
        flags = getattr(cell_rec, "flags", None)
        is_interior = bool(getattr(flags, "isInterior", False)) if flags else False
        try:
            persist = mob_cell.persistent_refs
            persist_count = len(getattr(persist, "id_records", {}) or {})
        except Exception:
            persist_count = 0
        try:
            temp = mob_cell.temp_refs
            temp_count = len(getattr(temp, "id_records", {}) or {})
        except Exception:
            temp_count = 0
        out.append({
            "formid": format_fid(fid),
            "edid": get_eid(cell_rec),
            "full": get_full(cell_rec),
            "is_interior": is_interior,
            "persistent_ref_count": persist_count,
            "temp_ref_count": temp_count,
        })
    return out


def quest_extractor(block: Any) -> list[dict]:
    """QUST — header + list of stage indices. Per design doc decision #2 we
    skip per-stage script bodies."""
    out = []
    for fid, rec in block.id_records.items():
        stages = getattr(rec, "stages", None) or []
        stage_indices = []
        for s in stages:
            idx = getattr(s, "stage", None)
            if idx is None:
                # Try alternate attr names
                idx = getattr(s, "index", None)
            if idx is not None:
                stage_indices.append(int(idx))
        out.append({
            "formid": format_fid(fid),
            "edid": get_eid(rec),
            "full": get_full(rec),
            "stage_indices": sorted(stage_indices),
        })
    return out


def dial_extractor(block: Any) -> list[dict]:
    """DIAL — header + child INFO summary. Per design doc decision #3 we
    capture INFO count + EDIDs only, no conversation tree."""
    out = []
    for fid, mob_dial in block.id_records.items():
        # DIAL is a complex record like CELL; mob_dial.master_record is the MreDial
        dial_rec = getattr(mob_dial, "master_record", mob_dial)
        # Try to collect INFO children
        info_eids: list[str | None] = []
        # CellChildren-like access pattern; each game module varies
        children = getattr(mob_dial, "_mob_objects", None)
        if children:
            for child_block in children.values():
                for _info_fid, info_rec in getattr(child_block, "id_records", {}).items():
                    info_eids.append(get_eid(info_rec))
        out.append({
            "formid": format_fid(fid),
            "edid": get_eid(dial_rec),
            "full": get_full(dial_rec),
            "info_count": len(info_eids),
            "info_edids": info_eids,
        })
    return out


# Map record signature → extractor function. Anything not listed falls back
# to default_extractor.
EXTRACTORS: dict[bytes, Callable[[Any], list[dict]]] = {
    b"LVLI": leveled_extractor,
    b"LVLN": leveled_extractor,  # if present in OBR
    b"LVLC": leveled_extractor,
    b"LVSP": leveled_extractor,
    b"CELL": cell_extractor,
    b"QUST": quest_extractor,
    b"DIAL": dial_extractor,
}


# --------------------------------------------------------------------------- #
# Top-level flow
# --------------------------------------------------------------------------- #

def write_inventory(esp_path: Path, out_dir: Path | None = None,
                    keep_types: tuple[bytes, ...] = ALL_OBLIVION_TOP_SIGS) -> Path:
    """Parse `esp_path` and write the inventory bundle.

    Wipes and recreates the output directory before writing. Returns the
    output directory path.
    """
    if not esp_path.is_file():
        raise SystemExit(f"ESP not found: {esp_path}")

    out_dir = out_dir or (esp_path.parent / f"{esp_path.name}.records")

    mod_file = parse_esp(esp_path, keep_types=keep_types)

    # Wipe + create output directory.
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    # _meta.json
    meta = {
        "esp": esp_path.name,
        "tes4": {
            "version": float(mod_file.tes4.version),
            "masters": [str(m) for m in mod_file.tes4.masters],
        },
        "record_types": sorted(s.decode("ascii") for s in mod_file.tops),
    }
    (out_dir / "_meta.json").write_text(
        json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    # Per-type
    type_counts: dict[str, int] = {}
    for sig, block in mod_file.tops.items():
        type_name = sig.decode("ascii")
        extractor = EXTRACTORS.get(sig, default_extractor)
        try:
            records = extractor(block)
        except Exception as e:
            print(f"  [warn] {type_name}: extractor failed ({e}); falling back to defaults",
                  file=sys.stderr)
            records = default_extractor(block)
        # Sort by FormID for stable diffs
        records.sort(key=lambda r: (r.get("formid") or ""))
        (out_dir / f"{type_name}.json").write_text(
            json.dumps(records, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        type_counts[type_name] = len(records)

    # Pretty summary to stderr
    print(f"[build_records] wrote {out_dir}", file=sys.stderr)
    print(f"  _meta.json + {len(type_counts)} type files", file=sys.stderr)
    return out_dir


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("esp", type=Path, help="ESP/ESM to inventory")
    ap.add_argument("--out", type=Path, help="output directory (default: <esp>.records/)")
    ap.add_argument("--types", help="comma-separated 4-char sigs to include (default: all)")
    args = ap.parse_args()

    if args.types:
        keep = tuple(t.strip().encode("ascii") for t in args.types.split(","))
    else:
        keep = ALL_OBLIVION_TOP_SIGS

    out_dir = write_inventory(args.esp, args.out, keep)
    print(f"[build_records] done → {out_dir}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
