"""Declared program state, checked against evidence (spec 3.6).

Three states only. MET requires a registered check that agrees.
CONTRADICTED is a registered check that denies. UNVERIFIED is a claim with
no registered check -- amber, never green. A dashboard that renders
unverifiable claims as green is the failure these gates exist to prevent.
"""
import subprocess
from pathlib import Path

import yaml

from . import envelope

OOO = Path(r"X:\dev\OblivionRemastered_OOO")
CONFIG = OOO / "program" / "program.yaml"
REPO_PATHS = {"ItemClone": Path(r"X:\dev\OblivionRemastered_ItemClone"),
              "MapClone": Path(r"X:\dev\OblivionRemastered_MapClone"),
              "OOO": OOO}


def _check_merged(c: dict) -> bool:
    repo = REPO_PATHS.get(c.get("repo"))
    if not repo or not (repo / ".git").exists():
        return False
    out = subprocess.run(["git", "-C", str(repo), "branch", "--merged", "main"],
                         capture_output=True, text=True, timeout=30)
    return c.get("branch", "") in out.stdout.replace("*", "").split()


def _check_manifest_exists(c: dict) -> bool:
    return (OOO / "manifests" / f'{c.get("tag")}.json').exists()


CHECKS = {"merged": _check_merged, "manifest_exists": _check_manifest_exists}


def evaluate(criterion: dict) -> str:
    check = criterion.get("check") or {}
    fn = CHECKS.get(check.get("kind"))
    if fn is None:
        return "UNVERIFIED"
    return "MET" if fn(check) else "CONTRADICTED"


def collect(config_path: Path | None = None) -> dict:
    path = Path(config_path or CONFIG)
    try:
        cfg = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return envelope(None, source="milestones.collect", ok=False, error=str(exc))

    milestones = []
    for m in cfg.get("milestones", []):
        crits = [dict(c, state=evaluate(c)) for c in (m.get("criteria") or [])]
        milestones.append({"name": m["name"], "status": m.get("status", "not_started"),
                           "criteria": crits})
    nxt = next((m for m in milestones if m["status"] == "in_progress"),
               milestones[-1] if milestones else {"name": "—", "criteria": []})
    data = {"goal": cfg.get("goal", ""), "current_focus": cfg.get("current_focus", ""),
            "milestones": milestones, "branches": cfg.get("branches", {}),
            "next": {"name": nxt["name"],
                     "unmet": [c for c in nxt.get("criteria", []) if c["state"] != "MET"]}}
    return envelope(data, source="milestones.collect")
