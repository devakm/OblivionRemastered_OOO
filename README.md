# Oscuro's Oblivion Overhaul Remastered FULL — Release Tracker

> **License:** GNU General Public License v3.0 — see [`LICENSE`](LICENSE).
> Adopted because this project depends on [Wrye Bash](https://github.com/wrye-bash/wrye-bash) (GPL v3) for TES4 plugin parsing.

A version-controlled archive of every alpha / beta / release build of **Oscuro's Oblivion Overhaul Remastered FULL** ("OOORS Full"). The repo is the source of truth for the small editable parts of every release (configs, INIs, Lua, MagicLoader JSONs, tracking metadata); binaries (paks, ESPs, DLLs, etc.) live in `dist/<tag>.7z` and are uploaded as **GitHub Release assets**.

For the architecture rationale + every design decision: [`docs/v2-design.md`](docs/v2-design.md). For Claude / future-self instructions: [`CLAUDE.md`](CLAUDE.md). For the release runbook: [`docs/release-process.md`](docs/release-process.md).

## What you get

- **Editable working tree at [`release/`](release/)** — text-only mirror of the install layout. Edit JSON / INI / Lua / etc. directly in the repo.
- **Per-binary `.md` co-files** alongside every binary — track which release shipped which SHA, with direct download URL pointing at the matching GitHub Release asset.
- **Per-ESP `.records/` inventories** — structured per-record-type JSON files for every ESP/ESM. `git diff alpha85..alpha90 -- '*.records/'` shows actual armor / weapon / leveled-list / cell changes between any two releases.
- **Per-release notes at [`docs/per-release/`](docs/per-release/)** — auto-generated file-level diff + ESP content diff for every tag.
- **Manifests at [`manifests/`](manifests/)** — SHA-256 of every file (text + binary) per release; the integrity record.

## How history is organized

- One commit per release; commit subject = the release name (e.g. `alpha37`).
- One git tag per release; same name.
- Linear history on `main` from `alpha00-premerge` through `alpha90`.
- The `alpha32nex` variant lives on `variants/alpha32nex` (forked off the `alpha32` commit).

## Downloading a release

Every release's `.7z` install archive is attached to its **GitHub Release** at <https://github.com/devakm/OblivionRemastered_OOO/releases>. The Pages site at <https://devakm.github.io/devnull/docs/OOO/OBR/> has a friendlier index + per-release changelog.

To grab a binary that shipped with a specific historical release without downloading the whole `.7z`:

```powershell
py -3 scripts/fetch_binary.py --tag alpha75 release/.../Oscuro's_Oblivion_Overhaul.esp
```

This reads the binary's sibling `.md` co-file, downloads the matching `.7z` (cached at `work/_release_cache/`), extracts only the requested file, and verifies its SHA-256.

## Tooling at a glance

```
scripts/release.py          # cut a new release end-to-end (the user-facing command)
scripts/backfill_v2.py      # one-shot historical rebuild from source folders
scripts/fetch_binary.py     # grab a historical binary from its GitHub Release
scripts/sync_pages.py       # render HTML into the devnull pages repo
scripts/sync_syncmap.py     # generate both SyncMap variants from OOO_SyncGen source
scripts/publish_github.py   # standalone gh-release uploader
scripts/build_records.py    # standalone ESP inventory writer
scripts/diff_records.py     # standalone inventory diff renderer
scripts/update_cofile.py    # standalone .md co-file appender
scripts/tes4_parser.py      # Wrye Bash adapter
scripts/_wrye_bootstrap.py  # bootstraps Wrye Bash as a library
```

See [`CLAUDE.md`](CLAUDE.md) for the full toolchain reference and [`docs/release-process.md`](docs/release-process.md) for the runbook.

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
