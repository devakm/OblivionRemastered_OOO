# Changelog

Top-level rolling index. **One entry per release**, newest first. Each release has a per-release diff doc under [`per-release/`](per-release/) that lists the exact added / removed / changed files vs the previous release.

For machine-readable diffs, compare the manifests in [`../manifests/`](../manifests/):

```bash
git diff alpha75..alpha90 -- manifests/
```

## Release index

> Auto-maintainable — `scripts/sync_pages.py` walks `git tag --merged main --sort=v:refname` to enumerate the same list when generating the GitHub Pages changelog. If you add a release manually outside the ingest flow, regenerate this index with:
>
> ```bash
> py -3 -c "import subprocess; t=subprocess.run(['git','tag','--merged','main','--sort=v:refname'],capture_output=True,text=True).stdout.split(); [print(f'- [{x}](per-release/{x}.md)') for x in reversed(t)]"
> ```

### Main line

The full list lives at [`per-release/`](per-release/). Open any specific release's diff:

- Latest stable: see [`per-release/alpha90.md`](per-release/alpha90.md)
- Previous: see [`per-release/alpha89.md`](per-release/alpha89.md)
- … and so on, back to [`per-release/alpha00-premerge.md`](per-release/alpha00-premerge.md)

### Variants

- [`per-release/alpha32nex.md`](per-release/alpha32nex.md) — parallel Nexus-prep variant of `alpha32`. Lives on the `variants/alpha32nex` git branch.

## How releases are named

| Pattern | Example | Meaning |
|---------|---------|---------|
| `alphaNN` | `alpha37` | Main-line alpha. One per source folder `..._alphaNN`. |
| `alpha00-premerge` | `alpha00-premerge` | The pre-merge snapshot (multiple legacy ESPs side-by-side). Tagged from source folder `..._alpha00_preMerge`. |
| `alphaNNxxx` | `alpha32nex` | Variant of `alphaNN`. Lives on a `variants/<name>` branch off the parent tag. |

## How a release becomes a commit

Every release is one commit on `main` (or on `variants/<name>` for variants). Commit subject = the tag name. The commit body links to the per-release diff doc.

```
git log --oneline alpha85..alpha90
```

## Numbering gaps

Some alpha numbers are absent from the source folder set: alpha 55, 56, and 72. Those are missing source folders, not skipped releases — the repo simply has no record of them.
