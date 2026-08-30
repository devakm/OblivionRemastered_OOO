"""Per-repository run ledgers (spec 3.2).

Append-only .claude/runs.jsonl in each repo, gitignored, machine-local.
Per-repo rather than central so no repo's hook writes into another repo.
"""
import json
import subprocess
from pathlib import Path

from . import envelope
from .repos import REPOS, SHORT

LEDGER_NAME = ".claude/runs.jsonl"


def ledger(repo: Path) -> Path:
    return Path(repo) / LEDGER_NAME


def append(repo: Path, record: dict) -> None:
    path = ledger(repo)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record) + "\n")


def proc_start(pid: int) -> str | None:
    """Process start time, or None if no such process. Monkeypatched in tests."""
    out = subprocess.run(
        ["powershell", "-NoProfile", "-Command",
         f"(Get-Process -Id {int(pid)} -ErrorAction SilentlyContinue)"
         f".StartTime.ToString('o')"],
        capture_output=True, text=True, timeout=20)
    return out.stdout.strip() or None


def status_of(record: dict) -> str:
    if record.get("ended"):
        return "done"
    pid = record.get("pid")
    if not pid:
        return "orphaned"          # no handle -- e.g. a background subagent
    return "running" if proc_start(pid) == record.get("proc_started") else "orphaned"


def read(repo: Path) -> list[dict]:
    path = ledger(repo)
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                rows.append(json.loads(line))
            except ValueError:
                continue
    return rows


def sweep(repo: Path) -> int:
    """Mark dead unfinished records orphaned. Returns how many changed."""
    rows, changed = read(repo), 0
    for r in rows:
        new = status_of(r)
        if r.get("status") != new and new != "running":
            r["status"], changed = new, changed + 1
    if changed:
        ledger(repo).write_text(
            "".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
    return changed


def collect() -> dict:
    data = []
    for repo in REPOS:
        if not (repo / ".git").exists():
            continue
        for r in read(repo):
            r = dict(r, repo=SHORT[repo.name], status=r.get("status") or status_of(r))
            data.append(r)
    return envelope(data, source="runs.collect")
