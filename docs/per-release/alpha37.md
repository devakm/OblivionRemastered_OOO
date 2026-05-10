# alpha37 — release notes

_Compared against `alpha36`._

## File-level changes

- Added: 14
- Removed: 6
- Changed: 5

### Added

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_DOOR.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_SCPT.json`
- `OblivionRemastered/Content/Paks/~mods/L_OOOR1waterCave_Map.pak`
- `OblivionRemastered/Content/Paks/~mods/L_OOOR1waterCave_Map.ucas`
- `OblivionRemastered/Content/Paks/~mods/L_OOOR1waterCave_Map.utoc`
- `OblivionRemastered/Content/Paks/~mods/L_OOOR2waterCave02_Map.pak`
- `OblivionRemastered/Content/Paks/~mods/L_OOOR2waterCave02_Map.ucas`
- `OblivionRemastered/Content/Paks/~mods/L_OOOR2waterCave02_Map.utoc`
- `OblivionRemastered/Content/Paks/~mods/L_OscuroWaterCellCHMGWell0_Map.pak`
- `OblivionRemastered/Content/Paks/~mods/L_OscuroWaterCellCHMGWell0_Map.ucas`
- `OblivionRemastered/Content/Paks/~mods/L_OscuroWaterCellCHMGWell0_Map.utoc`
- `OblivionRemastered/Win64/ue4ss/Mods/RAX/dlls/main.dll`
- `OblivionRemastered/Win64/ue4ss/Mods/RAX/enabled.txt`
- `OblivionRemastered/Win64/ue4ss/Mods/RAX/scripts/main.lua`

### Removed

- `OblivionRemastered/Content/Dev/ObvData/Data/OOMC_ImperialCityMages.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/OOMC_ImperialCityMages.ini`
- `OblivionRemastered/Win64/ue4ss/Mods/LVSP_Fix/dlls/OREF/OOO.json`
- `OblivionRemastered/Win64/ue4ss/Mods/LVSP_Fix/dlls/main.dll`
- `OblivionRemastered/Win64/ue4ss/Mods/LVSP_Fix/enabled.txt`
- `OblivionRemastered/Win64/ue4ss/Mods/LVSP_Fix/scripts/main.lua`

### Changed

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CELL.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CELLMAP.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_NPC_.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Cell (CELL) — +2 -0 ~0

**Added:**

- `CheydinhalMagesGuildBasement` (FormID `006917`) — "LOC_FN_CheydinhalMagesGuildBasement"
- `HrotandaVale02` (FormID `0463F6`) — "LOC_FN_HrotandaVale02"

### Door (DOOR) — +0 -0 ~9

**Changed:**

- `AyleidWeapDoor` (FormID `00353D`) — "LOC_FN_AyleidWeapDoor" — `full`: `'Wooden Door'` → `'LOC_FN_AyleidWeapDoor'`
- `OOOARDoor01bVarastal` (FormID `0173D6`) — "LOC_FN_OOOARDoor01bVarastal" — `full`: `'Stone Door'` → `'LOC_FN_OOOARDoor01bVarastal'`; `modl`: `'dungeons\\ayleidruins\\exterior\\OOOardoor01Varastal.nif'` → `'Dungeons\\AyleidRuins\\Exterior\\ARDoor01.NIF'`
- `OOOSE32PCDoor` (FormID `02364A`) — "LOC_FN_OOOSE32PCDoor" — `full`: `'Door to My Chamber'` → `'LOC_FN_OOOSE32PCDoor'`
- `DisplayCasePurple01DoorUmbacano` (FormID `02E2B4`) — "LOC_FN_DisplayCasePurple01DoorUmbacano" — `full`: `'Display Case'` → `'LOC_FN_DisplayCasePurple01DoorUmbacano'`
- `DisplayCasePurple02DoorUmbacano` (FormID `02E2B5`) — "LOC_FN_DisplayCasePurple02DoorUmbacano" — `full`: `'Display Case'` → `'LOC_FN_DisplayCasePurple02DoorUmbacano'`
- `RicketyFenceGateSlavers` (FormID `0356FE`) — "LOC_FN_RicketyFenceGateSlavers" — `full`: `'Stick Fence Gate'` → `'LOC_FN_RicketyFenceGateSlavers'`
- `OOOSEGateToTamriel` (FormID `07FE1E`) — "LOC_FN_OOOSEGateToTamriel" — `full`: `"Madgod's Portal"` → `'LOC_FN_OOOSEGateToTamriel'`
- `OOOSEGateToSEWorld` (FormID `0A6F5D`) — "LOC_FN_OOOSEGateToSEWorld" — `full`: `"Madgod's Portal"` → `'LOC_FN_OOOSEGateToSEWorld'`
- `OOOSE38MuseumDisplayCase` (FormID `1325B6`) — "LOC_FN_OOOSE38MuseumDisplayCase" — `full`: `'Display Case'` → `'LOC_FN_OOOSE38MuseumDisplayCase'`

### Leveled Creature List (LVLC) — +0 -0 ~7

**Changed:**

- `LL1BanditMelee100` (FormID `03407B`) — + entry: level 1 × 1 → `003A1A`; + entry: level 1 × 1 → `003A1B`; + entry: level 1 × 1 → `003A1C`; + entry: level 1 × 1 → `003A1D`; + entry: level 1 × 1 → `010EAE`; + entry: level 1 × 1 → `010EAF`; + entry: level 1 × 1 → `010EB1`; + entry: level 1 × 1 → `010EB2`; + entry: level 1 × 1 → `010EB3`; + entry: level 1 × 1 → `010EB4`; + entry: level 1 × 1 → `010EB5`; + entry: level 1 × 1 → `010EB6`
- `LL1Bandit0ArcticMeleePack` (FormID `010EE4`) — + entry: level 1 × 1 → `03DB33`; - entry: level 1 × 1 → `0039DD`; - entry: level 1 × 1 → `0039DE`; - entry: level 1 × 1 → `010ECB`; - entry: level 1 × 1 → `010ECC`; - entry: level 1 × 1 → `010ECD`; - entry: level 1 × 1 → `010ECE`; - entry: level 1 × 1 → `010ECF`; - entry: level 1 × 1 → `010ED0`; - entry: level 1 × 1 → `010ED1`; - entry: level 1 × 1 → `010ED2`; - entry: level 1 × 1 → `010ED3`; - entry: level 1 × 1 → `010ED4`; - entry: level 1 × 1 → `010ED5`; - entry: level 1 × 1 → `010ED6`; - entry: level 1 × 1 → `01383A`; - entry: level 1 × 1 → `01383B`
- `LL1Bandit0ArcticMissilePack` (FormID `010EE5`) — + entry: level 1 × 1 → `03DB33`; - entry: level 1 × 1 → `0039E1`; - entry: level 1 × 1 → `010ED7`; - entry: level 1 × 1 → `010ED8`; - entry: level 1 × 1 → `010ED9`; - entry: level 1 × 1 → `010EDA`; - entry: level 1 × 1 → `010EDB`; - entry: level 1 × 1 → `010EDC`; - entry: level 1 × 1 → `010EDD`; - entry: level 1 × 1 → `010EDE`; - entry: level 1 × 1 → `010EDF`; - entry: level 1 × 1 → `010EE0`; - entry: level 1 × 1 → `010EE1`; - entry: level 1 × 1 → `010EE2`; - entry: level 1 × 1 → `010EE3`; - entry: level 1 × 1 → `01383C`; - entry: level 1 × 1 → `01383D`
- `LL1Bandit0ArcticMissile100` (FormID `010EE7`) — + entry: level 1 × 1 → `03DB33`; - entry: level 1 × 1 → `0039E1`; - entry: level 1 × 1 → `010ED7`; - entry: level 1 × 1 → `010ED8`; - entry: level 1 × 1 → `010ED9`; - entry: level 1 × 1 → `010EDA`; - entry: level 1 × 1 → `010EDB`; - entry: level 1 × 1 → `010EDC`; - entry: level 1 × 1 → `010EDD`; - entry: level 1 × 1 → `010EDE`; - entry: level 1 × 1 → `010EDF`; - entry: level 1 × 1 → `010EE0`; - entry: level 1 × 1 → `010EE1`; - entry: level 1 × 1 → `010EE2`; - entry: level 1 × 1 → `010EE3`; - entry: level 1 × 1 → `01383C`; - entry: level 1 × 1 → `01383D`; - entry: level 1 × 2 → `010EE5`; - entry: level 1 × 3 → `010EE5`
- `LL1WildernessSnowHuntOOO` (FormID `012313`) — - entry: level 1 × 1 → `0017DC`; - entry: level 1 × 1 → `0017E1`; - entry: level 1 × 1 → `004231`; - entry: level 1 × 1 → `004237`; - entry: level 1 × 1 → `004238`; - entry: level 1 × 1 → `02797B`; - entry: level 1 × 1 → `02F502`; - entry: level 1 × 2 → `004231`; - entry: level 1 × 3 → `004231`
- `LL1WildernessSnowHunt50` (FormID `012316`) — - entry: level 1 × 1 → `0017DC`; - entry: level 1 × 1 → `0017E1`; - entry: level 1 × 1 → `004231`; - entry: level 1 × 1 → `004237`; - entry: level 1 × 1 → `004238`; - entry: level 1 × 1 → `02797B`; - entry: level 1 × 1 → `02F502`; - entry: level 1 × 2 → `004231`; - entry: level 1 × 3 → `004231`
- `LL1Bandit0ArcticMissile25` (FormID `02B938`) — + entry: level 1 × 1 → `03DB33`; - entry: level 1 × 1 → `0039E1`; - entry: level 1 × 1 → `010ED7`; - entry: level 1 × 1 → `010ED8`; - entry: level 1 × 1 → `010ED9`; - entry: level 1 × 1 → `010EDA`; - entry: level 1 × 1 → `010EDB`; - entry: level 1 × 1 → `010EDC`; - entry: level 1 × 1 → `010EDD`; - entry: level 1 × 1 → `010EDE`; - entry: level 1 × 1 → `010EDF`; - entry: level 1 × 1 → `010EE0`; - entry: level 1 × 1 → `010EE1`; - entry: level 1 × 1 → `010EE2`; - entry: level 1 × 1 → `010EE3`; - entry: level 1 × 1 → `01383C`; - entry: level 1 × 1 → `01383D`; - entry: level 1 × 2 → `010EE5`; - entry: level 1 × 3 → `010EE5`

### Leveled Item List (LVLI) — +3 -0 ~0

**Added:**

- `LL0NPCWeaponZArrow100Lvl20Low` (FormID `00DDFF`)
- `LL0NPCArmorZWeaponPackArrowLvl20Low` (FormID `00DE00`)
- `LL0NPCWeapon0ZMagicArrow100lvl20Low` (FormID `00DE01`)

### NPC (NPC_) — +0 -0 ~39

**Changed:**

- `GhostMinionMeleeMale1a` (FormID `00312E`) — "LOC_FN_GhostMinionMeleeMale1a" — `full`: `'Ghostly Warrior'` → `'LOC_FN_GhostMinionMeleeMale1a'`
- `GhostMinionMeleeMale1b` (FormID `003130`) — "LOC_FN_GhostMinionMeleeMale1b" — `full`: `'Ghostly Warrior'` → `'LOC_FN_GhostMinionMeleeMale1b'`
- `GhostMinionMeleeMale1c` (FormID `003131`) — "LOC_FN_GhostMinionMeleeMale1c" — `full`: `'Ghostly Warrior'` → `'LOC_FN_GhostMinionMeleeMale1c'`
- `GhostMinionMeleeMale1d` (FormID `003132`) — "LOC_FN_GhostMinionMeleeMale1d" — `full`: `'Ghostly Warrior'` → `'LOC_FN_GhostMinionMeleeMale1d'`
- `GhostMinionMeleeMale1e` (FormID `003133`) — "LOC_FN_GhostMinionMeleeMale1e" — `full`: `'Ghostly Warrior'` → `'LOC_FN_GhostMinionMeleeMale1e'`
- `GhostMinionMeleeMale1f` (FormID `003134`) — "LOC_FN_GhostMinionMeleeMale1f" — `full`: `'Ghostly Warrior'` → `'LOC_FN_GhostMinionMeleeMale1f'`
- `GhostMinionMeleeMale1g` (FormID `003135`) — "LOC_FN_GhostMinionMeleeMale1g" — `full`: `'Ghostly Warrior'` → `'LOC_FN_GhostMinionMeleeMale1g'`
- `GhostMinionMeleeMale1h` (FormID `003136`) — "LOC_FN_GhostMinionMeleeMale1h" — `full`: `'Ghostly Warrior'` → `'LOC_FN_GhostMinionMeleeMale1h'`
- `GhostMinionMeleeMale2a` (FormID `003137`) — "LOC_FN_GhostMinionMeleeMale2a" — `full`: `'Spectral Warrior'` → `'LOC_FN_GhostMinionMeleeMale2a'`
- `GhostMinionMeleeMale2b` (FormID `003138`) — "LOC_FN_GhostMinionMeleeMale2b" — `full`: `'Spectral Warrior'` → `'LOC_FN_GhostMinionMeleeMale2b'`
- `GhostMinionMeleeMale2c` (FormID `003139`) — "LOC_FN_GhostMinionMeleeMale2c" — `full`: `'Spectral Warrior'` → `'LOC_FN_GhostMinionMeleeMale2c'`
- `GhostMinionMeleeMale2d` (FormID `00313A`) — "LOC_FN_GhostMinionMeleeMale2d" — `full`: `'Spectral Warrior'` → `'LOC_FN_GhostMinionMeleeMale2d'`
- `GhostMinionMeleeMale2e` (FormID `00313B`) — "LOC_FN_GhostMinionMeleeMale2e" — `full`: `'Spectral Warrior'` → `'LOC_FN_GhostMinionMeleeMale2e'`
- `GhostMinionMeleeMale2f` (FormID `00313C`) — "LOC_FN_GhostMinionMeleeMale2f" — `full`: `'Spectral Warrior'` → `'LOC_FN_GhostMinionMeleeMale2f'`
- `GhostMinionMeleeMale2g` (FormID `00313D`) — "LOC_FN_GhostMinionMeleeMale2g" — `full`: `'Spectral Warrior'` → `'LOC_FN_GhostMinionMeleeMale2g'`
- `GhostMinionMeleeMale2h` (FormID `00313E`) — "LOC_FN_GhostMinionMeleeMale2h" — `full`: `'Spectral Warrior'` → `'LOC_FN_GhostMinionMeleeMale2h'`
- `GhostMinionMeleeMale3` (FormID `003635`) — "LOC_FN_GhostMinionMeleeMale3" — `full`: `'Spectral Reaver'` → `'LOC_FN_GhostMinionMeleeMale3'`
- `GhostMinionMeleeMale3a` (FormID `003636`) — "LOC_FN_GhostMinionMeleeMale3a" — `full`: `'Spectral Reaver'` → `'LOC_FN_GhostMinionMeleeMale3a'`
- `GhostMinionMeleeMale3b` (FormID `003637`) — "LOC_FN_GhostMinionMeleeMale3b" — `full`: `'Spectral Reaver'` → `'LOC_FN_GhostMinionMeleeMale3b'`
- `GhostMinionMeleeMale3c` (FormID `003638`) — "LOC_FN_GhostMinionMeleeMale3c" — `full`: `'Spectral Reaver'` → `'LOC_FN_GhostMinionMeleeMale3c'`

_…19 more changed omitted (see JSON for full list)_

### Worldspace (WRLD) — +1 -0 ~0

**Added:**

- `?` (FormID `01C318`)

