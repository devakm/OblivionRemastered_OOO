# alpha93 — release notes

_Compared against `alpha92.1`._

## Highlights

### Fixed: same-model creatures showing the wrong creature

In OOO, many creatures share one 3D model (all imps and gargoyles use the imp
model). In the remaster, every creature in such a group showed whichever one the
game looked up last: its name, stats and loot. A gargoyle group could show up as
five Ancient Gargoyles, and an imp spawn as a gargoyle. The game placed the right
creatures; it only displayed the wrong one.

**RAX now gives each creature its own copy of the shared form**, so each one shows
its own name, stats and loot. In testing, 20–28% of these creatures showed the
wrong creature before the fix and 0 of 181 after it. The fix is on by default; to
turn it off, create
`OblivionRemastered\Binaries\Win64\ue4ss\Mods\RAX\formsplit.json` (next to RAX's
`enabled.txt`) containing `{ "enabled": false }`.

alpha93 still needs **"UE4SS new" (v3.0.1-1164)**, as alpha92 did.

### Ayleid weapons

The new Ayleid set gives the Ayleid weapons (daggers, swords, claymores, maces, axes,
war hammers and bows, 122 items) their own meshes and materials. In alpha92 they
borrowed the Elven weapons.

### Ancient Harbinger gear without Deluxe

Without the Deluxe Edition patch, the Ancient Harbinger armor and weapons now use
the Obsidian set instead of Glass armor and Iron weapons. With Deluxe they keep the
Deluxe Edition models, as before. The Harbinger greaves also use the greaves mesh
now; they showed the boots mesh before.

### Wilderness spawns rebalanced

- The six general wilderness lists (Highlands, Plains, Mountains, Hills, Forest
  Mountain and Snowy Mountains) now add creatures in steps at levels 14, 18 and 24.
- Shivering Isles water, shoreline and wilderness lists move their level steps up
  (19 to 20 or 22, 27 to 30), so the danger rises a little later.

### West Kvatch Sylvan Ranger Camp moved onto the terrain

OOO placed this camp on a flat terrain pad that the remaster's terrain does not
have, so its tents, bedrolls and clutter floated above the slope. The whole camp
(32 objects) now sits 225 units west, on the remaster's ground, with its tents and
bedrolls resting on the terrain. A large vanilla rock that sat under the camp is
moved out of it.

**Known gap for existing saves:** a save records the Tamriel worldspace the moment
the character first enters Tamriel, so any save that has left the starter dungeon
with an earlier OOORF alpha installed keeps the old camp positions, and parts of the
camp (barrels, bedrolls and other items) may still float. It does not matter
whether that save has visited the camp. Only these show all the corrections:

- a new game that has not yet left the starter dungeon, or
- a save that has never had an OOORF alpha installed. OOOR Slim makes no world
  changes, so saves that only ran Slim count as clean.

### Other changes

- **Item textures:** every item set's mips and inventory icons are regenerated from
  the edited art. This includes the alpha92.1 Draconis shield and Ancestral icon
  fixes, so alpha93 installs over alpha92 or alpha92.1.

## Summary

- **Item sets added (1):** Ayleid
- **Item sets updated (34):** Ancestral, ArcticFur, Aureus, BladesElite, BloodLeather, DaedricPrince, DarkMalachite, Draconis, Dragonborne, Drakefired, Dread, DremoraElite, DurableSteel, Eboron, ElvenEldar, ElvenNight, ElvenSky, GoldenBronze, GrayFox, ImagoStorm, LightOfDawn, LightOfDawn0, LightOfDawnA, LightOfDawnB, Noble, ShadowMail, TheBear, UnfinishedAncestral, UnfinishedSteel, UnfinishedWornSteel, WornAncestral, WornFur, WornLeather, WornSteel
- **Map assets added (1):** WestKvatchCampExterior_P
- **SyncMap:** ~137 asset remappings (+0 -0) — see below
- **ESP records:** see ESP changes section(s) below

## File-level changes

- Added: 9
- Removed: 0
- Changed: 89

### Added (9)

- `OblivionRemastered/Content/Paks/~mods/AyleidItems.pak`
- `OblivionRemastered/Content/Paks/~mods/AyleidItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/AyleidItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/AyleidMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/AyleidMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/AyleidMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/WestKvatchCampExterior_P.pak`
- `OblivionRemastered/Content/Paks/~mods/WestKvatchCampExterior_P.ucas`
- `OblivionRemastered/Content/Paks/~mods/WestKvatchCampExterior_P.utoc`

### Changed (89)

- `OblivionRemastered/Binaries/Win64/ue4ss/Mods/RAX/dlls/main.dll`
- `OblivionRemastered/Content/Dev/ObvData/Data/OptionalPatches/OOO_DeluxeEdition.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/OptionalPatches/SyncMap - DeluxeEdition/Oscuro's_Oblivion_Overhaul.ini`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`
- `OblivionRemastered/Content/Paks/~mods/AncestralMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/AncestralMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/ArcticFurMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/ArcticFurMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/AureusItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/AureusItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/AureusMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/AureusMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/BladesEliteItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/BladesEliteItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/BladesEliteMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/BladesEliteMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/BloodLeatherMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/BloodLeatherMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DaedricPrinceMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DaedricPrinceMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DarkMalachiteMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DarkMalachiteMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DraconisMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DraconisMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DragonborneItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/DragonborneItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/DragonborneMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DragonborneMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DrakefiredMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DrakefiredMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DreadMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DreadMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DremoraEliteMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DremoraEliteMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DurableSteelItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/DurableSteelItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/DurableSteelMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DurableSteelMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/EboronItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/EboronItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/EboronMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/EboronMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/ElvenEldarMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/ElvenEldarMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/ElvenNightMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/ElvenNightMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/ElvenSkyMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/ElvenSkyMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/GoldenBronzeItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/GoldenBronzeItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/GoldenBronzeMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/GoldenBronzeMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/GrayFoxMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/GrayFoxMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/ImagoStormMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/ImagoStormMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawn0Materials.ucas`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawn0Materials.utoc`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnAMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnAMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnBMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnBMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/LightOfDawnMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/NobleItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/NobleItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/NobleMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/NobleMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/ShadowMailItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/ShadowMailItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/ShadowMailMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/ShadowMailMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/TheBearMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/TheBearMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedAncestralMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedAncestralMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedSteelMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedSteelMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedWornSteelMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/UnfinishedWornSteelMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/WornAncestralMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/WornAncestralMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/WornFurMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/WornFurMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/WornLeatherMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/WornLeatherMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/WornSteelMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/WornSteelMaterials.utoc`

## SyncMap asset remappings — +0 -0 ~137

FormID → UE5 asset mappings (TesSyncMapInjector). Changed entries re-point existing FormIDs at new item-set visuals, grouped by target set.

### Changed (137)

**WeapAyleidBow** (26)

- `001F1A`: `WeapElvenBow` → `WeapAyleidBow`
- `001F1B`: `WeapElvenBow` → `WeapAyleidBow`
- `001F1C`: `WeapElvenBow` → `WeapAyleidBow`
- `001F1D`: `WeapElvenBow` → `WeapAyleidBow`
- `001F1E`: `WeapElvenBow` → `WeapAyleidBow`
- `001F1F`: `WeapElvenBow` → `WeapAyleidBow`
- `001F20`: `WeapElvenBow` → `WeapAyleidBow`
- `001F21`: `WeapElvenBow` → `WeapAyleidBow`
- `001F22`: `WeapElvenBow` → `WeapAyleidBow`
- `001F23`: `WeapElvenBow` → `WeapAyleidBow`
- `001F24`: `WeapElvenBow` → `WeapAyleidBow`
- `001F25`: `WeapElvenBow` → `WeapAyleidBow`
- `001F26`: `WeapElvenBow` → `WeapAyleidBow`
- `001F27`: `WeapElvenBow` → `WeapAyleidBow`
- `001F28`: `WeapElvenBow` → `WeapAyleidBow`
- `001F29`: `WeapElvenBow` → `WeapAyleidBow`
- `001F2A`: `WeapElvenBow` → `WeapAyleidBow`
- `001F2B`: `WeapElvenBow` → `WeapAyleidBow`
- `051374`: `WeapElvenBow` → `WeapAyleidBow`
- `051375`: `WeapElvenBow` → `WeapAyleidBow`
- `051376`: `WeapElvenBow` → `WeapAyleidBow`
- `051377`: `WeapElvenBow` → `WeapAyleidBow`
- `051378`: `WeapElvenBow` → `WeapAyleidBow`
- `051379`: `WeapElvenBow` → `WeapAyleidBow`
- `05137A`: `WeapElvenBow` → `WeapAyleidBow`
- `05137B`: `WeapElvenBow` → `WeapAyleidBow`

**WeapAyleidClaymore** (19)

- `0016CC`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `0016CD`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `0016CE`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `0016E8`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `0016EB`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `001F2E`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `001F2F`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `009A60`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `00A92B`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `00A92C`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `00A92D`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `00A92F`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `00AE2F`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `00AE31`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `051355`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `051364`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `05136B`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `051386`: `WeapElvenClaymore` → `WeapAyleidClaymore`
- `051387`: `WeapElvenClaymore` → `WeapAyleidClaymore`

**WeapAyleidBattleAxe** (16)

- `0016C7`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `0016C8`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `0016DF`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `0016E0`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `0016E2`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `009A5F`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `00A925`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `00A927`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `00A928`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `00A929`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `00A92A`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `00AE27`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `05136A`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `05136C`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `051384`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`
- `051385`: `WeapElvenBattleAxe` → `WeapAyleidBattleAxe`

**WeapAyleidDagger** (14)

- `001F2C`: `WeapElvenDagger` → `WeapAyleidDagger`
- `001F31`: `WeapElvenDagger` → `WeapAyleidDagger`
- `001F32`: `WeapElvenDagger` → `WeapAyleidDagger`
- `001F33`: `WeapElvenDagger` → `WeapAyleidDagger`
- `001F34`: `WeapElvenDagger` → `WeapAyleidDagger`
- `051361`: `WeapElvenDagger` → `WeapAyleidDagger`
- `051373`: `WeapElvenDagger` → `WeapAyleidDagger`
- `05137C`: `WeapElvenDagger` → `WeapAyleidDagger`
- `05137D`: `WeapElvenDagger` → `WeapAyleidDagger`
- `05137E`: `WeapElvenDagger` → `WeapAyleidDagger`
- `05137F`: `WeapElvenDagger` → `WeapAyleidDagger`
- `051380`: `WeapElvenDagger` → `WeapAyleidDagger`
- `051381`: `WeapElvenDagger` → `WeapAyleidDagger`
- `051388`: `WeapElvenDagger` → `WeapAyleidDagger`

**WeapAyleidLongSword** (11)

- `001F2D`: `WeapElvenLongSword` → `WeapAyleidLongSword`
- `0025D8`: `WeapElvenLongSword` → `WeapAyleidLongSword`
- `008BA6`: `WeapElvenLongSword` → `WeapAyleidLongSword`
- `051363`: `WeapElvenLongSword` → `WeapAyleidLongSword`
- `05136E`: `WeapElvenLongSword` → `WeapAyleidLongSword`
- `05136F`: `WeapElvenLongSword` → `WeapAyleidLongSword`
- `051370`: `WeapElvenLongSword` → `WeapAyleidLongSword`
- `051371`: `WeapElvenLongSword` → `WeapAyleidLongSword`
- `051372`: `WeapElvenLongSword` → `WeapAyleidLongSword`
- `051382`: `WeapElvenLongSword` → `WeapAyleidLongSword`
- `051383`: `WeapElvenLongSword` → `WeapAyleidLongSword`

**WeapAyleidMace** (10)

- `0016CF`: `WeapElvenMace` → `WeapAyleidMace`
- `0016D0`: `WeapElvenMace` → `WeapAyleidMace`
- `0016D1`: `WeapElvenMace` → `WeapAyleidMace`
- `0025D7`: `WeapElvenMace` → `WeapAyleidMace`
- `008BA7`: `WeapElvenMace` → `WeapAyleidMace`
- `05135C`: `WeapElvenMace` → `WeapAyleidMace`
- `05135E`: `WeapElvenMace` → `WeapAyleidMace`
- `05135F`: `WeapElvenMace` → `WeapAyleidMace`
- `051360`: `WeapElvenMace` → `WeapAyleidMace`
- `051369`: `WeapElvenMace` → `WeapAyleidMace`

**WeapAyleidShortsword** (9)

- `001F30`: `WeapElvenShortsword` → `WeapAyleidShortsword`
- `051352`: `WeapElvenShortsword` → `WeapAyleidShortsword`
- `051353`: `WeapElvenShortsword` → `WeapAyleidShortsword`
- `051354`: `WeapElvenShortsword` → `WeapAyleidShortsword`
- `051362`: `WeapElvenShortsword` → `WeapAyleidShortsword`
- `051389`: `WeapElvenShortsword` → `WeapAyleidShortsword`
- `05138A`: `WeapElvenShortsword` → `WeapAyleidShortsword`
- `05138B`: `WeapElvenShortsword` → `WeapAyleidShortsword`
- `05138C`: `WeapElvenShortsword` → `WeapAyleidShortsword`

**WeapAyleidWarHammer** (9)

- `0025CF`: `WeapElvenWarHammer` → `WeapAyleidWarHammer`
- `0025D1`: `WeapElvenWarHammer` → `WeapAyleidWarHammer`
- `0025D2`: `WeapElvenWarHammer` → `WeapAyleidWarHammer`
- `0025D3`: `WeapElvenWarHammer` → `WeapAyleidWarHammer`
- `0025D4`: `WeapElvenWarHammer` → `WeapAyleidWarHammer`
- `0025D5`: `WeapElvenWarHammer` → `WeapAyleidWarHammer`
- `0025D6`: `WeapElvenWarHammer` → `WeapAyleidWarHammer`
- `051356`: `WeapElvenWarHammer` → `WeapAyleidWarHammer`
- `05136D`: `WeapElvenWarHammer` → `WeapAyleidWarHammer`

**WeapAyleidWarAxe** (8)

- `002AC3`: `WeapElvenWarAxe` → `WeapAyleidWarAxe`
- `051357`: `WeapElvenWarAxe` → `WeapAyleidWarAxe`
- `051358`: `WeapElvenWarAxe` → `WeapAyleidWarAxe`
- `051359`: `WeapElvenWarAxe` → `WeapAyleidWarAxe`
- `05135A`: `WeapElvenWarAxe` → `WeapAyleidWarAxe`
- `05135B`: `WeapElvenWarAxe` → `WeapAyleidWarAxe`
- `05135D`: `WeapElvenWarAxe` → `WeapAyleidWarAxe`
- `051365`: `WeapElvenWarAxe` → `WeapAyleidWarAxe`

**Obsidian** (6)

- `00DE56`: `GlassBoots` → `ObsidianBoots`
- `00DE57`: `GlassCuirass` → `ObsidianCuirass`
- `00DE58`: `GlassGauntlets` → `ObsidianGauntlets`
- `00DE59`: `GlassGreaves` → `ObsidianGreaves`
- `00DE5A`: `GlassHelmet` → `ObsidianHelmet`
- `00DE5B`: `GlassShield` → `ObsidianShield`

**WeapObsidianBattleAxe** (1)

- `00DE6D`: `WeapIronBattleAxe` → `WeapObsidianBattleAxe`

**WeapObsidianBow** (1)

- `00DE6F`: `WeapIronBow` → `WeapObsidianBow`

**WeapObsidianClaymore** (1)

- `00DE6A`: `WeapIronClaymore` → `WeapObsidianClaymore`

**WeapObsidianDagger** (1)

- `00DE68`: `WeapIronDagger` → `WeapObsidianDagger`

**WeapObsidianLongsword** (1)

- `00DE69`: `WeapIronLongsword` → `WeapObsidianLongsword`

**WeapObsidianMace** (1)

- `00DE6B`: `WeapIronMace` → `WeapObsidianMace`

**WeapObsidianShortsword** (1)

- `00DE67`: `WeapIronShortsword` → `WeapObsidianShortsword`

**WeapObsidianWarAxe** (1)

- `00DE6C`: `WeapIronWarAxe` → `WeapObsidianWarAxe`

**WeapObsidianWarhammer** (1)

- `00DE6E`: `WeapIronWarhammer` → `WeapObsidianWarhammer`

## Map cell changes since `alpha92.1`

Each OOO cell layers TES4-injected OOO content over UE5-baked remaster geometry; these reconcile the two so each object renders from exactly one layer. Sourced from MapClone configs (baseline `1b0b4080b23a`).

- **TES4 REFR suppression** — disable OOO REFRs that *duplicate* UE5-baked architecture (drop the TES4 twin, keep the UE5 copy).
- **UE5-layer ghost suppression (static)** — remove UE5-baked actors with *no* TES4 counterpart (drop the UE5 ghost, keep TES4). Applied at build time by MapClone's static patcher and baked into the map paks; the Begone UE4SS mod no longer suppresses anything at runtime.
- **Position overrides** — re-seat OOO REFRs (chests/furniture) left floating once a supporting STAT was disabled.

### Exterior foliage fixes

- **WestKvatchCamp** *(new)*

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Armor (ARMO) — +0 -0 ~1

**Changed:**

- `UniqueHarbingerGreavesOOO` (FormID `00DE59`) — "LOC_FN_UniqueHarbingerGreavesOOO" — `modl`: `'Armor\\Glass\\M\\Boots.NIF'` → `'Armor\\Glass\\M\\Greaves.NIF'`

### Leveled Creature List (LVLC) — +0 -0 ~14

**Changed:**

- `LL1WildernessHighlands` (FormID `0343DB`) — + entry: level 14 × 1 → `0343C9`; + entry: level 14 × 1 → `007FCE`; + entry: level 14 × 1 → `009474`; + entry: level 14 × 1 → `02F502`; + entry: level 14 × 1 → `0417EE`; + entry: level 18 × 1 → `007FCE`; + entry: level 18 × 1 → `009474`; + entry: level 18 × 1 → `02F502`; + entry: level 18 × 1 → `0417EE`; + entry: level 24 × 1 → `0343C9`; + entry: level 24 × 1 → `007FC2`; + entry: level 24 × 1 → `007FCE`; + entry: level 24 × 1 → `008F69`; + entry: level 24 × 1 → `009474`; + entry: level 24 × 1 → `0099A3`; + entry: level 24 × 1 → `00DE1C`; + entry: level 24 × 1 → `0102F8`; + entry: level 24 × 1 → `014312`; + entry: level 24 × 1 → `016F8D`; + entry: level 24 × 1 → `02797C`; + entry: level 24 × 1 → `02F502`; + entry: level 24 × 1 → `0417EE`; - entry: level 12 × 1 → `0417EE`; - entry: level 13 × 1 → `02F502`; - entry: level 15 × 1 → `007FCE`; - entry: level 16 × 1 → `0343C9`; - entry: level 16 × 1 → `009474`
- `LL1WildernessPlains` (FormID `0343DC`) — + entry: level 14 × 1 → `0343C9`; + entry: level 14 × 1 → `007FC2`; + entry: level 14 × 1 → `007FC6`; + entry: level 14 × 1 → `007FCE`; + entry: level 14 × 1 → `008F64`; + entry: level 14 × 1 → `009474`; + entry: level 14 × 1 → `02F502`; + entry: level 14 × 1 → `0417EE`; + entry: level 18 × 1 → `007FC6`; + entry: level 18 × 1 → `007FCE`; + entry: level 18 × 1 → `008F64`; + entry: level 18 × 1 → `009474`; + entry: level 18 × 1 → `02F502`; + entry: level 18 × 1 → `0417EE`; + entry: level 24 × 1 → `0343C9`; + entry: level 24 × 1 → `007FC2`; + entry: level 24 × 1 → `007FC6`; + entry: level 24 × 1 → `007FCE`; + entry: level 24 × 1 → `008F64`; + entry: level 24 × 1 → `009474`; + entry: level 24 × 1 → `00DE1C`; + entry: level 24 × 1 → `02F502`; + entry: level 24 × 1 → `0417EE`; - entry: level 12 × 1 → `0417EE`; - entry: level 13 × 1 → `02F502`
- `LL1WildernessMountains` (FormID `0343DF`) — + entry: level 14 × 1 → `0343C9`; + entry: level 14 × 1 → `008F61`; + entry: level 14 × 1 → `009474`; + entry: level 14 × 1 → `027979`; + entry: level 14 × 1 → `02797B`; + entry: level 14 × 1 → `02F502`; + entry: level 14 × 1 → `0417EE`; + entry: level 18 × 1 → `007FCE`; + entry: level 18 × 1 → `008F61`; + entry: level 18 × 1 → `009474`; + entry: level 18 × 1 → `027979`; + entry: level 18 × 1 → `02797B`; + entry: level 18 × 1 → `02F502`; + entry: level 18 × 1 → `0417EE`; + entry: level 24 × 1 → `0343C9`; + entry: level 24 × 1 → `007FC2`; + entry: level 24 × 1 → `007FCE`; + entry: level 24 × 1 → `008F61`; + entry: level 24 × 1 → `008F69`; + entry: level 24 × 1 → `009474`; + entry: level 24 × 1 → `0099A8`; + entry: level 24 × 1 → `00DE1C`; + entry: level 24 × 1 → `0102F7`; + entry: level 24 × 1 → `0102F8`; + entry: level 24 × 1 → `016F8D`; + entry: level 24 × 1 → `023E8A`; + entry: level 24 × 1 → `027979`; + entry: level 24 × 1 → `02797B`; + entry: level 24 × 1 → `02797C`; + entry: level 24 × 1 → `02797D`; + entry: level 24 × 1 → `02F502`; + entry: level 24 × 1 → `0417EE`; - entry: level 12 × 1 → `009474`; - entry: level 12 × 1 → `0417EE`; - entry: level 13 × 1 → `02797B`; - entry: level 13 × 1 → `02F502`; - entry: level 15 × 1 → `0343C9`
- `LL1WildernessHills` (FormID `0343E0`) — + entry: level 14 × 1 → `02797B`; + entry: level 14 × 1 → `02F502`; + entry: level 14 × 1 → `0417EE`; + entry: level 18 × 1 → `0343C9`; + entry: level 18 × 1 → `03F14D`; + entry: level 18 × 1 → `007FCE`; + entry: level 18 × 1 → `02797B`; + entry: level 18 × 1 → `02F502`; + entry: level 18 × 1 → `0417EE`; + entry: level 24 × 1 → `0343C9`; + entry: level 24 × 1 → `03F14D`; + entry: level 24 × 1 → `007FC2`; + entry: level 24 × 1 → `007FCE`; + entry: level 24 × 1 → `008F69`; + entry: level 24 × 1 → `0099A5`; + entry: level 24 × 1 → `0099A7`; + entry: level 24 × 1 → `0099A9`; + entry: level 24 × 1 → `00DE1C`; + entry: level 24 × 1 → `02797B`; + entry: level 24 × 1 → `02797C`; + entry: level 24 × 1 → `02F502`; + entry: level 24 × 1 → `0417EE`
- `LL1WildernessForestMountain` (FormID `0343E2`) — + entry: level 14 × 1 → `0343C9`; + entry: level 14 × 1 → `008F61`; + entry: level 14 × 1 → `0102F7`; + entry: level 14 × 1 → `023E8A`; + entry: level 14 × 1 → `027979`; + entry: level 14 × 1 → `02F502`; + entry: level 14 × 1 → `0417EE`; + entry: level 18 × 1 → `008F61`; + entry: level 18 × 1 → `023E8A`; + entry: level 18 × 1 → `027979`; + entry: level 24 × 1 → `0343C9`; + entry: level 24 × 1 → `03F14D`; + entry: level 24 × 1 → `007FC2`; + entry: level 24 × 1 → `007FCE`; + entry: level 24 × 1 → `008F5C`; + entry: level 24 × 1 → `008F61`; + entry: level 24 × 1 → `0099A5`; + entry: level 24 × 1 → `0099A6`; + entry: level 24 × 1 → `00DE1C`; + entry: level 24 × 1 → `0102F7`; + entry: level 24 × 1 → `01430C`; + entry: level 24 × 1 → `014312`; + entry: level 24 × 1 → `023E8A`; + entry: level 24 × 1 → `023E8B`; + entry: level 24 × 1 → `027979`; + entry: level 24 × 1 → `02797B`; + entry: level 24 × 1 → `02F502`; + entry: level 24 × 1 → `0417EE`; - entry: level 15 × 1 → `0102F7`; - entry: level 16 × 1 → `0343C9`; - entry: level 16 × 1 → `008F61`; - entry: level 16 × 1 → `023E8A`; - entry: level 16 × 1 → `027979`
- `LL1WildernessMountainsSnow` (FormID `064F66`) — + entry: level 14 × 1 → `0017DD`; + entry: level 14 × 1 → `004237`; + entry: level 14 × 1 → `004238`; + entry: level 14 × 1 → `027979`; + entry: level 14 × 1 → `02F502`; + entry: level 14 × 1 → `0417EE`; + entry: level 18 × 1 → `0017DD`; + entry: level 18 × 1 → `004231`; + entry: level 18 × 1 → `004237`; + entry: level 18 × 1 → `004238`; + entry: level 18 × 1 → `027979`; + entry: level 18 × 1 → `02F502`; + entry: level 18 × 1 → `0417EE`; + entry: level 24 × 1 → `0343C9`; + entry: level 24 × 1 → `0017DC`; + entry: level 24 × 1 → `0017DD`; + entry: level 24 × 1 → `0017E1`; + entry: level 24 × 1 → `0017E2`; + entry: level 24 × 1 → `004231`; + entry: level 24 × 1 → `004236`; + entry: level 24 × 1 → `004237`; + entry: level 24 × 1 → `004238`; + entry: level 24 × 1 → `00423A`; + entry: level 24 × 1 → `007FC2`; + entry: level 24 × 1 → `0098C5`; + entry: level 24 × 1 → `00DE1C`; + entry: level 24 × 1 → `027979`; + entry: level 24 × 1 → `02797B`; + entry: level 24 × 1 → `02F502`; + entry: level 24 × 1 → `0417EE`; - entry: level 15 × 1 → `027979`
- `OOOSELL2WaterMania100Pack` (FormID `005AAE`) — + entry: level 22 × 1 → `011B7A`; + entry: level 30 × 1 → `011B7B`; - entry: level 19 × 1 → `011B7A`; - entry: level 27 × 1 → `011B7B`
- `OOOSELL2WaterDementia100Pack` (FormID `005AB0`) — + entry: level 22 × 1 → `011B7F`; + entry: level 30 × 1 → `011B80`; - entry: level 19 × 1 → `011B7F`; - entry: level 27 × 1 → `011B80`
- `OOOSELL2ShorelineDementia100Special` (FormID `005AB3`) — + entry: level 20 × 1 → `012010`; + entry: level 20 × 1 → `012018`; - entry: level 19 × 1 → `012010`; - entry: level 19 × 1 → `012018`
- `OOOSELL2ShorelineMania100Special` (FormID `005AB4`) — + entry: level 20 × 1 → `012006`; + entry: level 20 × 1 → `012018`; - entry: level 19 × 1 → `012006`; - entry: level 19 × 1 → `012018`
- `OOOSELL2WildernessMania100Special` (FormID `005AB9`) — + entry: level 20 × 1 → `012006`; + entry: level 20 × 1 → `012009`; + entry: level 20 × 1 → `012018`; - entry: level 19 × 1 → `012006`; - entry: level 19 × 1 → `012009`; - entry: level 19 × 1 → `012018`
- `OOOSELL2WildernessDementia100Special` (FormID `005ABA`) — + entry: level 20 × 1 → `012009`; + entry: level 20 × 1 → `012010`; + entry: level 20 × 1 → `012018`; - entry: level 19 × 1 → `012009`; - entry: level 19 × 1 → `012010`; - entry: level 19 × 1 → `012018`
- `OOOSELL2NaturalDementia100Special` (FormID `016192`) — + entry: level 20 × 1 → `012010`; - entry: level 19 × 1 → `012010`
- `OOOSELL2NaturalMania100Special` (FormID `016193`) — + entry: level 20 × 1 → `012006`; - entry: level 19 × 1 → `012006`

## ESP changes — `OOO_DeluxeEdition.esp`

### Armor (ARMO) — +6 -0 ~0

**Added:**

- `UniqueHarbingerBootsOOO` (FormID `00DE56`) — "LOC_FN_UniqueHarbingerBootsOOO"
- `UniqueHarbingerCuirassOOO` (FormID `00DE57`) — "LOC_FN_UniqueHarbingerCuirassOOO"
- `UniqueHarbingerGauntletsOOO` (FormID `00DE58`) — "LOC_FN_UniqueHarbingerGauntletsOOO"
- `UniqueHarbingerGreavesOOO` (FormID `00DE59`) — "LOC_FN_UniqueHarbingerGreavesOOO"
- `UniqueHarbingerHelmetOOO` (FormID `00DE5A`) — "LOC_FN_UniqueHarbingerHelmetOOO"
- `UniqueHarbingerShieldOOO` (FormID `00DE5B`) — "LOC_FN_UniqueHarbingerShieldOOO"

## ESP changes — `OOO_OOMC_Compatibility_Patch.esp`

_No record-level changes detected._

## ESP changes — `OOO_UnlimitedRingsReduxPatch.esp`

_No record-level changes detected._

## ESP changes — `OOO_UORP.esp`

_No record-level changes detected._

