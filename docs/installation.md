# Installation

> **First time?** Install the [dependencies](dependencies.md) (Oblivion Remastered, UE4SS, MagicLoader, TesSyncMapInjector) before installing OOORS Full.

> **Upgrading from alpha91 or earlier:** install "UE4SS new" (see
> [dependencies](dependencies.md)) **before** you install alpha92. Install the
> UE4SS update and the alpha92 archive together. The alpha92 `RAX` DLL is not
> safe on the old UE4SS, and the old `RAX` DLL is not safe on the new UE4SS.
>
> alpha91 also installed `Begone` and `OOO_REFRFix` into `…\Binaries\Win64\ue4ss\Mods\`
> by default. alpha92 does not: they are optional test mods under
> `alpha92_test_optional\`. Installing over alpha91 does **not** remove the old
> copies. Delete `Mods\Begone\` and `Mods\OOO_REFRFix\` unless you want them; to
> use them, copy the alpha92 versions in from `alpha92_test_optional\`.

## Get the archive

Download the latest `.7z` from the [GitHub Releases page](https://github.com/devakm/OblivionRemastered_OOO/releases). Each release archive's contents mirror the structure of the game install — the top-level folders inside the `.7z` are `OblivionRemastered\` and `OOOInstallerFloydian1.jpg` (the latter is just the installer banner image; not needed in-game).

## Install — Mod Organizer 2 (recommended)

1. In MO2, **Add a new mod** → **Install a new mod from archive**.
2. Select the OOORS Full `.7z` you downloaded.
3. MO2 will detect the `OblivionRemastered\` root and offer to install it as a "Game data" mod. Accept.
4. Activate the mod (check it in the left pane).
5. In the right-pane plugin list, ensure `Oscuro's_Oblivion_Overhaul.esp` is checked. Optionally check any of the OptionalPatches that match your other mods.
6. Sort load order with LOOT (or your preferred tool).

### Optional test mods

`OblivionRemastered\alpha92_test_optional\` holds UE4SS mods that are not installed by default (`Begone`, `OOO_REFRFix`). Their install tree is intact: to enable one, copy its folder from `alpha92_test_optional\Binaries\Win64\ue4ss\Mods\` into `…\Binaries\Win64\ue4ss\Mods\`.

### Optional patches

To enable any OptionalPatch, **drag the relevant `.esp` from `…\Data\OptionalPatches\` up into `…\Data\`** so the engine sees it. Repeat for each you want.

If you're on the Deluxe Edition, also replace the regular `…\Data\SyncMap\Oscuro's_Oblivion_Overhaul.ini` with the one from `…\Data\OptionalPatches\SyncMap - DeluxeEdition\`.

## Install — manual

1. Open the `.7z` in 7-Zip.
2. Drag the contents of `OblivionRemastered\` into your `…\Oblivion Remastered\OblivionRemastered\` folder, accepting overwrites.
3. (Optional) For each patch you want active, move its ESP from `…\Data\OptionalPatches\` up one level into `…\Data\`.
4. (Optional) To enable a test mod, copy its folder from `…\alpha92_test_optional\Binaries\Win64\ue4ss\Mods\` into `…\Binaries\Win64\ue4ss\Mods\`.
5. Launch the game once and check the logs (see *Verifying the install*).

## Verifying the install

After the first launch, `<game>\OblivionRemastered\Binaries\Win64\ue4ss\UE4SS.log` should contain these lines:

```
UE4SS - v3.0.1 Beta #0 - Git SHA #5e627997
[RAX] build 7e53ab7
[RAX][AR] Maps: add "/game/maps/interiors/..." from "Oscuro's_Oblivion_Overhaul_CELLMAP.json" (MagicLoader)
[Lua] [BB's TesSyncMapInjector v0.1.8] --[[ Got Oblivion's Unreal Sync Map! ]]--
[Lua] [BB's TesSyncMapInjector v0.1.8] Applying Oscuro's_Oblivion_Overhaul.ini...
```

If the first line shows a different Git SHA, you have the wrong UE4SS. If there is no `[RAX] build` line, the RAX DLL did not load.

MagicLoader is a separate program that runs before the game. It writes its own log at `<game>\MagicLoader\Log.txt`, not the UE4SS log.

In-game smoke test: spawn into the world (any new game or existing save). Encountering OOO-only creatures, items, or the Obsidian armor / weapons confirms records loaded; teleporting to one of the new `L_*_Map` cells confirms the engine paks loaded.

## Updating to a newer release

1. Download the new `.7z` from GitHub Releases.
2. **Recommended:** review the diff doc on the release page (auto-generated from the manifest) to see which files changed — useful for spotting breaking changes ahead of time.
3. Reinstall on top of the existing install (overwrite). MO2 users: install the new archive as a separate mod and disable the old one, OR overwrite the existing mod entry.
4. **Save compatibility**: most updates are compatible with existing saves, but check the per-release notes — any release that changes ESP record FormIDs or removes ESPs may require a clean save or a new game.

## Uninstalling

- **MO2**: deactivate the mod entry, optionally delete it.
- **Manual**: delete the `Oscuro's_Oblivion_Overhaul.esp` from `…\Data\`, the matching `MagicLoader/Oscuro's_Oblivion_Overhaul_*.json`, the `SyncMap/Oscuro's_Oblivion_Overhaul.ini`, and any `L_*_Map.{pak,ucas,utoc}` plus the Obsidian paks from `…\Paks\~mods\`.
