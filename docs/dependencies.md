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

[Nexus page](https://www.nexusmods.com/oblivionremastered/mods/1966).

OOORS Full ships its plugin in **two complementary forms**: a single `Oscuro's_Oblivion_Overhaul.esp` plus a per-record-type JSON config family containing localization strings and map-loading instructions under `…\ObvData\Data\MagicLoader\`. **MagicLoader** reads those JSONs at game start and merges them into the live record set. For non-English speakers, the localization strings can be replaced with your language of choice.

- Required for custom dungeons to load correctly and for localization strings to work (books, creature names, item names, spell names, location names, quest dialogue, etc.).

### TesSyncMapInjector (UE4SS Lua mod)

[Nexus page](https://www.nexusmods.com/oblivionremastered/mods/1272).

OOORS Full's `…\ObvData\Data\SyncMap\Oscuro's_Oblivion_Overhaul.ini` is a list of `<TES4 FormID hex>=<UE5 SoftObjectPath>` lines. **TesSyncMapInjector** consumes this at load time and rebinds each FormID to its UE5 asset path — the bridge that lets ESP records point at UE5 meshes/blueprints.

- Required to avoid invisible or missing assets and to prevent crashes when NPCs and creatures spawn. Also required for any new items, like the bundled item sets.

### UE4SS

The Unreal Engine 4 / 5 Scripting System. A loader for native DLL and Lua mods inside Unreal games.

**UE4SS — "UE4SS new", v3.0.1-1164 or later (required).**
Get it from <https://www.nexusmods.com/oblivionremastered/mods/32>, under
**Update files**, the file named **"UE4SS new"** (uploaded 10 Oct 2026). It
installs over an existing UE4SS: overwrite the files.

The **"UE4SS stable"** main file (3.0.1.a) is **not supported** from alpha92.
OOO's `RAX` mod contains a native DLL built for one exact UE4SS version.

- Required by **TesSyncMapInjector** (Lua) and by the bundled `RAX` mod (and by the optional `Begone` and `OOO_REFRFix` test mods, if you deploy them).

## Optional but supported

The OptionalPatches/ subfolder ships ESPs that add compatibility with these mods if you also have them installed:

| Patch ESP | Provides compatibility with |
|-----------|------------------------------|
| `OOO_DeluxeEdition.esp` | Oblivion Remastered Deluxe Edition (extra cosmetic/content). Pair with `SyncMap - DeluxeEdition/` override. |
| `OOO_OOMC_Compatibility_Patch.esp` | OOMC ([Opulent Outfits: Mages of Cyrodiil](https://www.nexusmods.com/oblivionremastered/mods/4992)). |
| `OOO_UORP.esp` | [The Unofficial Oblivion Remaster Patch](https://www.nexusmods.com/oblivionremastered/mods/477). |
| `OOO_UnlimitedRingsReduxPatch.esp` | [Unlimited Rings Redux](https://www.nexusmods.com/oblivionremastered/mods/2457). |

## Bundled UE4SS mods (auto-installed)

These ride along *inside* the OOORS Full archive — don't install separately, but they DO require UE4SS to be installed first.

| Mod (under `…\Binaries\Win64\ue4ss\Mods\`) | Role |
|--------------|------|
| `RAX/` | Allows loading of custom UE5 maps (the new `L_*_Map` dungeons). Native DLL (`dlls/main.dll`), built for "UE4SS new" v3.0.1-1164. Do not use it with any other UE4SS version. |

## Optional test UE4SS mods (manual deploy)

These run on UE4SS too, but are **not required for normal play**; they support the alpha-testing workflow. From alpha92 they are **not** installed by default. They ship under `OblivionRemastered\alpha92_test_optional\` with their install tree intact. To use one, copy its folder from `alpha92_test_optional\Binaries\Win64\ue4ss\Mods\` into `OblivionRemastered\Binaries\Win64\ue4ss\Mods\`.

| Mod | Role |
|-----|------|
| `Begone/` | **Test recording and debugging.** Originally Begone hid UE5 ghost objects at runtime per `Config/OscurosOblivionOverhaul.json`; alpha90 baked that suppression into the map paks. From alpha92 Begone is log-only: it suppresses nothing. Its remaining use is capturing per-cell object inventories during alpha-test walkthroughs and checking suppression coverage when new map paks are built. |
| `OOO_REFRFix/` | **Save-file migration helper.** Patches OOO reference placements that need runtime correction; see `Scripts/spawn_deltas.lua`. Only needed if you have existing saves carrying OOO references from older alpha releases. |

## Game install layout reference

```
…\Oblivion Remastered\
├── OblivionRemastered\
│   ├── Binaries\Win64\
│   │   └── ue4ss\          ← UE4SS install lives here; bundled Mods\ overlays into it
│   ├── alpha92_test_optional\  ← optional test mods, same tree; copy by hand to enable
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
