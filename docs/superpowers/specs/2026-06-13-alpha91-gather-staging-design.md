# alpha91 gather-staging design

**Date:** 2026-06-13
**Status:** approved
**Topic:** Turn `scripts/gather_live.py` into a tracker-driven staging planner that
produces a reviewable curated change list (additions / updates / deletions) for the
alpha91 release, then stage everything and build the non-Deluxe SyncMap.

## Problem

`gather_live.py` today walks only files **already present** in `release/` and
refreshes each from the live install (copy when the live file is both newer by mtime
and different by SHA-256). It cannot pull brand-new files. alpha91 adds a large batch
of new `~mods/` pak triplets (15 OOO item sets + a map-entrance fix) that have no
counterpart in `release/` yet, so the current script silently ignores them.

Separately, the old `BGlass*` / `RGlass*` item paks in `release/~mods/` were renamed
upstream (now `BlueGlass…`) and no longer exist in the live install — they are dead
weight that should be removed.

## Decisions (locked)

1. **Ship all 15 item sets** (every set present in live `~mods/` and listed in the
   item tracker): ArcticFur, Aureus, BloodLeather, BlueGlass, Drakefired, Eboron,
   ElvenEldar, ElvenNight, ElvenSky, GoldenBronze, GrayFox, Obsidian, ShadowMail,
   WornFur, WornLeather. Each ships `…Items` + `…Materials` pak triplets.
2. **No new ESPs.** Only the 5 ESPs already shipped in alpha90 get refreshed
   (main `Oscuro's_Oblivion_Overhaul.esp` + the 4 OptionalPatches ESPs). The
   companion `OOO_*Icons.esp` / `OOO_Obsidian*.esp` files in live `Data/` are **not**
   added — item integration rides in the main OOO ESP. The existing release walk
   already refreshes the 5 shipped ESPs; no gather change needed for ESPs.
3. **Remove the stale `BGlass*` / `RGlass*` paks** (4 triplets + their committed
   `.md` co-files) — superseded by `BlueGlass`, no live source.
4. **Tracker-driven staging with a clean review gate.** The staging step derives the
   authoritative ship-list from structured upstream sources, cross-references live +
   `release/`, and emits a curated add/update/delete plan for review *before*
   packaging.
5. **SyncMap divergence stops for review.** If the live Deluxe SyncMap (pulled by
   gather) and the OOO_SyncGen source-of-truth (used by `sync_syncmap.py`) diverge at
   the `diff-check` gate, surface it and stop — do not auto-pick a winner.

## Authoritative sources the staging parser reads

| Category | Source (parsed) | Yields |
|---|---|---|
| Item paks | `X:\dev\OblivionRemastered_ItemClone\docs\item-tracker.html` — "Set summary" table, "dist packages" column | 15 sets × `…Items`+`…Materials` = 30 triplets |
| Dungeon-map paks | `X:\dev\OblivionRemastered_MapClone\ooo_clone_config.json` — `clones[].container_name` where `status == "ready"` | 17 `L_*_Map` triplets |
| Map "related" paks | `X:\dev\OblivionRemastered_MapClone\ooo_exterior_foliage_config.json` — top-level cell keys → `<key>Exterior_P` | `GraveGroundExterior_P` (+ any future) |
| Map in-game ✓ status | `X:\dev\OblivionRemastered_MapClone\docs\phase9-unify-tracker.md` — validation grid | review annotation only (confidence per zone) |
| Everything else | existing `release/` walk | refresh in place |

All four cross-repo paths are configurable via CLI flags (defaults to the absolute
paths above), so the script degrades gracefully if a sibling repo is absent (those
categories just contribute nothing and a warning is logged).

The item ESPs listed in the tracker's "dist packages" column are intentionally
**ignored** by the parser (decision 2) — only `.pak/.ucas/.utoc` triplets are pulled.

## States the planner emits

Per `~mods/`-relative pak file (and, unchanged, per existing `release/` file):

- **`added`** — in ship-list + present in live `~mods/`, absent from `release/`.
  → 28 new item triplets (Obsidian already present) + `GraveGroundExterior_P`.
  Always copied on `--apply`.
- **`updated`** / **`up-to-date`** / **`stale-mtime`** — existing newer-and-differs
  logic, unchanged, for everything already in `release/`.
- **`no-source`** — existing: a tracked `release/` file with no live counterpart.
- **`orphan`** — a `release/~mods/` pak (a `.pak/.ucas/.utoc`) that is **not** in the
  ship-list **and** has no live source. Catches `BGlass*` / `RGlass*` and their
  committed `.md` co-files. Reported as a deletion candidate.
- **`missing-from-live`** — a ship-list entry the tracker/config promises but live
  `~mods/` lacks. A completeness alarm: never ship a half-built set.
- **`skipped-managed`** — unchanged: the non-Deluxe SyncMap ini (owned by
  `sync_syncmap.py`).

Legacy maps not in `ooo_clone_config.json` (`L_OOOR1waterCave`,
`L_OOOR2waterCave02`, `L_OOORCastleInterior`, `L_OscuroWaterCellCHMGWell0`) are
**not** orphans: they exist in live `~mods/`, so they refresh normally and are never
flagged for deletion. The orphan test is "no live source", which keeps deletions safe.

## Safety model

- Dry-run is the default and is fully non-destructive (no copies, no deletes).
- `--apply` performs copies (additions + updates) preserving live mtime (`copy2`).
- **Deletions are never silent.** Orphans are always reported; the actual removal of
  `BGlass*` / `RGlass*` + co-files is a separate, reviewed `git rm` step after the
  review gate — not auto-deleted by `--apply`.
- Output: console report + `work/alpha91_gathered.json` staging manifest (the durable
  review artifact), extended with the new states.

## Full alpha91 sequence

1. **Stage (dry-run)** → review curated add/update/delete plan + map ✓ status + any
   `missing-from-live` alarms. **← review gate.**
2. **Apply** gather (`--apply`): copy item paks + `GraveGroundExterior_P`; refresh
   ESP / MagicLoader / Deluxe SyncMap / the 21 maps / Obsidian.
3. **Remove orphans** (`BGlass*` / `RGlass*` + `.md` co-files) — reviewed `git rm`.
4. **SyncMap 3-gate** (`sync_syncmap.py`): `diff-check` → if live-Deluxe vs
   OOO_SyncGen diverge, **stop and show**; else `sync-content` → `apply-swap`
   (builds the non-Deluxe variant). Each gate is its own pause.
5. **Final readiness review** of everything staged. Tagging / `release.py --for-real`
   stays user-triggered.

## Out of scope (unchanged division of labour)

`.md` co-file regeneration, `.records/` inventory rebuilds, manifest hashing, the
per-release diff doc, commit + tag, and `.7z` packaging all remain `release.py`'s job.
`gather_live.py` only stages working-tree content and emits the review manifest.
