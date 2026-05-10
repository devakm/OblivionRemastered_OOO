# alpha47 — release notes

_Compared against `alpha46`._

## File-level changes

- Added: 1
- Removed: 0
- Changed: 8

### Added

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ENCH.json`

### Changed

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_AMMO.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_BOOK.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CLOT.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_DIAL.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_NPC_.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_SCPT.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Activator (ACTI) — +0 -0 ~1

**Changed:**

- `OscuroObeliskActivator` (FormID `001702`) — "LOC_FN_OscuroObeliskActivator" — `modl`: `'Obelisk\\Obelisk01.NIF'` → `'Architecture\\ImperialCity\\ICTombstone02.NIF'`

### Clothing (CLOT) — +0 -0 ~9

**Changed:**

- `XNecrocloakOOO` (FormID `005685`) — "LOC_FN_XNecrocloakOOO" — `modl`: `'Clothes\\RobeMCBlack\\Hood.NIF'` → `'Clothes\\RobeMCBlack\\M\\RobeMCBlack.NIF'`
- `ArchMageRobeTravenDead` (FormID `006258`) — "LOC_FN_ArchMageRobeTravenDead" — `full`: `"Arch-Mage's Robe"` → `'LOC_FN_ArchMageRobeTravenDead'`
- `XnecrorobeUOOO` (FormID `006F2D`) — "LOC_FN_XnecrorobeUOOO" — `modl`: `'Clothes\\RobeMCBlack\\Hood.NIF'` → `'Clothes\\RobeMCBlack\\M\\RobeMCBlack.NIF'`
- `EnchRingZWormKing` (FormID `013E1E`) — "LOC_FN_EnchRingZWormKing" — `full`: `"Worm's Blood"` → `'LOC_FN_EnchRingZWormKing'`
- `JewelryZNecklaceAmazonJade` (FormID `02A60F`) — "LOC_FN_JewelryZNecklaceAmazonJade" — `full`: `'Heart of Fury'` → `'LOC_FN_JewelryZNecklaceAmazonJade'`
- `BlackHoodOOO` (FormID `03924A`) — "LOC_FN_BlackHoodOOO" — `full`: `"Carla's Hood of Night"` → `'LOC_FN_BlackHoodOOO'`
- `BlackRobeOOO` (FormID `03CABF`) — "LOC_FN_BlackRobeOOO" — `full`: `"Carla's Robe of Night"` → `'LOC_FN_BlackRobeOOO'`
- `OOOHooves` (FormID `06EA65`) — "LOC_FN_OOOHooves" — `full`: `'Hooves'` → `'LOC_FN_OOOHooves'`
- `OOOWings` (FormID `06EA66`) — "LOC_FN_OOOWings" — `full`: `'SeducerWings'` → `'LOC_FN_OOOWings'`

### Dialogue Topic (DIAL) — +12 -0 ~0

**Added:**

- `HouseTooMuchLeyawiin` (FormID `04ED77`) — "LOC_FN_HouseTooMuchLeyawiin"
- `HouseBuyLeyawiin` (FormID `04ED78`) — "LOC_FN_HouseBuyLeyawiin"
- `HouseTooMuchBravil` (FormID `04ED79`) — "LOC_FN_HouseTooMuchBravil"
- `HouseBuyBravil` (FormID `04ED7B`) — "LOC_FN_HouseBuyBravil"
- `HouseTooMuchChorrol` (FormID `04F203`) — "LOC_FN_HouseTooMuchChorrol"
- `HouseBuyChorrol` (FormID `04F204`) — "LOC_FN_HouseBuyChorrol"
- `HouseTooMuchSkingrad` (FormID `04F205`) — "LOC_FN_HouseTooMuchSkingrad"
- `HouseBuySkingrad` (FormID `04F206`) — "LOC_FN_HouseBuySkingrad"
- `HouseTooMuchBruma` (FormID `04F207`) — "LOC_FN_HouseTooMuchBruma"
- `HouseBuyBruma` (FormID `04F208`) — "LOC_FN_HouseBuyBruma"
- `HouseTooMuchCheydinhal` (FormID `04F209`) — "LOC_FN_HouseTooMuchCheydinhal"
- `HouseBuyCheydinhal` (FormID `04F20A`) — "LOC_FN_HouseBuyCheydinhal"

### NPC (NPC_) — +0 -0 ~4

**Changed:**

- `NecromancerBossFemaleHighElf` (FormID `04B945`) — "LOC_FN_NecromancerBossFemaleHighElf" — `full`: `'Keeper of the Dead'` → `'LOC_FN_NecromancerBossFemaleHighElf'`
- `NecromancerBossFemaleBreton` (FormID `04B946`) — "LOC_FN_NecromancerBossFemaleBreton" — `full`: `'Keeper of the Dead'` → `'LOC_FN_NecromancerBossFemaleBreton'`
- `NecromancerBossMaleHighElf` (FormID `04B947`) — "LOC_FN_NecromancerBossMaleHighElf" — `full`: `'Keeper of the Dead'` → `'LOC_FN_NecromancerBossMaleHighElf'`
- `NecromancerBossMaleBreton` (FormID `04B948`) — "LOC_FN_NecromancerBossMaleBreton" — `full`: `'Keeper of the Dead'` → `'LOC_FN_NecromancerBossMaleBreton'`

