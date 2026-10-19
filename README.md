# Oscuro's Oblivion Overhaul Remastered FULL — Release Tracker

> **License:** GNU General Public License v3.0 — see [`LICENSE`](LICENSE).
> Adopted because this project depends on [Wrye Bash](https://github.com/wrye-bash/wrye-bash) (GPL v3) for TES4 plugin parsing.

A version-controlled archive of every alpha / beta / release build of **Oscuro's Oblivion Overhaul Remastered FULL** (OOORF). The repo is the source of truth for the small editable parts of every release (configs, INIs, Lua, MagicLoader JSONs, tracking metadata); binaries (paks, ESPs, DLLs, etc.) live in `dist/<tag>.7z` and are uploaded as **GitHub Release assets**.

For the architecture rationale + every design decision: [`docs/v2-design.md`](docs/v2-design.md).

## What you get

- **Editable working tree at [`release/`](release/)** — text-only mirror of the install layout. Edit JSON / INI / Lua / etc. directly in the repo.
- **Per-binary `.md` co-files** alongside every binary — track which release shipped which SHA, with direct download URL pointing at the matching GitHub Release asset.
- **Per-ESP `.records/` inventories** — structured per-record-type JSON files for every ESP/ESM. `git diff alpha85..alpha90 -- '*.records/'` shows actual armor / weapon / leveled-list / cell changes between any two releases.
- **Per-release notes at [`docs/per-release/`](docs/per-release/)** — auto-generated file-level diff + ESP content diff for every tag.
- **Manifests at [`manifests/`](manifests/)** — SHA-256 of every file (text + binary) per release; the integrity record.

## How history is organized

- One commit per release; commit subject = the release name (e.g. `alpha37`).
- One git tag per release; same name.
- Linear history on `main` from `alpha00-premerge` through the latest alpha.
- The `alpha32nex` variant lives on `variants/alpha32nex` (forked off the `alpha32` commit).

## Downloading a release

Every release's `.7z` install archive is attached to its **GitHub Release** at <https://github.com/devakm/OblivionRemastered_OOO/releases>. The Pages site at [https://devakm.github.io/devnull/OOO/OBR/](https://devakm.github.io/devnull/OOO/OBR/index.html) has a friendlier index + per-release changelog.

To grab a binary that shipped with a specific historical release without downloading the whole `.7z`:

```powershell
py -3 scripts/fetch_binary.py --tag alpha75 release/.../Oscuro's_Oblivion_Overhaul.esp
```

This reads the binary's sibling `.md` co-file, downloads the matching `.7z` (cached at `work/_release_cache/`), extracts only the requested file, and verifies its SHA-256.

## Dependencies

These are the runtime components a player installs separately. **None of them are bundled in the OOORF release archive**; install them before deploying OOORF. The same information is on the [Dependencies page](https://devakm.github.io/devnull/OOO/OBR/dependencies.html) and in [`docs/dependencies.md`](docs/dependencies.md).

### Required

| Dependency | Why OOORF needs it |
| ------------ | -------------------- |
| **Oblivion Remastered** | The base game (Unreal Engine 5.3), via Steam, Game Pass or your platform of choice. |
| **[MagicLoader](https://www.nexusmods.com/oblivionremastered/mods/1966)** | OOORF ships its plugin in two complementary forms: `Oscuro's_Oblivion_Overhaul.esp` plus a per-record-type JSON family under `…\ObvData\Data\MagicLoader\` that carries localization strings and map-loading instructions. MagicLoader reads those JSONs at game start and merges them into the live record set. Required for the custom dungeons to load and for localized strings (books, creature, item, spell and location names, quest dialogue). Non-English speakers can swap the strings for their own language. |
| **[TesSyncMapInjector](https://www.nexusmods.com/oblivionremastered/mods/1272)** (UE4SS Lua mod) | Reads `…\ObvData\Data\SyncMap\Oscuro's_Oblivion_Overhaul.ini` (`<TES4 FormID>=<UE5 SoftObjectPath>` lines) at load time and binds each FormID to its UE5 asset. Required to avoid invisible or missing assets and crashes when NPCs and creatures spawn, and for every new item set. |
| **UE4SS — "UE4SS new", v3.0.1-1164 or later** | Required from alpha92. Get it from the [UE4SS Nexus page](https://www.nexusmods.com/oblivionremastered/mods/32), under **Update files**, the file named **"UE4SS new"**; it installs over an existing UE4SS. The older **"UE4SS stable"** (3.0.1.a) is **not supported**: OOORF's `RAX` DLL is built for one exact UE4SS version (the alpha92 DLL is not safe on the old UE4SS, and the alpha91 DLL is not safe on the new one). TesSyncMapInjector v0.1.8 and MagicLoader v2.9 work with "UE4SS new". |

### Bundled UE4SS mod

| Mod (under `…\Binaries\Win64\ue4ss\Mods\`) | Role |
|--------------------------------------------|------|
| `RAX/` | Ships inside the OOORF archive (UE4SS must be installed first). Loads the custom UE5 maps (the new `L_*_Map` dungeons). Native DLL built for "UE4SS new" v3.0.1-1164; do not use it with any other UE4SS version. |

### Optional compatibility patches

ESPs under `…\Data\OptionalPatches\`; move one up into `…\Data\` to enable it.

| Patch ESP | Compatibility with |
| ----------- | -------------------- |
| `OOO_DeluxeEdition.esp` | Oblivion Remastered Deluxe Edition. Pair with the `SyncMap - DeluxeEdition/` override. |
| `OOO_OOMC_Compatibility_Patch.esp` | [Opulent Outfits: Mages of Cyrodiil](https://www.nexusmods.com/oblivionremastered/mods/4992) |
| `OOO_UORP.esp` | [The Unofficial Oblivion Remaster Patch](https://www.nexusmods.com/oblivionremastered/mods/477) |
| `OOO_UnlimitedRingsReduxPatch.esp` | [Unlimited Rings Redux](https://www.nexusmods.com/oblivionremastered/mods/2457) |

### Optional test UE4SS mods (manual deploy)

Not required for normal play; they support the alpha-testing workflow. From alpha92 they ship under `OblivionRemastered\alpha92_test_optional\` with their install tree intact. To use one, copy its folder from `alpha92_test_optional\Binaries\Win64\ue4ss\Mods\` into `OblivionRemastered\Binaries\Win64\ue4ss\Mods\`. Installing alpha92 over alpha91 does not remove the alpha91 copies; delete `Mods\Begone\` and `Mods\OOO_REFRFix\` unless you want them.

| Mod | Role |
|-----|------|
| `Begone/` | Test recording and debugging. Log-only from alpha92 (it suppresses nothing; ghost suppression is baked into the map paks). |
| `OOO_REFRFix/` | Save-file migration helper for saves carrying OOO references from older alpha releases. |

## Tooling at a glance

```
scripts/release.py          # cut a new release end-to-end (the user-facing command)
scripts/backfill_v2.py      # one-shot historical rebuild from source folders
scripts/fetch_binary.py     # grab a historical binary from its GitHub Release
scripts/gather_live.py      # stage live-install files into release/ (dry-run default; --apply, --only)
scripts/sync_pages.py       # diff-only preview of the devnull OBR pages (pages are hand-maintained)
scripts/sync_syncmap.py     # generate both SyncMap variants from OOO_SyncGen source (3-gate workflow)
scripts/publish_github.py   # standalone gh-release uploader
scripts/build_records.py    # standalone ESP inventory writer
scripts/diff_records.py     # standalone inventory diff renderer
scripts/update_cofile.py    # standalone .md co-file appender
scripts/tes4_parser.py      # Wrye Bash adapter
scripts/_wrye_bootstrap.py  # bootstraps Wrye Bash as a library
```

See [`docs/toolchain.md`](docs/toolchain.md) for the full toolchain reference and [`docs/release-process.md`](docs/release-process.md) for the runbook.

## Setup

```powershell
# 1. Python deps (runtime requirements for the parser adapter)
py -3 -m pip install -r requirements.txt

# 2. Wrye Bash checkout (GPL v3) — used as a library for TES4 parsing
git clone https://github.com/wrye-bash/wrye-bash X:\dev\wrye-bash
# OR set WRYE_BASH_MOPY env var if your checkout is elsewhere

# 3. 7-Zip + GitHub CLI (for packaging + publishing)
winget install 7zip.7zip
winget install GitHub.cli
gh auth login
```

## Credits

OOORF stands on the work of many people. Thank you to:

- **Sotobrastos** — creator of classic Oscuro's Oblivion Overhaul.
- **Walker In Shadows** and **CorePC** — for keeping classic OOO supported over the years.
- **Saldron** — classic OOO for Shivering Isles.
- **[SquigM](https://www.nexusmods.com/profile/SquigM/mods?gameId=7587)** — [Gold-Blue Glass Armour and Weapons](https://www.nexusmods.com/oblivionremastered/mods/4671) and [Bronze-Black Glass Armour and Weapons](https://www.nexusmods.com/oblivionremastered/mods/5019), the bases of the BlueGlass and Obsidian sets.
- **[ProhagonCreations](https://www.nexusmods.com/profile/ProhagonCreations/mods?gameId=7587)** — [Blackened Steel Glass Armor and Weapons](https://www.nexusmods.com/oblivionremastered/mods/556), the base of the DarkMalachite and Drakefired sets.
- **Antrix** — for the inspiration and the initial version of RAX.
- **Wrye**, and all contributors to [Wrye Bash](https://github.com/wrye-bash/wrye-bash).
- **VibrantLGBT** — [MagicLoader](https://www.nexusmods.com/oblivionremastered/mods/1966).
- **Godschildgaming** — [TesSyncMapInjector](https://www.nexusmods.com/oblivionremastered/mods/1272).
- The **UE4SS** team and contributors — [RE-UE4SS](https://github.com/UE4SS-RE/RE-UE4SS).
- The developers of [FModel](https://github.com/4sval/FModel) and [retoc](https://github.com/trumank/retoc).
- **ElminsterAU** and **Robert** — for the xEdit updates.
- **shadeMe** — for the updates to CSE.
- **Arthmoor** — for the UOP and the UORP.
- **Psymon** — OOORF playtesting and Discord admin.
- **slowpard** — Discord help.
- **Tripster** — UE5 brainstorming.
- **wxMichael** — mesh fixes.
- **Davitto94** — feedback.

Special thanks to all the [classic OOO](https://www.nexusmods.com/oblivion/mods/15256) fans and contributors over the last 20+ years.
