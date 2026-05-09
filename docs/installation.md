# Installation

> **First time?** Install the [dependencies](dependencies.md) (Oblivion Remastered, UE4SS, MagicLoader, TesSyncMapInjector) before installing OOORS Full.

## Get the archive

Download the latest `.7z` from the [GitHub Releases page](https://github.com/devakm/OblivionRemastered_OOO/releases). Each release archive's contents mirror the structure of the game install — the top-level folders inside the `.7z` are `OblivionRemastered\` and `OOOInstallerFloydian1.jpg` (the latter is just the installer banner image; not needed in-game).

## Install — Mod Organizer 2 (recommended)

1. In MO2, **Add a new mod** → **Install a new mod from archive**.
2. Select the OOORS Full `.7z` you downloaded.
3. MO2 will detect the `OblivionRemastered\` root and offer to install it as a "Game data" mod. Accept.
4. Activate the mod (check it in the left pane).
5. In the right-pane plugin list, ensure `Oscuro's_Oblivion_Overhaul.esp` is checked. Optionally check any of the OptionalPatches that match your other mods.
6. Sort load order with LOOT (or your preferred tool).

### Optional patches

To enable any OptionalPatch, **drag the relevant `.esp` from `…\Data\OptionalPatches\` up into `…\Data\`** so the engine sees it. Repeat for each you want.

If you're on the Deluxe Edition, also replace the regular `…\Data\SyncMap\Oscuro's_Oblivion_Overhaul.ini` with the one from `…\Data\OptionalPatches\SyncMap - DeluxeEdition\`.

## Install — manual

1. Open the `.7z` in 7-Zip.
2. Drag the contents of `OblivionRemastered\` into your `…\Oblivion Remastered\OblivionRemastered\` folder, accepting overwrites.
3. (Optional) For each patch you want active, move its ESP from `…\Data\OptionalPatches\` up one level into `…\Data\`.
4. Launch the game once via UE4SS to confirm MagicLoader logs the OOORS Full JSONs and TesSyncMapInjector loads the SyncMap INI.

## Verifying the install

After the first launch, you should see in the UE4SS log:

- `MagicLoader: loaded N records from Oscuro's_Oblivion_Overhaul_*.json` (one line per record-type JSON).
- `TesSyncMapInjector: loaded Oscuro's_Oblivion_Overhaul.ini`.

In-game smoke test: spawn into the world (any new game or existing save). Encountering OOO-only creatures, items, or the Obsidian armor / weapons confirms records loaded; teleporting to one of the new `L_*_Map` cells confirms the engine paks loaded.

## Updating to a newer release

1. Download the new `.7z` from GitHub Releases.
2. **Recommended:** review the diff doc on the release page (auto-generated from the manifest) to see which files changed — useful for spotting breaking changes ahead of time.
3. Reinstall on top of the existing install (overwrite). MO2 users: install the new archive as a separate mod and disable the old one, OR overwrite the existing mod entry.
4. **Save compatibility**: most updates are compatible with existing saves, but check the per-release notes — any release that changes ESP record FormIDs or removes ESPs may require a clean save or a new game.

## Uninstalling

- **MO2**: deactivate the mod entry, optionally delete it.
- **Manual**: delete the `Oscuro's_Oblivion_Overhaul.esp` from `…\Data\`, the matching `MagicLoader/Oscuro's_Oblivion_Overhaul_*.json`, the `SyncMap/Oscuro's_Oblivion_Overhaul.ini`, and any `L_*_Map.{pak,ucas,utoc}` plus the Obsidian paks from `…\Paks\~mods\`.
