"""MapClone water/diagnostic plots -- the newest review artifacts (spec 3.x).

Why this is a collector and not a view: a plot is not a single regenerated
file with a freshness verdict. Each run writes a NEW timestamped png, so the
honest reading is "here are the most recent ones, and when they landed" --
mtime is the content, not a staleness signal.

Canonical producers (do not add ad-hoc variants -- see MapClone CLAUDE.md):
    work/plot_water_xy_actual.py     single-test XY, --cell for any cell
    work/plot_water_analysis.py      cumulative XY grid
    work/plot_water_z_analysis.py    YZ side view

Both output folders are read: plots/ is the review copy the user browses and
work/tests/water/ is the pre-build gate copy. A plot present ONLY in the gate
folder is still reported, flagged gate_only, because that asymmetry is exactly
the bug that made new plots invisible for review.
"""
import time
from pathlib import Path

from . import envelope

MAPCLONE = Path(r"X:\dev\OblivionRemastered_MapClone")
REVIEW_DIR = MAPCLONE / "plots"
GATE_DIR = MAPCLONE / "work" / "tests" / "water"
LIMIT = 12

# Scripts that write ONLY the gate copy, by design and by explicit comment in
# their source. A gate-only plot from anything else is the dual-save bug.
SINGLE_SAVE_PREFIXES = ("water_analysis_", "water_z_analysis_")


def _rows(limit: int = LIMIT) -> list[dict]:
    seen: dict[str, dict] = {}
    for folder, gate in ((REVIEW_DIR, False), (GATE_DIR, True)):
        if not folder.is_dir():
            continue
        for p in folder.glob("*.png"):
            row = seen.get(p.name)
            if row is None:
                st = p.stat()
                seen[p.name] = {
                    "name": p.name,
                    "mtime": st.st_mtime,
                    "age_hours": round((time.time() - st.st_mtime) / 3600, 1),
                    "kb": round(st.st_size / 1024),
                    # file:// so the dashboard opens it straight from disk
                    "url": p.resolve().as_uri(),
                    "in_review": not gate,
                    "in_gate": gate,
                }
            else:
                row["in_gate"] = row["in_gate"] or gate
                row["in_review"] = row["in_review"] or not gate
    rows = sorted(seen.values(), key=lambda r: -r["mtime"])[:limit]
    for r in rows:
        r["gate_only"] = r["in_gate"] and not r["in_review"]
        # Gate-only is normal for the two scripts that single-save BY DESIGN
        # (plot_water_analysis.py, plot_water_z_analysis.py -- both carry a
        # "write ONLY to work/tests/water/" comment). Flagging those as
        # anomalies buries the one row that is genuinely wrong: a single-test
        # XY plot never copied for review is the dual-save regression.
        r["expected_gate_only"] = r["name"].startswith(SINGLE_SAVE_PREFIXES)
        r["unexpected"] = r["gate_only"] and not r["expected_gate_only"]
    return rows


def collect() -> dict:
    try:
        rows = _rows()
        data = {
            "plots": rows,
            "review_dir": str(REVIEW_DIR),
            "gate_dir": str(GATE_DIR),
            "gate_only_count": sum(1 for r in rows if r["gate_only"]),
            "unexpected_count": sum(1 for r in rows if r["unexpected"]),
            "newest_age_hours": rows[0]["age_hours"] if rows else None,
        }
    except OSError as exc:
        return envelope(None, source="plots.collect", ok=False, error=str(exc))
    return envelope(data, source="plots.collect")
