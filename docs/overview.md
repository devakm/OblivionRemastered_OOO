# Overview — what OOORS Full bundles

**Oscuro's Oblivion Overhaul Remastered FULL** ("OOORS Full") is the Oblivion Remastered (UE5) re-release of the long-running **Oscuro's Oblivion Overhaul** (OOO) gameplay mod, with Shivering Isles content extended to match. This repo tracks every alpha build.

## How releases are stored

The repo uses a **Releases-for-Assets** split — text content is checked into git, binary content lives only in the `.7z` attached to the matching GitHub Release.

| What | Where |
|------|-------|
| Per-release manifest (SHA-256 of every file) | `manifests/<tag>.json` in git |
| Per-release diff doc (added/removed/changed) | `docs/per-release/<tag>.md` in git |
| Text files from the release tree (JSON, INI, Lua, etc.) | `release/` in git, mirroring source paths |
| Binary files (paks, ESPs, DLLs, textures) | `dist/<tag>.7z` (locally built, gitignored) → uploaded to [GitHub Releases](https://github.com/devakm/OblivionRemastered_OOO/releases) |

This means `git checkout <tag>` reproduces the **text content** of any historical release, and `git diff <tagA>..<tagB> -- release/` shows actual line-level changes inside MagicLoader records / SyncMap mappings / Lua scripts. To get the binaries for a historical release, download `<tag>.7z` from the matching GitHub Release.

## What ships in a release

A release is a directory tree the user merges into their `Oblivion Remastered\` install. The latest build (`alpha90`) includes:

### Game-data overlay (`OblivionRemastered/Content/Dev/ObvData/Data/`)

| Path | Purpose |
|------|---------|
| `Oscuro's_Oblivion_Overhaul.esp` | The main OOO TES4 plugin — leveled lists, NPCs, creatures, items, quests, factions, dialog, etc. |
| `OptionalPatches/OOO_DeluxeEdition.esp` | Optional content for the Deluxe edition of the game. |
| `OptionalPatches/OOO_OOMC_Compatibility_Patch.esp` | Compatibility for **OOMC** (Oscuro's Oblivion Modular Companions / Mod Components). |
| `OptionalPatches/OOO_UORP.esp` | Compatibility for the Unofficial Oblivion Remaster Patch. |
| `OptionalPatches/OOO_UnlimitedRingsReduxPatch.esp` | Compatibility for the Unlimited Rings Redux mod. |
| `OptionalPatches/SyncMap - DeluxeEdition/Oscuro's_Oblivion_Overhaul.ini` | Alternate SyncMap override for Deluxe-edition users. |
| `MagicLoader/Oscuro's_Oblivion_Overhaul_*.json` | Per-record-type JSON exports (ACTI, ALCH, AMMO, ARMO, BOOK, CELL, CELLMAP, CLAS, CLOT, CONT, CREA, DIAL, DOOR, ENCH, FACT, INGR, KEY, MISC, NPC_, QUST, SCPT, SGST, SLGM, SPELL, WEAP). Consumed by **MagicLoader** at game launch. |
| `SyncMap/Oscuro's_Oblivion_Overhaul.ini` | TES4 FormID → UE5 SoftObjectPath mappings consumed by **TesSyncMapInjector** at load time. |

### Engine overlay (`OblivionRemastered/Content/Paks/~mods/`)

21 new outdoor / cave maps as IoStore triplets (`.pak` + `.ucas` + `.utoc`):

`L_Arondar_Map`, `L_Baras_Map`, `L_BloodClotCave_Map`, `L_BrokenToothCaveXX_Map`, `L_Cehan_Map`, `L_DeepCoverCav_Map`, `L_Dostares_Map`, `L_DrownedHopesCa_Map`, `L_GloomWayCaveXX_Map`, `L_GraveGroundCaveXX_Map`, `L_LipsTarn03_Map`, `L_NarindXXX_Map`, `L_OOOR1waterCave_Map`, `L_OOOR2waterCave02_Map`, `L_OOORCastleInterior_Map`, `L_OscuroWaterCellCHMGWell0_Map`, `L_RedGillCave_Map`, `L_RosulasXX_Map`, `L_ThunderingSte_Map`, `L_VarastalXX_Map`, `L_Yele_Map`.

Plus the **Obsidian set** (Glass-armor recolor from the sister `OblivionRemastered_ItemClone` project):

- `ObsidianItems.{pak,ucas,utoc}` — cloned Glass weapons + armor renamed to Obsidian.
- `ObsidianMaterials.{pak,ucas,utoc}` — bronze/black retexture overlays for the Obsidian set.

### UE4SS Lua mods (`OblivionRemastered/Binaries/Win64/ue4ss/Mods/`)

| Mod | What it does |
|-----|--------------|
| `Begone/` | Removes specific actor/object references at runtime; configured by `Config/OscurosOblivionOverhaul.json`. |
| `OOO_REFRFix/` | Fixes spawn / placement deltas for OOO references (`Scripts/spawn_deltas.lua`). |
| `RAX/` | Native DLL helper (`dlls/main.dll`) plus Lua glue. |

## How a release evolves

| Number range | What was happening |
|--------------|---------------------|
| `alpha00-premerge` | Pre-merge snapshot — multiple legacy ESPs side-by-side (137, 137ESM, _ESP, _merged) before consolidation. |
| `alpha01`–`alpha14` | Single consolidated ESP + the first MagicLoader JSON (SPELL only at first), gradually adding more record-type JSONs. |
| `alpha15`–`alpha40` | The full record-type JSON family lands; OptionalPatches start appearing. |
| `alpha32nex` | Parallel Nexus-prep variant of `alpha32` (lives on the `variants/alpha32nex` branch). |
| `alpha41`–`alpha70` | Mostly tuning passes — small file counts changing each build, ESP iteration. |
| `alpha71`–`alpha90` | UE4SS mods (`RAX`, `Begone`, `OOO_REFRFix`) and IoStore content (`L_*_Map`, Obsidian set) get layered in. |

## Where the source comes from

Source release folders live at `X:\games\Oscuro\Oscuro's_Oblivion_Remastered_Shivering_Full_alphaNN\` — these are read-only inputs; the repo is downstream of them. Every git commit is a faithful snapshot of one such folder.

## How to compare two releases

```bash
git diff alpha75..alpha90 -- manifests/    # see exactly which file SHA-256s changed
cat docs/per-release/alpha90.md            # human-readable added/removed/changed list
git log --oneline alpha75..alpha90         # the commit subjects (= release names) between
```
