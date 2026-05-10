# alpha26 — release notes

_Compared against `alpha25`._

## File-level changes

- Added: 1
- Removed: 115
- Changed: 1

### Added

- `Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul_Test.ini`

### Removed

- `Content/Dev/ObvData/Data/Archive/OOO_FGD09HistPatch.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_GameSettings.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_GameSettings.esp.save.2025_06_26_20_13_21`
- `Content/Dev/ObvData/Data/Archive/OOO_NewAmmo04.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewAmmoComps.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewArmor.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewArmor03.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewArmor04Amazon.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewArmor04Bosmer.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewArmorCombined.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewArmorCombined04.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewArmorComps.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewArmorOdds.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewArmorUnused.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewBooks04.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewBooksComp.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewCells04.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewChestComps.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewChests.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewChests03.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewChests2.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewChests2.esp.save.2025_06_26_21_29_56`
- `Content/Dev/ObvData/Data/Archive/OOO_NewChestsSkip.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewClothing04.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewClothingComps.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewCreatureComps.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewCreatures01.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewCreatures02.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewCreatures03.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewCreatures04Fish.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewCreatures04Golems.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewCreatures04Special.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewCreaturesCombined04.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewDoors04.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewDoors04Temp.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewGear04Amazon.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewGear04Bosmer.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewGear04Sylvan.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewGemShards04.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewInteriorDoors.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewMapMarkers04.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewMiscComp04.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewMiscItems.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewNPCs03.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewNPCs04.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewNPCs04Odd.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewNPCs04Seducer.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewNPCs04Special.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewNPCsCombined.esp`
- `Content/Dev/ObvData/Data/Archive/OOO_NewPotions04.esp`
_…65 more removed omitted_

### Changed

- `Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Cell (CELL) — +0 -1 ~1

**Removed:**

- `MarshPunk` (FormID `02EFE5`) — "LOC_FN_MarshPunk"

**Changed:**

- `zOOOBarastas02` (FormID `000D63`) — "LOC_FN_zOOOBarastas02" — `full`: `'Barastas Nelar'` → `'LOC_FN_zOOOBarastas02'`

### Creature (CREA) — +0 -0 ~21

**Changed:**

- `OOOSEVCWispMidi150` (FormID `00FB97`) — "LOC_FN_OOOSEVCWispMidi150" — `full`: `'Vatte-lys'` → `'LOC_FN_OOOSEVCWispMidi150'`; `modl`: `'OOOSE\\Creatures\\VCVatteLys\\skeleton150.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispVari000` (FormID `010946`) — "LOC_FN_OOOSEVCWispVari000" — `full`: `'Vafurlogi'` → `'LOC_FN_OOOSEVCWispVari000'`; `modl`: `'OOOSE\\Creatures\\VCVafurlogi\\skeleton000m000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispVari180` (FormID `01096E`) — "LOC_FN_OOOSEVCWispVari180" — `full`: `'Vafurlogi'` → `'LOC_FN_OOOSEVCWispVari180'`; `modl`: `'OOOSE\\Creatures\\VCVafurlogi\\skeleton180m000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispHiggs000` (FormID `021A58`) — "LOC_FN_OOOSEVCWispHiggs000" — `full`: `'Higgs'` → `'LOC_FN_OOOSEVCWispHiggs000'`; `modl`: `'OOOSE\\Creatures\\VCHiggs\\skeletonm000s000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispBloodCloud` (FormID `02512C`) — "LOC_FN_OOOSEVCWispBloodCloud" — `full`: `'Blood Cloud'` → `'LOC_FN_OOOSEVCWispBloodCloud'`; `modl`: `'OOOSE\\Creatures\\VCBloodCloud\\skeleton.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispEidolon000` (FormID `0280FC`) — "LOC_FN_OOOSEVCWispEidolon000" — `full`: `'Eidolon'` → `'LOC_FN_OOOSEVCWispEidolon000'`; `modl`: `'OOOSE\\Creatures\\VCEidolon\\skeleton000p000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispSGod000` (FormID `028103`) — "LOC_FN_OOOSEVCWispSGod000" — `full`: `'Small God'` → `'LOC_FN_OOOSEVCWispSGod000'`; `modl`: `'OOOSE\\Creatures\\VCSmallGod\\skeleton000a000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispHiggs144` (FormID `02BF39`) — "LOC_FN_OOOSEVCWispHiggs144" — `full`: `'Higgs'` → `'LOC_FN_OOOSEVCWispHiggs144'`; `modl`: `'OOOSE\\Creatures\\VCHiggs\\skeletonm144s000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispHiggs288` (FormID `02BFD9`) — "LOC_FN_OOOSEVCWispHiggs288" — `full`: `'Higgs'` → `'LOC_FN_OOOSEVCWispHiggs288'`; `modl`: `'OOOSE\\Creatures\\VCHiggs\\skeletonm288s000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispEidolon144` (FormID `02DC15`) — "LOC_FN_OOOSEVCWispEidolon144" — `full`: `'Eidolon'` → `'LOC_FN_OOOSEVCWispEidolon144'`; `modl`: `'OOOSE\\Creatures\\VCEidolon\\skeleton144p000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispEidolon288` (FormID `02DCB5`) — "LOC_FN_OOOSEVCWispEidolon288" — `full`: `'Eidolon'` → `'LOC_FN_OOOSEVCWispEidolon288'`; `modl`: `'OOOSE\\Creatures\\VCEidolon\\skeleton288p000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispSGod144` (FormID `02F21D`) — "LOC_FN_OOOSEVCWispSGod144" — `full`: `'Small God'` → `'LOC_FN_OOOSEVCWispSGod144'`; `modl`: `'OOOSE\\Creatures\\VCSmallGod\\skeleton144a000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispSGod288` (FormID `02F2BD`) — "LOC_FN_OOOSEVCWispSGod288" — `full`: `'Small God'` → `'LOC_FN_OOOSEVCWispSGod288'`; `modl`: `'OOOSE\\Creatures\\VCSmallGod\\skeleton288a000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispVari270` (FormID `0300DB`) — "LOC_FN_OOOSEVCWispVari270" — `full`: `'Vafurlogi'` → `'LOC_FN_OOOSEVCWispVari270'`; `modl`: `'OOOSE\\Creatures\\VCVafurlogi\\skeleton270m000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispBale` (FormID `033902`) — "LOC_FN_OOOSEVCWispBale" — `full`: `'Baleful Spirit'` → `'LOC_FN_OOOSEVCWispBale'`; `modl`: `'OOOSE\\Creatures\\VCChiindi\\skeleton.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispEidolonTemplate` (FormID `0915D5`) — "LOC_FN_OOOSEVCWispEidolonTemplate" — `full`: `'Eidolon'` → `'LOC_FN_OOOSEVCWispEidolonTemplate'`; `modl`: `'OOOSE\\Creatures\\VCEidolon\\skeleton000p000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispReg144` (FormID `091D66`) — "LOC_FN_OOOSEVCWispReg144" — `full`: `'Will-o-the-Wisp'` → `'LOC_FN_OOOSEVCWispReg144'`; `modl`: `'Creatures\\willothewisp\\OOOSEskelm144g000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispReg288` (FormID `091D70`) — "LOC_FN_OOOSEVCWispReg288" — `full`: `'Will-o-the-Wisp'` → `'LOC_FN_OOOSEVCWispReg288'`; `modl`: `'Creatures\\willothewisp\\OOOSEskelm288g000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispMidi000` (FormID `095DE7`) — "LOC_FN_OOOSEVCWispMidi000" — `full`: `'Vatte-lys'` → `'LOC_FN_OOOSEVCWispMidi000'`; `modl`: `'OOOSE\\Creatures\\VCVatteLys\\skeleton000.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`
- `OOOSEVCWispMidi300` (FormID `09E758`) — "LOC_FN_OOOSEVCWispMidi300" — `full`: `'Vatte-lys'` → `'LOC_FN_OOOSEVCWispMidi300'`; `modl`: `'OOOSE\\Creatures\\VCVatteLys\\skeleton300.nif'` → `'Creatures\\WillOTheWisp\\skeleton.nif'`

_…1 more changed omitted (see JSON for full list)_

### Leveled Creature List (LVLC) — +0 -0 ~16

**Changed:**

- `SELL2WildernessMania100` (FormID `03B7FE`) — - entry: level 19 × 1 → `00DDBF`
- `SELL2WaterMania100` (FormID `03B802`) — + entry: level 1 × 1 → `033FD8`; + entry: level 10 × 1 → `033FD8`; + entry: level 19 × 1 → `033FD8`
- `SELL2NaturalManiaLvl100` (FormID `03B803`) — + entry: level 1 × 1 → `0287DD`; + entry: level 12 × 1 → `0287DD`; + entry: level 16 × 1 → `0287DE`; + entry: level 24 × 1 → `008035`
- `SELL2NaturalMania100` (FormID `03B805`) — + entry: level 1 × 1 → `033FD8`; + entry: level 10 × 1 → `033FD8`; + entry: level 18 × 1 → `033FD8`; + entry: level 19 × 2 → `033FD8`; + entry: level 25 × 1 → `008035`
- `SELL2ShorelineMania100` (FormID `03BAA4`) — + entry: level 1 × 1 → `033FD8`; + entry: level 10 × 1 → `033FD8`; + entry: level 19 × 1 → `033FD8`
- `OOOSELL2WaterMania100Pack` (FormID `005AAE`) — + entry: level 10 × 1 → `0D868D`; + entry: level 19 × 1 → `0D868D`
- `OOOSELL2WaterDementia100Pack` (FormID `005AB0`) — + entry: level 10 × 1 → `0D868A`; + entry: level 19 × 1 → `0D868A`
- `OOOSELL2ShorelineMania100Pack` (FormID `005AB1`) — + entry: level 1 × 1 → `0D868D`
- `OOOSELL2ShorelineDementia100Pack` (FormID `005AB2`) — + entry: level 1 × 1 → `0D868A`
- `OOOSELL2ShorelineDementia100Special` (FormID `005AB3`) — + entry: level 13 × 1 → `00F4BB`; + entry: level 22 × 1 → `021A62`
- `OOOSELL2ShorelineMania100Special` (FormID `005AB4`) — + entry: level 13 × 1 → `0287DE`; + entry: level 22 × 1 → `008035`
- `OOOSELL2WildernessMania100Pack` (FormID `005ABD`) — + entry: level 1 × 1 → `0D868D`
- `OOOSELL2NaturalDementia100Pack` (FormID `006867`) — + entry: level 1 × 1 → `0D868A`
- `OOOSELL2NaturalDementia100Special` (FormID `016192`) — + entry: level 13 × 1 → `00F4BB`; + entry: level 19 × 1 → `021A62`
- `OOOSELL2NaturalMania100Special` (FormID `016193`) — + entry: level 13 × 1 → `0287DE`; + entry: level 19 × 1 → `008035`; + entry: level 27 × 2 → `008035`
- `OOOSELL2NaturalMania100Pack` (FormID `017CE9`) — + entry: level 1 × 1 → `0D868D`

### Script (SCPT) — +0 -1 ~0

**Removed:**

- `OOOSlaverGuarMountScript` (FormID `02EFD5`)

