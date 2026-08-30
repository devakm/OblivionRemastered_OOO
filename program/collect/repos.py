"""Branch and working-tree state across the OOO program (spec 3.4).

Narratives come from ItemClone's git_narrative.py -- the only sanctioned
source. Structural queries (ahead/behind, merged, remotes) use plumbing
that produces no narrative.
"""
import subprocess
from pathlib import Path

from . import envelope

DEV = Path(r"X:\dev")
REPOS = [DEV / n for n in (
    "OblivionRemastered_ItemClone", "OblivionRemastered_MapClone",
    "OblivionRemastered_OOO", "OblivionRemastered_CrashTools",
    "OblivionRemastered_PluginTools", "OblivionRemastered_SCDA_message_patcher",
    "devnull")]
SHORT = {p.name: p.name.replace("OblivionRemastered_", "") for p in REPOS}


def _git(repo: Path, *args: str) -> str:
    out = subprocess.run(["git", "-C", str(repo), *args],
                         capture_output=True, text=True, timeout=30)
    return out.stdout.strip()


def bucket(branch: dict) -> str:
    if branch.get("merged"):
        return "merged-undeleted"
    return "open-ahead" if branch.get("ahead", 0) > 0 else "in-sync"


def _repo_row(repo: Path, annotations: dict) -> dict:
    short = SHORT[repo.name]
    main = "main" if _git(repo, "rev-parse", "--verify", "-q", "main") else "master"
    merged = set(_git(repo, "branch", "--merged", main).replace("*", "").split())
    rows = []
    for line in _git(repo, "for-each-ref", "--sort=-committerdate",
                     "--format=%(refname:short)|%(committerdate:short)",
                     "refs/heads/").splitlines():
        name, _, last = line.partition("|")
        if not name or name == main:
            continue
        counts = _git(repo, "rev-list", "--left-right", "--count", f"{main}...{name}").split()
        behind, ahead = (int(counts[0]), int(counts[1])) if len(counts) == 2 else (0, 0)
        b = {"name": name, "last": last, "ahead": ahead, "behind": behind,
             "merged": name in merged, "subject": _git(repo, "log", "-1", "--format=%s", name)}
        b["bucket"] = bucket(b)
        b["intent"] = annotations.get(f"{short}/{name}", "unexplained")
        rows.append(b)
    dirty = len([l for l in _git(repo, "status", "--porcelain").splitlines() if l.strip()])
    return {"repo": short, "head": _git(repo, "rev-parse", "--abbrev-ref", "HEAD"),
            "dirty": dirty, "has_remote": bool(_git(repo, "remote")), "branches": rows}


def collect(annotations: dict | None = None) -> dict:
    annotations = annotations or {}
    try:
        data = [_repo_row(r, annotations) for r in REPOS if (r / ".git").exists()]
    except (OSError, subprocess.SubprocessError) as exc:
        return envelope(None, source="repos.collect", ok=False, error=str(exc))
    return envelope(data, source="repos.collect")
