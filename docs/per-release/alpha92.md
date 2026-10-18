# alpha92 — release notes

_Compared against `alpha91`._

## Highlights

### Requires a UE4SS update

alpha92 needs **"UE4SS new" (v3.0.1-1164)** from the
[UE4SS Nexus page](https://www.nexusmods.com/oblivionremastered/mods/32) (under
**Update files**). Install it over your existing UE4SS **before** you install
alpha92. The older "UE4SS stable" (3.0.1.a) is no longer supported: the alpha92
`RAX` DLL is not safe on it, and the alpha91 `RAX` DLL is not safe on the new one.

- **RAX rebuilt for the new UE4SS.** No change to what RAX does: custom map
  loading and the leveled-spell fix work as before.
- **Fewer crashes after level loads (expected).** The new UE4SS fixes a crash in
  Lua mods that check a game object after a fast travel, a cell change or a save
  load. In testing, repeated fast travel and loading a different save after a long
  session are more stable. Testing continues.
- **Other UE4SS mods:** the UE4SS page warns that some older UE4SS mods may not
  work with "UE4SS new". TesSyncMapInjector v0.1.8 and MagicLoader v2.9 work with it.

### Begone and OOO_REFRFix are now optional test mods

RAX is now the only UE4SS mod installed by default. `Begone` (now log-only: it
suppresses nothing) and `OOO_REFRFix` ship under
`OblivionRemastered\alpha92_test_optional\` with their install tree intact; copy a
mod's folder from `alpha92_test_optional\Binaries\Win64\ue4ss\Mods\` into
`Binaries\Win64\ue4ss\Mods\` to use it.

**Upgrading from alpha91:** installing over alpha91 does **not** remove the old
`Mods\Begone\` and `Mods\OOO_REFRFix\` folders. Delete them unless you want them.

### 21 new item sets, and SyncMap remapping

Ancestral, BladesElite, DaedricPrince, DarkMalachite, Draconis, Dragonborne,
Dread, DremoraElite, DurableSteel, ImagoStorm, Light of Dawn (four sword
variants), Noble, TheBear, UnfinishedAncestral, UnfinishedSteel,
UnfinishedWornSteel, WornAncestral and WornSteel.

About 120 OOO items that borrowed a vanilla mesh in alpha91 now point at their own
set in the SyncMap: for example Dread armor (was Daedric), Noble (was Ebony),
Durable Steel (was Steel), the Ancestral sets (were Amelion), Daedric Prince (was
Daedric and Dremora), Vella's armor (now BlueGlass and DarkMalachite), the Light
of Dawn swords (were Rugdumph's sword) and the enchanted RGlass greaves (now
Drakefired greaves). The Aureus, Drakefired, Eboron, GrayFox and Obsidian sets
were rebuilt.

### Dungeons

**All classic OOO dungeons are now complete.** Gloom Way Cave and Red Gill Cave,
the last two, are finished in alpha92, with their water approved in-game.

## Summary

- **Item sets added (21):** Ancestral, BladesElite, DaedricPrince, DarkMalachite, Draconis, Dragonborne, Dread, DremoraElite, DurableSteel, ImagoStorm, LightOfDawn, LightOfDawn0, LightOfDawnA, LightOfDawnB, Noble, TheBear, UnfinishedAncestral, UnfinishedSteel, UnfinishedWornSteel, WornAncestral, WornSteel
- **Dungeon map paks rebuilt (2 paks / 3 zones):** L_GloomWayCaveXX_Map, L_RedGillCave_Map
- **Item sets updated (5):** Aureus, Drakefired, Eboron, GrayFox, Obsidian
- **SyncMap:** ~120 asset remappings (+4 -2) — see below
- **MagicLoader `Oscuro's_Oblivion_Overhaul_ARMO.json`:** +0 -0 ~6 display names
- **MagicLoader `Oscuro's_Oblivion_Overhaul_SPELL.json`:** +8 -0 ~0 display names
- **TES4 REFR suppression:** +0 disabled REFRs, +0 position overrides — see Map cell changes
- **UE5-layer ghost suppression (static, baked into map paks):** net +30 entries
- **ESP records:** see ESP changes section(s) below

## File-level changes

- Added: 133
- Removed: 7
- Changed: 27

### Added (133)

- `OblivionRemastered/Content/Paks/~mods/AncestralItems.pak`
- `OblivionRemastered/Content/Paks/~mods/AncestralItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/AncestralItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/AncestralMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/AncestralMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/AncestralMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/BladesEliteItems.pak`
- `OblivionRemastered/Content/Paks/~mods/BladesEliteItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/BladesEliteItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/BladesEliteMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/BladesEliteMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/BladesEliteMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DaedricPrinceItems.pak`
- `OblivionRemastered/Content/Paks/~mods/DaedricPrinceItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/DaedricPrinceItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/DaedricPrinceMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/DaedricPrinceMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DaedricPrinceMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DarkMalachiteItems.pak`
- `OblivionRemastered/Content/Paks/~mods/DarkMalachiteItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/DarkMalachiteItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/DarkMalachiteMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/DarkMalachiteMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DarkMalachiteMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DraconisItems.pak`
- `OblivionRemastered/Content/Paks/~mods/DraconisItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/DraconisItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/DraconisMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/DraconisMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DraconisMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DragonborneItems.pak`
- `OblivionRemastered/Content/Paks/~mods/DragonborneItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/DragonborneItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/DragonborneMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/DragonborneMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DragonborneMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DreadItems.pak`
- `OblivionRemastered/Content/Paks/~mods/DreadItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/DreadItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/DreadMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/DreadMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DreadMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DremoraEliteItems.pak`
- `OblivionRemastered/Content/Paks/~mods/DremoraEliteItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/DremoraEliteItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/DremoraEliteMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/DremoraEliteMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DremoraEliteMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DurableSteelItems.pak`
- `OblivionRemastered/Content/Paks/~mods/DurableSteelItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/DurableSteelItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/DurableSteelMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/DurableSteelMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DurableSteelMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/ImagoStormItems.pak`
- `OblivionRemastered/Content/Paks/~mods/ImagoStormItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/ImagoStormItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/ImagoStormMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/ImagoStormMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/ImagoStormMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawn0Items.pak`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawn0Items.ucas`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawn0Items.utoc`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawn0Materials.pak`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawn0Materials.ucas`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawn0Materials.utoc`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnAItems.pak`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnAItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnAItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnAMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnAMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnAMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnBItems.pak`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnBItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnBItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnBMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnBMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnBMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnItems.pak`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/NobleItems.pak`
- `OblivionRemastered/Content/Paks/~mods/NobleItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/NobleItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/NobleMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/NobleMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/NobleMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/TheBearItems.pak`
- `OblivionRemastered/Content/Paks/~mods/TheBearItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/TheBearItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/TheBearMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/TheBearMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/TheBearMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedAncestralItems.pak`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedAncestralItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedAncestralItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedAncestralMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedAncestralMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedAncestralMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedSteelItems.pak`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedSteelItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedSteelItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedSteelMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedSteelMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedSteelMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedWornSteelItems.pak`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedWornSteelItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedWornSteelItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedWornSteelMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedWornSteelMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedWornSteelMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/WornAncestralItems.pak`
- `OblivionRemastered/Content/Paks/~mods/WornAncestralItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/WornAncestralItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/WornAncestralMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/WornAncestralMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/WornAncestralMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/WornSteelItems.pak`
- `OblivionRemastered/Content/Paks/~mods/WornSteelItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/WornSteelItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/WornSteelMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/WornSteelMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/WornSteelMaterials.utoc`
- `OblivionRemastered/alpha92_test_optional/Binaries/Win64/ue4ss/Mods/Begone/Config/OscurosOblivionOverhaul.json`
- `OblivionRemastered/alpha92_test_optional/Binaries/Win64/ue4ss/Mods/Begone/Scripts/main.lua`
- `OblivionRemastered/alpha92_test_optional/Binaries/Win64/ue4ss/Mods/Begone/enabled.txt`
- `OblivionRemastered/alpha92_test_optional/Binaries/Win64/ue4ss/Mods/OOO_REFRFix/Scripts/main.lua`
- `OblivionRemastered/alpha92_test_optional/Binaries/Win64/ue4ss/Mods/OOO_REFRFix/Scripts/spawn_deltas.lua`
- `OblivionRemastered/alpha92_test_optional/Binaries/Win64/ue4ss/Mods/OOO_REFRFix/Scripts/tests.lua`
- `OblivionRemastered/alpha92_test_optional/Binaries/Win64/ue4ss/Mods/OOO_REFRFix/enabled.txt`

### Removed (7)

- `OblivionRemastered/Binaries/Win64/ue4ss/Mods/Begone/Config/OscurosOblivionOverhaul.json`
- `OblivionRemastered/Binaries/Win64/ue4ss/Mods/Begone/Scripts/main.lua`
- `OblivionRemastered/Binaries/Win64/ue4ss/Mods/Begone/enabled.txt`
- `OblivionRemastered/Binaries/Win64/ue4ss/Mods/OOO_REFRFix/Scripts/main.lua`
- `OblivionRemastered/Binaries/Win64/ue4ss/Mods/OOO_REFRFix/Scripts/spawn_deltas.lua`
- `OblivionRemastered/Binaries/Win64/ue4ss/Mods/OOO_REFRFix/Scripts/tests.lua`
- `OblivionRemastered/Binaries/Win64/ue4ss/Mods/OOO_REFRFix/enabled.txt`

### Changed (27)

- `OblivionRemastered/Binaries/Win64/ue4ss/Mods/RAX/dlls/main.dll`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ARMO.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CREA.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_QUST.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_SPELL.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_WEAP.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/OptionalPatches/SyncMap - DeluxeEdition/Oscuro's_Oblivion_Overhaul.ini`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`
- `OblivionRemastered/Content/Paks/~mods/AureusMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/AureusMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DrakefiredMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DrakefiredMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/EboronMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/EboronMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/GrayFoxItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/GrayFoxItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/GrayFoxMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/GrayFoxMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/L_GloomWayCaveXX_Map.ucas`
- `OblivionRemastered/Content/Paks/~mods/L_GloomWayCaveXX_Map.utoc`
- `OblivionRemastered/Content/Paks/~mods/L_RedGillCave_Map.ucas`
- `OblivionRemastered/Content/Paks/~mods/L_RedGillCave_Map.utoc`
- `OblivionRemastered/Content/Paks/~mods/ObsidianItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/ObsidianItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/ObsidianMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/ObsidianMaterials.utoc`

## SyncMap asset remappings — +4 -2 ~120

FormID → UE5 asset mappings (TesSyncMapInjector). Changed entries re-point existing FormIDs at new item-set visuals, grouped by target set.

### Changed (120)

**DaedricPrince** (14)

- `01ABF9`: `DaedricBoots` → `DaedricPrinceBoots`
- `01ABFA`: `Dremora3KynreeveCuirass` → `DaedricPrinceCuirass`
- `01ABFB`: `DaedricGauntlets` → `DaedricPrinceGauntlets`
- `01ABFC`: `DaedricGreaves` → `DaedricPrinceGreaves`
- `01ABFD`: `DaedricHelmet` → `DaedricPrinceHelmet`
- `01ABFE`: `DaedricHelmet` → `DaedricPrinceHelmet`
- `01ABFF`: `DaedricShield` → `DaedricPrinceShield`
- `038D4F`: `DaedricBoots` → `DaedricPrinceBoots`
- `038D50`: `Dremora3KynreeveCuirass` → `DaedricPrinceCuirass`
- `038D51`: `DaedricGauntlets` → `DaedricPrinceGauntlets`
- `038D52`: `DaedricGreaves` → `DaedricPrinceGreaves`
- `038D53`: `DaedricHelmet` → `DaedricPrinceHelmet`
- `038D54`: `DaedricShield` → `DaedricPrinceShield`
- `04F482`: `DaedricHelmet` → `DaedricPrinceHelmet`

**DremoraElite** (11)

- `033A6F`: `DaedricBoots` → `DremoraEliteBoots`
- `033A70`: `Dremora3KynreeveCuirass` → `DremoraEliteCuirass`
- `033A71`: `DaedricGauntlets` → `DremoraEliteGauntlets`
- `033A72`: `DaedricGreaves` → `DremoraEliteGreaves`
- `033A73`: `DaedricHelmet` → `DremoraEliteHelmet`
- `034941`: `DaedricBoots` → `DremoraEliteBoots`
- `034942`: `Dremora3KynreeveCuirass` → `DremoraEliteCuirass`
- `034943`: `DaedricGauntlets` → `DremoraEliteGauntlets`
- `034944`: `DaedricGreaves` → `DremoraEliteGreaves`
- `034945`: `DaedricHelmet` → `DremoraEliteHelmet`
- `034952`: `DaedricShield` → `DremoraEliteShield`

**Dread** (10)

- `002650`: `DaedricBoots` → `DreadBoots`
- `002651`: `DaedricCuirass` → `DreadCuirass`
- `002652`: `DaedricGauntlets` → `DreadGauntlets`
- `002653`: `DaedricGreaves` → `DreadGreaves`
- `002654`: `DaedricHelmet` → `DreadHelmet`
- `06EA3C`: `DaedricCuirass` → `DreadCuirass`
- `06EA3D`: `DaedricBoots` → `DreadBoots`
- `06EA3E`: `DaedricGauntlets` → `DreadGauntlets`
- `06EA3F`: `DaedricGreaves` → `DreadGreaves`
- `06EA40`: `DaedricHelmet` → `DreadHelmet`

**Ancestral** (8)

- `00DE61`: `FGC07AmelionBoots` → `AncestralBoots`
- `00DE62`: `FGC07AmelionCuirass` → `AncestralCuirass`
- `00DE63`: `FGC07AmelionGauntlets` → `AncestralGauntlets`
- `00DE64`: `FGC07AmelionGreaves` → `AncestralGreaves`
- `00DE65`: `FGC07AmelionHelmet` → `AncestralHelmet`
- `00DE66`: `FGC07AmelionShield` → `AncestralShield`
- `026C63`: `FGC07AmelionHelmet` → `AncestralHelmet`
- `026C64`: `FGC07AmelionShield` → `AncestralShield`

**Drakefired** (8)

- `0079F5`: `DrakefiredBoots` → `DrakefiredGreaves`
- `0079F6`: `DrakefiredBoots` → `DrakefiredGreaves`
- `0079F7`: `DrakefiredBoots` → `DrakefiredGreaves`
- `0079F8`: `DrakefiredBoots` → `DrakefiredGreaves`
- `0079F9`: `DrakefiredBoots` → `DrakefiredGreaves`
- `0079FA`: `DrakefiredBoots` → `DrakefiredGreaves`
- `0079FB`: `DrakefiredBoots` → `DrakefiredGreaves`
- `007A05`: `DrakefiredBoots` → `DrakefiredGreaves`

**BlueGlass** (6)

- `0329CF`: `GlassBoots` → `BlueGlassBoots`
- `0329D0`: `GlassCuirass` → `BlueGlassCuirass`
- `0329D1`: `GlassGauntlets` → `BlueGlassGauntlets`
- `0329D2`: `GlassGreaves` → `BlueGlassGreaves`
- `0329D3`: `GlassHelmet` → `BlueGlassHelmet`
- `0329D4`: `GlassShield` → `BlueGlassShield`

**DurableSteel** (6)

- `00DE2E`: `SteelBoots` → `DurableSteelBoots`
- `00DE2F`: `SteelCuirass` → `DurableSteelCuirass`
- `00DE30`: `SteelGauntlets` → `DurableSteelGauntlets`
- `00DE31`: `SteelGreaves` → `DurableSteelGreaves`
- `00DE32`: `SteelHelmet` → `DurableSteelHelmet`
- `00DE33`: `SteelShield` → `DurableSteelShield`

**Noble** (6)

- `0072EF`: `EbonyBoots` → `NobleBoots`
- `0072F0`: `EbonyCuirass` → `NobleCuirass`
- `0072F1`: `EbonyGauntlets` → `NobleGauntlets`
- `0072F2`: `EbonyGreaves` → `NobleGreaves`
- `0072F3`: `EbonyHelmet` → `NobleHelmet`
- `0072F4`: `EbonyShield` → `NobleShield`

**TheBear** (6)

- `044F32`: `FGC07AmelionBoots` → `TheBearBoots`
- `044F33`: `FGC07AmelionCuirass` → `TheBearCuirass`
- `044F34`: `FGC07AmelionGauntlets` → `TheBearGauntlets`
- `044F35`: `FGC07AmelionGreaves` → `TheBearGreaves`
- `044F36`: `FGC07AmelionHelmet` → `TheBearHelmet`
- `044F37`: `FGC07AmelionShield` → `TheBearShield`

**WornSteel** (6)

- `021BC1`: `SteelBoots` → `WornSteelBoots`
- `021BC2`: `SteelCuirass` → `WornSteelCuirass`
- `021BC3`: `SteelGauntlets` → `WornSteelGauntlets`
- `021BC4`: `SteelGreaves` → `WornSteelGreaves`
- `021BC5`: `SteelHelmet` → `WornSteelHelmet`
- `021BC6`: `SteelShield` → `WornSteelShield`

**BladesElite** (5)

- `03578B`: `BladesBoots` → `BladesEliteBoots`
- `03578C`: `BladesCuirass` → `BladesEliteCuirass`
- `03578D`: `BladesGauntlets` → `BladesEliteGauntlets`
- `03578E`: `BladesGreaves` → `BladesEliteGreaves`
- `03578F`: `BladesHelmet` → `BladesEliteHelmet`

**Dragonborne** (5)

- `027156`: `ChainmailBoots` → `DragonborneBoots`
- `027157`: `ChainmailCuirass` → `DragonborneCuirass`
- `027158`: `ChainmailGauntlets` → `DragonborneGauntlets`
- `027159`: `ChainmailGreaves` → `DragonborneGreaves`
- `02715A`: `ChainmailShield` → `DragonborneShield`

**ImagoStorm** (5)

- `029F17`: `DaedricBoots` → `ImagoStormBoots`
- `029F18`: `Dremora3KynreeveCuirass` → `ImagoStormCuirass`
- `029F19`: `DaedricGauntlets` → `ImagoStormGauntlets`
- `029F1A`: `DaedricGreaves` → `ImagoStormGreaves`
- `029F1B`: `DaedricHelmet` → `ImagoStormHelmet`

**DarkMalachite** (4)

- `0329CD`: `GlassCuirass` → `DarkMalachiteCuirass`
- `0329CE`: `GlassBoots` → `DarkMalachiteGreaves`
- `034754`: `GlassBoots` → `DarkMalachiteBoots`
- `034C3B`: `GlassGauntlets` → `DarkMalachiteGauntlets`

**UnfinishedAncestral** (4)

- `0392F3`: `FGC07AmelionBoots` → `UnfinishedAncestralBoots`
- `0392F4`: `FGC07AmelionCuirass` → `UnfinishedAncestralCuirass`
- `0392F5`: `FGC07AmelionGauntlets` → `UnfinishedAncestralGauntlets`
- `0392F6`: `FGC07AmelionGreaves` → `UnfinishedAncestralGreaves`

**WornAncestral** (4)

- `0392EF`: `FGC07AmelionBoots` → `WornAncestralBoots`
- `0392F0`: `FGC07AmelionCuirass` → `WornAncestralCuirass`
- `0392F1`: `FGC07AmelionGauntlets` → `WornAncestralGauntlets`
- `0392F2`: `FGC07AmelionGreaves` → `WornAncestralGreaves`

**Draconis** (2)

- `003C1C`: `GlassCuirass` → `DraconisCuirass`
- `003C1D`: `GlassShield` → `DraconisShield`

**LightOfDawn0Sword** (2)

- `004E56`: `FGC09RugdumphSword` → `LightOfDawn0Sword`
- `013400`: `WeapAkaviriLongSword2H` → `LightOfDawn0Sword`

**LightOfDawnASword** (2)

- `004E57`: `FGC09RugdumphSword` → `LightOfDawnASword`
- `006C93`: `FGC09RugdumphSword` → `LightOfDawnASword`

**LightOfDawnBSword** (2)

- `004E58`: `FGC09RugdumphSword` → `LightOfDawnBSword`
- `006C94`: `FGC09RugdumphSword` → `LightOfDawnBSword`

**LightOfDawnSword** (2)

- `004E59`: `FGC09RugdumphSword` → `LightOfDawnSword`
- `006C95`: `FGC09RugdumphSword` → `LightOfDawnSword`

**UnfinishedSteel** (1)

- `03AB9D`: `SteelCuirass` → `UnfinishedSteelCuirass`

**UnfinishedWornSteel** (1)

- `03ABA1`: `SteelCuirass` → `UnfinishedWornSteelCuirass`

### Added (4)

- `00DE98`: `LightOfDawn0Sword`
- `00DE99`: `LightOfDawnASword`
- `00DE9A`: `LightOfDawnBSword`
- `00DE9B`: `LightOfDawnSword`

### Removed (2)

- `025E4C`: `TestIstZombie01`
- `05D2BC`: `CreatureGhost`

## MagicLoader changes

Display-name (`FullNames`) changes in the MagicLoader JSON exports.

### `Oscuro's_Oblivion_Overhaul_ARMO.json` — +0 -0 ~6

- ~ `LOC_FN_UniqueHarbingerBootsOOO`: "Harbinger Boots" → "Ancient Harbinger Boots"
- ~ `LOC_FN_UniqueHarbingerCuirassOOO`: "Harbinger Cuirass" → "Ancient Harbinger Cuirass"
- ~ `LOC_FN_UniqueHarbingerGauntletsOOO`: "Harbinger Gauntlets" → "Ancient Harbinger Gauntlets"
- ~ `LOC_FN_UniqueHarbingerGreavesOOO`: "Harbinger Greaves" → "Ancient Harbinger Greaves"
- ~ `LOC_FN_UniqueHarbingerHelmetOOO`: "Harbinger Helmet" → "Ancient Harbinger Helmet"
- ~ `LOC_FN_UniqueHarbingerShieldOOO`: "Harbinger Shield" → "Ancient Harbinger Shield"

### `Oscuro's_Oblivion_Overhaul_SPELL.json` — +8 -0 ~0

- + `LOC_FN_ZZBoarSummonPlayer` = "Jephre's Tusks"
- + `LOC_FN_ZZDeerSummonPlayer` = "Jephre's Pride"
- + `LOC_FN_ZZLeopardSnowSummonPlayer` = "Jephre's White Shadow"
- + `LOC_FN_ZZLeopardSummonPlayer` = "Jephre's Jungle Guardian"
- + `LOC_FN_ZZLionSnowSummonPlayer` = "Jephre's Arctic Claws"
- + `LOC_FN_ZZLionSummonPlayer` = "Jephre's Fangs"
- + `LOC_FN_ZZWolfSummonPlayer` = "Jephre's Forest Guardian"
- + `LOC_FN_ZZWolfTundraSummonPlayer` = "Jephre's Tundra Guardian"

## Map cell changes since `alpha91`

Each OOO cell layers TES4-injected OOO content over UE5-baked remaster geometry; these reconcile the two so each object renders from exactly one layer. Sourced from MapClone configs (baseline `3a97a51b10a9`).

- **TES4 REFR suppression** — disable OOO REFRs that *duplicate* UE5-baked architecture (drop the TES4 twin, keep the UE5 copy).
- **UE5-layer ghost suppression (static)** — remove UE5-baked actors with *no* TES4 counterpart (drop the UE5 ghost, keep TES4). Applied at build time by MapClone's static patcher and baked into the map paks; the Begone UE4SS mod no longer suppresses anything at runtime.
- **Position overrides** — re-seat OOO REFRs (chests/furniture) left floating once a supporting STAT was disabled.

### UE5-layer ghost suppression (static, baked into map paks)

net +30 entries (1333 → 1363; 46 → 46 cells)

- **L_GloomWayCaveXX**: +20 (total 94)
- **L_GloomWayCave02**: +10 (total 94)
- **L_GloomWayCaveXX_Li**: +2 (total 6)
- **L_DrownedHopesCa02**: -1 (total 28)
- **L_RedGillCave_Li**: -1 (total 12)

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Armor (ARMO) — +0 -0 ~12

**Changed:**

- `EnchRLeatherGreavesFortAcrobaticsOOO` (FormID `0020DA`) — "LOC_FN_EnchRLeatherGreavesFortAcrobaticsOOO" — `modl`: `'Armor\\Thief\\M\\Gauntlets.NIF'` → `'Armor\\Thief\\M\\Greaves.NIF'`
- `EnchRLeatherGreavesFortAgilityOOO` (FormID `0020DB`) — "LOC_FN_EnchRLeatherGreavesFortAgilityOOO" — `modl`: `'Armor\\Thief\\M\\Gauntlets.NIF'` → `'Armor\\Thief\\M\\Greaves.NIF'`
- `EnchRLeatherGreavesFortLightArmorOOO` (FormID `0020DC`) — "LOC_FN_EnchRLeatherGreavesFortLightArmorOOO" — `modl`: `'Armor\\Thief\\M\\Gauntlets.NIF'` → `'Armor\\Thief\\M\\Greaves.NIF'`
- `EnchRGlassGreavesFortAcrobaticsOOO` (FormID `0079F5`) — "LOC_FN_EnchRGlassGreavesFortAcrobaticsOOO" — `modl`: `'Armor\\Glass\\M\\Boots.NIF'` → `'Armor\\Glass\\M\\Greaves.NIF'`
- `EnchRGlassGreavesFortAgilityOOO` (FormID `0079F6`) — "LOC_FN_EnchRGlassGreavesFortAgilityOOO" — `modl`: `'Armor\\Glass\\M\\Boots.NIF'` → `'Armor\\Glass\\M\\Greaves.NIF'`
- `EnchRGlassGreavesFortFatigueOOO` (FormID `0079F7`) — "LOC_FN_EnchRGlassGreavesFortFatigueOOO" — `modl`: `'Armor\\Glass\\M\\Boots.NIF'` → `'Armor\\Glass\\M\\Greaves.NIF'`
- `EnchRGlassGreavesFortLightArmorOOO` (FormID `0079F8`) — "LOC_FN_EnchRGlassGreavesFortLightArmorOOO" — `modl`: `'Armor\\Glass\\M\\Boots.NIF'` → `'Armor\\Glass\\M\\Greaves.NIF'`
- `EnchRGlassGreavesResistFireOOO` (FormID `0079F9`) — "LOC_FN_EnchRGlassGreavesResistFireOOO" — `modl`: `'Armor\\Glass\\M\\Boots.NIF'` → `'Armor\\Glass\\M\\Greaves.NIF'`
- `EnchRGlassGreavesResistParalysisOOO` (FormID `0079FA`) — "LOC_FN_EnchRGlassGreavesResistParalysisOOO" — `modl`: `'Armor\\Glass\\M\\Boots.NIF'` → `'Armor\\Glass\\M\\Greaves.NIF'`
- `EnchRGlassGreavesSpellAbsorptionOOO` (FormID `0079FB`) — "LOC_FN_EnchRGlassGreavesSpellAbsorptionOOO" — `modl`: `'Armor\\Glass\\M\\Boots.NIF'` → `'Armor\\Glass\\M\\Greaves.NIF'`
- `UniqueRGlassGreavesMasterElementsOOO` (FormID `007A05`) — "LOC_FN_UniqueRGlassGreavesMasterElementsOOO" — `modl`: `'Armor\\Glass\\M\\Boots.NIF'` → `'Armor\\Glass\\M\\Greaves.NIF'`
- `vellaChainGreavesOOO` (FormID `0329CE`) — "LOC_FN_vellaChainGreavesOOO" — `modl`: `'Armor\\Glass\\M\\Boots.NIF'` → `'Armor\\Glass\\M\\Greaves.NIF'`

### Creature (CREA) — +0 -0 ~2

**Changed:**

- `CreatureLeopardSummon` (FormID `025BC2`) — "LOC_FN_CreatureLeopardSummon" — `full`: `"Jephre's Jungle Guardian"` → `'LOC_FN_CreatureLeopardSummon'`
- `CreatureLeopardSnowSummon` (FormID `025BC4`) — "LOC_FN_CreatureLeopardSnowSummon" — `full`: `"Jephre's White Shadow"` → `'LOC_FN_CreatureLeopardSnowSummon'`

### Spell (SPEL) — +0 -0 ~8

**Changed:**

- `ZZWolfSummonPlayer` (FormID `025165`) — "LOC_FN_ZZWolfSummonPlayer" — `full`: `"Jephre's Forest Guardian"` → `'LOC_FN_ZZWolfSummonPlayer'`
- `ZZWolfTundraSummonPlayer` (FormID `025BCD`) — "LOC_FN_ZZWolfTundraSummonPlayer" — `full`: `"Jephre's Tundra Guardian"` → `'LOC_FN_ZZWolfTundraSummonPlayer'`
- `ZZLionSummonPlayer` (FormID `025BCE`) — "LOC_FN_ZZLionSummonPlayer" — `full`: `"Jephre's Fangs"` → `'LOC_FN_ZZLionSummonPlayer'`
- `ZZLionSnowSummonPlayer` (FormID `025BD0`) — "LOC_FN_ZZLionSnowSummonPlayer" — `full`: `"Jephre's Arctic Claws"` → `'LOC_FN_ZZLionSnowSummonPlayer'`
- `ZZLeopardSnowSummonPlayer` (FormID `025BD2`) — "LOC_FN_ZZLeopardSnowSummonPlayer" — `full`: `"Jephre's White Shadow"` → `'LOC_FN_ZZLeopardSnowSummonPlayer'`
- `ZZLeopardSummonPlayer` (FormID `025BD4`) — "LOC_FN_ZZLeopardSummonPlayer" — `full`: `"Jephre's Jungle Guardian"` → `'LOC_FN_ZZLeopardSummonPlayer'`
- `ZZBoarSummonPlayer` (FormID `025BD6`) — "LOC_FN_ZZBoarSummonPlayer" — `full`: `"Jephre's Tusks"` → `'LOC_FN_ZZBoarSummonPlayer'`
- `ZZDeerSummonPlayer` (FormID `025BDB`) — "LOC_FN_ZZDeerSummonPlayer" — `full`: `"Jephre's Pride"` → `'LOC_FN_ZZDeerSummonPlayer'`

### Weapon (WEAP) — +4 -0 ~0

**Added:**

- `WeapLightOfDawnFlameTest` (FormID `00DE98`) — "LOC_FN_WeapLightOfDawnFlameTest"
- `WeapLightOfDawnFlameTestA` (FormID `00DE99`) — "LOC_FN_WeapLightOfDawnFlameTestA"
- `WeapLightOfDawnFlameTestB` (FormID `00DE9A`) — "LOC_FN_WeapLightOfDawnFlameTestB"
- `WeapLightOfDawnFlameTestC` (FormID `00DE9B`) — "LOC_FN_WeapLightOfDawnFlameTestC"

## ESP changes — `OOO_DeluxeEdition.esp`

_No record-level changes detected._

## ESP changes — `OOO_OOMC_Compatibility_Patch.esp`

_No record-level changes detected._

## ESP changes — `OOO_UnlimitedRingsReduxPatch.esp`

_No record-level changes detected._

## ESP changes — `OOO_UORP.esp`

_No record-level changes detected._

