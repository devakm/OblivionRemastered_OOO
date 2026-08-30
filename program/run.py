"""Run-ledger CLI (spec 3.2).

  py -3 program/run.py note --repo <path> --kind agent --purpose "..."
  py -3 program/run.py sweep
"""
import argparse
import sys
import uuid
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from program.collect import runs  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("note", help="record work that has no process handle")
    n.add_argument("--repo", default=".")
    n.add_argument("--kind", default="other",
                   choices=["build", "server", "agent", "other"])
    n.add_argument("--purpose", required=True)
    n.add_argument("--pid", type=int, default=None)
    n.add_argument("--session", default=None)
    sub.add_parser("sweep", help="mark dead records orphaned in every repo")
    a = ap.parse_args()

    if a.cmd == "note":
        runs.append(Path(a.repo), {
            "id": uuid.uuid4().hex[:8],
            "started": datetime.now().isoformat(timespec="seconds"),
            "kind": a.kind, "cmd": None, "cwd": str(Path(a.repo).resolve()),
            "pid": a.pid,
            "proc_started": runs.proc_start(a.pid) if a.pid else None,
            "session": a.session, "purpose": a.purpose,
            "ended": None, "status": "running" if a.pid else "orphaned"})
        return 0

    total = sum(runs.sweep(r) for r in runs.REPOS if (r / ".git").exists())
    print(f"swept: {total} record(s) marked orphaned")
    return 0


if __name__ == "__main__":
    sys.exit(main())
