# alpha30 — release notes

_Compared against `alpha29`._

## File-level changes

- Added: 1
- Removed: 0
- Changed: 4

### Added

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_SLGM.json`

### Changed

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_FACT.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_NPC_.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Cell (CELL) — +175 -0 ~1

**Added:**

- `ChorrolCastaScriboniasHouse` (FormID `000828`) — "LOC_FN_ChorrolCastaScriboniasHouse"
- `AnvilMagesGuildLibrary` (FormID `0097B6`) — "LOC_FN_AnvilMagesGuildLibrary"
- `HornCave` (FormID `01499A`) — "LOC_FN_HornCave"
- `BramblepointCave` (FormID `0149A4`) — "Bramblepoint Cave"
- `WindCave` (FormID `0149A5`) — "LOC_FN_WindCave"
- `NewtCave` (FormID `0149AE`) — "LOC_FN_NewtCave"
- `CrayfishCave` (FormID `0149AF`) — "LOC_FN_CrayfishCave"
- `SerpentHollowCave` (FormID `0149B8`) — "LOC_FN_SerpentHollowCave"
- `ExhaustedMine` (FormID `015C32`) — "LOC_FN_ExhaustedMine"
- `FortHastrel01` (FormID `015E1C`) — "LOC_FN_FortHastrel01"
- `FortNomore` (FormID `015E26`) — "LOC_FN_FortNomore"
- `FortAurus` (FormID `015E30`) — "LOC_FN_FortAurus"
- `FortAlessia` (FormID `015E3A`) — "LOC_FN_FortAlessia"
- `Veyond04` (FormID `015F85`) — "Veyond Gandrasel"
- `Bawn` (FormID `016628`) — "LOC_FN_Bawn"
- `HrotandaVale` (FormID `016629`) — "LOC_FN_HrotandaVale"
- `Varondo` (FormID `016632`) — "LOC_FN_Varondo"
- `Ondo` (FormID `016633`) — "LOC_FN_Ondo"
- `Fanacasecul` (FormID `01663C`) — "LOC_FN_Fanacasecul"
- `Piukanda` (FormID `01663D`) — "LOC_FN_Piukanda"

_…155 more added omitted (see JSON for full list)_

**Changed:**

- `AnvilCastlePrivateQuarters` (FormID `007966`) — "LOC_FN_AnvilCastlePrivateQuarters" — `full`: `'Castle Anvil Private Quarters'` → `'LOC_FN_AnvilCastlePrivateQuarters'`

### Class (CLAS) — +0 -0 ~24

**Changed:**

- `ValenWarrior` (FormID `00491C`) — "LOC_FN_ValenWarrior" — `full`: `'Sylvan Warsmer'` → `'LOC_FN_ValenWarrior'`
- `ValenArcher` (FormID `00491D`) — "LOC_FN_ValenArcher" — `full`: `'Sylvan Archermer'` → `'LOC_FN_ValenArcher'`
- `ValenWizard` (FormID `00491E`) — "LOC_FN_ValenWizard" — `full`: `'Sylvan Sorcerermer'` → `'LOC_FN_ValenWizard'`
- `OscuroUOPMQ11Allies` (FormID `005D77`) — "LOC_FN_OscuroUOPMQ11Allies" — `full`: `'MQ11 Allies'` → `'LOC_FN_OscuroUOPMQ11Allies'`
- `BanditWizardBlunt` (FormID `005DFF`) — "LOC_FN_BanditWizardBlunt" — `full`: `'Hedge Wizard'` → `'LOC_FN_BanditWizardBlunt'`
- `KnightDragonborn` (FormID `005E01`) — "LOC_FN_KnightDragonborn" — `full`: `'Dragonborn Knight'` → `'LOC_FN_KnightDragonborn'`
- `SlaveTraderHeavy` (FormID `007062`) — "LOC_FN_SlaveTraderHeavy" — `full`: `'Slave Trader Thug'` → `'LOC_FN_SlaveTraderHeavy'`
- `SlaveTraderLight` (FormID `007063`) — "LOC_FN_SlaveTraderLight" — `full`: `'Slave Trader Hunter'` → `'LOC_FN_SlaveTraderLight'`
- `ArgonianBMSFighter` (FormID `00722A`) — "LOC_FN_ArgonianBMSFighter" — `full`: `'Black Marsh Fighter'` → `'LOC_FN_ArgonianBMSFighter'`
- `ArgonianBMSShaman` (FormID `00722B`) — "LOC_FN_ArgonianBMSShaman" — `full`: `'Black Marsh Shaman'` → `'LOC_FN_ArgonianBMSShaman'`
- `ArgonianBMSSmuggler` (FormID `00722C`) — "LOC_FN_ArgonianBMSSmuggler" — `full`: `'Black Marsh Smuggler'` → `'LOC_FN_ArgonianBMSSmuggler'`
- `ValenZGoodProtector` (FormID `0077AD`) — "LOC_FN_ValenZGoodProtector" — `full`: `'Bosmer Protector'` → `'LOC_FN_ValenZGoodProtector'`
- `ValenZGoodRanger` (FormID `0077AE`) — "LOC_FN_ValenZGoodRanger" — `full`: `'Bosmer Ranger'` → `'LOC_FN_ValenZGoodRanger'`
- `JanusMageClass` (FormID `00EC2F`) — "LOC_FN_JanusMageClass" — `full`: `'Janus Mage Class'` → `'LOC_FN_JanusMageClass'`
- `SlaveTraderChief` (FormID `01CA7B`) — "LOC_FN_SlaveTraderChief" — `full`: `'Slave Trader Chief'` → `'LOC_FN_SlaveTraderChief'`
- `OOOSE32Fanatic` (FormID `020053`) — "LOC_FN_OOOSE32Fanatic" — `full`: `'Fanatic'` → `'LOC_FN_OOOSE32Fanatic'`
- `AmazonMelee` (FormID `0303DD`) — "LOC_FN_AmazonMelee" — `full`: `'Amazon Man-Eater'` → `'LOC_FN_AmazonMelee'`
- `AmazonMissile` (FormID `0303DE`) — "LOC_FN_AmazonMissile" — `full`: `'Amazon Man-Hunter'` → `'LOC_FN_AmazonMissile'`
- `AmazonPriestess` (FormID `0303DF`) — "LOC_FN_AmazonPriestess" — `full`: `'Amazon Raging Priestess'` → `'LOC_FN_AmazonPriestess'`
- `NecromancerPutridHand` (FormID `0308C6`) — "LOC_FN_NecromancerPutridHand" — `full`: `'Necromancer Putrid Hand'` → `'LOC_FN_NecromancerPutridHand'`

_…4 more changed omitted (see JSON for full list)_

### Faction (FACT) — +0 -0 ~44

**Changed:**

- `AmazonFaction` (FormID `00491B`) — "LOC_FN_AmazonFaction" — `full`: `'Amazons'` → `'LOC_FN_AmazonFaction'`
- `ValenBosmer` (FormID `004E16`) — "LOC_FN_ValenBosmer" — `full`: `'ValenWood Bosmer'` → `'LOC_FN_ValenBosmer'`
- `OscuroUOPHackdirtVillagers` (FormID `005D78`) — "LOC_FN_OscuroUOPHackdirtVillagers" — `full`: `'UOP-added Hackdirt Villagers (non-Brethren)'` → `'LOC_FN_OscuroUOPHackdirtVillagers'`
- `SlaveTraderFaction` (FormID `007064`) — "LOC_FN_SlaveTraderFaction" — `full`: `'Slave Traders'` → `'LOC_FN_SlaveTraderFaction'`
- `ArgonianBlackMarshFaction` (FormID `00722E`) — "LOC_FN_ArgonianBlackMarshFaction" — `full`: `'Black Marsh Smuggler Faction'` → `'LOC_FN_ArgonianBlackMarshFaction'`
- `ValenBosmerGood` (FormID `00779E`) — "LOC_FN_ValenBosmerGood" — `full`: `'Bosmer Protectors'` → `'LOC_FN_ValenBosmerGood'`
- `zzOOODragonborneKnights` (FormID `00831F`) — "LOC_FN_zzOOODragonborneKnights" — `full`: `'Knights of the Dragonborne'` → `'LOC_FN_zzOOODragonborneKnights'`
- `ZOOOBears` (FormID `00CD9C`) — "LOC_FN_ZOOOBears" — `full`: `'Yogi Faction'` → `'LOC_FN_ZOOOBears'`
- `ZOOOBoars` (FormID `00CD9D`) — "LOC_FN_ZOOOBoars" — `full`: `'Cochino Faction'` → `'LOC_FN_ZOOOBoars'`
- `ZOOODeers` (FormID `00CD9E`) — "LOC_FN_ZOOODeers" — `full`: `'Bambi Faction'` → `'LOC_FN_ZOOODeers'`
- `ZOOOCougars` (FormID `00CD9F`) — "LOC_FN_ZOOOCougars" — `full`: `'Puma Faction'` → `'LOC_FN_ZOOOCougars'`
- `ZOOOMinotaurs` (FormID `00CDA0`) — "LOC_FN_ZOOOMinotaurs" — `full`: `'King Minos Faction'` → `'LOC_FN_ZOOOMinotaurs'`
- `ZOOOOgres` (FormID `00CDA1`) — "LOC_FN_ZOOOOgres" — `full`: `'Ann Coulter Faction'` → `'LOC_FN_ZOOOOgres'`
- `ZOOOSpriggan` (FormID `00CDA2`) — "LOC_FN_ZOOOSpriggan" — `full`: `'Eeeeeeeennt Faction'` → `'LOC_FN_ZOOOSpriggan'`
- `ZOOOSlaughterfish` (FormID `00CDA3`) — "LOC_FN_ZOOOSlaughterfish" — `full`: `'Jaws Faction'` → `'LOC_FN_ZOOOSlaughterfish'`
- `ZOOORats` (FormID `00CDA4`) — "LOC_FN_ZOOORats" — `full`: `"Micky's Faction"` → `'LOC_FN_ZOOORats'`
- `ZOOOWillowisps` (FormID `00CDA5`) — "LOC_FN_ZOOOWillowisps" — `full`: `'Greater Lightstone Faction'` → `'LOC_FN_ZOOOWillowisps'`
- `ZOOOSheep` (FormID `00CDA6`) — "LOC_FN_ZOOOSheep" — `full`: `"Hill-Billies' Consolation Faction"` → `'LOC_FN_ZOOOSheep'`
- `ZOOOMudcrabs` (FormID `00CDA7`) — "LOC_FN_ZOOOMudcrabs" — `full`: `'STD Scare Faction'` → `'LOC_FN_ZOOOMudcrabs'`
- `ZOOOWolves` (FormID `00CDA8`) — "LOC_FN_ZOOOWolves" — `full`: `"Kevin's Faction"` → `'LOC_FN_ZOOOWolves'`

_…24 more changed omitted (see JSON for full list)_

### Leveled Spell List (LVSP) — +0 -0 ~5

**Changed:**

- `LL2ArgonianBlackMarsh100` (FormID `007786`) — + entry: level 1 × 1 → `007755`; + entry: level 1 × 1 → `007756`; + entry: level 1 × 1 → `007758`; + entry: level 1 × 1 → `00775A`; + entry: level 1 × 1 → `00775C`; + entry: level 1 × 1 → `00775E`; + entry: level 1 × 1 → `007760`; + entry: level 1 × 1 → `007762`; + entry: level 1 × 1 → `007764`; + entry: level 1 × 1 → `007766`; + entry: level 1 × 1 → `007768`; + entry: level 1 × 1 → `00776A`; + entry: level 1 × 1 → `00776C`; + entry: level 1 × 1 → `00776E`; + entry: level 1 × 1 → `007770`; + entry: level 1 × 1 → `007772`; + entry: level 1 × 1 → `007774`; + entry: level 1 × 1 → `007776`; + entry: level 1 × 1 → `007778`; + entry: level 1 × 1 → `00777A`; + entry: level 1 × 1 → `00777C`; + entry: level 1 × 1 → `00777E`; + entry: level 1 × 1 → `007780`; + entry: level 1 × 1 → `007782`; + entry: level 1 × 1 → `007784`; - entry: level 1 × 1 → `0A936D`
- `LL2CreatureImpCrazed100` (FormID `02F4FE`) — + entry: level 1 × 1 → `028D59`; + entry: level 1 × 1 → `028D5F`; + entry: level 1 × 1 → `02F9EA`; + entry: level 1 × 1 → `02F9EB`
- `LL2CreatureImpMystical100` (FormID `02F500`) — + entry: level 1 × 1 → `028D5B`; + entry: level 1 × 1 → `028D5D`; + entry: level 1 × 1 → `028D61`; + entry: level 1 × 1 → `02F9ED`; + entry: level 1 × 1 → `02F9EF`; + entry: level 1 × 1 → `02F9F1`; + entry: level 1 × 1 → `02F9F3`; - entry: level 1 × 1 → `0A97A9`
- `LL2AmazonLvl100` (FormID `03BFDF`) — + entry: level 1 × 1 → `03BFCD`; + entry: level 1 × 1 → `03BFCF`; + entry: level 1 × 1 → `03BFD1`; + entry: level 1 × 1 → `03BFD3`; + entry: level 1 × 1 → `03BFD5`; + entry: level 1 × 1 → `03BFD7`; + entry: level 1 × 1 → `03BFD9`; + entry: level 1 × 1 → `03BFDB`; + entry: level 1 × 1 → `03BFDD`; + entry: level 1 × 1 → `03D414`; + entry: level 1 × 1 → `03D416`; + entry: level 1 × 1 → `03D418`; + entry: level 1 × 1 → `03D41A`; + entry: level 1 × 1 → `03E2E5`; + entry: level 1 × 1 → `03E2E6`; + entry: level 1 × 1 → `03E2E8`; + entry: level 1 × 1 → `03E2EA`; + entry: level 1 × 1 → `03E2EC`; + entry: level 1 × 1 → `03E2EE`; + entry: level 1 × 1 → `03E2F0`; + entry: level 1 × 1 → `03E2F2`; + entry: level 1 × 1 → `03E2F4`; + entry: level 1 × 1 → `03E2F6`; + entry: level 1 × 1 → `03E2F8`; + entry: level 1 × 1 → `03E2FA`; + entry: level 1 × 1 → `03E2FC`; + entry: level 1 × 1 → `03E2FE`; + entry: level 1 × 1 → `03E306`; + entry: level 1 × 1 → `03E310`; - entry: level 1 × 1 → `03C3FB`
- `LL2OblivionGuardianLvl100` (FormID `03CF10`) — + entry: level 1 × 1 → `00DA57`; + entry: level 1 × 1 → `00DA58`; + entry: level 1 × 1 → `00DA5A`; + entry: level 1 × 1 → `00DA5C`; + entry: level 1 × 1 → `00DA5E`

### NPC (NPC_) — +0 -6 ~33

**Removed:**

- `ConjurerXGuardianBossFemaleBreton` (FormID `00DDF6`) — "LOC_FN_ConjurerXGuardianBossFemaleBreton"
- `ConjurerXGuardianBossFemaleBreton2` (FormID `00DDF7`) — "LOC_FN_ConjurerXGuardianBossFemaleBreton2"
- `ConjurerXGuardianBossFemaleBreton3` (FormID `00DDF8`) — "LOC_FN_ConjurerXGuardianBossFemaleBreton3"
- `ConjurerXGuardianBossFemaleHighElf` (FormID `00DDF9`) — "LOC_FN_ConjurerXGuardianBossFemaleHighElf"
- `ConjurerXGuardianBossFemaleHighElf2` (FormID `00DDFA`) — "LOC_FN_ConjurerXGuardianBossFemaleHighElf2"
- `ConjurerXGuardianBossFemaleHighElf3` (FormID `00DDFB`) — "LOC_FN_ConjurerXGuardianBossFemaleHighElf3"

**Changed:**

- `BanditAmazonWizardFemale4A` (FormID `022F99`) — "LOC_FN_BanditAmazonWizardFemale4A" — `full`: `'Amazon Raging Priestess'` → `'LOC_FN_BanditAmazonWizardFemale4A'`
- `BanditAmazonWizardFemale3A` (FormID `022F9A`) — "LOC_FN_BanditAmazonWizardFemale3A" — `full`: `'Amazon Raging Priestess'` → `'LOC_FN_BanditAmazonWizardFemale3A'`
- `BanditAmazonMissileFemale4B` (FormID `022F9B`) — "LOC_FN_BanditAmazonMissileFemale4B" — `full`: `'Amazon Man-Hunter'` → `'LOC_FN_BanditAmazonMissileFemale4B'`
- `BanditAmazonMissileFemale4A` (FormID `022F9C`) — "LOC_FN_BanditAmazonMissileFemale4A" — `full`: `'Amazon Man-Hunter'` → `'LOC_FN_BanditAmazonMissileFemale4A'`
- `BanditAmazonMissileFemale3B` (FormID `022F9D`) — "LOC_FN_BanditAmazonMissileFemale3B" — `full`: `'Amazon Man-Hunter'` → `'LOC_FN_BanditAmazonMissileFemale3B'`
- `BanditAmazonMissileFemale3A` (FormID `022F9E`) — "LOC_FN_BanditAmazonMissileFemale3A" — `full`: `'Amazon Man-Hunter'` → `'LOC_FN_BanditAmazonMissileFemale3A'`
- `BanditAmazonMissileFemale2` (FormID `022F9F`) — "LOC_FN_BanditAmazonMissileFemale2" — `full`: `'Amazon Man-Hunter'` → `'LOC_FN_BanditAmazonMissileFemale2'`
- `BanditAmazonMeleeFemale4B` (FormID `022FA0`) — "LOC_FN_BanditAmazonMeleeFemale4B" — `full`: `'Amazon Man-Eater'` → `'LOC_FN_BanditAmazonMeleeFemale4B'`
- `BanditAmazonMeleeFemale4A` (FormID `022FA1`) — "LOC_FN_BanditAmazonMeleeFemale4A" — `full`: `'Amazon Man-Eater'` → `'LOC_FN_BanditAmazonMeleeFemale4A'`
- `BanditAmazonMeleeFemale3B` (FormID `022FA2`) — "LOC_FN_BanditAmazonMeleeFemale3B" — `full`: `'Amazon Man-Eater'` → `'LOC_FN_BanditAmazonMeleeFemale3B'`
- `BanditAmazonMeleeFemale3A` (FormID `022FA3`) — "LOC_FN_BanditAmazonMeleeFemale3A" — `full`: `'Amazon Man-Eater'` → `'LOC_FN_BanditAmazonMeleeFemale3A'`
- `BanditAmazonMeleeFemale2` (FormID `022FA4`) — "LOC_FN_BanditAmazonMeleeFemale2" — `full`: `'Amazon Man-Eater'` → `'LOC_FN_BanditAmazonMeleeFemale2'`
- `BanditAmazonBossFemale3` (FormID `022FA5`) — "LOC_FN_BanditAmazonBossFemale3" — `full`: `'Amazon Wise Mother'` → `'LOC_FN_BanditAmazonBossFemale3'`
- `BanditAmazonBossFemale2` (FormID `022FA6`) — "LOC_FN_BanditAmazonBossFemale2" — `full`: `'Amazon Wise Mother'` → `'LOC_FN_BanditAmazonBossFemale2'`
- `BanditAmazonBossFemale1` (FormID `022FA7`) — "LOC_FN_BanditAmazonBossFemale1" — `full`: `'Amazon Wise Mother'` → `'LOC_FN_BanditAmazonBossFemale1'`
- `BanditAmazonBigBoss` (FormID `022FA8`) — "LOC_FN_BanditAmazonBigBoss" — `full`: `'Voice of Nature'` → `'LOC_FN_BanditAmazonBigBoss'`
- `BanditAmazonWizardFemale5A` (FormID `022FA9`) — "LOC_FN_BanditAmazonWizardFemale5A" — `full`: `'Amazon Raging Priestess'` → `'LOC_FN_BanditAmazonWizardFemale5A'`
- `BanditAmazonMeleeFemaleA` (FormID `029C79`) — "LOC_FN_BanditAmazonMeleeFemaleA" — `full`: `'Amazon Man-Eater'` → `'LOC_FN_BanditAmazonMeleeFemaleA'`
- `BanditAmazonMeleeFemaleAb` (FormID `029C7A`) — "LOC_FN_BanditAmazonMeleeFemaleAb" — `full`: `'Amazon Man-Eater'` → `'LOC_FN_BanditAmazonMeleeFemaleAb'`
- `BanditAmazonMeleeFemaleAc` (FormID `029C7B`) — "LOC_FN_BanditAmazonMeleeFemaleAc" — `full`: `'Amazon Man-Eater'` → `'LOC_FN_BanditAmazonMeleeFemaleAc'`

_…13 more changed omitted (see JSON for full list)_

### Soul Gem (SLGM) — +0 -0 ~3

**Changed:**

- `TandCommonOOO` (FormID `048A3E`) — "LOC_FN_TandCommonOOO" — `full`: `''` → `'LOC_FN_TandCommonOOO'`; `modl`: `'clutter\\StarBoiSoulGems\\SoulgemCommonEmpty.nif'` → `'Clutter\\SoulGemLesser01.NIF'`
- `TandLesserOOO` (FormID `048A3F`) — "LOC_FN_TandLesserOOO" — `full`: `''` → `'LOC_FN_TandLesserOOO'`; `modl`: `'clutter\\StarBoiSoulGems\\SoulgemLesserEmpty.nif'` → `'Clutter\\SoulGemLesser01.NIF'`
- `TandPettyOOO` (FormID `048A40`) — "LOC_FN_TandPettyOOO" — `full`: `''` → `'LOC_FN_TandPettyOOO'`; `modl`: `'clutter\\StarBoiSoulGems\\SoulgemPettyEmpty.nif'` → `'Clutter\\SoulGemPetty01.NIF'`

