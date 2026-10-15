"""The six existing views, and whether each is current (spec 3.3)."""
from pathlib import Path

from . import envelope

ITEMCLONE = Path(r"X:\dev\OblivionRemastered_ItemClone")
MAPCLONE = Path(r"X:\dev\OblivionRemastered_MapClone")
DEVNULL = Path(r"X:\dev\devnull")

VIEWS = [
    {"name": "review dashboard", "path": ITEMCLONE / "work/pub/dash/index.html",
     "generator": "python tools/review_dash.py", "inputs": [ITEMCLONE / "work/pub/dash"]},
    {"name": "object tuning QC guide",
     "path": ITEMCLONE / "work/object-tuning-qc/amelion/noble/index.html",
     "generator": "python tools/object_tuning_qc.py --set noble",
     "inputs": [ITEMCLONE / "sets/noble"]},
    {"name": "item tracker", "path": ITEMCLONE / "docs/item-tracker.html",
     "generator": "python tools/gen_item_tracker.py", "inputs": [ITEMCLONE / "sets"]},
    {"name": "published docs", "path": DEVNULL / "docs/OOO/OBR/index.html",
     "generator": "python scripts/sync_pages.py", "inputs": [Path(r"X:\dev\OblivionRemastered_OOO\docs")]},
    # The devlog is hand-written in devnull; sync_pages.py never touches it, so
    # it has no generator and no inputs that could prove it current.
    {"name": "devlog", "path": DEVNULL / "docs/OOO/OBR/devlog.html",
     "generator": None, "inputs": []},
]
# MapClone's phase 9 tracker is deliberately NOT a view. It has no generator
# because every row is validated by a person playing the zone in-game, so
# mtime cannot speak to whether it is current and any staleness verdict would
# be a category error. Its progress is reported by collect/maps.py instead.


def _newest_mtime(paths) -> float:
    best = 0.0
    for p in paths:
        p = Path(p)
        if p.is_dir():
            for child in p.rglob("*"):
                if child.is_file():
                    best = max(best, child.stat().st_mtime)
        elif p.exists():
            best = max(best, p.stat().st_mtime)
    return best


def classify(path, inputs) -> str:
    path = Path(path)
    if not path.exists():
        return "STALE"
    if not inputs:
        return "UNKNOWN"          # never green without evidence
    return "STALE" if _newest_mtime(inputs) > path.stat().st_mtime else "FRESH"


def collect() -> dict:
    import time
    rows = []
    for v in VIEWS:
        p = Path(v["path"])
        rows.append({
            "name": v["name"], "path": str(p), "generator": v["generator"],
            "state": classify(p, v["inputs"]),
            "age_days": round((time.time() - p.stat().st_mtime) / 86400, 1) if p.exists() else None,
        })
    return envelope(rows, source="views.collect")
