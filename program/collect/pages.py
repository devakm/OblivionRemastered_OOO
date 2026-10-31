"""Every dashboard, tracker, guide and report across the OOO projects -- the
hub's directory -- plus every page on disk that is NOT registered, so a new
one surfaces instead of getting lost among same-named tabs.

Project codes/colours are the tab identity each generator stamps on its own
pages (tools/tab_id.py in ItemClone and MapRender, program/tab_id.py here).
Freshness is not re-derived: rows that are also a registered view take the
views.collect() verdict by path.
"""
import html
import re
import time
from pathlib import Path

from . import envelope, views

DEV = Path(r"X:\dev")
PROJECTS = {
    "OOO": {"name": "OOO program", "color": "#6b3fa0", "root": DEV / "OblivionRemastered_OOO"},
    "IC": {"name": "ItemClone", "color": "#b8860b", "root": DEV / "OblivionRemastered_ItemClone"},
    "MR": {"name": "MapRender", "color": "#0f766e", "root": DEV / "OblivionRemastered_MapRender"},
    "MC": {"name": "MapClone", "color": "#3f7d20", "root": DEV / "OblivionRemastered_MapClone"},
    "RAX": {"name": "RAX (spawn fixes)", "color": "#a8323e", "root": DEV / "RAX/docs"},
    "PUB": {"name": "devnull (published site)", "color": "#1a4d8f",
            "root": DEV / "devnull/docs/OOO"},
}

IC, MR, MC = (PROJECTS[k]["root"] for k in ("IC", "MR", "MC"))
OBR = PROJECTS["PUB"]["root"] / "OBR"
# (project, kind, label, path, what it answers)
PAGES = [
    ("IC", "review", "Review dash", IC / "work/pub/dash/index.html",
     "Per-object tuning iterations and your rulings, newest target first"),
    ("IC", "tracker", "Item Set Tracker", IC / "docs/item-tracker.html",
     "Every Obsidian/OOO item set and how far along it is"),
    ("IC", "guide", "Noble tuning QC — amelion", IC / "work/object-tuning-qc/amelion/noble/index.html",
     "Per-object off-target severity, built vs vanilla, linked to review logs"),
    ("IC", "guide", "Amelion object guide", IC / "docs/object-guides/amelion/index.html",
     "Object map + names for the Amelion material"),
    ("IC", "guide", "Steel object guide", IC / "docs/object-guides/steel/index.html",
     "Object map + names for the Steel material"),
    ("IC", "review", "SyncMap review", IC / "work/syncmap_review/index.html",
     "MASTER / LIVE / GENERATED SyncMap three-way diff awaiting rulings"),
    ("IC", "report", "Loot Atlas", IC / "work/reports/loot_atlas/index.html",
     "Where each set drops, per player level — aim playtests"),
    ("OOO", "report", "Creature Atlas",
     PROJECTS["OOO"]["root"] / "work/reports/creature_atlas/index.html",
     "Which outdoor spawn lists put which creatures where, per level — gargoyle frequency"),
    ("MR", "review", "Review dash", MR / "out/pub/dash/index.html",
     "Cave map renders and overlays, per zone"),
    ("MC", "tracker", "Phase 9 zone tracker (markdown)", MC / "docs/phase9-unify-tracker.md",
     "Map zones validated in-game, row by row"),
    ("RAX", "report", "OOO Spawn Danger heatmap", DEV / "RAX/docs/ooo-spawn-heatmap.html",
     "How dangerous spawns are by player level and place"),
    ("PUB", "public", "OOORF Release Tracker", OBR / "index.html",
     "The public release page (devakm.github.io/devnull)"),
    ("PUB", "public", "OOORF Devlog", OBR / "devlog.html", "Hand-written per-alpha devlog"),
    ("PUB", "public", "OOORF Changelog", OBR / "changelog.html", "Generated per-release changes"),
    ("PUB", "public", "OOORF New Items", OBR / "new-Items.html", "Public new-item gallery"),
    ("PUB", "public", "OOORF Overview", OBR / "overview.html", "What OOORS Full bundles"),
    ("PUB", "public", "OOORF Install", OBR / "install.html", "Install steps"),
    ("PUB", "public", "OOORF Dependencies", OBR / "dependencies.html", "What users install separately"),
    ("PUB", "classic", "Classic OOO home (2006 game)", PROJECTS["PUB"]["root"] / "OOO_Guide.html",
     "Original Oblivion OOO 1.3x guide — not the Remastered mod"),
    ("PUB", "classic", "Classic OOO FAQ & changelog", PROJECTS["PUB"]["root"] / "OOO_Changelog_FAQ.html",
     "Original OOO 1.3x"),
    ("PUB", "classic", "Classic OOO hints & spoilers", PROJECTS["PUB"]["root"] / "OOO_Spoilers.html",
     "Original OOO 1.3x"),
    ("PUB", "classic", "Classic OOO add-ons", PROJECTS["PUB"]["root"] / "OOO_Add-Ons.html",
     "Original OOO 1.3x"),
    ("PUB", "classic", "Classic OOO 1.32 RC5 known issues", PROJECTS["PUB"]["root"] / "OOO_Problems132RC5.html",
     "Original OOO 1.3x"),
    ("PUB", "classic", "Classic OOO 1.34 readme", PROJECTS["PUB"]["root"] / "OOO_134_readme_viewer.html",
     "Original OOO 1.3x"),
]

# Known non-current copies and experiments; they still show under "other
# pages" (so nothing is hidden) but say what they are.
KNOWN_OTHER = {
    IC / "docs/OOO Loot Atlas.html": "browser 'Save page' copy of the Loot Atlas",
    IC / "work/_tracker_before.html": "old Item Set Tracker snapshot",
    IC / "work/tmp_tracker/item-tracker.html": "scratch Item Set Tracker copy",
    IC / "work/tmp_tracker/old.html": "scratch Item Set Tracker copy",
    IC / "work/syncmap_review_prefix/index.html": "older SyncMap review variant",
    IC / "work/rollup_validate/index.html": "object-guide experiment",
    IC / "work/rollup_piece_test/index.html": "object-guide experiment",
    IC / "work/guide_shield_validate/index.html": "object-guide experiment",
    IC / "work/guide_mockup/mockup.html": "object-guide layout mockup",
}

_SKIP = re.compile(r"[\\/](\.superpowers|node_modules|\.git|\.venv|venv|\.worktrees|worktrees"
                   r"|\.claude|vendor|__pycache__|[^\\/]*_files)[\\/]", re.I)
_DASH_CHILD = re.compile(r"[\\/]pub[\\/]dash[\\/](?!index\.html$)", re.I)
_TITLE = re.compile(r"<title>(.*?)</title>", re.S | re.I)


def _title(p: Path) -> str:
    try:
        m = _TITLE.search(p.read_text(encoding="utf-8", errors="ignore")[:20000])
    except OSError:
        return ""
    return html.unescape(re.sub(r"\s+", " ", m.group(1)).strip()) if m else ""


def _age_days(p: Path):
    return round((time.time() - p.stat().st_mtime) / 86400, 1) if p.exists() else None


def discover(registered: set) -> list:
    """HTML pages under each project root that the registry does not list."""
    out = []
    for code, proj in PROJECTS.items():
        root = proj["root"]
        if not root.exists():
            continue
        for p in root.rglob("*.htm*"):
            s = str(p)
            if (p.suffix.lower() not in (".html", ".htm") or _SKIP.search(s)
                    or _DASH_CHILD.search(s) or p.resolve() in registered):
                continue
            if code == "OOO" and p.parent.name == "program":
                continue          # the hub itself
            out.append({"project": code, "path": s, "url": p.as_uri(),
                        "title": _title(p), "age_days": _age_days(p),
                        "note": KNOWN_OTHER.get(p, "")})
    return sorted(out, key=lambda r: (r["project"], r["age_days"] is None, r["age_days"] or 0))


def collect() -> dict:
    vstate = {}
    venv = views.collect()
    for v in venv["data"] if venv["ok"] else []:
        vstate[str(Path(v["path"]).resolve())] = v
    rows = []
    for code, kind, label, path, about in PAGES:
        v = vstate.get(str(path.resolve()), {})
        rows.append({"project": code, "kind": kind, "label": label, "about": about,
                     "path": str(path), "url": path.as_uri(), "exists": path.exists(),
                     "tab": _title(path) if path.suffix != ".md" else path.name,
                     "age_days": _age_days(path), "state": v.get("state"),
                     "generator": v.get("generator")})
    other = discover({r_path.resolve() for _, _, _, r_path, _ in PAGES})
    return envelope({"projects": {k: {"name": p["name"], "color": p["color"]}
                                  for k, p in PROJECTS.items()},
                     "pages": rows, "other": other}, source="pages.collect")
