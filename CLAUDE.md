# Oscuro's Oblivion Overhaul Remastered FULL — Release Tracker

> These instructions are ALWAYS active. Domain docs live in `docs/` and should only be loaded when working on that domain.

## Project Goal

Track every alpha / beta / release version of **Oscuro's Oblivion Overhaul Remastered FULL** ("OOORS Full") in a single git repository so we can:

1. **See what changed between any two releases** — added files, removed files, mutated files — via per-release manifests checked into git.
2. **Reproduce the exact contents of any historical release** — `git checkout alphaXX` lands the full release tree at `release/`.
3. **Publish install packages and update notes** to the GitHub Pages site at <https://devakm.github.io/devnull/> by writing into the sibling repo at `X:\dev\devnull\`.
4. **Distribute** the actual `.7z` install archive per release via **GitHub Releases** attached to each tag.

## Repo layout

| Path | Role |
|------|------|
| `release/` | The working tree of the **latest** ingested alpha. `git checkout <tag>` rewinds it to that historical release. |
| `manifests/alpha{NN}.json` | SHA-256 + size of every file in release `alphaNN`. One per release, sorted by path, pretty-printed JSON for line-level diffs. |
| `docs/overview.md` | What OOORS Full is, the bundle contents, design rationale. |
| `docs/dependencies.md` | OBSE, UE4SS, MagicLoader, TesSyncMapInjector — what the user must install separately. |
| `docs/installation.md` | Install steps (MO2 / Wabbajack / manual) for the latest release. |
| `docs/changelog.md` | Rolling top-level changelog. One section per release with a link to its per-release diff. |
| `docs/per-release/alpha{NN}.md` | Auto-generated added/removed/changed file list vs the previous release. |
| `scripts/` | Tooling — see *Tooling* below. |
| `dist/` | **Gitignored.** 7z packages produced by `package_release.py`. |
| `work/` | **Gitignored.** Scratch / experiments. |

## Source of truth

The release source folders are at `X:\games\Oscuro\Oscuro's_Oblivion_Remastered_Shivering_Full_alphaNN\` — **read-only** as far as this project is concerned. The repo is downstream of those folders.

| Source folder | Becomes |
|---------------|---------|
| `..._alpha00_preMerge\` | git tag `alpha00-premerge` (initial release commit) |
| `..._alpha01\` … `..._alpha90\` | git tags `alpha01` … `alpha90` on `main` |
| `..._alpha32nex\` | git tag `alpha32nex` on branch `alpha32nex` (forked off `alpha32`) |

Gaps in numbering (alpha 55, 56, 72) are missing source folders, not skipped releases.

## Tooling

| Script | Role |
|--------|------|
| `scripts/build_manifest.py` | Walk a directory, emit `{path: {sha256, size}}` JSON to stdout or file. Pure function, no side effects. |
| `scripts/diff_releases.py` | Given two manifest files, emit added / removed / changed file lists (as Markdown or JSON). |
| `scripts/ingest_release.py` | Single-release flow: copy `<source-folder>` → `release/`, write `manifests/<name>.json`, write `docs/per-release/<name>.md` (diff vs previous), `git add -A`, `git commit -m "<name>"`, `git tag <name>`. |
| `scripts/backfill_history.py` | Walk every alpha source folder in order and call `ingest_release.py` per folder. Handles `alpha00_preMerge` → `alpha32` → branch off `alpha32nex` → resume `main` at `alpha33` → … → `alpha90`. |
| `scripts/package_release.py` | 7zip `release/` → `dist/<name>.7z`. Idempotent. |
| `scripts/publish_github.py` | `gh release create <tag> dist/<tag>.7z --notes-file docs/per-release/<tag>.md`. **Defaults to `--dry-run`**; requires explicit `--for-real` flag to call `gh`. |
| `scripts/sync_pages.py` | Render the per-release index, changelog, and install instructions as HTML and write them into `X:\dev\devnull\docs\OOO\OBR\`. **Does not commit or push** the Pages repo — staging only. |

## Constraints

| Rule | Detail |
|------|--------|
| **Game install is READ-ONLY** | `C:\games\Steam\steamapps\common\Oblivion Remastered\` and everything beneath it must never be written to. The hook at `.claude/hooks/restrict-path.py` enforces this. |
| **Source release folders are READ-ONLY** | `X:\games\Oscuro\Oscuro's_Oblivion_Remastered_Shivering_Full_*` — copy from, never write to. The ingest script reads only. |
| **No publish without explicit approval** | `publish_github.py` and any `git push` must be invoked by the user, not initiated autonomously. Building, packaging, and writing to Pages staging is fine; uploading or pushing is not. |
| **LFS for binaries** | Anything matching `.gitattributes` LFS rules (`*.pak`, `*.ucas`, `*.utoc`, `*.esp`, `*.dll`, `*.exe`, etc.) goes through Git LFS. `.gitattributes` was committed in the very first commit so no `lfs migrate import` is ever needed. |
| **One commit per release** | `git log` is the canonical release history. Commit subject = release name (e.g. `alpha37`). Body links to the per-release diff doc. |
| **Tag every release** | Lightweight tag matching the release name. Tags are how `publish_github.py` finds the artifact to upload. |

## Implementation rules

| Rule | Detail |
|------|--------|
| **No writes to game install** | Hook-enforced; don't try to find workarounds. |
| **Dry-run by default** | Any script that produces external side effects (GitHub upload, git push, Pages commit) defaults to dry-run. |
| **Idempotent ingest** | Re-ingesting an already-tagged release is allowed (e.g. if the source folder gets re-fetched) but must detect the prior tag and either skip or `--force` re-tag. |
| **Manifest format is stable** | Keys sorted alphabetically; values pretty-printed with 2-space indent. So that `git diff` of two manifests is human-readable. |
| **Cross-platform paths in JSON** | Manifests store relative POSIX paths (`/`-separated), even on Windows. So manifests don't churn if regenerated on a different OS. |

## Critical files

| File | Role |
|------|------|
| `.gitattributes` | LFS routing rules. **Must** be in the first commit, before any binary is added. |
| `.gitignore` | Excludes `dist/`, `work/`, `*.7z`, `.claude/settings.local.json`. |
| `.claude/settings.json` | Permissions + the restrict-path hook. Committed. |
| `.claude/settings.local.json` | Per-user allow list. **Not** committed. |
| `.claude/hooks/restrict-path.py` | PreToolUse hook. Hard-blocks any tool call that would write to the game install path. Allows reads anywhere. |

## External resources

| Path | Role |
|------|------|
| `X:\games\Oscuro\` | Source release folders (read only). |
| `X:\dev\devnull\` | GitHub Pages site (`devakm/devnull` → <https://devakm.github.io/devnull/>). Output of `sync_pages.py` lands under `docs/OOO/OBR/` here. |
| `X:\dev\OblivionRemastered_ItemClone\` | Sister project. The `.claude/` setup here is borrowed and adapted from there. |
| `C:\games\Steam\steamapps\common\Oblivion Remastered\` | Game install. **Read-only**, hook-enforced. |

## Documentation discipline

After any meaningful change to the toolchain or repo layout: ask "does any `docs/*.md` need updating?" If yes, the doc update is part of the same commit. Undocumented findings are lost between sessions.
