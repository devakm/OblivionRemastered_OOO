# alpha50 — release notes

_Compared against `alpha49`._

## File-level changes

- Added: 0
- Removed: 0
- Changed: 6

### Changed

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_BOOK.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CELLMAP.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_CREA.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ENCH.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_QUST.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Creature (CREA) — +0 -0 ~1

**Changed:**

- `DeadSkeletonSpecialOOODreadSetHelmet` (FormID `04D52F`) — "LOC_FN_DeadSkeletonSpecialOOODreadSetHelmet" — `full`: `'Skeleton'` → `'LOC_FN_DeadSkeletonSpecialOOODreadSetHelmet'`

### Light (LIGH) — +0 -0 ~2

**Changed:**

- `torch04` (FormID `003DEB`) — "LOC_FN_Torch02" — `full`: `'Torch'` → `'LOC_FN_Torch02'`
- `Torch03` (FormID `051331`) — "LOC_FN_Torch02" — `full`: `'Torch'` → `'LOC_FN_Torch02'`

### Leveled Creature List (LVLC) — +0 -0 ~9

**Changed:**

- `LL1WildernessRainforest` (FormID `0343D9`) — + entry: level 9 × 1 → `0343C9`; + entry: level 16 × 1 → `0094B9`; - entry: level 13 × 1 → `0317CF`; - entry: level 17 × 1 → `0094B9`
- `LL1WildernessSwamp` (FormID `0343DA`) — + entry: level 1 × 1 → `026C05`; + entry: level 10 × 1 → `01E64A`; + entry: level 13 × 1 → `008A63`; + entry: level 13 × 1 → `008F64`; + entry: level 13 × 1 → `0094B9`; - entry: level 3 × 1 → `0317CF`; - entry: level 11 × 1 → `01E64A`; - entry: level 12 × 1 → `0317CF`; - entry: level 14 × 1 → `008A63`; - entry: level 15 × 1 → `008F64`
- `LL0LandDreugh100` (FormID `0094B9`) — + entry: level 1 × 1 → `0084FA`; + entry: level 1 × 1 → `0084FB`; + entry: level 1 × 1 → `0084FC`
- `LL1OgreBog25Low` (FormID `0099AC`) — - entry: level 1 × 1 → `0317CF`
- `LL1LionLeopard25Low` (FormID `00B443`) — - entry: level 1 × 1 → `0317CF`
- `LL1WildernessVvardenfellFrontierOOO` (FormID `0430CA`) — + entry: level 15 × 1 → `008F6A`; + entry: level 15 × 1 → `0094B9`; - entry: level 1 × 1 → `0430CB`; - entry: level 3 × 1 → `0430CC`; - entry: level 9 × 1 → `0430CC`; - entry: level 12 × 1 → `0430CC`; - entry: level 15 × 1 → `0430CC`; - entry: level 17 × 1 → `008F6A`; - entry: level 17 × 1 → `0094B9`; - entry: level 17 × 1 → `0430CC`
- `LL1GuarMixedFrontier100` (FormID `0430CC`) — - entry: level 1 × 1 → `0317CE`; - entry: level 1 × 1 → `0430CB`; - entry: level 1 × 2 → `0430CB`; - entry: level 1 × 3 → `0430CB`
- `LL1WildernessVvardenfellFrontierDryOOO` (FormID `0430DA`) — - entry: level 1 × 1 → `0430CB`; - entry: level 3 × 1 → `0430CC`; - entry: level 6 × 1 → `0430CC`; - entry: level 9 × 1 → `0430CB`; - entry: level 9 × 1 → `0430CC`; - entry: level 12 × 1 → `0430CC`; - entry: level 13 × 1 → `0430CB`; - entry: level 15 × 1 → `0430CC`; - entry: level 16 × 1 → `0430CC`
- `LL1WildernessVvardenfellFrontierDryOOO40` (FormID `0430F4`) — - entry: level 1 × 1 → `0430CB`; - entry: level 6 × 1 → `0430CC`; - entry: level 9 × 1 → `0430CB`; - entry: level 9 × 1 → `0430CC`; - entry: level 12 × 1 → `0430CC`; - entry: level 13 × 1 → `0430CB`; - entry: level 15 × 1 → `0430CC`; - entry: level 16 × 1 → `0430CC`

### Leveled Item List (LVLI) — +0 -0 ~16

**Changed:**

- `OOOViIngBearMeat` (FormID `000814`) — + entry: level 1 × 1 → `03266F`
- `OOOViIngBlackPearlDust` (FormID `005E7B`) — + entry: level 1 × 1 → `006C7B`
- `OOOViIngCopperDust` (FormID `005E7F`) — + entry: level 1 × 1 → `006C8B`
- `OOOViIngAmethystDust` (FormID `005E86`) — + entry: level 1 × 1 → `006C7E`
- `OOOViIngDiamondDust` (FormID `005E8D`) — + entry: level 1 × 1 → `00CC8E`
- `OOOViIngEmeraldDust` (FormID `005E8E`) — + entry: level 1 × 1 → `00CC8C`
- `OOOViIngGarnetDust` (FormID `005E8F`) — + entry: level 1 × 1 → `00615D`
- `OOOViIngGoldDust` (FormID `005E90`) — + entry: level 1 × 1 → `004D2A`
- `OOOViIngOpalDust` (FormID `005E91`) — + entry: level 1 × 1 → `006C7C`
- `OOOViIngPearlDust` (FormID `005E92`) — + entry: level 1 × 1 → `00CC92`
- `OOOViIngPlatinumDust` (FormID `005E93`) — + entry: level 1 × 1 → `006C8C`
- `OOOViIngRubyDust` (FormID `005E94`) — + entry: level 1 × 1 → `00CC90`
- `OOOViIngSapphireDust` (FormID `005E95`) — + entry: level 1 × 1 → `00CC8A`
- `OOOViIngSilverDust` (FormID `005E96`) — + entry: level 1 × 1 → `00CC87`
- `OOOViIngTopazDust` (FormID `005E97`) — + entry: level 1 × 1 → `00CC88`
- `OOOViIngTourmalineDust` (FormID `005E98`) — + entry: level 1 × 1 → `00615E`

