# alpha68 — release notes

_Compared against `alpha67`._

## File-level changes

- Added: 0
- Removed: 0
- Changed: 6

### Changed

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ARMO.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_BOOK.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CLOT.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/OptionalPatches/SyncMap - DeluxeEdition/Oscuro's_Oblivion_Overhaul.ini`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Armor (ARMO) — +0 -0 ~10

**Changed:**

- `1grayfoxsbootsDeception` (FormID `005673`) — "LOC_FN_1grayfoxsbootsDeception" — `edid`: `'1grayfoxsboots'` → `'1grayfoxsbootsDeception'`; `full`: `'LOC_FN_1grayfoxsboots'` → `'LOC_FN_1grayfoxsbootsDeception'`
- `1grayfoxsbracersDeception` (FormID `005674`) — "LOC_FN_1grayfoxsbracersDeception" — `edid`: `'1grayfoxsbracers'` → `'1grayfoxsbracersDeception'`; `full`: `'LOC_FN_1grayfoxsbracers'` → `'LOC_FN_1grayfoxsbracersDeception'`
- `1grayfoxscuirassDeception` (FormID `005675`) — "LOC_FN_1grayfoxscuirassDeception" — `edid`: `'1grayfoxscuirass'` → `'1grayfoxscuirassDeception'`; `full`: `'LOC_FN_1grayfoxscuirass'` → `'LOC_FN_1grayfoxscuirassDeception'`
- `1grayfoxsglovesDeception` (FormID `005676`) — "LOC_FN_1grayfoxsglovesDeception" — `edid`: `'1grayfoxsgloves'` → `'1grayfoxsglovesDeception'`; `full`: `'LOC_FN_1grayfoxsgloves'` → `'LOC_FN_1grayfoxsglovesDeception'`
- `1grayfoxsgreavesDeception` (FormID `005677`) — "LOC_FN_1grayfoxsgreavesDeception" — `edid`: `'1grayfoxsgreaves'` → `'1grayfoxsgreavesDeception'`; `full`: `'LOC_FN_1grayfoxsgreaves'` → `'LOC_FN_1grayfoxsgreavesDeception'`
- `1greyfoxsbootsWar` (FormID `0073E7`) — "LOC_FN_1greyfoxsbootsWar" — `edid`: `'1greyfoxsboots'` → `'1greyfoxsbootsWar'`; `full`: `"Gray Fox's Boots"` → `'LOC_FN_1greyfoxsbootsWar'`; `modl`: `'armor\\Gray Fox Armory\\m\\greyfoxsboots.nif'` → `'Armor\\Thief\\M\\Boots.NIF'`
- `1greyfoxsgreavesWar` (FormID `0513CD`) — "LOC_FN_1greyfoxsgreavesWar" — `edid`: `'1greyfoxsgreaves'` → `'1greyfoxsgreavesWar'`; `full`: `'LOC_FN_1greyfoxsgreaves'` → `'LOC_FN_1greyfoxsgreavesWar'`; `modl`: `'armor\\Gray Fox Armory\\m\\greyfoxsgreaves.nif'` → `'Armor\\Thief\\M\\Greaves.NIF'`
- `1greyfoxscuirassWar` (FormID `0513CF`) — "LOC_FN_1greyfoxscuirassWar" — `edid`: `'1greyfoxscuirass'` → `'1greyfoxscuirassWar'`; `full`: `'LOC_FN_1greyfoxscuirass'` → `'LOC_FN_1greyfoxscuirassWar'`; `modl`: `'armor\\Gray Fox Armory\\m\\greyfoxscuirass.nif'` → `'Armor\\Thief\\M\\Cuirass.NIF'`
- `1greyfoxsglovesWar` (FormID `0513D0`) — "LOC_FN_1greyfoxsglovesWar" — `edid`: `'1greyfoxsgloves'` → `'1greyfoxsglovesWar'`; `full`: `'LOC_FN_1greyfoxsgloves'` → `'LOC_FN_1greyfoxsglovesWar'`; `modl`: `'armor\\Gray Fox Armory\\m\\greyfoxsgloves.nif'` → `'Armor\\Thief\\M\\Gauntlets.NIF'`
- `1greyfoxsbracersWar` (FormID `0513D1`) — "LOC_FN_1greyfoxsbracersWar" — `edid`: `'1greyfoxsbracers'` → `'1greyfoxsbracersWar'`; `full`: `'LOC_FN_1greyfoxsbracers'` → `'LOC_FN_1greyfoxsbracersWar'`; `modl`: `'armor\\Gray Fox Armory\\m\\greyfoxsbracers.nif'` → `'Armor\\Bracers\\Bracer01M.NIF'`

### Clothing (CLOT) — +1 -0 ~3

**Added:**

- `TGGrayFoxCowl` (FormID `022E81`) — "LOC_FN_TGGrayFoxCowl"

**Changed:**

- `1grayfoxshoodDeception` (FormID `0073E3`) — "LOC_FN_GrayFoxHoodDeception" — `edid`: `'1grayfoxshood'` → `'1grayfoxshoodDeception'`; `full`: `"Gray Fox's Hood"` → `'LOC_FN_GrayFoxHoodDeception'`; `modl`: `'armor\\Gray Fox Armory\\m\\grayfoxshood.nif'` → `'Clothes\\RobeDarkBrotherhood\\Hood.NIF'`
- `1greyfoxshoodWar` (FormID `0073E4`) — "LOC_FN_GrayFoxHoodWar" — `edid`: `'1greyfoxshood'` → `'1greyfoxshoodWar'`; `full`: `"Grey Fox's Hood"` → `'LOC_FN_GrayFoxHoodWar'`; `modl`: `'armor\\Gray Fox Armory\\m\\greyfoxshood.nif'` → `'Clothes\\RobeDarkBrotherhood\\Hood.NIF'`
- `1grayfoxhoodLoot` (FormID `0073E5`) — "LOC_FN_GrayFoxHoodLoot" — `edid`: `'1grayfoxhood'` → `'1grayfoxhoodLoot'`; `full`: `'Gray Fox Hood'` → `'LOC_FN_GrayFoxHoodLoot'`; `modl`: `'armor\\Gray Fox Armory\\m\\grayfoxhood.nif'` → `'Clothes\\RobeDarkBrotherhood\\Hood.NIF'`

### Enchantment (ENCH) — +7 -0 ~5

**Added:**

- `TGGrayCowlEnchanment` (FormID `03A82C`)
- `1ENgrayfoxhoodDeception` (FormID `00DE4E`)
- `1ENgrayfoxhoodWar` (FormID `00DE4F`)
- `1ENgrayfoxbootsDeception` (FormID `00DE50`)
- `1ENgrayfoxcuirassDeception` (FormID `00DE51`)
- `1ENgrayfoxglovesDeception` (FormID `00DE52`)
- `1ENgrayfoxgreavesDeception` (FormID `00DE53`)

**Changed:**

- `1ENgrayfoxglovesWar` (FormID `002574`) — `edid`: `'1ENgrayfoxgloves'` → `'1ENgrayfoxglovesWar'`
- `1ENgrayfoxhoodLoot` (FormID `0073E6`) — `edid`: `'1ENgrayfoxhood'` → `'1ENgrayfoxhoodLoot'`
- `1ENgrayfoxcuirassWar` (FormID `0513C7`) — `edid`: `'1ENgrayfoxcuirass'` → `'1ENgrayfoxcuirassWar'`
- `1ENgrayfoxbootsWar` (FormID `0513C8`) — `edid`: `'1ENgrayfoxboots'` → `'1ENgrayfoxbootsWar'`
- `1ENgrayfoxgreavesWar` (FormID `0513C9`) — `edid`: `'1ENgrayfoxgreaves'` → `'1ENgrayfoxgreavesWar'`

## ESP changes — `OOO_DeluxeEdition.esp`

_No record-level changes detected._

## ESP changes — `OOO_OOMC_Compatibility_Patch.esp`

_No record-level changes detected._

## ESP changes — `OOO_UnlimitedRingsReduxPatch.esp`

_No record-level changes detected._

## ESP changes — `OOO_UORP.esp`

_No record-level changes detected._

