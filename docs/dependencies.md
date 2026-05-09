# Dependencies

These are the runtime components a player needs to install themselves. **None of them are bundled in the OOORS Full release archive** — install them separately before deploying OOORS Full.

## Required

### Oblivion Remastered

The base game. Install via Steam, Game Pass, or your platform of choice.

| Detail | Value |
|--------|-------|
| Engine | Unreal Engine 5.3 |
| Default content path | `…\Oblivion Remastered\OblivionRemastered\Content\` |
| Default mod-pak path | `…\Oblivion Remastered\OblivionRemastered\Content\Paks\~mods\` |
| TES4 data path | `…\Oblivion Remastered\OblivionRemastered\Content\Dev\ObvData\Data\` |

### MagicLoader

OOORS Full ships its plugin in **two complementary forms**: a single `Oscuro's_Oblivion_Overhaul.esp` plus a per-record-type JSON family under `…\ObvData\Data\MagicLoader\`. **MagicLoader** reads those JSONs at game start and merges them into the live record set, sidestepping the 255-plugin load-order limit.

- Required for everything record-related to work (creatures, items, spells, etc.) beyond what the bare ESP defines.

### TesSyncMapInjector (UE4SS Lua mod)

OOORS Full's `…\ObvData\Data\SyncMap\Oscuro's_Oblivion_Overhaul.ini` is a list of `<TES4 FormID hex>=<UE5 SoftObjectPath>` lines. **TesSyncMapInjector** consumes this at load time and rebinds each FormID to its UE5 asset path — the bridge that lets ESP records point at UE5 meshes/blueprints.

- Required for any item / object whose ESP record was authored to point at a non-default UE5 asset (e.g. the bundled Obsidian items).

### UE4SS

The Unreal Engine 4 / 5 Scripting System. A loader for native DLL and Lua mods inside Unreal games.

- Required by **TesSyncMapInjector** (Lua) and by the bundled `Begone`, `OOO_REFRFix`, `RAX` mods.

## Optional but supported

The OptionalPatches/ subfolder ships ESPs that add compatibility with these mods if you also have them installed:

| Patch ESP | Provides compatibility with |
|-----------|------------------------------|
| `OOO_DeluxeEdition.esp` | Oblivion Remastered Deluxe Edition (extra cosmetic/content). Pair with `SyncMap - DeluxeEdition/` override. |
| `OOO_OOMC_Compatibility_Patch.esp` | OOMC (Oscuro's Oblivion Modular Companions / Mod Components). |
| `OOO_UORP.esp` | The Unofficial Oblivion Remaster Patch. |
| `OOO_UnlimitedRingsReduxPatch.esp` | Unlimited Rings Redux. |

## Bundled UE4SS mods (auto-installed)

These ride along *inside* the OOORS Full archive — don't install separately, but they DO require UE4SS to be installed first.

| Mod (under `…\Binaries\Win64\ue4ss\Mods\`) | Role |
|--------------|------|
| `Begone/` | Removes specific references at runtime per the bundled `Config/OscurosOblivionOverhaul.json`. |
| `OOO_REFRFix/` | Patches OOO reference placements that need runtime correction; see `Scripts/spawn_deltas.lua`. |
| `RAX/` | Provides native helpers via `dlls/main.dll` plus Lua glue. |

## Game install layout reference

```
…\Oblivion Remastered\
├── OblivionRemastered\
│   ├── Binaries\Win64\
│   │   └── ue4ss\          ← UE4SS install lives here; bundled Mods\ overlays into it
│   └── Content\
│       ├── Dev\ObvData\Data\
│       │   ├── MagicLoader\         ← MagicLoader looks here
│       │   ├── SyncMap\             ← TesSyncMapInjector looks here
│       │   ├── OptionalPatches\     ← OOORS-shipped patch ESPs (move into Data\ to enable)
│       │   ├── *.esp                ← TES4 plugins
│       │   └── *.esm                ← TES4 master files
│       └── Paks\
│           └── ~mods\               ← IoStore content (.pak/.ucas/.utoc) drops here
```
