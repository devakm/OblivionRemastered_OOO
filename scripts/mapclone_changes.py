#!/usr/bin/env python3
"""
Summarize MapClone per-cell map changes between a baseline date and now, for
the OOO per-release notes "Map cell changes" section.

This REUSES MapClone's authoritative config artifacts as the source of truth --
it does NOT parse the ESP (REFR INITIALLY_DISABLED flags etc. are enumerated in
the configs; `fix_ooo_flickering.py` is what applies them). Sources:

  - ooo_flicker_config.json
        architecture_disable_refrs  (cell -> [REFR FormIDs] disabled so the
                                     TES4 copy is suppressed and only the UE5
                                     baked geometry renders)
        position_overrides          (cell -> [entries] z/xy corrections)
  - ue4ss_mods/Begone/Config/OscurosOblivionOverhaul.v?.json
        ghost suppression (cell -> [entries]); version-stamped, newest wins.
  - ooo_exterior_foliage_config.json
        cave-entrance foliage shifts (cell -> {...})

Baseline = the MapClone commit as of a given ISO datetime (the prior release's
tag date). All diffs are baseline -> current working tree. If MapClone is
absent or a config can't be read, that part is skipped (never fatal).

Usage (standalone, for testing):
    py -3 scripts/mapclone_changes.py --before 2026-05-18T04:46:53-05:00 \
        --prev-tag alpha90
    py -3 scripts/mapclone_changes.py --before <iso> --prev-tag alpha90 \
        --mapclone X:/dev/OblivionRemastered_MapClone
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

DEFAULT_MAPCLONE = Path(r"X:\dev\OblivionRemastered_MapClone")

FLICKER_REL = "ooo_flicker_config.json"
EXTERIOR_REL = "ooo_exterior_foliage_config.json"
# Ghost-suppression source: the Begone STATIC-PATCHER INPUT (baked into the map
# paks at build time; the runtime Config/*.json is empty in v3 static-patch
# mode). Version-stamped; newest present wins at each ref. Per-cell data is
# nested under the "Cells" key, keyed by L_<level> name.
BEGONE_CANDIDATES = (
    "ue4ss_mods/Begone/_StaticPatcherInput/OscurosOblivionOverhaul.v2.json",
    "ue4ss_mods/Begone/_StaticPatcherInput/OscurosOblivionOverhaul.json",
)


# --- git / json helpers ---------------------------------------------------- #

def _git(mapclone: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(mapclone), *args], capture_output=True)


def _loads(raw: bytes | str | None):
    if raw is None:
        return None
    if isinstance(raw, bytes):
        raw = raw.decode("utf-8-sig", errors="replace")
    try:
        return json.loads(raw)
    except Exception:
        return None


def _show_json(mapclone: Path, ref: str, path: str):
    r = _git(mapclone, "show", f"{ref}:{path}")
    return _loads(r.stdout) if r.returncode == 0 else None


def _read_json(mapclone: Path, path: str):
    p = mapclone / path
    if not p.is_file():
        return None
    return _loads(p.read_text(encoding="utf-8-sig", errors="replace"))


def _exists_at(mapclone: Path, ref: str, path: str) -> bool:
    return _git(mapclone, "cat-file", "-e", f"{ref}:{path}").returncode == 0


def resolve_baseline(mapclone: Path, before_iso: str) -> str | None:
    r = _git(mapclone, "rev-list", "-1", f"--before={before_iso}", "HEAD")
    c = r.stdout.decode("utf-8", errors="replace").strip()
    return c or None


def _begone_rel_at(mapclone: Path, ref: str | None) -> str | None:
    for rel in BEGONE_CANDIDATES:
        if ref is None:
            if (mapclone / rel).is_file():
                return rel
        elif _exists_at(mapclone, ref, rel):
            return rel
    return None


# --- per-cell delta primitives --------------------------------------------- #

def _cell_keys(d: dict | None) -> set[str]:
    return {k for k in (d or {}) if not k.startswith("_")} if isinstance(d, dict) else set()


def _fids(entries) -> set[str]:
    """FormID set from a cell's entry list. Entries are dicts ({'formid': ...})
    or, defensively, bare hashable values."""
    out: set[str] = set()
    for e in entries or []:
        if isinstance(e, dict):
            fid = e.get("formid")
            if fid is not None:
                out.add(str(fid))
        else:
            out.add(str(e))
    return out


def _delta_setvalued(prev: dict | None, cur: dict | None) -> dict:
    """For cell -> [entries-keyed-by-formid] maps (disabled REFRs): per-cell
    added count via FormID set difference. Returns totals + per-cell added."""
    prev = prev or {}
    cur = cur or {}
    per_cell = {}
    for cell in _cell_keys(cur):
        cv = _fids(cur.get(cell))
        pv = _fids(prev.get(cell))
        added = len(cv - pv)
        if added:
            per_cell[cell] = {"added": added, "total": len(cv), "new_cell": cell not in prev}
    return {
        "prev_cells": len(_cell_keys(prev)),
        "cur_cells": len(_cell_keys(cur)),
        "prev_entries": sum(len(prev.get(c) or []) for c in _cell_keys(prev)),
        "cur_entries": sum(len(cur.get(c) or []) for c in _cell_keys(cur)),
        "per_cell": per_cell,
    }


def _delta_countvalued(prev: dict | None, cur: dict | None) -> dict:
    """For cell -> [non-hashable entries] maps (e.g. position_overrides, Begone
    entries): per-cell delta by count (entries may be dicts, not set-diffable)."""
    prev = prev or {}
    cur = cur or {}
    per_cell = {}
    for cell in _cell_keys(cur):
        cn = len(cur.get(cell) or [])
        pn = len(prev.get(cell) or [])
        if cn != pn or cell not in prev:
            per_cell[cell] = {"delta": cn - pn, "total": cn, "new_cell": cell not in prev}
    return {
        "prev_cells": len(_cell_keys(prev)),
        "cur_cells": len(_cell_keys(cur)),
        "prev_entries": sum(len(prev.get(c) or []) for c in _cell_keys(prev)),
        "cur_entries": sum(len(cur.get(c) or []) for c in _cell_keys(cur)),
        "per_cell": per_cell,
    }


# --- top-level compute ----------------------------------------------------- #

def compute_changes(mapclone: Path, before_iso: str) -> dict | None:
    """Return structured deltas, or None if MapClone/baseline unavailable."""
    if not (mapclone / ".git").is_dir() and not (mapclone / ".git").is_file():
        return None
    baseline = resolve_baseline(mapclone, before_iso)
    if not baseline:
        return None

    flick_prev = _show_json(mapclone, baseline, FLICKER_REL)
    flick_cur = _read_json(mapclone, FLICKER_REL)
    ext_prev = _show_json(mapclone, baseline, EXTERIOR_REL)
    ext_cur = _read_json(mapclone, EXTERIOR_REL)

    beg_prev_rel = _begone_rel_at(mapclone, baseline)
    beg_cur_rel = _begone_rel_at(mapclone, None)
    beg_prev = _show_json(mapclone, baseline, beg_prev_rel) if beg_prev_rel else None
    beg_cur = _read_json(mapclone, beg_cur_rel) if beg_cur_rel else None

    out = {"baseline": baseline[:12], "baseline_full": baseline}
    if flick_cur is not None:
        out["disable"] = _delta_setvalued(
            (flick_prev or {}).get("architecture_disable_refrs"),
            flick_cur.get("architecture_disable_refrs"))
        out["overrides"] = _delta_countvalued(
            (flick_prev or {}).get("position_overrides"),
            flick_cur.get("position_overrides"))
    if beg_cur is not None:
        # Per-cell suppression lives under "Cells" (keyed by L_<level>).
        out["begone"] = _delta_countvalued(
            (beg_prev or {}).get("Cells"), beg_cur.get("Cells"))
        out["begone_versioned"] = (beg_prev_rel != beg_cur_rel)
    if ext_cur is not None:
        prev_cells = _cell_keys(ext_prev)
        cur_cells = _cell_keys(ext_cur)
        out["exterior"] = {
            "added_cells": sorted(cur_cells - prev_cells),
            "cur_cells": sorted(cur_cells),
        }
    return out


# --- markdown rendering ---------------------------------------------------- #

def _render_setvalued(title: str, d: dict, noun: str, limit: int) -> list[str]:
    out = [f"### {title}\n"]
    out.append(f"+{d['cur_entries'] - d['prev_entries']} {noun} "
               f"({d['prev_entries']} → {d['cur_entries']}; "
               f"{d['prev_cells']} → {d['cur_cells']} cells)\n")
    rows = sorted(d["per_cell"].items(), key=lambda kv: (-kv[1]["added"], kv[0]))
    for cell, info in rows[:limit]:
        tag = " *(new cell)*" if info["new_cell"] else ""
        out.append(f"- **{cell}**: +{info['added']} (total {info['total']}){tag}")
    if len(rows) > limit:
        out.append(f"_…{len(rows) - limit} more cells_")
    out.append("")
    return out


def _render_countvalued(title: str, d: dict, noun: str, limit: int,
                        versioned: bool = False) -> list[str]:
    out = [f"### {title}\n"]
    note = "  _(config version changed; deltas approximate)_" if versioned else ""
    out.append(f"net {d['cur_entries'] - d['prev_entries']:+d} {noun} "
               f"({d['prev_entries']} → {d['cur_entries']}; "
               f"{d['prev_cells']} → {d['cur_cells']} cells){note}\n")
    rows = sorted(d["per_cell"].items(), key=lambda kv: (-kv[1]["delta"], kv[0]))
    for cell, info in rows[:limit]:
        tag = " *(new cell)*" if info["new_cell"] else ""
        out.append(f"- **{cell}**: {info['delta']:+d} (total {info['total']}){tag}")
    if len(rows) > limit:
        out.append(f"_…{len(rows) - limit} more cells_")
    out.append("")
    return out


def render_section(changes: dict, prev_tag: str | None, limit: int = 0) -> str:
    if not changes:
        return ""
    lim = limit if limit > 0 else 10_000
    since = f" since `{prev_tag}`" if prev_tag else ""
    out = [f"## Map cell changes{since}\n"]
    out.append("UE5-layer map work, sourced from MapClone configs "
               f"(baseline `{changes['baseline']}`).\n")
    if changes.get("disable") and changes["disable"]["per_cell"]:
        out += _render_setvalued(
            "UE5-layer object suppression (ESP `INITIALLY_DISABLED`)",
            changes["disable"], "disabled REFRs", lim)
    if changes.get("overrides") and changes["overrides"]["per_cell"]:
        out += _render_countvalued(
            "REFR position overrides", changes["overrides"], "overrides", lim)
    if changes.get("begone") and changes["begone"]["per_cell"]:
        out += _render_countvalued(
            "Ghost suppression (Begone)", changes["begone"], "entries", lim,
            versioned=changes.get("begone_versioned", False))
    if changes.get("exterior") and changes["exterior"]["added_cells"]:
        out.append("### Exterior foliage fixes\n")
        for c in changes["exterior"]["added_cells"]:
            out.append(f"- **{c}** *(new)*")
        out.append("")
    # If nothing had per-cell deltas, say so rather than emit an empty header.
    if len(out) <= 2:
        return ""
    return "\n".join(out)


def build_section(mapclone: Path, before_iso: str, prev_tag: str | None,
                  limit: int = 0) -> str:
    changes = compute_changes(mapclone, before_iso)
    return render_section(changes, prev_tag, limit) if changes else ""


def main(argv=None) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--before", required=True,
                    help="ISO datetime of the prior release tag (baseline cutoff)")
    ap.add_argument("--prev-tag", default=None, help="prior release tag name (for the header)")
    ap.add_argument("--mapclone", type=Path, default=DEFAULT_MAPCLONE)
    ap.add_argument("--limit", type=int, default=0, help="max cells per subsection (0 = all)")
    args = ap.parse_args(argv)
    section = build_section(args.mapclone, args.before, args.prev_tag, args.limit)
    if not section:
        print("(no MapClone map-cell changes / MapClone unavailable)", file=sys.stderr)
        return 0
    sys.stdout.write(section + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
