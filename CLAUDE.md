# Oscuro's Oblivion Overhaul Remastered FULL — Release Tracker

> These instructions are ALWAYS active. Domain docs live in `docs/` and should only be loaded when working on that domain. The full v2 architecture rationale lives in [`docs/v2-design.md`](docs/v2-design.md).

## Project Goal

Track every alpha / beta / release version of **Oscuro's Oblivion Overhaul Remastered FULL** ("OOORS Full") in a single git repository so we can:

1. **Edit in place** — `release/` is the working tree of the latest release. You edit small files (text, configs, Lua, etc.) directly in the repo, drop binaries (paks, ESPs, DLLs) in physically when staging a release, and `release.py` packages everything.
2. **See what changed between any two releases** at the **record level**, not just the file level — every ESP gets a `.records/` directory of structured per-record-type JSON files; `git diff <tagA>..<tagB> -- '*.records/'` shows added/removed/modified armor, weapons, leveled lists, cells, etc.
3. **Track every binary's history** via per-binary `.md` co-files that record which release shipped which SHA + GitHub Release URL.
4. **Distribute** install archives via **GitHub Releases** attached to each tag.
5. **Publish** install info + changelogs to <https://devakm.github.io/devnull/> by writing into the sibling repo at `X:\dev\devnull\`.

## Architecture (v2 — current)

The repo is the source of truth for **text content + metadata**. Binary content lives only in `dist/<tag>.7z` (gitignored, uploaded as a GitHub Release asset).

For every binary file in `release/`, two sibling artifacts live next to it:

```
…/Oscuro's_Oblivion_Overhaul.esp           ← gitignored binary, present at staging time
…/Oscuro's_Oblivion_Overhaul.esp.md        ← committed: per-release tracking table
…/Oscuro's_Oblivion_Overhaul.esp.records/  ← committed (ESPs only): per-record-type inventory
    _meta.json                              ← TES4 header + masters + record types present
    ARMO.json                               ← array of {formid, edid, full, modl}
    WEAP.json
    LVLI.json                               ← leveled list entries
    CELL.json                               ← cell headers + ref counts
    QUST.json                               ← stage indices
    DIAL.json                               ← INFO summary
    ... (one file per record type the ESP defines)
```

`.md` co-files and `.records/` directories are EXCLUDED from `dist/<tag>.7z` (they're repo metadata, not release content).

## Repo layout

| Path | Role |
|------|------|
| `release/` | Working tree of the latest release. Mirrors the install layout: `release/OblivionRemastered/Content/...`, `release/Content/...` (early alphas), etc. Text files + co-files are committed; binaries are gitignored but physically present at staging time. |
| `manifests/<tag>.json` | SHA-256 + size for every file (text + binary) per release. Used for fast file-level diffs and as the integrity record. |
| `dist/` | **Gitignored.** Per-tag `.7z` archives produced by `release.py`. Uploaded to GitHub Releases. |
| `docs/v2-design.md` | The architecture rationale (read this first). |
| `docs/release-process.md` | The runbook for cutting a new release. |
| `docs/overview.md` | What OOORS Full bundles. |
| `docs/dependencies.md` | OBSE / UE4SS / MagicLoader / TesSyncMapInjector — what users install separately. |
| `docs/installation.md` | Install steps. |
| `docs/changelog.md` | Rolling top-level changelog index. |
| `docs/per-release/<tag>.md` | Auto-generated per-release notes (file-level diff + ESP content diff). |
| `scripts/` | Tooling — see *Tooling* below. |
| `work/` | **Gitignored.** Scratch / experiments / `_release_cache/` for fetch_binary. |

## Tooling

| Script | Role |
|--------|------|
| `scripts/release.py` | **The release command.** End-to-end: regenerate SyncMap → hash → parse ESPs → update co-files → diff doc → commit + tag → build .7z → optionally push + `gh release create`. |
| `scripts/backfill_v2.py` | One-shot historical rebuild from source folders. Already run for the 89 alpha lineage; rerun only if you need to redo history. |
| `scripts/fetch_binary.py` | Download a historical binary from a GitHub Release using its `.md` co-file as the URL index. Caches `.7z` at `work/_release_cache/<tag>.7z`. |
| `scripts/sync_syncmap.py` | Generate the two SyncMap variants (default + Deluxe) from the OOO_SyncGen source-of-truth INI. Run automatically by `release.py`. |
| `scripts/sync_pages.py` | Render the per-release index, changelog, install instructions as HTML and write them into `X:\dev\devnull\docs\OOO\OBR\`. **Does not commit or push** the Pages repo. |
| `scripts/publish_github.py` | Standalone `gh release create / upload` driver for ad-hoc publishing of a single tag. Defaults to dry-run; needs `--for-real`. |
| `scripts/build_records.py` | Standalone ESP inventory writer. Used by `release.py`/`backfill_v2.py` internally; can also be invoked directly for testing. |
| `scripts/diff_records.py` | Standalone ESP-inventory diff renderer. Used by `release.py`/`backfill_v2.py` to produce the ESP-changes section of `docs/per-release/<tag>.md`. |
| `scripts/update_cofile.py` | Standalone per-binary `.md` co-file appender. Used by `release.py`/`backfill_v2.py`; can also be invoked directly to re-stamp a row. |
| `scripts/tes4_parser.py` | Wrye Bash adapter: `parse_esp(path)` → loaded `ModFile`. |
| `scripts/_wrye_bootstrap.py` | Bootstraps Wrye Bash as a library (skips desktop-app init). |

## What gets committed per release

| Pattern | Committed? | Notes |
|---------|------------|-------|
| `*.json`, `*.ini`, `*.lua`, `*.md`, `*.txt`, `*.html`, `*.css`, `*.py`, `*.cfg`, `*.xml`, `*.csv`, `*.yaml`, `*.yml`, `*.toml` | yes | Text source files (in `release/`) |
| `*.esp.records/**/*.json`, `*.esm.records/**/*.json` | yes | ESP inventory bundle |
| `*.<binary-ext>.md` | yes | Per-binary release tracking co-files |
| `*.esp`, `*.esm` | **no** | Replaced by `.records/` for diffing + `.md` for tracking |
| `*.pak`, `*.ucas`, `*.utoc` | no | IoStore binaries |
| `*.dll`, `*.exe` | no | Native binaries |
| `*.dds`, `*.tga`, `*.png`, `*.jpg`, `*.jpeg`, `*.webp` | no | Image binaries |
| `*.uasset`, `*.uexp`, `*.umap`, `*.bsa` | no | UE asset blobs |
| `manifests/<tag>.json` | yes | Full file-level integrity record |
| `docs/per-release/<tag>.md` | yes | Per-release notes (auto-generated) |

## Source of truth

The release source folders are at `X:\games\Oscuro\Oscuro's_..._alphaNN\` — **read-only** for Claude (hook-enforced via `.claude/hooks/restrict-path.py`). Going forward they're only used by `backfill_v2.py` when rebuilding historical state. For new releases, you edit `release/` directly — no separate source folder needed.

| Tag pattern | Branch |
|-------------|--------|
| `alpha00-premerge` | `main` (initial release commit) |
| `alpha01` … `alpha90` | `main` (one commit each) |
| `alpha32nex` | `variants/alpha32nex` (forked off `alpha32`) |

## Constraints

| Rule | Detail |
|------|--------|
| **Game install is READ-ONLY** | `C:\games\Steam\steamapps\common\Oblivion Remastered\` and below — never written to. Hook-enforced. |
| **Source release folders are READ-ONLY** | `X:\games\Oscuro\` — read for backfill only. |
| **No publish without explicit approval** | `release.py --for-real`, `git push`, `gh release create` are user-initiated. |
| **No Git LFS** | The repo deliberately does not use LFS. Binaries stay out of git entirely (gitignored), distributed via GitHub Release assets. |
| **One commit per release** | `git log` is the canonical release history. Subject = release name. |
| **Tag every release** | Lightweight tag matching the release name. Tags are how `gh release` finds the artifact. |

## Implementation rules

| Rule | Detail |
|------|--------|
| **Edit in place** | The repo IS the source of truth for text + metadata. Don't reintroduce wipe-and-refill patterns. |
| **Dry-run by default** | Anything with external side effects (push, gh, Pages commit) defaults to dry-run; `--for-real` to commit. |
| **Manifest format is stable** | Keys sorted alphabetically; values pretty-printed with 2-space indent. |
| **Inventory format is stable** | Each `.records/<TYPE>.json` sorted by FormID. |
| **Cross-platform paths in JSON** | Manifests + inventories store relative POSIX paths. |
| **UTF-8 everywhere** | All scripts that print to stdout call `sys.stdout.reconfigure(encoding="utf-8")` to render arrows / em-dashes correctly on Windows cp1252 consoles. |

## External dependencies

| Dep | Why | Install |
|-----|-----|---------|
| `chardet` | Wrye Bash transitive | `py -3 -m pip install chardet` |
| `wxPython` | Wrye Bash transitive (via patcher imports) | `py -3 -m pip install wxPython` |
| `lz4` | Wrye Bash transitive (BSA handling) | `py -3 -m pip install lz4` |
| `pyyaml` | Wrye Bash transitive (LOOT parser) | `py -3 -m pip install pyyaml` |
| `7-Zip` | Packaging | `winget install 7zip.7zip` (or have it on PATH) |
| `gh` CLI | GitHub Releases | `winget install GitHub.cli` |
| Wrye Bash checkout | TES4 parsing | `git clone https://github.com/wrye-bash/wrye-bash X:\dev\wrye-bash` (dev branch); set `WRYE_BASH_MOPY` env var if elsewhere |

`requirements.txt` lists the four pip deps. The license is **GPL v3** because we use Wrye Bash directly (see [`LICENSE`](LICENSE) and [`docs/v2-design.md`](docs/v2-design.md) decision #8).

## Critical files

| File | Role |
|------|------|
| `LICENSE` | GNU GPL v3.0. |
| `.gitattributes` | Only `eol=lf` rules. No LFS routing. |
| `.gitignore` | Excludes `dist/`, `work/`, `*.7z`, all binary extensions, `.claude/settings.local.json`. |
| `.claude/settings.json` | Permissions + the restrict-path hook. Committed. |
| `.claude/settings.local.json` | Per-user allow list. **Not** committed. |
| `.claude/hooks/restrict-path.py` | PreToolUse hook. Hard-blocks any tool call that would write to game install or source release folders. Reads anywhere are fine. |
| `requirements.txt` | Python deps for the parser adapter. |

## External resources

| Path | Role |
|------|------|
| `X:\games\Oscuro\` | Source release folders (read-only; only used for backfill). |
| `X:\dev\wrye-bash\` | Wrye Bash checkout (dev branch). Used by `tes4_parser.py`. |
| `X:\dev\devnull\` | GitHub Pages site (`devakm/devnull` → <https://devakm.github.io/devnull/>). Output of `sync_pages.py` lands under `docs/OOO/OBR/`. |
| `X:\mod-tools\OOO_SyncGen\SyncGen\Overrides\Oscuro's_Oblivion_Overhaul_Overrides.ini` | SyncMap source-of-truth (Deluxe variant). Read by `sync_syncmap.py`. |
| `C:\games\Steam\steamapps\common\Oblivion Remastered\` | Game install. **Read-only**, hook-enforced. |

## Publishing a release

The full runbook lives in **[`docs/release-process.md`](docs/release-process.md)**. Read it before doing anything that touches `git push`, `gh release`, or the devnull Pages repo.

## Documentation discipline

After any meaningful change to the toolchain or repo layout: ask "does any `docs/*.md` need updating?" If yes, the doc update is part of the same commit. Undocumented findings are lost between sessions.

## Migration history

This repo went through two architectures:

- **v1 (LFS)** — binaries committed via Git LFS. ~1.6 GB of LFS objects, exceeded GitHub's 1 GB free quota.
- **v1.5 (Releases-for-Assets, no LFS)** — binaries excluded from git, manifests + small text files only. Solved the LFS problem but the repo was a passive snapshot store, not an editing surface.
- **v2 (current)** — edit-in-place, per-binary `.md` co-files, per-ESP `.records/` inventories. Diff + tag-vs-tag changelogs work natively via `git diff`. Designed in [`docs/v2-design.md`](docs/v2-design.md).

The historical v1 commits were dropped during the v2 cutover (Phase 8 of the migration). The 89 alpha tags now point at v2-shaped commits; the GitHub Releases stay intact (they reference tag names, not SHAs, and the `.7z` assets were uploaded earlier).
