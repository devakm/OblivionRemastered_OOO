# alpha09 — release notes

_Compared against `alpha08`._

## File-level changes

- Added: 16
- Removed: 2
- Changed: 4

### Added

- `Content/Dev/ObvData/Data/OOO_NewArmor.esp`
- `Content/Dev/ObvData/Data/OOO_NewArmor03.esp`
- `Content/Dev/ObvData/Data/OOO_NewArmorComps.esp`
- `Content/Dev/ObvData/Data/OOO_NewArmorOdds.esp`
- `Content/Dev/ObvData/Data/OOO_NewChestComps.esp`
- `Content/Dev/ObvData/Data/OOO_NewChests.esp`
- `Content/Dev/ObvData/Data/OOO_NewCreatureComps.esp`
- `Content/Dev/ObvData/Data/OOO_NewCreatures01.esp`
- `Content/Dev/ObvData/Data/OOO_NewCreatures02.esp`
- `Content/Dev/ObvData/Data/OOO_NewCreatures04Special.esp`
- `Content/Dev/ObvData/Data/OOO_NewMiscItems.esp`
- `Content/Dev/ObvData/Data/OOO_NewNPCs04Special.esp`
- `Content/Dev/ObvData/Data/OOO_NewRobesComp.esp`
- `Content/Dev/ObvData/Data/OOO_NewWeaponComps.esp`
- `Content/Dev/ObvData/Data/OOO_NewWeapons01.esp`
- `Content/Dev/ObvData/Data/OOO_NewWeapons03.esp`

### Removed

- `Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp.save.2025_07_01_19_43_28`
- `Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp.save.2025_07_01_20_01_19`

### Changed

- `Content/Dev/ObvData/Data/OOO_NewChests03.esp`
- `Content/Dev/ObvData/Data/OOO_NewCreatures03.esp`
- `Content/Dev/ObvData/Data/OOO_NewNPCs03.esp`
- `Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`

## ESP changes — `OOO_GameSettings.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewArmor.esp`

_Initial inventory (no prior version to compare against)._

- **Armor (ARMO):** 298 records

## ESP changes — `OOO_NewArmor03.esp`

_Initial inventory (no prior version to compare against)._

- **Armor (ARMO):** 185 records

## ESP changes — `OOO_NewArmorComps.esp`

_Initial inventory (no prior version to compare against)._

- **Armor (ARMO):** 109 records
- **Clothing (CLOT):** 1 records

## ESP changes — `OOO_NewArmorOdds.esp`

_Initial inventory (no prior version to compare against)._

- **Armor (ARMO):** 36 records

## ESP changes — `OOO_NewChestComps.esp`

_Initial inventory (no prior version to compare against)._

- **Container (CONT):** 12 records

## ESP changes — `OOO_NewChests.esp`

_Initial inventory (no prior version to compare against)._

- **Container (CONT):** 7 records
- **Misc Item (MISC):** 1 records

## ESP changes — `OOO_NewChests03.esp`

### Container (CONT) — +0 -12 ~34

**Removed:**

- `ChestVendorPawnbrokerLow01` (FormID `0244B1`) — "LOC_FN_ChestVendorPawnbrokerLow01"
- `ChestVendorPawnbrokerLow02` (FormID `0244B2`) — "LOC_FN_ChestVendorPawnbrokerLow02"
- `DungBanditChest03` (FormID `03752C`) — "LOC_FN_DungBanditChest03"
- `DungBanditChest04Healing` (FormID `03752D`) — "LOC_FN_DungBanditChest04Healing"
- `DungBanditBossChest01` (FormID `03752E`) — "LOC_FN_DungBanditBossChest01"
- `DungMarauderBossChestAlyied01` (FormID `037538`) — "LOC_FN_DungMarauderBossChestAlyied01"
- `DungMarauderBossChestAlyied02` (FormID `037539`) — "LOC_FN_DungMarauderBossChestAlyied02"
- `DungNecroChestAlyied01` (FormID `037541`) — "LOC_FN_DungNecroChestAlyied01"
- `ChestJewelryNoble01` (FormID `064F55`) — "LOC_FN_ChestJewelryNoble01"
- `DungTombCoffin01Empty` (FormID `06AB40`) — "Coffin"
- `ChestHouseTreasuryLower01` (FormID `0A496A`) — "Chest"
- `ChestHouseTreasuryLower02` (FormID `0A496B`) — "Chest"

**Changed:**

- `DungOblivionBossClawExt02OOO` (FormID `01CC49`) — "Fleshy Pod" — `modl`: `'harvest\\containers\\XMSClawFleshContainer01.nif'` → `'Oblivion\\Clutter\\Containers\\ClawfleshContainer.NIF'`
- `DungOblivionBossSack01OOO` (FormID `01CC4B`) — "Fleshy Pod" — `modl`: `'harvest\\containers\\XMSGroundFleshContainer02.nif'` → `'Oblivion\\Clutter\\Containers\\GroundFleshContainer02.NIF'`
- `FieldhouseCave03ChestOOO` (FormID `01CC4D`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestLowerChest02LoFi.nif'` → `'Clutter\\LowerClass\\LowerClassChest02.NIF'`
- `SQ04DungMythEnemyChest02OOO` (FormID `01CC4E`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestLowerChest02LoFi.nif'` → `'Clutter\\LowerClass\\LowerClassChest02.NIF'`
- `TG09FathisArenChestOOO` (FormID `01CC4F`) — "Fathis Aren's Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest01LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest01.NIF'`
- `TG09FathisArenChest1OOO` (FormID `01CC50`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest01LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest01.NIF'`
- `Dark13VampireChest01OOO` (FormID `01CC52`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestLowerChest01LoFi.nif'` → `'Clutter\\LowerClass\\LowerClassChest01.NIF'`
- `ChestVendorzOOOCapes` (FormID `022F5F`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOODungVampireChestMid01Treasury` (FormID `024427`) — "Studded Chest" — `modl`: `'Dungeons\\AyleidRuins\\Interior\\ARChest02.NIF'` → `'Clutter\\MiddleClass\\Middlechest02.NIF'`
- `ZOOODungVampireChestMid02ArmoryLesser` (FormID `02442C`) — "Fine Banded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOODungVampireChestMid02ArmoryLesserWiz` (FormID `02442F`) — "Rune Banded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOODungVampireChestNobleAlchemyTopT100` (FormID `024437`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOODungVampireChestNobleArmoryTop` (FormID `024445`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOODungVampireChestNobleMagicTopT100` (FormID `024448`) — "Ornate Runed Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest01LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest01.NIF'`
- `ZOOODungVampireChestNobleTreasury` (FormID `024449`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOODungVampireMidAlyied01Treasury` (FormID `02444D`) — "Ayleid Cask" — `modl`: `'harvest\\containers\\XMSharvestARChest01.nif'` → `'Dungeons\\AyleidRuins\\Interior\\ARChest01.NIF'`
- `ZOOODungVampireMidAlyied01TreasuryT100` (FormID `024451`) — "Ayleid Cask" — `modl`: `'harvest\\containers\\XMSharvestARChest01.nif'` → `'Dungeons\\AyleidRuins\\Interior\\ARChest01.NIF'`
- `ZOOODungVampireChestMid01TreasuryT100` (FormID `024452`) — "Studded Chest" — `modl`: `'Dungeons\\AyleidRuins\\Interior\\ARChest02.NIF'` → `'Clutter\\MiddleClass\\Middlechest02.NIF'`
- `ZOOODungVampireChestMid02ArmoryLesserT100` (FormID `024453`) — "Fine Banded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOODungVampireChestMid02ArmoryLesserWizT100` (FormID `024454`) — "Rune Banded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`

_…14 more changed omitted (see JSON for full list)_

### Misc Item (MISC) — +2 -0 ~0

**Added:**

- `Gold002a` (FormID `03A587`) — "Platinum Coin"
- `Gold002` (FormID `048F80`) — "Platinum Coin"

## ESP changes — `OOO_NewChests2.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatureComps.esp`

_Initial inventory (no prior version to compare against)._

- **Creature (CREA):** 14 records
- **Script (SCPT):** 1 records

## ESP changes — `OOO_NewCreatures01.esp`

_Initial inventory (no prior version to compare against)._

- **Creature (CREA):** 19 records
- **Misc Item (MISC):** 12 records

## ESP changes — `OOO_NewCreatures02.esp`

_Initial inventory (no prior version to compare against)._

- **Creature (CREA):** 1 records

## ESP changes — `OOO_NewCreatures03.esp`

**Master list changed:**

- before: ['Oblivion.esm', "Oscuro's_Oblivion_Overhaul.esp"]
- after:  ['Oblivion.esm', 'Knights.esp', "Oscuro's_Oblivion_Overhaul.esp"]

### Creature (CREA) — +197 -17 ~35

**Added:**

- `CreatureMudCrab` (FormID `000B7F`) — "Mud Crab"
- `CreatureMinotaur3` (FormID `009D6B`) — "LOC_FN_CreatureMinotaur3"
- `CreatureMinotaur4` (FormID `009D6C`) — "LOC_FN_CreatureMinotaur4"
- `CreatureMinotaur1Weapon` (FormID `009D6D`) — "LOC_FN_CreatureMinotaur1Weapon"
- `CreatureMinotaur2Weapon` (FormID `009D6E`) — "LOC_FN_CreatureMinotaur2Weapon"
- `CreatureMinotaur4Weapon` (FormID `009D6F`) — "LOC_FN_CreatureMinotaur4Weapon"
- `CreatureGoblin5Warlord` (FormID `00AB71`) — "Goblin Warlord"
- `CreatureGoblin5WarlordArcher` (FormID `00ABD1`) — "Goblin Warlord"
- `CreatureMinotaur2` (FormID `00B9ED`) — "LOC_FN_CreatureMinotaur2"
- `CreatureSheep` (FormID `0151DD`) — "LOC_FN_CreatureSheep"
- `CreatureAtronachFlame` (FormID `01E5EF`) — "LOC_FN_CreatureAtronachFlame"
- `CreatureDog` (FormID `01E5F5`) — "LOC_FN_CreatureDog"
- `CreatureMountainLion` (FormID `01E5FA`) — "Mountain Lion"
- `CreatureMinotaur3Weapon` (FormID `01E647`) — "LOC_FN_CreatureMinotaur3Weapon"
- `CreatureGoblin1` (FormID `01FCB1`) — "LOC_FN_CreatureGoblin1"
- `CreatureGoblin2Skirmisher` (FormID `01FCB2`) — "LOC_FN_CreatureGoblin2Skirmisher"
- `CreatureGoblin3Berserker` (FormID `01FCB3`) — "LOC_FN_CreatureGoblin3Berserker"
- `CreatureGoblin4Shaman` (FormID `01FCB4`) — "Goblin Shaman"
- `CreatureAtronachFrost` (FormID `01FF22`) — "LOC_FN_CreatureAtronachFrost"
- `CreatureAtronachStorm` (FormID `01FF23`) — "LOC_FN_CreatureAtronachStorm"

_…177 more added omitted (see JSON for full list)_

**Removed:**

- `CreatureOgreZ1` (FormID `0089F0`) — "Ravenous Ogre"
- `CreatureOgreZShadows1` (FormID `01647E`) — "Ogre"
- `CreatureOgreZShadows5` (FormID `01647F`) — "Ogre"
- `CreatureOgreZShadows3` (FormID `016480`) — "Ogre"
- `CreatureOgreZShadows6` (FormID `016481`) — "Ogre"
- `CreatureOgreZBrokenTooth1` (FormID `0399C2`) — "Ogre"
- `CreatureOgreZBrokenTooth2` (FormID `0399C4`) — "Ogre"
- `CreatureOgreZBrokenTooth3` (FormID `0399C5`) — "Ogre"
- `CreatureOgreZBrokenTooth4` (FormID `0399C6`) — "Ogre"
- `CreatureOgreZThunder1` (FormID `03A25C`) — "Ogre"
- `CreatureOgreZThunder2` (FormID `03A25D`) — "Ogre"
- `CreatureOgreZThunder3` (FormID `03A25E`) — "Ogre"
- `CreatureOgreZThunder4` (FormID `03A25F`) — "Ogre"
- `CreatureOgreZThunder5` (FormID `0438AF`) — "Ogre"
- `CreatureOgreZThunder6` (FormID `0438B0`) — "Ogre"
- `CreatureOgreZBrokenTooth5` (FormID `0438B1`) — "Ogre"
- `CreatureOgreZBrokenTooth6` (FormID `0438B2`) — "Ogre"

**Changed:**

- `CreatureOgre` (FormID `00C20D`) — "LOC_FN_CreatureOgre" — `full`: `'Ogre'` → `'LOC_FN_CreatureOgre'`
- `CreatureMinotaurLordWeapon` (FormID `01E648`) — "LOC_FN_CreatureMinotaurLordWeapon" — `full`: `'Minotaur Lord'` → `'LOC_FN_CreatureMinotaurLordWeapon'`
- `CreatureImp` (FormID `01E649`) — "LOC_FN_CreatureImp" — `full`: `'Imp'` → `'LOC_FN_CreatureImp'`
- `CreatureMinotaurLord` (FormID `03F14B`) — "LOC_FN_CreatureMinotaurLord" — `full`: `'Minotaur Lord'` → `'LOC_FN_CreatureMinotaurLord'`
- `CreatureRat1` (FormID `007FD0`) — "LOC_FN_CreatureRat" — `full`: `'Rat'` → `'LOC_FN_CreatureRat'`
- `CreatureRat2` (FormID `007FD2`) — "LOC_FN_CreatureRat" — `full`: `'Rat'` → `'LOC_FN_CreatureRat'`
- `CreatureRat3` (FormID `007FD3`) — "LOC_FN_CreatureRat" — `full`: `'Rat'` → `'LOC_FN_CreatureRat'`
- `CreatureRat4` (FormID `007FD4`) — "LOC_FN_CreatureRat" — `full`: `'Rat'` → `'LOC_FN_CreatureRat'`
- `CreatureImp1` (FormID `0084F4`) — "LOC_FN_CreatureImp" — `full`: `'Imp'` → `'LOC_FN_CreatureImp'`
- `CreatureImp2` (FormID `0084F5`) — "LOC_FN_CreatureImp" — `full`: `'Imp'` → `'LOC_FN_CreatureImp'`
- `CreatureOgre1` (FormID `0089EC`) — "LOC_FN_CreatureOgre" — `full`: `'Ogre'` → `'LOC_FN_CreatureOgre'`
- `CreatureOgre2` (FormID `0089ED`) — "LOC_FN_CreatureOgre" — `full`: `'Ogre'` → `'LOC_FN_CreatureOgre'`
- `CreatureOgre7` (FormID `00BE0D`) — "LOC_FN_CreatureOgre" — `full`: `'Ogre'` → `'LOC_FN_CreatureOgre'`
- `CreatureOgre8` (FormID `00BE0E`) — "LOC_FN_CreatureOgre" — `full`: `'Ogre'` → `'LOC_FN_CreatureOgre'`
- `CreatureMinotaur5OOO` (FormID `00BE14`) — "LOC_FN_CreatureMinotaur4" — `full`: `'Minotaur'` → `'LOC_FN_CreatureMinotaur4'`
- `CreatureMinotaur5WeaponOOO` (FormID `00BE15`) — "LOC_FN_CreatureMinotaur4Weapon" — `full`: `'Minotaur'` → `'LOC_FN_CreatureMinotaur4Weapon'`
- `CreatureMinotaur6WeaponOOO` (FormID `00BE16`) — "LOC_FN_CreatureMinotaur4Weapon" — `full`: `'Minotaur'` → `'LOC_FN_CreatureMinotaur4Weapon'`
- `CreatureMinotaur6OOO` (FormID `00BE17`) — "LOC_FN_CreatureMinotaur4" — `full`: `'Minotaur'` → `'LOC_FN_CreatureMinotaur4'`
- `CreatureMinotaur7WeaponOOO` (FormID `00BE18`) — "LOC_FN_CreatureMinotaur4Weapon" — `full`: `'Minotaur'` → `'LOC_FN_CreatureMinotaur4Weapon'`
- `CreatureMinotaur7OOO` (FormID `00BE19`) — "LOC_FN_CreatureMinotaur4" — `full`: `'Minotaur'` → `'LOC_FN_CreatureMinotaur4'`

_…15 more changed omitted (see JSON for full list)_

## ESP changes — `OOO_NewCreatures04Special.esp`

_Initial inventory (no prior version to compare against)._

- **Creature (CREA):** 41 records

## ESP changes — `OOO_NewMiscItems.esp`

_Initial inventory (no prior version to compare against)._

- **Misc Item (MISC):** 19 records

## ESP changes — `OOO_NewNPCs03.esp`

### NPC (NPC_) — +47 -0 ~0

**Added:**

- `zOOODragonborneLeader` (FormID `003E9C`) — "Sir Alain Uruk"
- `zOOODragonborneCaptive` (FormID `003E9D`) — "Order of the Dragonborne's Knight"
- `ZZZOOOPilgrimZenithar3` (FormID `006AC5`) — "Pilgrim of Zenithar"
- `ZZZOOOPilgrimZenithar2` (FormID `006AD2`) — "Pilgrim of Zenithar"
- `ZZZOOOPilgrimZenithar1` (FormID `006AD5`) — "Pilgrim of Zenithar"
- `ZZZOOOPilgrimTiber1` (FormID `006AD8`) — "Pilgrim of Tiber Septim"
- `ZZZOOOPilgrimTiber2` (FormID `006ADA`) — "Pilgrim of Tiber Septim"
- `ZZZOOOPilgrimTiber3` (FormID `006ADB`) — "Pilgrim of Tiber Septim"
- `ZZZOOOPilgrimStendarr3` (FormID `006ADD`) — "Pilgrim of Stendarr"
- `ZZZOOOPilgrimStendarr2` (FormID `006ADE`) — "Pilgrim of Stendarr"
- `ZZZOOOPilgrimStendarr1` (FormID `006AE0`) — "Pilgrim of Stendarr"
- `ZZZOOOPilgrimMara1` (FormID `006AE2`) — "Pilgrim of Mara"
- `ZZZOOOPilgrimMara2` (FormID `006B01`) — "Pilgrim of Mara"
- `ZZZOOOPilgrimMara3` (FormID `006B02`) — "Pilgrim of Mara"
- `ZZZOOOPilgrimKynareth1` (FormID `006B04`) — "Pilgrim of Kynareth"
- `ZZZOOOPilgrimKynareth2` (FormID `006B08`) — "Pilgrim of Kynareth"
- `ZZZOOOPilgrimKynareth3` (FormID `006B0A`) — "Pilgrim of Kynareth"
- `ZZZOOOPilgrimJulianos1` (FormID `006B0C`) — "Pilgrim of Julianos"
- `ZZZOOOPilgrimJulianos2` (FormID `006B0E`) — "Pilgrim of Julianos"
- `ZZZOOOPilgrimJulianos3` (FormID `006B10`) — "Pilgrim of Julianos"

_…27 more added omitted (see JSON for full list)_

## ESP changes — `OOO_NewNPCs04Special.esp`

_Initial inventory (no prior version to compare against)._

- **NPC (NPC_):** 31 records

## ESP changes — `OOO_NewRobesComp.esp`

_Initial inventory (no prior version to compare against)._

- **Clothing (CLOT):** 63 records

## ESP changes — `OOO_NewWeaponComps.esp`

_Initial inventory (no prior version to compare against)._

- **Weapon (WEAP):** 35 records

## ESP changes — `OOO_NewWeapons01.esp`

_Initial inventory (no prior version to compare against)._

- **Weapon (WEAP):** 1 records

## ESP changes — `OOO_NewWeapons03.esp`

_Initial inventory (no prior version to compare against)._

- **Weapon (WEAP):** 376 records

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Cell (CELL) — +3 -0 ~0

**Added:**

- `FortHorunn` (FormID `015E28`) — "LOC_FN_FortHorunn"
- `BrokenToothCave` (FormID `039749`) — "Broken Tooth Cave"
- `BrokenToothCave02` (FormID `0398D0`) — "Shattered Bone Halls"

### Creature (CREA) — +177 -0 ~0

**Added:**

- `CreatureAtronachFrost4` (FormID `00309D`) — "Frost Atronach"
- `CreatureMountainLionsnowOOO` (FormID `003298`) — "Snow Mountain Lion"
- `CreatureMountainLionsnowOOO1` (FormID `003D18`) — "Snow Mountain Lion"
- `CreatureMountainLionsnowOOO2` (FormID `003D1C`) — "Snow Mountain Lion"
- `CreatureMountainLionsnowOOO3` (FormID `003D1D`) — "Snow Mountain Lion"
- `ImpLegionHorseSardavarB` (FormID `004D3C`) — "Imperial Legion Horse"
- `ImpLegionHorseSlopeB` (FormID `004D44`) — "Imperial Legion Horse"
- `ImpLegionHorseRidgeB` (FormID `0052BC`) — "Imperial Legion Horse"
- `ImpLegionHorseGottshawB` (FormID `0052BF`) — "Imperial Legion Horse"
- `ImpLegionHorseRoxeyB` (FormID `0052CB`) — "Imperial Legion Horse"
- `ImpLegionHorseWellspringB` (FormID `0052D0`) — "Imperial Legion Horse"
- `ImpLegionHorseAnvilB` (FormID `0052D6`) — "Imperial Legion Horse"
- `CreatureBearBlack1` (FormID `007FD9`) — "Black Bear"
- `CreatureBearBlack2` (FormID `007FDA`) — "Black Bear"
- `CreatureBearBlack3` (FormID `007FDB`) — "Black Bear"
- `CreatureBearBlackStarved1` (FormID `007FDC`) — "Starved Black Bear"
- `CreatureBearBlackStarved2` (FormID `007FDD`) — "Starved Black Bear"
- `CreatureBearBlackStarved3` (FormID `007FDE`) — "Starved Black Bear"
- `CreatureBearBrown1` (FormID `007FDF`) — "Brown Bear"
- `CreatureBearBrown2` (FormID `007FE0`) — "Brown Bear"

_…157 more added omitted (see JSON for full list)_

### Ingredient (INGR) — +0 -0 ~45

**Changed:**

- `GolemFleshHeart` (FormID `002253`) — "Blood Golem's Heart" — `full`: `''` → `"Blood Golem's Heart"`
- `GolemEbonyHeart` (FormID `00225A`) — "Ebony Golem's Heart" — `full`: `''` → `"Ebony Golem's Heart"`
- `GolemGlassHeart` (FormID `00225B`) — "Glass Golem's Heart" — `full`: `''` → `"Glass Golem's Heart"`
- `GolemGoldHeart` (FormID `002261`) — "Gold Golem's Heart" — `full`: `''` → `"Gold Golem's Heart"`
- `GolemIronHeart` (FormID `002265`) — "Iron Golem's Heart" — `full`: `''` → `"Iron Golem's Heart"`
- `GolemMagmaHeart` (FormID `002269`) — "Magma Golem's Heart" — `full`: `''` → `"Magma Golem's Heart"`
- `GolemMithrilHeart` (FormID `00226F`) — "Mithril Golem's Heart" — `full`: `''` → `"Mithril Golem's Heart"`
- `GolemMudHeart` (FormID `002270`) — "Mud Golem's Heart" — `full`: `''` → `"Mud Golem's Heart"`
- `GolemSilverHeart` (FormID `002275`) — "Silver Golem's Heart" — `full`: `''` → `"Silver Golem's Heart"`
- `GolemWaterHeart` (FormID `002278`) — "Water Golem's Heart" — `full`: `''` → `"Water Golem's Heart"`
- `Lionmeatsnow` (FormID `00329D`) — "Snow Lion Meat" — `full`: `''` → `'Snow Lion Meat'`
- `Lionmeatleopard` (FormID `00329E`) — "Jaguar Meat" — `full`: `''` → `'Jaguar Meat'`
- `Lionmeatleopardsnow` (FormID `0032A0`) — "Snow Leopard Meat" — `full`: `''` → `'Snow Leopard Meat'`
- `Wolfmeatsnow` (FormID `0032A2`) — "Tundra Wolf Meat" — `full`: `''` → `'Tundra Wolf Meat'`
- `WolfmeatWarg` (FormID `003D12`) — "Shadow Wolf Meat" — `full`: `''` → `'Shadow Wolf Meat'`
- `GoldDust` (FormID `004D2A`) — "Gold Dust" — `full`: `''` → `'Gold Dust'`
- `GarnetDust` (FormID `00615D`) — "Garnet Dust" — `full`: `''` → `'Garnet Dust'`
- `TourmalineDust` (FormID `00615E`) — "Tourmaline Dust" — `full`: `''` → `'Tourmaline Dust'`
- `PearlBlackDust` (FormID `006C7B`) — "Black Pearl Dust" — `full`: `''` → `'Black Pearl Dust'`
- `OpalDust` (FormID `006C7C`) — "Opal Dust" — `full`: `''` → `'Opal Dust'`

_…25 more changed omitted (see JSON for full list)_

### Leveled Creature List (LVLC) — +0 -0 ~10

**Changed:**

- `LL0Sheep100Pack` (FormID `008F4B`) — + entry: level 1 × 1 → `0089F1`; + entry: level 1 × 1 → `0089F2`
- `LL0Ogre100` (FormID `008F69`) — + entry: level 1 × 1 → `0089EC`; + entry: level 1 × 1 → `0089ED`; + entry: level 1 × 1 → `01CD13`; + entry: level 1 × 1 → `01CD14`; + entry: level 1 × 1 → `01CD18`; + entry: level 1 × 1 → `01CD1A`
- `LL0OgreBog100` (FormID `008F6A`) — + entry: level 1 × 1 → `000D56`; + entry: level 1 × 1 → `0089EE`; + entry: level 1 × 1 → `0089EF`; + entry: level 1 × 1 → `01CD15`; + entry: level 1 × 1 → `01CD16`; + entry: level 1 × 1 → `01CD17`; + entry: level 1 × 1 → `01CD19`; - entry: level 1 × 1 → `00C20D`
- `LL0WolfJephre100Good` (FormID `00B456`) — + entry: level 1 × 1 → `00B444`; + entry: level 1 × 1 → `00B445`; + entry: level 1 × 1 → `00B446`; + entry: level 1 × 1 → `00B447`
- `LL0OgreBog100Special` (FormID `00BE07`) — + entry: level 1 × 1 → `000D56`; + entry: level 1 × 1 → `0089EE`; + entry: level 1 × 1 → `00BE09`; + entry: level 1 × 1 → `00BE0A`; + entry: level 1 × 1 → `01CD15`
- `LL0OgreBog50Special` (FormID `00BE08`) — + entry: level 1 × 1 → `000D56`; + entry: level 1 × 1 → `0089EE`; + entry: level 1 × 1 → `00BE09`; + entry: level 1 × 1 → `00BE0A`; + entry: level 1 × 1 → `01CD15`
- `LL0Ogre50Special` (FormID `00BE0F`) — + entry: level 1 × 1 → `0089EC`; + entry: level 1 × 1 → `00BE0D`; + entry: level 1 × 1 → `00BE0E`; + entry: level 1 × 1 → `01CD14`; + entry: level 1 × 1 → `01CD1A`
- `LL0Ogre100Special` (FormID `00BE10`) — + entry: level 1 × 1 → `0089EC`; + entry: level 1 × 1 → `00BE0D`; + entry: level 1 × 1 → `00BE0E`; + entry: level 1 × 1 → `01CD14`; + entry: level 1 × 1 → `01CD1A`
- `LL0Ogre50` (FormID `026462`) — + entry: level 1 × 1 → `0089EC`; + entry: level 1 × 1 → `0089ED`; + entry: level 1 × 1 → `01CD13`; + entry: level 1 × 1 → `01CD14`; + entry: level 1 × 1 → `01CD18`; + entry: level 1 × 1 → `01CD1A`
- `LL0OgreBog50` (FormID `026463`) — + entry: level 1 × 1 → `000D56`; + entry: level 1 × 1 → `0089EE`; + entry: level 1 × 1 → `0089EF`; + entry: level 1 × 1 → `01CD15`; + entry: level 1 × 1 → `01CD16`; + entry: level 1 × 1 → `01CD17`; + entry: level 1 × 1 → `01CD19`; - entry: level 1 × 1 → `00C20D`

### Leveled Item List (LVLI) — +0 -0 ~1

**Changed:**

- `LL0CrWeapMinotaurLordAyleid` (FormID `004E42`) — + entry: level 1 × 1 → `0025CF`; + entry: level 1 × 1 → `0025D1`; + entry: level 1 × 1 → `0025D2`; + entry: level 1 × 1 → `0025D3`; + entry: level 1 × 1 → `0025D4`; + entry: level 1 × 1 → `0025D5`; + entry: level 1 × 1 → `0025D6`; + entry: level 1 × 1 → `051356`

### NPC (NPC_) — +78 -0 ~0

**Added:**

- `GhostMinionMeleeMale1a` (FormID `00312E`) — "Ghostly Warrior"
- `GhostMinionMeleeMale1b` (FormID `003130`) — "Ghostly Warrior"
- `GhostMinionMeleeMale1c` (FormID `003131`) — "Ghostly Warrior"
- `GhostMinionMeleeMale1d` (FormID `003132`) — "Ghostly Warrior"
- `GhostMinionMeleeMale1e` (FormID `003133`) — "Ghostly Warrior"
- `GhostMinionMeleeMale1f` (FormID `003134`) — "Ghostly Warrior"
- `GhostMinionMeleeMale1g` (FormID `003135`) — "Ghostly Warrior"
- `GhostMinionMeleeMale1h` (FormID `003136`) — "Ghostly Warrior"
- `GhostMinionMeleeMale2a` (FormID `003137`) — "Spectral Warrior"
- `GhostMinionMeleeMale2b` (FormID `003138`) — "Spectral Warrior"
- `GhostMinionMeleeMale2c` (FormID `003139`) — "Spectral Warrior"
- `GhostMinionMeleeMale2d` (FormID `00313A`) — "Spectral Warrior"
- `GhostMinionMeleeMale2e` (FormID `00313B`) — "Spectral Warrior"
- `GhostMinionMeleeMale2f` (FormID `00313C`) — "Spectral Warrior"
- `GhostMinionMeleeMale2g` (FormID `00313D`) — "Spectral Warrior"
- `GhostMinionMeleeMale2h` (FormID `00313E`) — "Spectral Warrior"
- `GhostMinionMeleeMale3` (FormID `003635`) — "Spectral Reaver"
- `GhostMinionMeleeMale3a` (FormID `003636`) — "Spectral Reaver"
- `GhostMinionMeleeMale3b` (FormID `003637`) — "Spectral Reaver"
- `GhostMinionMeleeMale3c` (FormID `003638`) — "Spectral Reaver"

_…58 more added omitted (see JSON for full list)_

### AI Package (PACK) — +3 -0 ~0

**Added:**

- `OOOBrokenToothOgreTravelRaid` (FormID `0399C7`)
- `OOOBrokenToothOgreTravelHome` (FormID `0399C8`)
- `OOOHorunnMinoTravelHome` (FormID `0399D2`)

### Script (SCPT) — +42 -0 ~0

**Added:**

- `2MagicSpawnGolemWater` (FormID `0042B7`)
- `2MagicSpawnGolemGold` (FormID `00474E`)
- `2MagicSpawnGolemSilver` (FormID `00474F`)
- `2MagicSpawnGolemMithril` (FormID `004750`)
- `2MagicSpawnGolemGlass` (FormID `004751`)
- `2MagicSpawnGolemIron` (FormID `004752`)
- `2MagicSpawnGolemEbony` (FormID `004753`)
- `2MagicSpawnGolemGlassAthragar` (FormID `004754`)
- `2MagicSpawnGolemGoldAthragar` (FormID `004759`)
- `2MagicSpawnGolemWaterAthragar` (FormID `00475A`)
- `2MagicSpawnGolemSilverAthragar` (FormID `00475B`)
- `2MagicSpawnGolemMithrilAthragar` (FormID `00475C`)
- `2MagicSpawnSpectralReaver` (FormID `004B1B`)
- `1NewCowlScript` (FormID `0051C0`)
- `2MagicSpawnWolfJephre` (FormID `005D5F`)
- `2MagicSpawnBoarGood` (FormID `00B451`)
- `2MagicSpawnLionGood` (FormID `00B453`)
- `2MagicSpawnWolfJephreGood` (FormID `00B455`)
- `2MagicSpawnGolemMithrilBad` (FormID `00DA51`)
- `2MagicSpawnGolemGoldBad` (FormID `00DA52`)

_…22 more added omitted (see JSON for full list)_

### Spell (SPEL) — +15 -0 ~120

**Added:**

- `ManniReaverSummon` (FormID `004B1C`) — "Mannimarco's Call of Spirits"
- `ValenSummonBoarJephre` (FormID `007F71`) — "Jephre's Tusks"
- `ValenSummonLionJephre` (FormID `007F73`) — "Jephre's Fangs"
- `ValenSummonSprigganJephre` (FormID `007F75`) — "Jephre's Mistress"
- `ValenSummonGiantWolfJephre` (FormID `007F77`) — "Jephre's Hunter"
- `ValenSummonKodiakJephre` (FormID `007F79`) — "Jephre's Spirit"
- `ValenBosmerGoodSummon1` (FormID `00B457`) — "Jephre's Forest Companion"
- `ValenBosmerGoodBoarJephre` (FormID `00B458`) — "Jephre's Tusks"
- `ValenBosmerGoodLionJephre` (FormID `00B45A`) — "Jephre's Fangs"
- `ValenSummon3` (FormID `0100F4`) — "Jephre's Forest Companion"
- `AbGhostNPC2` (FormID `014667`) — "Ghostly powers"
- `AbGhostNPC3` (FormID `014B5E`) — "Ghostly powers"
- `AbAtronachFlameEffect2` (FormID `015551`) — "Atronach Fire"
- `AbGhostSpriggan` (FormID `015558`) — "Ghostly powers"
- `ManniSummonLich` (FormID `03BFA5`) — "Mannimarco's Summon Lich"

**Changed:**

- `AbSeducer` (FormID `00126B`) — "Seducer's Vanity" — `full`: `''` → `"Seducer's Vanity"`
- `DreadSetBonusOOO` (FormID `002656`) — "Dread Visage" — `full`: `''` → `'Dread Visage'`
- `ManniShockTarget1` (FormID `003253`) — "Mannimarco's Anguish" — `full`: `''` → `"Mannimarco's Anguish"`
- `AbAnimalResisFireOOO` (FormID `0037DB`) — "Resist Fire" — `full`: `''` → `'Resist Fire'`
- `FalcarDrain1` (FormID `003D63`) — "Falcar's Life Drain" — `full`: `''` → `"Falcar's Life Drain"`
- `FalcarDrain3` (FormID `003D64`) — "Falcar's Grevious Wounds" — `full`: `''` → `"Falcar's Grevious Wounds"`
- `FalcarSilence` (FormID `003D66`) — "Falcar's Silent Betrayal" — `full`: `''` → `"Falcar's Silent Betrayal"`
- `1detectlifeeffect` (FormID `0042FA`) — "Cowl's Life Detection" — `full`: `''` → `"Cowl's Life Detection"`
- `1nighteyeeffect` (FormID `0042FB`) — "Cowl's Night Vision" — `full`: `''` → `"Cowl's Night Vision"`
- `1waterbreatheffect` (FormID `004300`) — "Cowl's Limitless Breath" — `full`: `''` → `"Cowl's Limitless Breath"`
- `AbUndeadBoneResistBossOscuro` (FormID `005DFC`) — "Undead Bone Lord Resistances" — `full`: `''` → `'Undead Bone Lord Resistances'`
- `ArgonianWeakness1` (FormID `007755`) — "Mud Pool's Chant" — `full`: `''` → `"Mud Pool's Chant"`
- `ArgonianAbsorb1` (FormID `007756`) — "Touch of Endless Treading" — `full`: `''` → `'Touch of Endless Treading'`
- `ArgonianAbsorb2` (FormID `007758`) — "Touch of Sorrowful Hopes" — `full`: `''` → `'Touch of Sorrowful Hopes'`
- `ArgonianAbsorb3` (FormID `00775A`) — "Touch of Exhausting Journey" — `full`: `''` → `'Touch of Exhausting Journey'`
- `ArgonianAbsorb4` (FormID `00775C`) — "Touch of Seeping Vitality" — `full`: `''` → `'Touch of Seeping Vitality'`
- `ArgonianAbsorb5` (FormID `00775E`) — "Touch of Seeping Blood" — `full`: `''` → `'Touch of Seeping Blood'`
- `ArgonianAbsorb6` (FormID `007760`) — "Touch of Seeping Magicka" — `full`: `''` → `'Touch of Seeping Magicka'`
- `ArgonianHeal1` (FormID `007762`) — "Blessings of Water Borne" — `full`: `''` → `'Blessings of Water Borne'`
- `ArgonianHeal2` (FormID `007764`) — "Comforting Depths" — `full`: `''` → `'Comforting Depths'`

_…100 more changed omitted (see JSON for full list)_

### Worldspace (WRLD) — +1 -0 ~0

**Added:**

- `?` (FormID `00003C`)

## ESP changes — `OOO_GameSettings.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChests03.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChests2.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatures03.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewNPCs03.esp`

_No record-level changes detected._

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

_No record-level changes detected._

