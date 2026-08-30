"""Outstanding map cells, read from MapClone's phase 9 tracker.

The tracker is hand-maintained, so mtime says nothing useful about it -- it
has no generator and no inputs, which is why the Views panel can only ever
call it UNKNOWN. Its *content*, though, is machine-readable: a row carrying
the hourglass marker is a zone built but not yet validated in-game. That is
the signal worth surfacing, rather than a staleness verdict we cannot make.
"""
from pathlib import Path

from . import envelope

TRACKER = Path(r"X:\dev\OblivionRemastered_MapClone\docs\phase9-unify-tracker.md")
PENDING = "\u23f3"          # hourglass: built, awaiting in-game validation


def pending_cells(path=TRACKER) -> list[dict]:
    path = Path(path)
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or PENDING not in line:
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cols or set(cols[0]) <= set("-: "):
            continue
        rows.append({"cell": cols[0], "donor": cols[1] if len(cols) > 1 else "",
                     "note": cols[-1] if len(cols) > 2 else ""})
    return rows


def collect() -> dict:
    try:
        rows = pending_cells()
    except OSError as exc:
        return envelope(None, source="maps.collect", ok=False, error=str(exc))
    return envelope({"pending": rows, "tracker": str(TRACKER),
                     "tracker_exists": TRACKER.exists()}, source="maps.collect")
