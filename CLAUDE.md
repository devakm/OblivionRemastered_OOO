# Oscuro's Oblivion Overhaul Remastered FULL — Release Tracker

> These instructions are ALWAYS active. Domain docs live in `docs/` and should only be loaded when working on that domain.

## Project Goal

Track every alpha / beta / release version of **Oscuro's Oblivion Overhaul Remastered FULL** ("OOORS Full") in a single git repository so we can:

1. **See what changed between any two releases** — added files, removed files, mutated files — via per-release manifests checked into git, plus line-level diffs of the small text files (MagicLoader JSON, SyncMap INI, Lua scripts) that ARE committed.
2. **Reproduce the exact contents of any historical release** — `git checkout alphaXX` lands the text-only tree at `release/`; the `.7z` attached to the matching GitHub Release contains the full bundle (text + binaries).
3. **Publish install packages and update notes** to the GitHub Pages site at <https://devakm.github.io/devnull/> by writing into the sibling repo at `X:\dev\devnull\`.
4. **Distribute** the actual `.7z` install archive per release via **GitHub Releases** attached to each tag.

## Architecture: Releases-for-Assets

The repo stores **only the small, diff-friendly stuff**: manifests, per-release diff docs, text content from each release tree (`release/**/*.{json,ini,lua,md,txt,...}`). The binary payload (paks, ESPs, DLLs, etc.) is **not** committed. Instead, `ingest_release.py` packages each release into `dist/<tag>.7z` and the user uploads it as a GitHub Release asset via `publish_github.py`.

This keeps the repo tiny (no LFS quota concerns) while preserving full diffability:

- For binary files: compare `manifests/alphaXX.json` SHAs to see *which* files changed.
- For text files: `git diff alphaXX..alphaYY -- release/` shows exactly *what* changed inside MagicLoader records, SyncMap INI mappings, Lua scripts, etc.

## Repo layout

| Path | Role |
|------|------|
| `release/` | The **text-only** working tree of the latest ingested alpha. `git checkout <tag>` rewinds to that historical release's text content. Binary files are NOT here — get them from the matching GitHub Release's `.7z` attachment. |
| `manifests/alpha{NN}.json` | SHA-256 + size of every file (text AND binary) in release `alphaNN`. Sorted by path, pretty-printed. |
| `dist/` | **Gitignored.** Per-tag `.7z` archives produced by ingest. Uploaded to GitHub Releases. |
| `docs/overview.md` | What OOORS Full is and what each release bundles. |
| `docs/dependencies.md` | OBSE / UE4SS / MagicLoader / TesSyncMapInjector — what the user must install separately. |
| `docs/installation.md` | Install steps (MO2 / Wabbajack / manual). |
| `docs/changelog.md` | Rolling top-level changelog. |
| `docs/per-release/alpha{NN}.md` | Auto-generated added/removed/changed file list vs the previous release. |
| `scripts/` | Tooling — see *Tooling* below. |
| `work/` | **Gitignored.** Scratch / experiments. |

## Source of truth

The release source folders are at `X:\games\Oscuro\Oscuro's_Oblivion_Remastered_Shivering_Full_alphaNN\` — **read-only** as far as this project is concerned. The repo and the `.7z` archives are downstream.

| Source folder | Becomes | Tag | Branch |
|---------------|---------|-----|--------|
| `..._alpha00_preMerge\` | initial commit | `alpha00-premerge` | `main` |
| `..._alpha01\` … `..._alpha90\` | one commit each | `alpha01` … `alpha90` | `main` |
| `..._alpha32nex\` | one commit | `alpha32nex` | `variants/alpha32nex` |

Gaps in numbering (alpha 55, 56, 72) are missing source folders, not skipped releases.

## Tooling

| Script | Role |
|--------|------|
| `scripts/build_manifest.py` | Walk a directory, emit `{path: {sha256, size}}` JSON to stdout/file. Pure function. |
| `scripts/diff_releases.py` | Given two manifest files, emit added / removed / changed file lists (Markdown or JSON). |
| `scripts/ingest_release.py` | Single-release flow: hash source → manifest, diff vs previous → per-release doc, copy text files to `release/`, build `dist/<name>.7z` from full source, commit + tag. |
| `scripts/backfill_history.py` | Walk every alpha source folder in order and call `ingest_release.py` per folder. Variants (alpha32nex) handled on `variants/<name>` branches. |
| `scripts/package_release.py` | Standalone: 7zip a source directory → `dist/<name>.7z`. Used to rebuild a single archive without re-ingesting. |
| `scripts/publish_github.py` | `gh release create <tag> dist/<tag>.7z --notes-file docs/per-release/<tag>.md`. **Defaults to `--dry-run`**; requires `--for-real` to call gh. |
| `scripts/sync_pages.py` | Render the per-release index, changelog, and install instructions as HTML and write them into `X:\dev\devnull\docs\OOO\OBR\`. **Does not commit or push** the Pages repo. |

## What gets committed per release

| Type | Goes in git? | Where |
|------|--------------|-------|
| `.json`, `.ini`, `.lua`, `.md`, `.txt`, `.html`, `.css`, `.cfg`, `.xml`, `.csv`, `.yaml`, `.yml`, `.toml` | **Yes** | `release/` (full path mirroring the source) |
| `.pak`, `.ucas`, `.utoc`, `.esp`, `.esm`, `.dll`, `.exe`, `.dds`, `.tga`, `.png`, `.jpg`, `.webp`, `.uasset`, `.uexp`, `.umap`, `.bsa` | **No** | `dist/<tag>.7z` only (uploaded as GitHub Release asset) |
| Manifest of all files (text + binary) | **Yes** | `manifests/<tag>.json` |
| Per-release diff summary | **Yes** | `docs/per-release/<tag>.md` |

## Constraints

| Rule | Detail |
|------|--------|
| **Game install is READ-ONLY** | `C:\games\Steam\steamapps\common\Oblivion Remastered\` and below — never written to. Hook-enforced via `.claude/hooks/restrict-path.py`. |
| **Source release folders are READ-ONLY** | `X:\games\Oscuro\Oscuro's_Oblivion_Remastered_Shivering_Full_*` — copy from, never write to. Hook-enforced. |
| **No publish without explicit approval** | `publish_github.py` and any `git push` are user-initiated, not autonomous. Building, packaging, and writing to Pages staging is fine; uploading or pushing is not. |
| **No LFS** | The repo deliberately does NOT use Git LFS. Binaries don't enter the repo; they go into GitHub Releases. The `.gitattributes` file has only `eol=lf` rules — no `filter=lfs`. |
| **One commit per release** | `git log` is the canonical release history. Commit subject = release name. Body links the per-release diff doc. |
| **Tag every release** | Lightweight tag matching the release name. Tags are how `publish_github.py` finds the artifact to upload. |

## Implementation rules

| Rule | Detail |
|------|--------|
| **No writes to game install** | Hook-enforced; don't try to find workarounds. |
| **Dry-run by default** | Any script with external side effects (GitHub upload, git push, Pages commit) defaults to dry-run. |
| **Idempotent ingest** | Re-ingest of an already-tagged release requires `--force`. The .7z build skips itself if `dist/<tag>.7z` already exists (use `--force` to rebuild). |
| **Manifest format is stable** | Keys sorted alphabetically; values pretty-printed with 2-space indent. So `git diff` of two manifests is human-readable. |
| **Cross-platform paths in JSON** | Manifests store relative POSIX paths (`/`-separated), even on Windows. So manifests don't churn if regenerated on a different OS. |

## Critical files

| File | Role |
|------|------|
| `.gitattributes` | Only `eol=lf` rules. No LFS routing. |
| `.gitignore` | Excludes `dist/`, `work/`, `*.7z`, `.claude/settings.local.json`. |
| `.claude/settings.json` | Permissions + the restrict-path hook. Committed. |
| `.claude/settings.local.json` | Per-user allow list. **Not** committed. |
| `.claude/hooks/restrict-path.py` | PreToolUse hook. Hard-blocks any tool call that would write to game install or source release folders. Reads anywhere are fine. |

## External resources

| Path | Role |
|------|------|
| `X:\games\Oscuro\` | Source release folders (read-only). |
| `X:\dev\devnull\` | GitHub Pages site (`devakm/devnull` → <https://devakm.github.io/devnull/>). Output of `sync_pages.py` lands under `docs/OOO/OBR/` here. |
| `X:\dev\OblivionRemastered_ItemClone\` | Sister project. The `.claude/` setup here was originally borrowed from there. |
| `C:\games\Steam\steamapps\common\Oblivion Remastered\` | Game install. **Read-only**, hook-enforced. |

## Documentation discipline

After any meaningful change to the toolchain or repo layout: ask "does any `docs/*.md` need updating?" If yes, the doc update is part of the same commit. Undocumented findings are lost between sessions.

## Migration history

This project went through one major architectural change after initial backfill:

- **Phase 1 (initial)**: Used Git LFS for all binary content. Ended up with ~1.6 GB of LFS objects across 89 tags — would have exceeded GitHub's 1 GB free LFS quota.
- **Phase 2 (current)**: Migrated to "Releases-for-Assets" — text in git, binaries in GitHub Releases. Repo `.git` is now small enough to clone in seconds.

If you ever need to re-do the migration logic, the historical scripts are findable in `git reflog` from before the reset.
