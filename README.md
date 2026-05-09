# Oscuro's Oblivion Overhaul Remastered FULL — Release Tracker

A version-controlled archive of every alpha / beta / release build of **Oscuro's Oblivion Overhaul Remastered FULL** ("OOORS Full"), with auto-generated per-release manifests so you can see exactly what changed from one build to the next.

- **Latest release tree:** [`release/`](release/) — `git checkout <tag>` to view any historical version.
- **Per-release manifests:** [`manifests/`](manifests/) — SHA-256 of every file in every release, for diff and integrity checking.
- **Per-release changes:** [`docs/per-release/`](docs/per-release/) — added / removed / changed file lists vs the previous release.
- **Top-level changelog:** [`docs/changelog.md`](docs/changelog.md).
- **What this mod is:** [`docs/overview.md`](docs/overview.md).
- **Install instructions:** [`docs/installation.md`](docs/installation.md).
- **Dependencies:** [`docs/dependencies.md`](docs/dependencies.md).

## Downloading

The actual install archives (`.7z`) are attached to **GitHub Releases** for each tag. Browse releases at <https://github.com/devakm/OblivionRemastered_OOO/releases>.

A landing page with current and historical downloads is also published to <https://devakm.github.io/devnull/docs/OOO/OBR/>.

## Tooling

See [`CLAUDE.md`](CLAUDE.md) for the full toolchain reference. Quick view:

```
scripts/build_manifest.py     # hash a tree → manifest JSON
scripts/diff_releases.py      # compare two manifests
scripts/ingest_release.py     # one source folder → one repo commit + tag
scripts/backfill_history.py   # ingest every alpha source folder in order
scripts/package_release.py    # 7zip release/ → dist/<name>.7z
scripts/publish_github.py     # gh release create  (dry-run by default)
scripts/sync_pages.py         # render HTML into the devnull pages repo
```

## Repository status

Storage strategy:

- Plain git for everything text (ESP / INI / JSON / docs are small and benefit from line diffs).
- **Git LFS** for binaries (`*.pak`, `*.ucas`, `*.utoc`, `*.dll`, `*.exe`, `*.esp`, etc.) — see [`.gitattributes`](.gitattributes).

History strategy:

- **One commit per release**, message = the release name (e.g. `alpha37`).
- **One tag per release**, name = the release name.
- `alpha32nex` lives on its own branch off the `alpha32` commit.
