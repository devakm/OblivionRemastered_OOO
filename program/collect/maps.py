"""MapClone phase 9 zone validation -- a human-gated progress tracker.

This is NOT a generated view, which is why it is deliberately absent from
views.VIEWS: there is no generator to re-run and mtime proves nothing about
it. Every row is validated by a person playing the zone in-game, and only
flips to confirmed when the user says so. So the honest reading is its
CONTENT -- how many zones are confirmed, which remain -- plus the git
activity showing work in flight on the ones that remain, since that work
lands well before a row is allowed to flip.

Narratives come from ItemClone's git_narrative.py, the only sanctioned
source; --repo exists precisely so it can read MapClone.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

from . import envelope

MAPCLONE = Path(r"X:\dev\OblivionRemastered_MapClone")
TRACKER = MAPCLONE / "docs" / "phase9-unify-tracker.md"
GIT_NARRATIVE = Path(r"X:\dev\OblivionRemastered_ItemClone\tools\git_narrative.py")

PENDING = "\u23f3"          # hourglass: built, awaiting in-game validation
CONFIRMED = "\u2713"        # check: confirmed in-game by a human
ZONE = re.compile(r"^(?P<cell>[A-Z][^|(]*\((?P<edid>[A-Za-z0-9_]+)\))\s*$")


def zones(path=TRACKER) -> list[dict]:
    """Every tracked zone row. Legend rows have no `Name (EDID)` first cell."""
    path = Path(path)
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cols) < 2:
            continue
        m = ZONE.match(cols[0])
        if not m:
            continue                      # legend / header / prose row
        state = ("pending" if PENDING in line
                 else "confirmed" if CONFIRMED in line else "untested")
        rows.append({"cell": m.group("cell").strip(), "edid": m.group("edid"),
                     "donor": cols[1], "state": state, "note": cols[-1]})
    return rows


def pending_cells(path=TRACKER) -> list[dict]:
    return [z for z in zones(path) if z["state"] == "pending"]


def cave_of(cell: str) -> str:
    """'Gloom Way Cave (GloomWayCave02)' -> 'Gloom Way Cave'. Zones group by cave."""
    return cell.split("(")[0].strip()


def _initials(cave: str) -> str:
    """'Gloom Way Cave' -> 'gwc'. Commit subjects use these, e.g. GWCz1/RGCz1."""
    return "".join(w[0] for w in cave.split() if w).lower()


def recent_activity(terms, since: str = "2026-08-01", limit: int = 8) -> list[str]:
    """Commits in MapClone naming an outstanding zone -- work in flight.

    Matters because a row only flips after a human validates it, so the tracker
    lags the work by design. Without this, live effort looks like no progress.
    """
    needles = {t.lower() for t in terms if t}
    if not needles:
        return []
    try:
        # git_narrative decodes git as UTF-8, so decode its output the same way.
        # The locale default (cp1252 on Windows) turns em-dashes into mojibake.
        out = subprocess.run(
            [sys.executable, str(GIT_NARRATIVE), "--repo", str(MAPCLONE),
             "--since", since], capture_output=True, text=True, timeout=60,
            encoding="utf-8", errors="replace",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    except (OSError, subprocess.SubprocessError):
        return []
    if out.returncode != 0:
        return []
    hits = []
    for line in out.stdout.splitlines():
        low = line.lower()
        if any(n in low for n in needles):
            hits.append(line.strip())
            if len(hits) >= limit:
                break
    return hits


def collect() -> dict:
    try:
        rows = zones()
        pending = [z for z in rows if z["state"] == "pending"]
        confirmed = [z for z in rows if z["state"] == "confirmed"]
        caves = sorted({cave_of(z["cell"]) for z in pending})
        terms = ([z["edid"] for z in pending] + caves
                 + [_initials(c) for c in caves])
        data = {"zones": rows, "pending": pending, "caves": caves,
                "confirmed_count": len(confirmed), "pending_count": len(pending),
                "total": len(rows), "tracker": str(TRACKER),
                "tracker_exists": TRACKER.exists(),
                "recent": recent_activity(terms)}
    except OSError as exc:
        return envelope(None, source="maps.collect", ok=False, error=str(exc))
    return envelope(data, source="maps.collect")
