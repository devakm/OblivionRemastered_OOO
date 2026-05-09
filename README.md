# Oscuro's Oblivion Overhaul Remastered FULL — Release Tracker

A version-controlled archive of every alpha / beta / release build of **Oscuro's Oblivion Overhaul Remastered FULL** ("OOORS Full"), with auto-generated per-release manifests so you can see exactly what changed from one build to the next.

- **Latest text content:** [`release/`](release/) — only the text files (JSON / INI / Lua / etc.) are checked into git. `git checkout <tag>` rewinds the text tree to any historical release.
- **Per-release manifests:** [`manifests/`](manifests/) — SHA-256 of every file (text AND binary) in every release, for diff and integrity checking.
- **Per-release changes:** [`docs/per-release/`](docs/per-release/) — added / removed / changed file lists vs the previous release.
- **Top-level changelog:** [`docs/changelog.md`](docs/changelog.md).
- **What this mod is:** [`docs/overview.md`](docs/overview.md).
- **Install instructions:** [`docs/installation.md`](docs/installation.md).
- **Dependencies:** [`docs/dependencies.md`](docs/dependencies.md).

## Downloading

Binary install archives (`.7z`) are attached to **GitHub Releases** for each tag. Browse releases at <https://github.com/devakm/OblivionRemastered_OOO/releases>.

A landing page with current and historical downloads is also published to <https://devakm.github.io/devnull/docs/OOO/OBR/>.

## How storage is split

| What | Where | Why |
|------|-------|-----|
| Manifests, per-release diff docs, scripts, project docs | git, plain text | Small, diffable. |
| Text from each release tree (JSON / INI / Lua / MD) | git, in `release/` | Lets `git diff` show actual record / config / script changes between any two releases. |
| Binary from each release tree (paks, ESPs, DLLs, textures) | NOT in git — in `dist/<tag>.7z`, uploaded as a GitHub Release asset | Keeps the repo tiny; binaries don't compress further with delta. |

## Tooling

See [`CLAUDE.md`](CLAUDE.md) for the full toolchain reference. Quick view:

```
scripts/build_manifest.py     # hash a tree → manifest JSON
scripts/diff_releases.py      # compare two manifests
scripts/ingest_release.py     # one source folder → text commit + tag + dist/<tag>.7z
scripts/backfill_history.py   # ingest every alpha source folder in order
scripts/package_release.py    # standalone .7z rebuilder
scripts/publish_github.py     # gh release create  (dry-run by default)
scripts/sync_pages.py         # render HTML into the devnull pages repo
```

## Repository status

- **Plain git only** — no Git LFS. Binaries don't enter the repo.
- **One commit per release**, message = the release name (e.g. `alpha37`).
- **One tag per release**, name = the release name.
- `alpha32nex` lives on its own branch off the `alpha32` commit (`variants/alpha32nex`).

## Reproducing a historical release

```bash
git checkout alpha75              # text tree at alpha75 lands in release/
# Then download alpha75.7z from the matching GitHub Release for the binaries:
#   https://github.com/devakm/OblivionRemastered_OOO/releases/tag/alpha75
```
