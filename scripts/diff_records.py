#!/usr/bin/env python3
"""
Compare two `.records/` inventory bundles and emit a Markdown changelog
describing what changed inside an ESP between two versions.

Output is suitable for inclusion in `docs/per-release/<tag>.md` as the
"ESP changes" section. The diff is structured per-record-type (Added /
Changed / Removed) with per-type narration tailored to each record kind:

  - Base records (ARMO, WEAP, NPC_, etc.): show edid + full + modl changes.
  - LVLI / LVLN / LVLC / LVSP: show entry-level adds/removes (level, count,
    target FormID).
  - CELL: header changes + persistent/temp ref-count deltas.
  - QUST: stage-index adds/removes.
  - DIAL: info_count + info_edids changes.

Usage:
    python scripts/diff_records.py prev/Foo.esp.records/ curr/Foo.esp.records/
    python scripts/diff_records.py <prev> <curr> --esp-name Foo.esp
    python scripts/diff_records.py <prev> <curr> --out diff.md
    python scripts/diff_records.py --no-prev <curr>      # initial-release mode
"""

from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path
from typing import Any


# Pretty-print labels for each record type. Anything not listed falls back
# to the raw 4-char signature.
TYPE_LABELS: dict[str, str] = {
    "ACTI": "Activator",
    "ALCH": "Potion / Ingestible",
    "AMMO": "Ammunition",
    "ARMO": "Armor",
    "BOOK": "Book",
    "BSGN": "Birthsign",
    "CELL": "Cell",
    "CLAS": "Class",
    "CLMT": "Climate",
    "CLOT": "Clothing",
    "CONT": "Container",
    "CREA": "Creature",
    "CSTY": "Combat Style",
    "DIAL": "Dialogue Topic",
    "DOOR": "Door",
    "EFSH": "Effect Shader",
    "ENCH": "Enchantment",
    "EYES": "Eyes",
    "FACT": "Faction",
    "FLOR": "Flora",
    "FURN": "Furniture",
    "GLOB": "Global Variable",
    "GMST": "Game Setting",
    "GRAS": "Grass",
    "HAIR": "Hair",
    "IDLE": "Idle Animation",
    "INFO": "Dialogue Response",
    "INGR": "Ingredient",
    "KEYM": "Key",
    "LIGH": "Light",
    "LSCR": "Loading Screen",
    "LTEX": "Land Texture",
    "LVLC": "Leveled Creature List",
    "LVLI": "Leveled Item List",
    "LVLN": "Leveled NPC List",
    "LVSP": "Leveled Spell List",
    "MGEF": "Magic Effect",
    "MISC": "Misc Item",
    "NPC_": "NPC",
    "PACK": "AI Package",
    "QUST": "Quest",
    "RACE": "Race",
    "REGN": "Region",
    "SCPT": "Script",
    "SGST": "Sigil Stone",
    "SKIL": "Skill",
    "SLGM": "Soul Gem",
    "SOUN": "Sound",
    "SPEL": "Spell",
    "STAT": "Static Object",
    "TREE": "Tree",
    "WATR": "Water",
    "WEAP": "Weapon",
    "WRLD": "Worldspace",
    "WTHR": "Weather",
}


# --------------------------------------------------------------------------- #
# Diff primitives
# --------------------------------------------------------------------------- #

def _by_formid(records: list[dict]) -> dict[str, dict]:
    """Index a record array by FormID, ignoring entries with no FormID."""
    out: dict[str, dict] = {}
    for r in records:
        fid = r.get("formid")
        if fid is not None:
            out[fid] = r
    return out


def _load_type(records_dir: Path, type_name: str) -> list[dict]:
    """Load a per-type JSON file from a records directory; missing → []."""
    p = records_dir / f"{type_name}.json"
    if not p.is_file():
        return []
    with p.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def _load_meta(records_dir: Path) -> dict:
    p = records_dir / "_meta.json"
    if not p.is_file():
        return {}
    with p.open("r", encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------------------- #
# Record-kind narration helpers
# --------------------------------------------------------------------------- #

def _label(type_sig: str) -> str:
    return TYPE_LABELS.get(type_sig, type_sig)


def _short_fid(fid: str | None) -> str:
    """`Oblivion.esm:00C1D6` → `00C1D6`. We mostly care about object index."""
    if fid is None:
        return "?"
    if ":" in fid:
        return fid.rsplit(":", 1)[1]
    return fid


def _summary(rec: dict) -> str:
    """Compact 'EDID — FULL' for an arbitrary base record."""
    edid = rec.get("edid") or "?"
    full = rec.get("full")
    fid_short = _short_fid(rec.get("formid"))
    parts = [f"`{edid}` (FormID `{fid_short}`)"]
    if full:
        parts.append(f'— "{full}"')
    return " ".join(parts)


def _diff_record_default(prev: dict, curr: dict) -> list[str]:
    """Field-level narration for a generic base record (default extractor)."""
    notes: list[str] = []
    for field in ("edid", "full", "modl"):
        if prev.get(field) != curr.get(field):
            notes.append(f"`{field}`: `{prev.get(field)!r}` → `{curr.get(field)!r}`")
    return notes


def _diff_record_leveled(prev: dict, curr: dict) -> list[str]:
    """LVLI/LVLN/LVLC/LVSP entry-level diff."""
    notes: list[str] = []
    if prev.get("edid") != curr.get("edid"):
        notes.append(f"`edid`: `{prev.get('edid')!r}` → `{curr.get('edid')!r}`")
    prev_entries = prev.get("entries", []) or []
    curr_entries = curr.get("entries", []) or []
    # Build sets of (level, count, ref_formid) for set-diff
    prev_keys = {(e.get("level"), e.get("count"), e.get("ref_formid")) for e in prev_entries}
    curr_keys = {(e.get("level"), e.get("count"), e.get("ref_formid")) for e in curr_entries}
    added = sorted(curr_keys - prev_keys)
    removed = sorted(prev_keys - curr_keys)
    for lvl, cnt, ref in added:
        notes.append(f"+ entry: level {lvl} × {cnt} → `{_short_fid(ref)}`")
    for lvl, cnt, ref in removed:
        notes.append(f"- entry: level {lvl} × {cnt} → `{_short_fid(ref)}`")
    return notes


def _diff_record_cell(prev: dict, curr: dict) -> list[str]:
    notes: list[str] = []
    for field in ("edid", "full", "is_interior"):
        if prev.get(field) != curr.get(field):
            notes.append(f"`{field}`: `{prev.get(field)!r}` → `{curr.get(field)!r}`")
    pp = prev.get("persistent_ref_count", 0) or 0
    cp = curr.get("persistent_ref_count", 0) or 0
    if pp != cp:
        notes.append(f"persistent refs: {pp} → {cp}")
    pt = prev.get("temp_ref_count", 0) or 0
    ct = curr.get("temp_ref_count", 0) or 0
    if pt != ct:
        notes.append(f"temporary refs: {pt} → {ct}")
    return notes


def _diff_record_quest(prev: dict, curr: dict) -> list[str]:
    notes: list[str] = []
    for field in ("edid", "full"):
        if prev.get(field) != curr.get(field):
            notes.append(f"`{field}`: `{prev.get(field)!r}` → `{curr.get(field)!r}`")
    prev_stages = set(prev.get("stage_indices", []) or [])
    curr_stages = set(curr.get("stage_indices", []) or [])
    added = sorted(curr_stages - prev_stages)
    removed = sorted(prev_stages - curr_stages)
    if added:
        notes.append(f"+ stages: {added}")
    if removed:
        notes.append(f"- stages: {removed}")
    return notes


def _diff_record_dial(prev: dict, curr: dict) -> list[str]:
    notes: list[str] = []
    for field in ("edid", "full"):
        if prev.get(field) != curr.get(field):
            notes.append(f"`{field}`: `{prev.get(field)!r}` → `{curr.get(field)!r}`")
    pi = prev.get("info_count", 0) or 0
    ci = curr.get("info_count", 0) or 0
    if pi != ci:
        notes.append(f"INFO count: {pi} → {ci}")
    prev_eids = set(prev.get("info_edids") or [])
    curr_eids = set(curr.get("info_edids") or [])
    added_eids = sorted(curr_eids - prev_eids)
    removed_eids = sorted(prev_eids - curr_eids)
    if added_eids:
        notes.append(f"+ INFO EDIDs: {added_eids[:5]}{'…' if len(added_eids) > 5 else ''}")
    if removed_eids:
        notes.append(f"- INFO EDIDs: {removed_eids[:5]}{'…' if len(removed_eids) > 5 else ''}")
    return notes


# Map type sig → (record-diff fn). Default applies when not listed.
RECORD_DIFFERS = {
    "LVLI": _diff_record_leveled,
    "LVLN": _diff_record_leveled,
    "LVLC": _diff_record_leveled,
    "LVSP": _diff_record_leveled,
    "CELL": _diff_record_cell,
    "QUST": _diff_record_quest,
    "DIAL": _diff_record_dial,
}


# --------------------------------------------------------------------------- #
# Per-type section rendering
# --------------------------------------------------------------------------- #

def _render_type_section(
    type_sig: str,
    prev_records: list[dict],
    curr_records: list[dict],
    max_per_section: int,
) -> str:
    """Render the Markdown for one record type's diff. Returns '' if no
    changes."""
    prev_idx = _by_formid(prev_records)
    curr_idx = _by_formid(curr_records)

    added_fids = sorted(curr_idx.keys() - prev_idx.keys())
    removed_fids = sorted(prev_idx.keys() - curr_idx.keys())
    common_fids = prev_idx.keys() & curr_idx.keys()
    differ = RECORD_DIFFERS.get(type_sig, _diff_record_default)

    changed: list[tuple[str, list[str]]] = []
    for fid in sorted(common_fids):
        notes = differ(prev_idx[fid], curr_idx[fid])
        if notes:
            changed.append((fid, notes))

    if not (added_fids or removed_fids or changed):
        return ""

    label = _label(type_sig)
    out: list[str] = [f"### {label} ({type_sig}) — +{len(added_fids)} -{len(removed_fids)} ~{len(changed)}\n"]

    def _truncate(items, label_word):
        if max_per_section > 0 and len(items) > max_per_section:
            return items[:max_per_section], f"\n_…{len(items) - max_per_section} more {label_word} omitted (see JSON for full list)_"
        return items, ""

    if added_fids:
        out.append("**Added:**\n")
        shown, tail = _truncate(added_fids, "added")
        for fid in shown:
            out.append(f"- {_summary(curr_idx[fid])}")
        if tail:
            out.append(tail)
        out.append("")
    if removed_fids:
        out.append("**Removed:**\n")
        shown, tail = _truncate(removed_fids, "removed")
        for fid in shown:
            out.append(f"- {_summary(prev_idx[fid])}")
        if tail:
            out.append(tail)
        out.append("")
    if changed:
        out.append("**Changed:**\n")
        shown, tail = _truncate(changed, "changed")
        for fid, notes in shown:
            head = _summary(curr_idx[fid])
            note_text = "; ".join(notes)
            out.append(f"- {head} — {note_text}")
        if tail:
            out.append(tail)
        out.append("")

    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Top-level rendering
# --------------------------------------------------------------------------- #

def render_diff(prev_dir: Path | None, curr_dir: Path,
                esp_name: str | None = None,
                max_per_section: int = 0) -> str:
    """Produce the Markdown diff for an inventory comparison.

    Pass `prev_dir=None` for initial-release mode (everything is added).
    """
    curr_meta = _load_meta(curr_dir)
    esp_label = esp_name or curr_meta.get("esp", curr_dir.name)

    out: list[str] = [f"## ESP changes — `{esp_label}`\n"]

    if prev_dir is None:
        out.append("_Initial inventory (no prior version to compare against)._\n")
        # List all record types + counts
        for type_sig in curr_meta.get("record_types", []):
            recs = _load_type(curr_dir, type_sig)
            if recs:
                out.append(f"- **{_label(type_sig)} ({type_sig}):** {len(recs)} records")
        return "\n".join(out) + "\n"

    prev_meta = _load_meta(prev_dir)

    # Header summary: master list change?
    prev_masters = prev_meta.get("tes4", {}).get("masters", []) or []
    curr_masters = curr_meta.get("tes4", {}).get("masters", []) or []
    if prev_masters != curr_masters:
        out.append("**Master list changed:**\n")
        out.append(f"- before: {prev_masters}")
        out.append(f"- after:  {curr_masters}\n")

    # Walk the union of record types present in either side
    all_types = sorted(set(prev_meta.get("record_types") or []) |
                       set(curr_meta.get("record_types") or []))

    rendered_any = False
    for type_sig in all_types:
        prev_recs = _load_type(prev_dir, type_sig)
        curr_recs = _load_type(curr_dir, type_sig)
        section = _render_type_section(type_sig, prev_recs, curr_recs, max_per_section)
        if section:
            out.append(section)
            rendered_any = True

    if not rendered_any:
        out.append("_No record-level changes detected._\n")

    return "\n".join(out)


def main() -> int:
    # Force UTF-8 stdout so the unicode arrows etc. render on Windows consoles.
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--no-prev", action="store_true", help="initial-release mode")
    ap.add_argument("prev_or_curr", type=Path, nargs="?")
    ap.add_argument("curr", type=Path, nargs="?")
    ap.add_argument("--esp-name", help="display name for the ESP (default: from _meta.json)")
    ap.add_argument("--max-per-section", type=int, default=0,
                    help="cap number of items per Added/Removed/Changed section "
                         "(0 = no cap)")
    ap.add_argument("--out", type=Path, help="write to file (default: stdout)")
    args = ap.parse_args()

    if args.no_prev:
        if args.prev_or_curr is None:
            ap.error("--no-prev requires <curr-dir>")
        prev_dir, curr_dir = None, args.prev_or_curr
    else:
        if args.prev_or_curr is None or args.curr is None:
            ap.error("need <prev-dir> <curr-dir> (or --no-prev <curr-dir>)")
        prev_dir, curr_dir = args.prev_or_curr, args.curr

    if not curr_dir.is_dir():
        raise SystemExit(f"not a directory: {curr_dir}")
    if prev_dir is not None and not prev_dir.is_dir():
        raise SystemExit(f"not a directory: {prev_dir}")

    out_md = render_diff(prev_dir, curr_dir, esp_name=args.esp_name,
                         max_per_section=args.max_per_section)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(out_md, encoding="utf-8")
        print(f"[diff_records] wrote {args.out} ({len(out_md)} bytes)", file=sys.stderr)
    else:
        sys.stdout.write(out_md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
