# alpha91 — release notes

_Compared against `alpha90`._

## Summary

- **Item sets added (14):** ArcticFur, Aureus, BloodLeather, BlueGlass, Drakefired, Eboron, ElvenEldar, ElvenNight, ElvenSky, GoldenBronze, GrayFox, ShadowMail, WornFur, WornLeather
- **Item sets removed (2):** BGlass, RGlass
- **Dungeon map paks rebuilt (7 paks / 14 zones):** L_BloodClotCave_Map, L_BrokenToothCaveXX_Map, L_DeepCoverCav_Map, L_GraveGroundCaveXX_Map, L_LipsTarn03_Map, L_RosulasXX_Map, L_ThunderingSte_Map
- **Map assets added (1):** GraveGroundExterior_P
- **SyncMap:** ~307 asset remappings (+0 -0) — see below
- **MagicLoader `Oscuro's_Oblivion_Overhaul_ARMO.json`:** +0 -0 ~6 display names
- **UE5-layer suppression:** +254 disabled REFRs, +17 position overrides — see Map cell changes
- **Ghost suppression (Begone):** net +92 entries
- **ESP records:** see ESP changes section(s) below

## File-level changes

- Added: 87
- Removed: 13
- Changed: 18

### Added (87)

- `OblivionRemastered/Content/Paks/~mods/ArcticFurItems.pak`
- `OblivionRemastered/Content/Paks/~mods/ArcticFurItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/ArcticFurItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/ArcticFurMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/ArcticFurMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/ArcticFurMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/AureusItems.pak`
- `OblivionRemastered/Content/Paks/~mods/AureusItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/AureusItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/AureusMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/AureusMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/AureusMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/BloodLeatherItems.pak`
- `OblivionRemastered/Content/Paks/~mods/BloodLeatherItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/BloodLeatherItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/BloodLeatherMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/BloodLeatherMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/BloodLeatherMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/BlueGlassItems.pak`
- `OblivionRemastered/Content/Paks/~mods/BlueGlassItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/BlueGlassItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/BlueGlassMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/BlueGlassMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/BlueGlassMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/DrakefiredItems.pak`
- `OblivionRemastered/Content/Paks/~mods/DrakefiredItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/DrakefiredItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/DrakefiredMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/DrakefiredMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/DrakefiredMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/EboronItems.pak`
- `OblivionRemastered/Content/Paks/~mods/EboronItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/EboronItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/EboronMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/EboronMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/EboronMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/ElvenEldarItems.pak`
- `OblivionRemastered/Content/Paks/~mods/ElvenEldarItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/ElvenEldarItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/ElvenEldarMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/ElvenEldarMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/ElvenEldarMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/ElvenNightItems.pak`
- `OblivionRemastered/Content/Paks/~mods/ElvenNightItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/ElvenNightItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/ElvenNightMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/ElvenNightMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/ElvenNightMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/ElvenSkyItems.pak`
- `OblivionRemastered/Content/Paks/~mods/ElvenSkyItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/ElvenSkyItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/ElvenSkyMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/ElvenSkyMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/ElvenSkyMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/GoldenBronzeItems.pak`
- `OblivionRemastered/Content/Paks/~mods/GoldenBronzeItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/GoldenBronzeItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/GoldenBronzeMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/GoldenBronzeMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/GoldenBronzeMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/GraveGroundExterior_P.pak`
- `OblivionRemastered/Content/Paks/~mods/GraveGroundExterior_P.ucas`
- `OblivionRemastered/Content/Paks/~mods/GraveGroundExterior_P.utoc`
- `OblivionRemastered/Content/Paks/~mods/GrayFoxItems.pak`
- `OblivionRemastered/Content/Paks/~mods/GrayFoxItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/GrayFoxItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/GrayFoxMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/GrayFoxMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/GrayFoxMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/ShadowMailItems.pak`
- `OblivionRemastered/Content/Paks/~mods/ShadowMailItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/ShadowMailItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/ShadowMailMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/ShadowMailMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/ShadowMailMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/WornFurItems.pak`
- `OblivionRemastered/Content/Paks/~mods/WornFurItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/WornFurItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/WornFurMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/WornFurMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/WornFurMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/WornLeatherItems.pak`
- `OblivionRemastered/Content/Paks/~mods/WornLeatherItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/WornLeatherItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/WornLeatherMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/WornLeatherMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/WornLeatherMaterials.utoc`

### Removed (13)

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CELLMAP.working`
- `OblivionRemastered/Content/Paks/~mods/BGlassItems.pak`
- `OblivionRemastered/Content/Paks/~mods/BGlassItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/BGlassItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/BGlassMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/BGlassMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/BGlassMaterials.utoc`
- `OblivionRemastered/Content/Paks/~mods/RGlassItems.pak`
- `OblivionRemastered/Content/Paks/~mods/RGlassItems.ucas`
- `OblivionRemastered/Content/Paks/~mods/RGlassItems.utoc`
- `OblivionRemastered/Content/Paks/~mods/RGlassMaterials.pak`
- `OblivionRemastered/Content/Paks/~mods/RGlassMaterials.ucas`
- `OblivionRemastered/Content/Paks/~mods/RGlassMaterials.utoc`

### Changed (18)

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ARMO.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/OptionalPatches/SyncMap - DeluxeEdition/Oscuro's_Oblivion_Overhaul.ini`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`
- `OblivionRemastered/Content/Paks/~mods/L_BloodClotCave_Map.ucas`
- `OblivionRemastered/Content/Paks/~mods/L_BloodClotCave_Map.utoc`
- `OblivionRemastered/Content/Paks/~mods/L_BrokenToothCaveXX_Map.ucas`
- `OblivionRemastered/Content/Paks/~mods/L_BrokenToothCaveXX_Map.utoc`
- `OblivionRemastered/Content/Paks/~mods/L_DeepCoverCav_Map.ucas`
- `OblivionRemastered/Content/Paks/~mods/L_DeepCoverCav_Map.utoc`
- `OblivionRemastered/Content/Paks/~mods/L_GraveGroundCaveXX_Map.ucas`
- `OblivionRemastered/Content/Paks/~mods/L_GraveGroundCaveXX_Map.utoc`
- `OblivionRemastered/Content/Paks/~mods/L_LipsTarn03_Map.ucas`
- `OblivionRemastered/Content/Paks/~mods/L_LipsTarn03_Map.utoc`
- `OblivionRemastered/Content/Paks/~mods/L_RosulasXX_Map.ucas`
- `OblivionRemastered/Content/Paks/~mods/L_RosulasXX_Map.utoc`
- `OblivionRemastered/Content/Paks/~mods/L_ThunderingSte_Map.ucas`
- `OblivionRemastered/Content/Paks/~mods/L_ThunderingSte_Map.utoc`

## SyncMap asset remappings — +0 -0 ~307

FormID → UE5 asset mappings (TesSyncMapInjector). Changed entries re-point existing FormIDs at new item-set visuals, grouped by target set.

### Changed (307)

**GoldenBronze** (42)

- `0056F2`: `MithrilBoots` → `GoldenBronzeBoots`
- `0056F3`: `MithrilCuirass` → `GoldenBronzeCuirass`
- `0056F4`: `MithrilGauntlets` → `GoldenBronzeGauntlets`
- `0056F5`: `MithrilGreaves` → `GoldenBronzeGreaves`
- `0056F6`: `MithrilHelmet` → `GoldenBronzeHelmet`
- `0056F7`: `MithrilShield` → `GoldenBronzeShield`
- `006AAD`: `MithrilBoots` → `GoldenBronzeBoots`
- `006AAE`: `MithrilCuirass` → `GoldenBronzeCuirass`
- `006AAF`: `MithrilCuirass` → `GoldenBronzeCuirass`
- `006AB0`: `MithrilCuirass` → `GoldenBronzeCuirass`
- `006AB1`: `MithrilCuirass` → `GoldenBronzeCuirass`
- `006AB2`: `MithrilGauntlets` → `GoldenBronzeGauntlets`
- `006AB3`: `MithrilGauntlets` → `GoldenBronzeGauntlets`
- `006AB4`: `MithrilGauntlets` → `GoldenBronzeGauntlets`
- `006AB5`: `MithrilGauntlets` → `GoldenBronzeGauntlets`
- `006AB6`: `MithrilGauntlets` → `GoldenBronzeGauntlets`
- `006AB7`: `MithrilGreaves` → `GoldenBronzeGreaves`
- `006AB8`: `MithrilGreaves` → `GoldenBronzeGreaves`
- `006AB9`: `MithrilGreaves` → `GoldenBronzeGreaves`
- `006ABA`: `MithrilGreaves` → `GoldenBronzeGreaves`
- `006ABB`: `MithrilGreaves` → `GoldenBronzeGreaves`
- `006ABC`: `MithrilGreaves` → `GoldenBronzeGreaves`
- `006ABD`: `MithrilGreaves` → `GoldenBronzeGreaves`
- `006ABF`: `MithrilGreaves` → `GoldenBronzeGreaves`
- `006AC1`: `MithrilHelmet` → `GoldenBronzeHelmet`
- `006AC2`: `MithrilHelmet` → `GoldenBronzeHelmet`
- `006AC4`: `MithrilHelmet` → `GoldenBronzeHelmet`
- `006AC6`: `MithrilHelmet` → `GoldenBronzeHelmet`
- `006AC7`: `MithrilHelmet` → `GoldenBronzeHelmet`
- `006AC8`: `MithrilShield` → `GoldenBronzeShield`
- `006AC9`: `MithrilShield` → `GoldenBronzeShield`
- `006ACA`: `MithrilShield` → `GoldenBronzeShield`
- `006ACB`: `MithrilShield` → `GoldenBronzeShield`
- `006ACC`: `MithrilShield` → `GoldenBronzeShield`
- `006ACD`: `MithrilShield` → `GoldenBronzeShield`
- `006ACF`: `MithrilCuirass` → `GoldenBronzeCuirass`
- `0429DC`: `MithrilBoots` → `GoldenBronzeBoots`
- `0429DD`: `MithrilCuirass` → `GoldenBronzeCuirass`
- `0429DE`: `MithrilGauntlets` → `GoldenBronzeGauntlets`
- `0429DF`: `MithrilGreaves` → `GoldenBronzeGreaves`
- `0429E0`: `MithrilHelmet` → `GoldenBronzeHelmet`
- `0429E1`: `MithrilShield` → `GoldenBronzeShield`

**ElvenSky** (35)

- `001BE4`: `ElvenBoots` → `ElvenSkyBoots`
- `0020CB`: `ElvenCuirass` → `ElvenSkyCuirass`
- `0020CC`: `ElvenGauntlets` → `ElvenSkyGauntlets`
- `0025B3`: `ElvenGreaves` → `ElvenSkyGreaves`
- `0025B4`: `ElvenHelmet` → `ElvenSkyHelmet`
- `0025B5`: `ElvenShield` → `ElvenSkyShield`
- `006AD1`: `ElvenBoots` → `ElvenSkyBoots`
- `006AD3`: `ElvenBoots` → `ElvenSkyBoots`
- `006AD4`: `ElvenBoots` → `ElvenSkyBoots`
- `006FBB`: `ElvenBoots` → `ElvenSkyBoots`
- `006FBC`: `ElvenBoots` → `ElvenSkyBoots`
- `006FBD`: `ElvenCuirass` → `ElvenSkyCuirass`
- `006FBE`: `ElvenCuirass` → `ElvenSkyCuirass`
- `006FBF`: `ElvenCuirass` → `ElvenSkyCuirass`
- `006FC0`: `ElvenCuirass` → `ElvenSkyCuirass`
- `006FC1`: `ElvenCuirass` → `ElvenSkyCuirass`
- `006FC2`: `ElvenGauntlets` → `ElvenSkyGauntlets`
- `006FC3`: `ElvenGauntlets` → `ElvenSkyGauntlets`
- `006FC4`: `ElvenGauntlets` → `ElvenSkyGauntlets`
- `006FC5`: `ElvenGreaves` → `ElvenSkyGreaves`
- `006FC6`: `ElvenGreaves` → `ElvenSkyGreaves`
- `006FC7`: `ElvenGreaves` → `ElvenSkyGreaves`
- `006FC8`: `ElvenGreaves` → `ElvenSkyGreaves`
- `006FC9`: `ElvenGreaves` → `ElvenSkyGreaves`
- `006FCA`: `ElvenGreaves` → `ElvenSkyGreaves`
- `006FCB`: `ElvenGreaves` → `ElvenSkyGreaves`
- `006FCC`: `ElvenHelmet` → `ElvenSkyHelmet`
- `006FCD`: `ElvenHelmet` → `ElvenSkyHelmet`
- `006FCE`: `ElvenShield` → `ElvenSkyShield`
- `006FCF`: `ElvenShield` → `ElvenSkyShield`
- `006FD0`: `ElvenShield` → `ElvenSkyShield`
- `006FD1`: `ElvenShield` → `ElvenSkyShield`
- `006FD2`: `ElvenShield` → `ElvenSkyShield`
- `006FD3`: `ElvenShield` → `ElvenSkyShield`
- `006FD5`: `ElvenHelmet` → `ElvenSkyHelmet`

**BlueGlass** (34)

- `00125A`: `BGlassGreaves` → `BlueGlassGreaves`
- `0065AA`: `BGlassBoots` → `BlueGlassBoots`
- `0065AB`: `BGlassBoots` → `BlueGlassBoots`
- `0065AC`: `BGlassBoots` → `BlueGlassBoots`
- `0065AD`: `BGlassBoots` → `BlueGlassBoots`
- `0065AE`: `BGlassBoots` → `BlueGlassBoots`
- `0065AF`: `BGlassCuirass` → `BlueGlassCuirass`
- `0065B0`: `BGlassCuirass` → `BlueGlassCuirass`
- `0065B1`: `BGlassCuirass` → `BlueGlassCuirass`
- `0065B2`: `BGlassCuirass` → `BlueGlassCuirass`
- `0065B3`: `BGlassCuirass` → `BlueGlassCuirass`
- `0065B4`: `BGlassGauntlets` → `BlueGlassGauntlets`
- `0065B5`: `BGlassGauntlets` → `BlueGlassGauntlets`
- `0065B6`: `BGlassGauntlets` → `BlueGlassGauntlets`
- `0065B7`: `BGlassGreaves` → `BlueGlassGreaves`
- `0065B9`: `BGlassGreaves` → `BlueGlassGreaves`
- `0065BA`: `BGlassGreaves` → `BlueGlassGreaves`
- `0065BB`: `BGlassGreaves` → `BlueGlassGreaves`
- `0065BC`: `BGlassGreaves` → `BlueGlassGreaves`
- `0065BD`: `BGlassGreaves` → `BlueGlassGreaves`
- `0065BE`: `BGlassHelmet` → `BlueGlassHelmet`
- `0065BF`: `BGlassHelmet` → `BlueGlassHelmet`
- `0065C0`: `BGlassShield` → `BlueGlassShield`
- `0065C1`: `BGlassShield` → `BlueGlassShield`
- `0065C2`: `BGlassShield` → `BlueGlassShield`
- `0065C3`: `BGlassShield` → `BlueGlassShield`
- `0065C4`: `BGlassShield` → `BlueGlassShield`
- `0065C6`: `BGlassHelmet` → `BlueGlassHelmet`
- `048F2F`: `BGlassBoots` → `BlueGlassBoots`
- `048F30`: `BGlassCuirass` → `BlueGlassCuirass`
- `048F31`: `BGlassGauntlets` → `BlueGlassGauntlets`
- `048F32`: `BGlassGreaves` → `BlueGlassGreaves`
- `048F33`: `BGlassHelmet` → `BlueGlassHelmet`
- `048F34`: `BGlassShield` → `BlueGlassShield`

**Eboron** (34)

- `001BC3`: `MithrilBoots` → `EboronBoots`
- `001BC4`: `MithrilBoots` → `EboronBoots`
- `001BC5`: `MithrilBoots` → `EboronBoots`
- `001BC6`: `MithrilBoots` → `EboronBoots`
- `001BC7`: `MithrilCuirass` → `EboronCuirass`
- `001BC8`: `MithrilCuirass` → `EboronCuirass`
- `001BC9`: `MithrilCuirass` → `EboronCuirass`
- `001BCA`: `MithrilCuirass` → `EboronCuirass`
- `001BCB`: `MithrilGauntlets` → `EboronGauntlets`
- `001BCC`: `MithrilGauntlets` → `EboronGauntlets`
- `001BCD`: `MithrilGauntlets` → `EboronGauntlets`
- `001BCE`: `MithrilGauntlets` → `EboronGauntlets`
- `001BCF`: `MithrilGauntlets` → `EboronGauntlets`
- `001BD0`: `MithrilGreaves` → `EboronGreaves`
- `001BD1`: `MithrilGreaves` → `EboronGreaves`
- `001BD2`: `MithrilGreaves` → `EboronGreaves`
- `001BD3`: `MithrilGreaves` → `EboronGreaves`
- `001BD4`: `MithrilHelmet` → `EboronHelmet`
- `001BD5`: `MithrilHelmet` → `EboronHelmet`
- `001BD6`: `MithrilHelmet` → `EboronHelmet`
- `001BD7`: `MithrilHelmet` → `EboronHelmet`
- `001BD8`: `MithrilShield` → `EboronShield`
- `001BD9`: `MithrilShield` → `EboronShield`
- `001BDA`: `MithrilShield` → `EboronShield`
- `001BDB`: `MithrilShield` → `EboronShield`
- `001BDC`: `MithrilShield` → `EboronShield`
- `001BDD`: `MithrilShield` → `EboronShield`
- `001BDF`: `MithrilShield` → `EboronShield`
- `006A95`: `MithrilBoots` → `EboronBoots`
- `006A96`: `MithrilCuirass` → `EboronCuirass`
- `006A97`: `MithrilGauntlets` → `EboronGauntlets`
- `006A98`: `MithrilGreaves` → `EboronGreaves`
- `006A99`: `MithrilHelmet` → `EboronHelmet`
- `006A9A`: `MithrilShield` → `EboronShield`

**Drakefired** (33)

- `0056EC`: `RGlassBoots` → `DrakefiredBoots`
- `0056ED`: `RGlassCuirass` → `DrakefiredCuirass`
- `0056EE`: `RGlassGauntlets` → `DrakefiredGauntlets`
- `0056EF`: `RGlassGreaves` → `DrakefiredGreaves`
- `0056F0`: `RGlassHelmet` → `DrakefiredHelmet`
- `0056F1`: `RGlassShield` → `DrakefiredShield`
- `0079E9`: `RGlassBoots` → `DrakefiredBoots`
- `0079EA`: `RGlassBoots` → `DrakefiredBoots`
- `0079EB`: `RGlassBoots` → `DrakefiredBoots`
- `0079EC`: `RGlassBoots` → `DrakefiredBoots`
- `0079ED`: `RGlassCuirass` → `DrakefiredCuirass`
- `0079EE`: `RGlassCuirass` → `DrakefiredCuirass`
- `0079EF`: `RGlassCuirass` → `DrakefiredCuirass`
- `0079F0`: `RGlassCuirass` → `DrakefiredCuirass`
- `0079F1`: `RGlassCuirass` → `DrakefiredCuirass`
- `0079F2`: `RGlassGauntlets` → `DrakefiredGauntlets`
- `0079F3`: `RGlassGauntlets` → `DrakefiredGauntlets`
- `0079F4`: `RGlassGauntlets` → `DrakefiredGauntlets`
- `0079F5`: `RGlassBoots` → `DrakefiredBoots`
- `0079F6`: `RGlassBoots` → `DrakefiredBoots`
- `0079F7`: `RGlassBoots` → `DrakefiredBoots`
- `0079F8`: `RGlassBoots` → `DrakefiredBoots`
- `0079F9`: `RGlassBoots` → `DrakefiredBoots`
- `0079FA`: `RGlassBoots` → `DrakefiredBoots`
- `0079FB`: `RGlassBoots` → `DrakefiredBoots`
- `0079FC`: `RGlassHelmet` → `DrakefiredHelmet`
- `0079FD`: `RGlassHelmet` → `DrakefiredHelmet`
- `0079FE`: `RGlassShield` → `DrakefiredShield`
- `0079FF`: `RGlassShield` → `DrakefiredShield`
- `007A00`: `RGlassShield` → `DrakefiredShield`
- `007A01`: `RGlassShield` → `DrakefiredShield`
- `007A02`: `RGlassShield` → `DrakefiredShield`
- `007A05`: `RGlassBoots` → `DrakefiredBoots`

**ElvenEldar** (33)

- `0025BC`: `ElvenBoots` → `ElvenEldarBoots`
- `0025BD`: `ElvenCuirass` → `ElvenEldarCuirass`
- `0025BE`: `ElvenGauntlets` → `ElvenEldarGauntlets`
- `0025BF`: `ElvenGreaves` → `ElvenEldarGreaves`
- `0025C0`: `ElvenHelmet` → `ElvenEldarHelmet`
- `0025C1`: `ElvenShield` → `ElvenEldarShield`
- `006FD7`: `ElvenBoots` → `ElvenEldarBoots`
- `006FD8`: `ElvenBoots` → `ElvenEldarBoots`
- `006FD9`: `ElvenBoots` → `ElvenEldarBoots`
- `006FDA`: `ElvenCuirass` → `ElvenEldarCuirass`
- `006FDB`: `ElvenCuirass` → `ElvenEldarCuirass`
- `006FDC`: `ElvenCuirass` → `ElvenEldarCuirass`
- `006FDD`: `ElvenCuirass` → `ElvenEldarCuirass`
- `006FDE`: `ElvenCuirass` → `ElvenEldarCuirass`
- `006FDF`: `ElvenGauntlets` → `ElvenEldarGauntlets`
- `006FE0`: `ElvenGauntlets` → `ElvenEldarGauntlets`
- `006FE1`: `ElvenGauntlets` → `ElvenEldarGauntlets`
- `006FE2`: `ElvenGreaves` → `ElvenEldarGreaves`
- `006FE3`: `ElvenGreaves` → `ElvenEldarGreaves`
- `006FE4`: `ElvenGreaves` → `ElvenEldarGreaves`
- `006FE5`: `ElvenGreaves` → `ElvenEldarGreaves`
- `006FE6`: `ElvenGreaves` → `ElvenEldarGreaves`
- `006FE7`: `ElvenGreaves` → `ElvenEldarGreaves`
- `006FE8`: `ElvenGreaves` → `ElvenEldarGreaves`
- `006FE9`: `ElvenHelmet` → `ElvenEldarHelmet`
- `006FEA`: `ElvenHelmet` → `ElvenEldarHelmet`
- `006FEE`: `ElvenShield` → `ElvenEldarShield`
- `006FF0`: `ElvenShield` → `ElvenEldarShield`
- `006FF1`: `ElvenShield` → `ElvenEldarShield`
- `006FF2`: `ElvenShield` → `ElvenEldarShield`
- `006FF3`: `ElvenShield` → `ElvenEldarShield`
- `006FF4`: `ElvenShield` → `ElvenEldarShield`
- `006FF6`: `ElvenGauntlets` → `ElvenEldarGauntlets`

**ElvenNight** (32)

- `007EEE`: `ElvenBoots` → `ElvenNightBoots`
- `007EEF`: `ElvenCuirass` → `ElvenNightCuirass`
- `007EF0`: `ElvenGauntlets` → `ElvenNightGauntlets`
- `007EF1`: `ElvenGreaves` → `ElvenNightGreaves`
- `007EF2`: `ElvenHelmet` → `ElvenNightHelmet`
- `007EF3`: `ElvenShield` → `ElvenNightShield`
- `048F35`: `ElvenBoots` → `ElvenNightBoots`
- `048F36`: `ElvenBoots` → `ElvenNightBoots`
- `048F37`: `ElvenBoots` → `ElvenNightBoots`
- `048F38`: `ElvenBoots` → `ElvenNightBoots`
- `048F39`: `ElvenCuirass` → `ElvenNightCuirass`
- `048F3A`: `ElvenCuirass` → `ElvenNightCuirass`
- `048F3B`: `ElvenCuirass` → `ElvenNightCuirass`
- `048F3C`: `ElvenCuirass` → `ElvenNightCuirass`
- `048F3D`: `ElvenCuirass` → `ElvenNightCuirass`
- `048F3E`: `ElvenGauntlets` → `ElvenNightGauntlets`
- `048F3F`: `ElvenGauntlets` → `ElvenNightGauntlets`
- `048F40`: `ElvenGauntlets` → `ElvenNightGauntlets`
- `048F41`: `ElvenGreaves` → `ElvenNightGreaves`
- `048F42`: `ElvenGreaves` → `ElvenNightGreaves`
- `048F43`: `ElvenGreaves` → `ElvenNightGreaves`
- `048F44`: `ElvenGreaves` → `ElvenNightGreaves`
- `048F45`: `ElvenGreaves` → `ElvenNightGreaves`
- `048F46`: `ElvenGreaves` → `ElvenNightGreaves`
- `048F47`: `ElvenGreaves` → `ElvenNightGreaves`
- `048F48`: `ElvenHelmet` → `ElvenNightHelmet`
- `048F49`: `ElvenHelmet` → `ElvenNightHelmet`
- `048F4A`: `ElvenShield` → `ElvenNightShield`
- `048F4B`: `ElvenShield` → `ElvenNightShield`
- `048F4C`: `ElvenShield` → `ElvenNightShield`
- `048F4D`: `ElvenShield` → `ElvenNightShield`
- `048F4E`: `ElvenShield` → `ElvenNightShield`

**BloodLeather** (24)

- `0020CD`: `LeatherBoots` → `BloodLeatherBoots`
- `0020CE`: `LeatherBoots` → `BloodLeatherBoots`
- `0020CF`: `LeatherBoots` → `BloodLeatherBoots`
- `0020D0`: `LeatherBoots` → `BloodLeatherBoots`
- `0020D1`: `LeatherCuirass` → `BloodLeatherCuirass`
- `0020D2`: `LeatherCuirass` → `BloodLeatherCuirass`
- `0020D3`: `LeatherCuirass` → `BloodLeatherCuirass`
- `0020D4`: `LeatherCuirass` → `BloodLeatherCuirass`
- `0020D5`: `LeatherCuirass` → `BloodLeatherCuirass`
- `0020D6`: `LeatherGauntlets` → `BloodLeatherGauntlets`
- `0020D7`: `LeatherGauntlets` → `BloodLeatherGauntlets`
- `0020D8`: `LeatherGauntlets` → `BloodLeatherGauntlets`
- `0020D9`: `LeatherGauntlets` → `BloodLeatherGauntlets`
- `0020DA`: `LeatherGauntlets` → `BloodLeatherGreaves`
- `0020DB`: `LeatherGauntlets` → `BloodLeatherGreaves`
- `0020DC`: `LeatherGauntlets` → `BloodLeatherGreaves`
- `0020DD`: `LeatherHelmet` → `BloodLeatherHelmet`
- `0020DE`: `LeatherHelmet` → `BloodLeatherHelmet`
- `0020DF`: `LeatherHelmet` → `BloodLeatherHelmet`
- `006A90`: `LeatherBoots` → `BloodLeatherBoots`
- `006A91`: `LeatherCuirass` → `BloodLeatherCuirass`
- `006A92`: `LeatherGauntlets` → `BloodLeatherGauntlets`
- `006A93`: `LeatherGreaves` → `BloodLeatherGreaves`
- `006A94`: `LeatherHelmet` → `BloodLeatherHelmet`

**GrayFox** (10)

- `005673`: `LeatherBoots` → `GrayFoxBoots`
- `005674`: `LeatherBracer` → `GrayFoxBracer`
- `005675`: `LeatherCuirass` → `GrayFoxCuirass`
- `005676`: `LeatherGauntlets` → `GrayFoxGauntlets`
- `005677`: `LeatherGreaves` → `GrayFoxGreaves`
- `0073E7`: `LeatherBoots` → `GrayFoxBoots`
- `0513CD`: `LeatherGreaves` → `GrayFoxGreaves`
- `0513CF`: `LeatherCuirass` → `GrayFoxCuirass`
- `0513D0`: `LeatherGauntlets` → `GrayFoxGauntlets`
- `0513D1`: `LeatherBracer` → `GrayFoxBracer`

**ArcticFur** (6)

- `005BCD`: `FurBoots` → `ArcticFurBoots`
- `005BCE`: `FurCuirass` → `ArcticFurCuirass`
- `005BCF`: `FurGauntlets` → `ArcticFurGauntlets`
- `005BD0`: `FurHelmet` → `ArcticFurHelmet`
- `005BD1`: `FurGreaves` → `ArcticFurGreaves`
- `03BE6E`: `FurGauntlets` → `ArcticFurGauntlets`

**Aureus** (6)

- `0025C8`: `MithrilBoots` → `AureusBoots`
- `0025C9`: `MithrilCuirass` → `AureusCuirass`
- `0025CA`: `MithrilGauntlets` → `AureusGauntlets`
- `0025CB`: `MithrilGreaves` → `AureusGreaves`
- `0025CC`: `MithrilHelmet` → `AureusHelmet`
- `0025CD`: `MithrilShield` → `AureusShield`

**ShadowMail** (6)

- `03885B`: `MithrilBoots` → `ShadowMailBoots`
- `03885C`: `MithrilCuirass` → `ShadowMailCuirass`
- `03885D`: `MithrilGauntlets` → `ShadowMailGauntlets`
- `03885E`: `MithrilGreaves` → `ShadowMailGreaves`
- `03885F`: `MithrilHelmet` → `ShadowMailHelmet`
- `038861`: `MithrilShield` → `ShadowMailShield`

**WornFur** (6)

- `030DB8`: `FurCuirass` → `WornFurCuirass`
- `030DB9`: `FurBoots` → `WornFurBoots`
- `030DBA`: `FurGauntlets` → `WornFurGauntlets`
- `030DBB`: `FurGreaves` → `WornFurGreaves`
- `030DBC`: `FurHelmet` → `WornFurHelmet`
- `030DBD`: `FurShield` → `WornFurShield`

**WornLeather** (6)

- `001C49`: `LeatherBoots` → `WornLeatherBoots`
- `001C4A`: `LeatherCuirass` → `WornLeatherCuirass`
- `001C4B`: `LeatherGauntlets` → `WornLeatherGauntlets`
- `001C4C`: `LeatherGreaves` → `WornLeatherGreaves`
- `001C4D`: `LeatherHelmet` → `WornLeatherHelmet`
- `001C4E`: `LeatherShield` → `WornLeatherShield`

## MagicLoader changes

Display-name (`FullNames`) changes in the MagicLoader JSON exports.

### `Oscuro's_Oblivion_Overhaul_ARMO.json` — +0 -0 ~6

- ~ `LOC_FN_vellaGlassBootsOOO`: "Ornate Obsidian Boots" → "Blue Glass Boots"
- ~ `LOC_FN_vellaGlassCuirassOOO`: "Ornate Obsidian Cuirass" → "Blue Glass Cuirass"
- ~ `LOC_FN_vellaGlassGauntletsOOO`: "Ornate Obsidian Gauntlets" → "Blue Glass Gauntlets"
- ~ `LOC_FN_vellaGlassGreavesOOO`: "Ornate Obsidian Greaves" → "Blue Glass Greaves"
- ~ `LOC_FN_vellaGlassHelmetOOO`: "Ornate Obsidian Helmet" → "Blue Glass Helmet"
- ~ `LOC_FN_vellaGlassShieldOOO`: "Ornate Obsidian Shield" → "Blue Glass Shield"

## Map cell changes since `alpha90`

Each OOO cell layers TES4-injected OOO content over UE5-baked remaster geometry; these reconcile the two so each object renders from exactly one layer. Sourced from MapClone configs (baseline `8e9efaf5a62a`).

- **TES4 REFR suppression** — disable OOO REFRs that *duplicate* UE5-baked architecture (drop the TES4 twin, keep the UE5 copy).
- **Ghost suppression (Begone)** — remove UE5-baked actors with *no* TES4 counterpart (drop the UE5 ghost, keep TES4).
- **Position overrides** — re-seat OOO REFRs (chests/furniture) left floating once a supporting STAT was disabled.

### TES4 REFR suppression — disable OOO duplicates of UE5-baked architecture (ESP `INITIALLY_DISABLED`)

+254 disabled REFRs (2127 → 2381; 25 → 27 cells)

- **LipsandTarn03OOO**: +125 (total 125) *(new cell)*
- **Varastal**: +125 (total 125) *(new cell)*
- **Rosulas**: +2 (total 117)
- **Rosulas02**: +2 (total 147)

### REFR position overrides

net +17 overrides (128 → 145; 17 → 21 cells)

- **LipsandTarn03OOO**: +7 (total 7) *(new cell)*
- **Varastal**: +6 (total 6) *(new cell)*
- **GraveGroundCave**: +2 (total 2) *(new cell)*
- **BrokenToothCave**: +1 (total 1) *(new cell)*
- **Rosulas02**: +1 (total 9)

### Ghost suppression (Begone)

net +92 entries (1241 → 1333; 44 → 46 cells)

- **L_BloodClotCave**: +58 (total 80)
- **L_GraveGroundCaveXX_Li**: +12 (total 12) *(new cell)*
- **L_BloodClotCave_Li**: +11 (total 11) *(new cell)*
- **L_BloodClotCave03_Li**: +4 (total 5)
- **L_BloodClotCave02_Li**: +3 (total 8)
- **L_RosulasXX**: +2 (total 32)
- **L_GraveGroundCaveXX**: +1 (total 34)
- **L_Rosulas02XX**: +1 (total 12)

### Exterior foliage fixes

- **GraveGround** *(new)*

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Armor (ARMO) — +6 -0 ~0

**Added:**

- `LairVileCrimsonScarRaiment01` (FormID `00BE65`) — "LOC_FN_LairVileCrimsonScarRaiment01"
- `LairVileCrimsonScarRaiment05` (FormID `00BE66`) — "LOC_FN_LairVileCrimsonScarRaiment05"
- `LairVileCrimsonScarRaiment10` (FormID `00BE67`) — "LOC_FN_LairVileCrimsonScarRaiment10"
- `LairVileCrimsonScarRaiment15` (FormID `00BE68`) — "LOC_FN_LairVileCrimsonScarRaiment15"
- `LairVileCrimsonScarRaiment25` (FormID `00BE6A`) — "LOC_FN_LairVileCrimsonScarRaiment25"
- `LairVileCrimsonScarRaiment20` (FormID `00C35E`) — "LOC_FN_LairVileCrimsonScarRaiment20"

## ESP changes — `OOO_DeluxeEdition.esp`

_No record-level changes detected._

## ESP changes — `OOO_OOMC_Compatibility_Patch.esp`

_No record-level changes detected._

## ESP changes — `OOO_UnlimitedRingsReduxPatch.esp`

_No record-level changes detected._

## ESP changes — `OOO_UORP.esp`

_No record-level changes detected._

