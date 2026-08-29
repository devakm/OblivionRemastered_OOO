"""Recent agent sessions joined to the handoff documents they produced."""
import re
import subprocess
import sys
from pathlib import Path

from . import envelope

ITEMCLONE = Path(r"X:\dev\OblivionRemastered_ItemClone")
ROW = re.compile(r"^(\d\d-\d\d \d\d:\d\d)\s+(\d\d-\d\d \d\d:\d\d)\s+(\w{8})\s+(.*)$")
HANDOFF = re.compile(r"^handoff-(\d{4}-\d{2}-\d{2})-([a-z0-9]+)-s\d+-(.+)\.md$", re.I)


def parse_list_sessions(text: str) -> list[dict]:
    rows = []
    for line in text.splitlines():
        m = ROW.match(line.strip())
        if m:
            rows.append({"started": m.group(1), "last_active": m.group(2),
                         "id": m.group(3), "label": m.group(4).strip()})
    return rows


def handoffs(docs: Path) -> list[dict]:
    rows = []
    for p in Path(docs).glob("handoff-*.md"):
        m = HANDOFF.match(p.name)
        if m:
            rows.append({"date": m.group(1), "set_name": m.group(2).lower(),
                         "path": str(p)})
    return sorted(rows, key=lambda r: r["date"], reverse=True)


def collect(limit: int = 10) -> dict:
    try:
        out = subprocess.run([sys.executable, "tools/list_sessions.py", "-n", str(limit)],
                             cwd=ITEMCLONE, capture_output=True, text=True, timeout=60)
        if out.returncode != 0:
            return envelope(None, source="sessions.collect", ok=False,
                            error=out.stderr.strip()[:300] or "list_sessions failed")
        data = {"sessions": parse_list_sessions(out.stdout),
                "handoffs": handoffs(ITEMCLONE / "docs")[:limit]}
    except (OSError, subprocess.SubprocessError) as exc:
        return envelope(None, source="sessions.collect", ok=False, error=str(exc))
    return envelope(data, source="sessions.collect")
