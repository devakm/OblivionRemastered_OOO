#!/usr/bin/env python3
"""
End-to-end release command for the v2 architecture.

For one tag this script does, in order:

  0. Check SyncMap drift via `sync_syncmap.py diff-check`. If drift is
     detected, ABORT and tell the user to run the 3-gate fix workflow
     (sync-content → apply-swap, with reviews between each phase). There
     is no shortcut flag — release is blocked until the workflow has
     been completed and diff-check returns 0.
  1. Validate the working tree (no unrelated WIP).
  2. Hash everything in release/ (text + binaries; skipping co-files and
     records bundles) → write manifests/<tag>.json.
  3. Parse every ESP/ESM in release/ → write the matching .records/
     directory bundle.
  4. Compute SHA-256 + size for every gitignored binary and append/update
     its <binary>.md co-file row for this tag.
  5. Diff vs the prior tag's manifest + ESP inventories → write
     docs/per-release/<tag>.md.
  6. git add release/ manifests/ docs/per-release/ → commit (subject =
     tag) → git tag <tag>.
  7. Build dist/<tag>.7z from release/ EXCLUDING *.md and *.records/.

If --for-real is passed, additionally:
  8. git push origin main
     git push origin <tag>
     gh release create <tag> dist/<tag>.7z --title <tag> --notes-file
                            docs/per-release/<tag>.md --latest|--prerelease

Without --for-real every external side effect (git push, gh release) is
printed but not executed. Local file/git operations always run.

Usage:
    py -3 scripts/release.py alpha91 --latest --for-real
    py -3 scripts/release.py alpha91 --prerelease     # local-only dry-publish
    py -3 scripts/release.py alpha91 --dry-run        # print every action
    py -3 scripts/release.py alpha91 --force          # overwrite existing tag
    py -3 scripts/release.py alpha91 --skip-syncmap   # skip SyncMap regen
    py -3 scripts/release.py alpha91 --skip-records   # skip ESP inventories
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RELEASE_DIR = REPO_ROOT / "release"
MANIFEST_DIR = REPO_ROOT / "manifests"
PER_RELEASE_DOC_DIR = REPO_ROOT / "docs" / "per-release"
DIST_DIR = REPO_ROOT / "dist"

# Extensions that identify binary files needing a .md co-file. Everything
# else committed in release/ is text and lives directly in the repo.
BINARY_EXTS = frozenset({
    ".esp", ".esm",
    ".pak", ".ucas", ".utoc",
    ".dll", ".exe",
    ".dds", ".tga", ".png", ".jpg", ".jpeg", ".webp",
    ".uasset", ".uexp", ".umap", ".bsa",
})

# ESP/ESM specifically — these get .records/ inventories (parsed by Wrye Bash).
ESP_EXTS = frozenset({".esp", ".esm"})


# --------------------------------------------------------------------------- #
# Working-tree helpers
# --------------------------------------------------------------------------- #

def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=REPO_ROOT,
                          capture_output=True, text=True, check=check)


def working_tree_clean_outside(allowed_prefixes: tuple[str, ...]) -> bool:
    r = git("status", "--porcelain")
    for line in r.stdout.splitlines():
        if len(line) < 4:
            continue
        path = line[3:].strip().strip('"')
        if not any(path.startswith(p) for p in allowed_prefixes):
            return False
    return True


def tag_exists(tag: str) -> bool:
    return git("rev-parse", "--verify", "--quiet", f"refs/tags/{tag}",
               check=False).returncode == 0


def latest_main_tag(exclude: str) -> str | None:
    r = git("tag", "--merged", "main", "--sort=v:refname", check=False)
    if r.returncode != 0:
        return None
    tags = [t.strip() for t in r.stdout.splitlines() if t.strip() and t.strip() != exclude]
    return tags[-1] if tags else None


# --------------------------------------------------------------------------- #
# File walking — what's a release file vs metadata
# --------------------------------------------------------------------------- #

def iter_release_files(root: Path):
    """Yield every file in `release/` that is part of the SHIPPED release —
    excludes our metadata (`.md` co-files anywhere, `.records/` directory
    contents, top-level `.gitkeep`).
    """
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        # Skip co-files (any *.md sibling to a binary).
        if p.suffix == ".md":
            continue
        # Skip anything under a *.records/ directory.
        if any(part.endswith(".records") for part in p.parts):
            continue
        # Skip placeholder
        if p.name == ".gitkeep":
            continue
        yield p


def iter_release_binaries(root: Path):
    """Yield every binary file (by extension) in release/."""
    for p in iter_release_files(root):
        if p.suffix.lower() in BINARY_EXTS:
            yield p


def iter_release_esps(root: Path):
    """Yield every ESP/ESM in release/."""
    for p in iter_release_files(root):
        if p.suffix.lower() in ESP_EXTS:
            yield p


# --------------------------------------------------------------------------- #
# Step implementations
# --------------------------------------------------------------------------- #

def step_check_syncmaps(dry: bool) -> None:
    """Step 0 — verify SyncMap drift via `sync_syncmap.py diff-check`.

    If drift is detected, ABORT. There is no shortcut flag. The user must
    run the 3-gate fix workflow (sync-content → apply-swap, with reviews
    between phases) before re-running release.py.
    """
    del dry  # check is read-only; always runs
    print(f"[release] step 0: check SyncMap drift", flush=True)
    check_cmd = [sys.executable, str(REPO_ROOT / "scripts" / "sync_syncmap.py"),
                 "diff-check", "--target", str(RELEASE_DIR)]
    rc = subprocess.run(check_cmd, cwd=REPO_ROOT).returncode
    if rc == 0:
        return
    # Drift detected — block release. No bypass.
    print("", file=sys.stderr, flush=True)
    print("[release] STOP: SyncMap drift detected. Release is blocked until",
          file=sys.stderr, flush=True)
    print("the 3-gate fix workflow has been completed:", file=sys.stderr, flush=True)
    print("", file=sys.stderr, flush=True)
    print("  GATE 1 -- Open VS Code diff between the two release SyncMap INIs",
          file=sys.stderr, flush=True)
    print("            and review that all intended changes are in Deluxe.",
          file=sys.stderr, flush=True)
    print("  ACTION -- py -3 scripts/sync_syncmap.py sync-content",
          file=sys.stderr, flush=True)
    print("  GATE 2 -- Review the auto-refreshed diff (should be empty).",
          file=sys.stderr, flush=True)
    print("  ACTION -- py -3 scripts/sync_syncmap.py apply-swap",
          file=sys.stderr, flush=True)
    print("  GATE 3 -- Review the auto-refreshed diff (~72 toggle-only lines).",
          file=sys.stderr, flush=True)
    print("", file=sys.stderr, flush=True)
    print("Then re-run release.py.", file=sys.stderr, flush=True)
    raise SystemExit(2)


def step_validate_tree(tag: str, force: bool, dry: bool) -> None:
    """Step 1 — assert clean tree outside our workspace dirs + tag handling."""
    print(f"[release] step 1: validate working tree + tag {tag!r}", flush=True)
    if not working_tree_clean_outside(("release/", "manifests/", "docs/per-release/")):
        raise SystemExit(
            "working tree has uncommitted changes outside release/, manifests/, "
            "docs/per-release/. Commit or stash them first."
        )
    if tag_exists(tag):
        if not force:
            raise SystemExit(f"tag {tag!r} already exists. Pass --force to overwrite.")
        if not dry:
            print(f"  --force: deleting existing local tag {tag}", flush=True)
            git("tag", "-d", tag)


def step_hash_manifest(tag: str, dry: bool) -> dict[str, dict]:
    """Step 2 — hash every file in release/ → manifests/<tag>.json."""
    print(f"[release] step 2: hash release/ → manifests/{tag}.json", flush=True)
    manifest: dict[str, dict] = {}
    for p in iter_release_files(RELEASE_DIR):
        rel = p.relative_to(RELEASE_DIR).as_posix()
        sha = hashlib.sha256(p.read_bytes()).hexdigest()
        manifest[rel] = {"sha256": sha, "size": p.stat().st_size}
    manifest = dict(sorted(manifest.items()))
    out_path = MANIFEST_DIR / f"{tag}.json"
    print(f"  {len(manifest)} files hashed → {out_path}", flush=True)
    if not dry:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                            encoding="utf-8")
    return manifest


def step_build_records(skip: bool, dry: bool) -> list[Path]:
    """Step 3 — for every ESP/ESM in release/, build its .records/ bundle.
    Returns the list of ESP paths processed."""
    print(f"[release] step 3: build ESP inventories", flush=True)
    if skip:
        print("  --skip-records: not building inventories", flush=True)
        return []
    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    from build_records import write_inventory  # noqa: E402

    esps = list(iter_release_esps(RELEASE_DIR))
    if not esps:
        print("  (no ESPs found in release/)", flush=True)
        return []
    for esp in esps:
        print(f"  parsing {esp.relative_to(RELEASE_DIR)}", flush=True)
        if not dry:
            write_inventory(esp)  # writes <esp>.records/ next to the binary
    return esps


def step_update_cofiles(tag: str, manifest: dict[str, dict], dry: bool) -> int:
    """Step 4 — append/update the .md co-file for every binary in release/.
    Uses sizes/SHAs from the manifest we just built (no double-hash)."""
    print(f"[release] step 4: update .md co-files for binaries", flush=True)
    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    from update_cofile import update_cofile  # noqa: E402

    count = 0
    for p in iter_release_binaries(RELEASE_DIR):
        rel = p.relative_to(RELEASE_DIR).as_posix()
        entry = manifest.get(rel)
        if entry is None:
            print(f"  WARN: no manifest entry for {rel}, skipping cofile", flush=True)
            continue
        if dry:
            print(f"  DRY: cofile for {rel}", flush=True)
        else:
            update_cofile(p, tag=tag, sha=entry["sha256"], size=entry["size"])
        count += 1
    print(f"  {count} co-files updated", flush=True)
    return count


# --------------------------------------------------------------------------- #
# Content-diff helpers for the per-release notes (text data files)
# --------------------------------------------------------------------------- #

SYNCMAP_REL = "OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini"
MAGICLOADER_PREFIX = "OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/"
MODS_PREFIX = "OblivionRemastered/Content/Paks/~mods/"
_FORMID_RE = re.compile(r"^(;)?\s*([0-9A-Fa-f]{6,8})\s*=\s*(.+?)\s*$")
_ARMOR_PIECES = ("Boots", "Cuirass", "Gauntlets", "Greaves", "Helmet", "Shield", "Bracer")


def _git_show_text(tag: str, repo_rel: str) -> str | None:
    r = git("show", f"{tag}:{repo_rel}", check=False)
    return r.stdout if r.returncode == 0 else None


def tag_date_iso(tag: str) -> str | None:
    r = git("log", "-1", "--format=%cI", tag, check=False)
    return r.stdout.strip() or None


def _parse_syncmap(text: str | None) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in (text or "").splitlines():
        m = _FORMID_RE.match(line.rstrip())
        if m and not m.group(1):
            out[m.group(2).upper()] = m.group(3)
    return out


def _asset_base(path: str) -> str:
    return path.rsplit("/", 1)[-1].split(".", 1)[0]


def _set_of(base: str) -> str:
    for pc in _ARMOR_PIECES:
        if base.endswith(pc):
            return base[:-len(pc)]
    return base


def syncmap_diff(prev_tag: str | None, manifest: dict) -> dict | None:
    """Diff the default (non-Deluxe) SyncMap vs prev tag → added/removed/changed
    FormID→asset mappings, or None if unchanged/unavailable."""
    if prev_tag is None or SYNCMAP_REL not in manifest:
        return None
    cur_p = RELEASE_DIR / SYNCMAP_REL
    if not cur_p.is_file():
        return None
    cur = _parse_syncmap(cur_p.read_text(encoding="utf-8"))
    prev = _parse_syncmap(_git_show_text(prev_tag, f"release/{SYNCMAP_REL}"))
    if not prev:
        return None
    added = {k: cur[k] for k in cur.keys() - prev.keys()}
    removed = {k: prev[k] for k in prev.keys() - cur.keys()}
    changed = {k: (prev[k], cur[k]) for k in cur.keys() & prev.keys() if cur[k] != prev[k]}
    if not (added or removed or changed):
        return None
    return {"added": added, "removed": removed, "changed": changed}


def render_syncmap_section(d: dict) -> str:
    out = [f"## SyncMap asset remappings — "
           f"+{len(d['added'])} -{len(d['removed'])} ~{len(d['changed'])}\n"]
    out.append("FormID → UE5 asset mappings (TesSyncMapInjector). Changed entries "
               "re-point existing FormIDs at new item-set visuals, grouped by "
               "target set.\n")
    if d["changed"]:
        groups: dict[str, list] = {}
        for fid, (old, new) in d["changed"].items():
            groups.setdefault(_set_of(_asset_base(new)), []).append((fid, old, new))
        out.append(f"### Changed ({len(d['changed'])})\n")
        for s in sorted(groups, key=lambda x: (-len(groups[x]), x)):
            out.append(f"**{s}** ({len(groups[s])})\n")
            for fid, old, new in sorted(groups[s]):
                out.append(f"- `{fid}`: `{_asset_base(old)}` → `{_asset_base(new)}`")
            out.append("")
    for label, mp in (("Added", d["added"]), ("Removed", d["removed"])):
        if mp:
            out.append(f"### {label} ({len(mp)})\n")
            for fid in sorted(mp):
                out.append(f"- `{fid}`: `{_asset_base(mp[fid])}`")
            out.append("")
    return "\n".join(out)


def magicloader_diffs(prev_tag: str | None, manifest: dict) -> list:
    """Per changed MagicLoader JSON, diff its FullNames map. Returns list of
    (filename, added, removed, changed)."""
    if prev_tag is None:
        return []
    res = []
    for rel in sorted(manifest):
        if not (rel.startswith(MAGICLOADER_PREFIX) and rel.endswith(".json")):
            continue
        try:
            cur = json.loads((RELEASE_DIR / rel).read_text(encoding="utf-8")).get("FullNames", {})
        except Exception:
            continue
        prevtxt = _git_show_text(prev_tag, f"release/{rel}")
        if prevtxt is None:
            continue
        try:
            prev = json.loads(prevtxt).get("FullNames", {})
        except Exception:
            continue
        added = {k: cur[k] for k in cur.keys() - prev.keys()}
        removed = {k: prev[k] for k in prev.keys() - cur.keys()}
        changed = {k: (prev[k], cur[k]) for k in cur.keys() & prev.keys() if cur[k] != prev[k]}
        if added or removed or changed:
            res.append((rel.rsplit("/", 1)[-1], added, removed, changed))
    return res


def render_magicloader_section(results: list) -> str:
    out = ["## MagicLoader changes\n",
           "Display-name (`FullNames`) changes in the MagicLoader JSON exports.\n"]
    for name, added, removed, changed in results:
        out.append(f"### `{name}` — +{len(added)} -{len(removed)} ~{len(changed)}\n")
        for k in sorted(added):
            out.append(f"- + `{k}` = \"{added[k]}\"")
        for k in sorted(removed):
            out.append(f"- − `{k}` = \"{removed[k]}\"")
        for k in sorted(changed):
            o, n = changed[k]
            out.append(f"- ~ `{k}`: \"{o}\" → \"{n}\"")
        out.append("")
    return "\n".join(out)


def render_summary_section(added, removed, changed, sm, ml, map_changes,
                           zone_counts=None) -> str:
    zone_counts = zone_counts or {}
    def sets(paths):
        return sorted({p[len(MODS_PREFIX):-len("Items.pak")] for p in paths
                       if p.startswith(MODS_PREFIX) and p.endswith("Items.pak")})
    added_sets = sets(added)
    removed_sets = sets(removed)
    new_assets = sorted({p[len(MODS_PREFIX):].split(".")[0] for p in added
                         if p.startswith(MODS_PREFIX) and p.endswith(".ucas")
                         and "Items" not in p and "Materials" not in p})
    changed_maps = sorted({p[len(MODS_PREFIX):].split(".")[0] for p in changed
                           if p.startswith(MODS_PREFIX) and p.endswith(".ucas")})
    out = ["## Summary\n"]
    if added_sets:
        out.append(f"- **Item sets added ({len(added_sets)}):** {', '.join(added_sets)}")
    if removed_sets:
        out.append(f"- **Item sets removed ({len(removed_sets)}):** {', '.join(removed_sets)}")
    if changed_maps:
        # Each L_*_Map pak is one dungeon bundling several zones (= TES4 cells).
        zsum = sum(zone_counts.get(m, 0) for m in changed_maps)
        zlabel = f" / {zsum} zones" if zsum else ""
        out.append(f"- **Dungeon map paks rebuilt ({len(changed_maps)} paks{zlabel}):** "
                   f"{', '.join(changed_maps)}")
    if new_assets:
        out.append(f"- **Map assets added ({len(new_assets)}):** {', '.join(new_assets)}")
    if sm:
        out.append(f"- **SyncMap:** ~{len(sm['changed'])} asset remappings "
                   f"(+{len(sm['added'])} -{len(sm['removed'])}) — see below")
    for name, a, r, c in ml:
        out.append(f"- **MagicLoader `{name}`:** +{len(a)} -{len(r)} ~{len(c)} display names")
    if map_changes:
        dis = map_changes.get("disable")
        ov = map_changes.get("overrides")
        bg = map_changes.get("begone")
        if dis and ov:
            out.append(f"- **TES4 REFR suppression:** "
                       f"+{dis['cur_entries'] - dis['prev_entries']} disabled REFRs, "
                       f"+{ov['cur_entries'] - ov['prev_entries']} position overrides — "
                       f"see Map cell changes")
        if bg:
            out.append(f"- **Ghost suppression (Begone):** "
                       f"net {bg['cur_entries'] - bg['prev_entries']:+d} entries")
    out.append("- **ESP records:** see ESP changes section(s) below")
    out.append("")
    return "\n".join(out)


def step_diff_doc(tag: str, prev_tag: str | None, manifest: dict[str, dict],
                  esp_paths: list[Path], dry: bool) -> Path:
    """Step 5 — write docs/per-release/<tag>.md combining a summary, file-level
    diff, SyncMap/MagicLoader content diffs, MapClone map-cell changes, and
    per-ESP content diffs (from .records/ bundles)."""
    print(f"[release] step 5: write docs/per-release/{tag}.md", flush=True)
    out_path = PER_RELEASE_DOC_DIR / f"{tag}.md"

    sections: list[str] = [f"# {tag} — release notes\n"]
    if prev_tag is None:
        sections.append("_Initial release in v2 layout (no prior tag for comparison)._\n")
    else:
        sections.append(f"_Compared against `{prev_tag}`._\n")

    # File-level diff vs prior manifest, if available
    added: list[str] = []
    removed: list[str] = []
    changed: list[str] = []
    prev_manifest_path = MANIFEST_DIR / f"{prev_tag}.json" if prev_tag else None
    have_prev = bool(prev_manifest_path and prev_manifest_path.exists())
    if have_prev:
        prev_manifest = json.loads(prev_manifest_path.read_text(encoding="utf-8"))
        added = sorted(set(manifest) - set(prev_manifest))
        removed = sorted(set(prev_manifest) - set(manifest))
        changed = sorted(k for k in set(manifest) & set(prev_manifest)
                         if manifest[k]["sha256"] != prev_manifest[k]["sha256"])

    # Content diffs of text data files (SyncMap, MagicLoader) — OOO-repo domain.
    sm = syncmap_diff(prev_tag, manifest)
    ml = magicloader_diffs(prev_tag, manifest)

    # MapClone per-cell map changes (suppression / overrides / ghost / exterior),
    # diffed from MapClone's configs as of the prior tag's date. Never fatal.
    map_changes = None
    mapclone_mod = None
    zone_counts: dict = {}
    if prev_tag is not None:
        sys.path.insert(0, str(REPO_ROOT / "scripts"))
        try:
            import mapclone_changes as mapclone_mod  # noqa: E402
            before = tag_date_iso(prev_tag)
            if before:
                map_changes = mapclone_mod.compute_changes(
                    mapclone_mod.DEFAULT_MAPCLONE, before)
            zone_counts = mapclone_mod.container_zone_counts(mapclone_mod.DEFAULT_MAPCLONE)
        except Exception as e:
            print(f"  WARN: MapClone change summary skipped: {e}", flush=True)

    # Summary (high-level highlights) — only when there's a prior to compare to.
    if have_prev and (added or removed or changed):
        sections.append(render_summary_section(added, removed, changed, sm, ml,
                                               map_changes, zone_counts))

    # File-level change detail
    if have_prev:
        sections.append(
            f"## File-level changes\n\n"
            f"- Added: {len(added)}\n- Removed: {len(removed)}\n- Changed: {len(changed)}\n"
        )
        for label, items in (("Added", added), ("Removed", removed), ("Changed", changed)):
            if items:
                sections.append(f"### {label} ({len(items)})\n")
                for it in items:
                    sections.append(f"- `{it}`")
                sections.append("")

    # SyncMap + MagicLoader + MapClone map-cell-changes content sections
    if sm:
        sections.append(render_syncmap_section(sm))
    if ml:
        sections.append(render_magicloader_section(ml))
    if map_changes and mapclone_mod is not None:
        sec = mapclone_mod.render_section(map_changes, prev_tag)
        if sec:
            sections.append(sec)

    # Per-ESP content diff sections
    if esp_paths and not dry:
        sys.path.insert(0, str(REPO_ROOT / "scripts"))
        from diff_records import render_diff  # noqa: E402

        for esp in esp_paths:
            curr_records = esp.parent / f"{esp.name}.records"
            if not curr_records.is_dir():
                continue
            # Find prior records via prior-tag git checkout -- is overkill;
            # simpler to read from current working tree if we re-walked esp
            # at prev_tag. For the in-repo workflow, we use git show:
            prev_records: Path | None = None
            if prev_tag:
                # git ls-tree -r prev_tag <records-dir-path> to see if it existed
                rel = curr_records.relative_to(REPO_ROOT).as_posix()
                ls = git("ls-tree", "-r", prev_tag, rel, check=False)
                if ls.returncode == 0 and ls.stdout.strip():
                    # Materialize prev records into a temp dir.
                    import tempfile
                    tmp = Path(tempfile.mkdtemp(prefix="prev_records_"))
                    for line in ls.stdout.splitlines():
                        # tab-separated: <mode> <type> <sha>\t<path>
                        if "\t" not in line:
                            continue
                        meta, path = line.split("\t", 1)
                        if not path.endswith(".json"):
                            continue
                        sub = path[len(rel) + 1:] if path.startswith(rel + "/") else None
                        if sub is None:
                            continue
                        show = git("show", f"{prev_tag}:{path}", check=False)
                        if show.returncode != 0:
                            continue
                        out_file = tmp / sub
                        out_file.parent.mkdir(parents=True, exist_ok=True)
                        out_file.write_text(show.stdout, encoding="utf-8")
                    if any(tmp.iterdir()):
                        prev_records = tmp
            md = render_diff(prev_records, curr_records,
                             esp_name=esp.name, max_per_section=20)
            sections.append(md)

    out_text = "\n".join(sections) + "\n"
    print(f"  → {out_path} ({len(out_text)} bytes)", flush=True)
    if not dry:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out_text, encoding="utf-8")
    return out_path


def step_commit_and_tag(tag: str, dry: bool) -> None:
    """Step 6 — git add release/ manifests/ docs/per-release/ → commit → tag."""
    print(f"[release] step 6: commit + tag {tag}", flush=True)
    cmd_add = ["git", "add", "-A", "release/", "manifests/", "docs/per-release/"]
    cmd_commit = ["git", "commit", "-m", tag]
    cmd_tag = ["git", "tag", tag]
    if dry:
        print(f"  DRY: {' '.join(cmd_add)}", flush=True)
        print(f"  DRY: {' '.join(cmd_commit)}", flush=True)
        print(f"  DRY: {' '.join(cmd_tag)}", flush=True)
        return
    subprocess.run(cmd_add, cwd=REPO_ROOT, check=True)
    try:
        subprocess.run(cmd_commit, cwd=REPO_ROOT, check=True,
                       capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        if "nothing to commit" in (e.stdout or "") + (e.stderr or ""):
            print("  (no changes — skipping commit)", flush=True)
        else:
            raise
    subprocess.run(cmd_tag, cwd=REPO_ROOT, check=True)


def step_package(tag: str, dry: bool) -> Path:
    """Step 7 — build dist/<tag>.7z from release/, excluding co-files + .records/."""
    print(f"[release] step 7: build dist/{tag}.7z", flush=True)
    sevenz = shutil.which("7z") or shutil.which("7z.exe")
    if not sevenz:
        raise SystemExit("7z not on PATH")
    out = DIST_DIR / f"{tag}.7z"
    if out.exists() and not dry:
        out.unlink()
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    cmd = [
        sevenz, "a", "-t7z", "-mx=9", "-m0=lzma2", "-ms=on", "-mmt=on",
        # Exclude all co-files anywhere in the tree:
        "-xr!*.md",
        # Exclude all .records directories:
        "-xr!*.records",
        "-xr!.gitkeep",
        str(out),
        f"{RELEASE_DIR.as_posix()}/*",
    ]
    if dry:
        print(f"  DRY: {' '.join(cmd)}", flush=True)
        return out
    r = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stdout + r.stderr)
        raise SystemExit(f"7z exited {r.returncode}")
    print(f"  → {out} ({out.stat().st_size // (1024*1024)} MiB)", flush=True)
    return out


def step_publish(tag: str, latest: bool, prerelease: bool,
                 archive: Path, notes: Path, for_real: bool) -> None:
    """Step 8 — push tag, create GitHub Release with the .7z attached."""
    print(f"[release] step 8: publish to GitHub", flush=True)

    # Push commit + tag.
    push_main = ["git", "push", "origin", "main"]
    push_tag = ["git", "push", "origin", tag]
    create_args = [
        "gh", "release", "create", tag, str(archive),
        "--title", tag,
        "--notes-file", str(notes),
    ]
    if latest:
        create_args.append("--latest")
    if prerelease:
        create_args.append("--prerelease")

    actions = [push_main, push_tag, create_args]
    for cmd in actions:
        if for_real:
            print(f"  EXEC: {' '.join(cmd)}", flush=True)
            r = subprocess.run(cmd, cwd=REPO_ROOT)
            if r.returncode != 0:
                raise SystemExit(f"{cmd[0]} exited {r.returncode}")
        else:
            print(f"  DRY: {' '.join(cmd)}", flush=True)


# --------------------------------------------------------------------------- #
# Top-level
# --------------------------------------------------------------------------- #

def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if isinstance(stream, io.TextIOWrapper):
            stream.reconfigure(encoding="utf-8")

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("tag", help="release tag (e.g. alpha91)")
    rel_group = ap.add_mutually_exclusive_group()
    rel_group.add_argument("--latest", action="store_true",
                           help="mark this release as Latest on GitHub")
    rel_group.add_argument("--prerelease", action="store_true",
                           help="mark as Pre-release on GitHub")
    ap.add_argument("--for-real", action="store_true",
                    help="actually push + create GitHub Release "
                         "(default: print without executing)")
    ap.add_argument("--dry-run", action="store_true",
                    help="print every action; do not modify any files or git state")
    ap.add_argument("--force", action="store_true",
                    help="overwrite an existing tag")
    ap.add_argument("--skip-syncmap", action="store_true",
                    help="skip the SyncMap drift check entirely (use only if you're sure)")
    ap.add_argument("--skip-records", action="store_true",
                    help="skip ESP inventory generation")
    args = ap.parse_args()

    if not RELEASE_DIR.is_dir():
        raise SystemExit(f"release/ not found: {RELEASE_DIR}")

    print(f"=== release.py: {args.tag} ===", flush=True)
    if args.dry_run:
        print("    (dry-run mode: no changes will be made)", flush=True)

    if not args.skip_syncmap:
        step_check_syncmaps(args.dry_run)

    step_validate_tree(args.tag, args.force, args.dry_run)

    manifest = step_hash_manifest(args.tag, args.dry_run)

    esp_paths = step_build_records(args.skip_records, args.dry_run)

    step_update_cofiles(args.tag, manifest, args.dry_run)

    prev_tag = latest_main_tag(exclude=args.tag)
    notes_path = step_diff_doc(args.tag, prev_tag, manifest, esp_paths, args.dry_run)

    step_commit_and_tag(args.tag, args.dry_run)

    archive_path = step_package(args.tag, args.dry_run)

    if args.latest or args.prerelease:
        step_publish(args.tag, args.latest, args.prerelease,
                     archive_path, notes_path, for_real=args.for_real)
    else:
        print("[release] step 8: skip publish (no --latest / --prerelease specified)",
              flush=True)

    print(f"=== release.py: done ===", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
