# alpha13 — release notes

_Compared against `alpha12`._

## File-level changes

- Added: 4
- Removed: 0
- Changed: 8

### Added

- `Content/Dev/ObvData/Data/OOO_NewChestsSkip.esp`
- `Content/Dev/ObvData/Data/OOO_NewDoors04.esp`
- `Content/Dev/ObvData/Data/OOO_NewQuestsAndRewards.esp`
- `OOOInstallerFloydian1.jpg`

### Changed

- `Content/Dev/ObvData/Data/OOO_NewAmmo04.esp`
- `Content/Dev/ObvData/Data/OOO_NewArmor03.esp`
- `Content/Dev/ObvData/Data/OOO_NewArmorComps.esp`
- `Content/Dev/ObvData/Data/OOO_NewArmorOdds.esp`
- `Content/Dev/ObvData/Data/OOO_NewChestComps.esp`
- `Content/Dev/ObvData/Data/OOO_NewChests03.esp`
- `Content/Dev/ObvData/Data/OOO_NewNPCs04.esp`
- `Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`

## ESP changes — `OOO_GameSettings.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewAmmo04.esp`

### Ammunition (AMMO) — +8 -0 ~27

**Added:**

- `Arrow1Iron` (FormID `017829`) — "LOC_FN_Arrow1Iron"
- `Arrow8Daedric` (FormID `01EFD3`) — "LOC_FN_Arrow8Daedric"
- `Arrow3Silver` (FormID `01EFD4`) — "LOC_FN_Arrow3Silver"
- `Arrow7Ebony` (FormID `01EFD5`) — "LOC_FN_Arrow7Ebony"
- `Arrow5Elven` (FormID `0229C0`) — "LOC_FN_Arrow5Elven"
- `Arrow2Steel` (FormID `0229C1`) — "LOC_FN_Arrow2Steel"
- `Arrow6Glass` (FormID `022BE1`) — "LOC_FN_Arrow6Glass"
- `Arrow4Dwarven` (FormID `022BE2`) — "LOC_FN_Arrow4Dwarven"

**Changed:**

- `ArrowCloudOrnateOOO` (FormID `001F3B`) — "Ornate Cloudwood Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\cloudornate.nif'` → `'Weapons\\Glass\\Arrow.NIF'`
- `ArrowCloudSimpleOOO` (FormID `001F3C`) — "Cloudwood Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\cloudsimple.nif'` → `'Weapons\\Glass\\Arrow.NIF'`
- `ArrowEbonyOrnateOOO` (FormID `001F3D`) — "Ayleid Ornate Ebony Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\ebonyornate.nif'` → `'Weapons\\Ebony\\Arrow.NIF'`
- `ArrowEbonySimpleOOO` (FormID `001F3E`) — "Ayleid Ebony Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\ebonysimple.nif'` → `'Weapons\\Ebony\\Arrow.NIF'`
- `ArrowElmOrnateOOO` (FormID `001F3F`) — "Ornate Elmwood Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\elmwoodornate.nif'` → `'Weapons\\Elven\\Arrow.NIF'`
- `ArrowElmSimpleOOO` (FormID `001F40`) — "Elmwood Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\elmwoodsimple.nif'` → `'Weapons\\Elven\\Arrow.NIF'`
- `ArrowIvoryOrnateOOO` (FormID `001F41`) — "Ayleid Ornate Royal Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\ivoryornate.nif'` → `'Weapons\\Ebony\\Arrow.NIF'`
- `ArrowIvorySimpleOOO` (FormID `001F42`) — "Ayleid Royal Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\ivorysimple.nif'` → `'Weapons\\Ebony\\Arrow.NIF'`
- `ArrowTreeOrnateOOO` (FormID `001F43`) — "Ornate Sunwood Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\treeornate.nif'` → `'Weapons\\Elven\\Arrow.NIF'`
- `ArrowTreeSimpleOOO` (FormID `001F44`) — "Sunwood Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\treesimple.nif'` → `'Weapons\\Elven\\Arrow.NIF'`
- `ArrowWhiteOrnateOOO` (FormID `001F45`) — "Ornate White Oak Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\whiteleatherornate.nif'` → `'Weapons\\Silver\\Arrow.NIF'`
- `ArrowWhiteSimpleOOO` (FormID `001F46`) — "White Oak Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\whiteleathersimple.nif'` → `'Weapons\\Silver\\Arrow.NIF'`
- `ArrowBraidedOOO` (FormID `013C57`) — "Braided Arrow" — `modl`: `'weapons\\Braided\\bquiver.nif'` → `'Weapons\\Ebony\\Arrow.NIF'`
- `TheDragonArrowOOO` (FormID `02566C`) — "The Dragon's Bites" — `modl`: `'Weapons\\TheSilverDragonOrder\\TheDragonArrow.nif'` → `'Weapons\\Silver\\Arrow.NIF'`
- `TheSilverDragonArrowsOOO` (FormID `02566E`) — "The Dragon's Teeth" — `modl`: `'Weapons\\TheSilverDragonOrder\\TheDragonQuiver.nif'` → `'Weapons\\Silver\\Arrow.NIF'`
- `WeaponsDraconicArmorarrowOOO` (FormID `02714B`) — "Draconic Arrow" — `modl`: `'Weapons\\DraconicArmor\\arrow.nif'` → `'Weapons\\Silver\\Arrow.NIF'`
- `KDWhiteRoseElvenOOO` (FormID `02714C`) — "White Rose Arrow" — `modl`: `'weapons\\KDwhiterosebow\\whiterosequiver.nif'` → `'Weapons\\Elven\\Arrow.NIF'`
- `ShadowMailArrowOOO` (FormID `038863`) — "Shadow Arrow" — `modl`: `'weapons\\ShadowMail\\arrow.nif'` → `'Weapons\\Steel\\Arrow.NIF'`
- `AyleidArrowEnchShock` (FormID `05138D`) — "Malatta Pilin" — `modl`: `'Weapons\\Meteoric\\metarrow1.nif'` → `'Weapons\\Elven\\Arrow.NIF'`
- `AyleidArrowEnchFireblast` (FormID `05138E`) — "Molagste Pilin" — `modl`: `'Weapons\\Meteoric\\metarrow1.nif'` → `'Weapons\\Elven\\Arrow.NIF'`

_…7 more changed omitted (see JSON for full list)_

## ESP changes — `OOO_NewAmmoComps.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewArmor.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewArmor03.esp`

### Armor (ARMO) — +13 -0 ~0

**Added:**

- `HeavenFuryBootsGold` (FormID `004C84`) — "Heaven's Fury Boots"
- `HeavenFuryCuirassGold` (FormID `004C85`) — "Heaven's Fury Cuirass"
- `HeavenFuryGauntletsGold` (FormID `004C86`) — "Heaven's Fury Gauntlets"
- `HeavenFuryGreavesGold` (FormID `004C87`) — "Heaven's Fury Greaves"
- `HeavenFuryHelmetGold` (FormID `004C88`) — "Heaven's Fury Helmet"
- `HeavenFuryShieldGold` (FormID `004C8A`) — "Heaven's Fury Shield"
- `CMIronBattleShield03OOOBosmerGood` (FormID `0077A8`) — "Protector's Insignia Shield"
- `CMIronBattleShield09OOO2` (FormID `00BE58`) — "Ranger's Insignia Shield"
- `ArmorDraconicArmorbootsOOO` (FormID `027156`) — "Dragonborne Boots"
- `ArmorDraconicArmorcuirassOOO` (FormID `027157`) — "Dragonborne Cuirass"
- `ArmorDraconicArmorgauntletsOOO` (FormID `027158`) — "Dragonborne Gauntlets"
- `ArmorDraconicArmorgreavesOOO` (FormID `027159`) — "Dragonborne Greaves"
- `ArmorDraconicArmorshieldOOO` (FormID `02715A`) — "Dragonborne Shield"

## ESP changes — `OOO_NewArmor04Amazon.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewArmor04Bosmer.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewArmorComps.esp`

**Master list changed:**

- before: ['Oblivion.esm', "Oscuro's_Oblivion_Overhaul.esp"]
- after:  ['Oblivion.esm', 'Knights.esp', "Oscuro's_Oblivion_Overhaul.esp"]

### Armor (ARMO) — +18 -14 ~0

**Added:**

- `NDArmorLightShield5` (FormID `000E92`) — "Shield of the Crusader"
- `NDArmorLightHelmet5` (FormID `000E93`) — "Helm of the Crusader"
- `NDArmorLightGreaves5` (FormID `000E94`) — "Greaves of the Crusader"
- `NDArmorLightGauntlets5` (FormID `000E95`) — "Gauntlets of the Crusader"
- `NDArmorLightCuirass5` (FormID `000E96`) — "Cuirass of the Crusader"
- `NDArmorLightBoots5` (FormID `000E97`) — "Boots of the Crusader"
- `NDArmorHeavyShield5` (FormID `000EB0`) — "Shield of the Crusader"
- `NDArmorHeavyHelmet5` (FormID `000EB1`) — "Helm of the Crusader"
- `NDArmorHeavyGreaves5` (FormID `000EB2`) — "Greaves of the Crusader"
- `NDArmorHeavyGauntlets5` (FormID `000EB3`) — "Gauntlets of the Crusader"
- `NDArmorHeavyCuirass5` (FormID `000EB4`) — "Cuirass of the Crusader"
- `NDArmorHeavyBoots5` (FormID `000EB5`) — "Boots of the Crusader"
- `HeavyBraidedBootsOOO` (FormID `03DDF3`) — "Heavy Braided Boots"
- `HeavyBraidedCuirassOOO` (FormID `03DDF4`) — "Heavy Braided Cuirass"
- `HeavyBraidedGauntletsOOO` (FormID `03DDF5`) — "Heavy Braided Gauntlets"
- `HeavyBraidedGreavesOOO` (FormID `03DDF6`) — "Heavy Braided Greaves"
- `HeavyBraidedHelmetOOO` (FormID `03DDF7`) — "Heavy Braided Helmet"
- `HeavyBraidedShieldOOO` (FormID `03DDF8`) — "Heavy Braided Shield"

**Removed:**

- `HeavenFuryBoots` (FormID `0046DB`) — "Heaven's Fury Boots"
- `HeavenFuryCuirass` (FormID `0046DC`) — "Heaven's Fury Cuirass"
- `HeavenFuryGauntlets` (FormID `0046DD`) — "Heaven's Fury Gauntlets"
- `HeavenFuryGreaves` (FormID `0046DE`) — "Heaven's Fury Greaves"
- `HeavenFuryHelmet` (FormID `0046DF`) — "Heaven's Fury Helmet"
- `HeavenFuryShield` (FormID `0046E0`) — "Heaven's Fury Shield"
- `HeavenFuryHelmetAlt` (FormID `0046E1`) — "Heaven's Fury Helmet"
- `HeavenFuryBootsGold` (FormID `004C84`) — "Heaven's Fury Boots"
- `HeavenFuryCuirassGold` (FormID `004C85`) — "Heaven's Fury Cuirass"
- `HeavenFuryGauntletsGold` (FormID `004C86`) — "Heaven's Fury Gauntlets"
- `HeavenFuryGreavesGold` (FormID `004C87`) — "Heaven's Fury Greaves"
- `HeavenFuryHelmetGold` (FormID `004C88`) — "Heaven's Fury Helmet"
- `HeavenFuryHelmetGoldAlt` (FormID `004C89`) — "Heaven's Fury Helmet"
- `HeavenFuryShieldGold` (FormID `004C8A`) — "Heaven's Fury Shield"

## ESP changes — `OOO_NewArmorOdds.esp`

### Armor (ARMO) — +8 -5 ~0

**Added:**

- `HeavenFuryBoots` (FormID `0046DB`) — "Heaven's Fury Boots"
- `HeavenFuryCuirass` (FormID `0046DC`) — "Heaven's Fury Cuirass"
- `HeavenFuryGauntlets` (FormID `0046DD`) — "Heaven's Fury Gauntlets"
- `HeavenFuryGreaves` (FormID `0046DE`) — "Heaven's Fury Greaves"
- `HeavenFuryHelmet` (FormID `0046DF`) — "Heaven's Fury Helmet"
- `HeavenFuryShield` (FormID `0046E0`) — "Heaven's Fury Shield"
- `HeavenFuryHelmetAlt` (FormID `0046E1`) — "Heaven's Fury Helmet"
- `HeavenFuryHelmetGoldAlt` (FormID `004C89`) — "Heaven's Fury Helmet"

**Removed:**

- `ArmorDraconicArmorbootsOOO` (FormID `027156`) — "Dragonborne Boots"
- `ArmorDraconicArmorcuirassOOO` (FormID `027157`) — "Dragonborne Cuirass"
- `ArmorDraconicArmorgauntletsOOO` (FormID `027158`) — "Dragonborne Gauntlets"
- `ArmorDraconicArmorgreavesOOO` (FormID `027159`) — "Dragonborne Greaves"
- `ArmorDraconicArmorshieldOOO` (FormID `02715A`) — "Dragonborne Shield"

## ESP changes — `OOO_NewChestComps.esp`

### Container (CONT) — +10 -18 ~172

**Added:**

- `PCCupboardClutterUpperShelfSilverware01` (FormID `005130`) — "LOC_FN_PCCupboardClutterUpperShelfSilverware01"
- `PCCupboardClutterUpper` (FormID `00514E`) — "LOC_FN_PCCupboardClutterUpper"
- `PCCupboardClothingUpper` (FormID `00514F`) — "LOC_FN_PCCupboardClothingUpper"
- `PCDrawerClutterUpper02` (FormID `00515A`) — "LOC_FN_PCDrawerClutterUpper02"
- `PCCupboardClutterMiddle` (FormID `00516F`) — "LOC_FN_PCCupboardClutterMiddle"
- `PCCupboardClutterLower` (FormID `005171`) — "LOC_FN_PCCupboardClutterLower"
- `ChestHouseTreasuryLower01` (FormID `0A496A`) — "LOC_FN_ChestHouseTreasuryLower01"
- `ChestHouseTreasuryLower02` (FormID `0A496B`) — "LOC_FN_ChestHouseTreasuryLower02"
- `ZOOOChestUpper01NobleArmoryFighterT100` (FormID `0062F0`) — "Elegant Chest"
- `BlackRockChest02OOO` (FormID `01CC57`) — "Chest"

**Removed:**

- `VendorRindirsStaffsDefStaffsOOO` (FormID `0011E8`) — "Chest"
- `VendorMysticEmporiumDefStaffsOOO` (FormID `0011EA`) — "Chest"
- `LapBrewer` (FormID `001BA3`) — "Still"
- `LapSecretGrapeBarrel` (FormID `00208A`) — "Secret, No Lookie!"
- `LapGrapeSmushingBarrel` (FormID `002572`) — "Grape Barrel"
- `LapWineMakingMachine` (FormID `002A6B`) — "Apple Press"
- `VendorArcaneUDefStaffOOO` (FormID `002AAE`) — "Chest"
- `LapKeg` (FormID `003479`) — "Keg"
- `XuniquerobechestrindirOOO` (FormID `006A3F`) — "Chest"
- `XRareRobeChestchednyhalOOO` (FormID `00AA0A`) — "Chest"
- `XuniquerobechestchedynhalOOO` (FormID `00AA0C`) — "Chest"
- `XRareRobeChestAnvilOOO` (FormID `00AEFA`) — "Chest"
- `XuniquerobechestskingradOOO` (FormID `00AEFB`) — "Chest"
- `XuniquerobechestsanvilOOO` (FormID `00AEFD`) — "Chest"
- `XuniquerobechestbravilOOO` (FormID `00AF00`) — "Chest"
- `XRareRobeChestbravilOOO` (FormID `00AF02`) — "Chest"
- `XRareRobeleyawinnOOO` (FormID `00B3EA`) — "Chest"
- `XRareRobeChestOOO` (FormID `048F76`) — "Chest"

**Changed:**

- `DeskClutterMiddle01` (FormID `024457`) — "Desk" — `modl`: `'harvest\\containers\\XMSharvestMiddleDesk01HiFi.nif'` → `'Furniture\\MiddleClass\\MiddleDesk01.NIF'`
- `DeskExecClutter01` (FormID `024951`) — "Desk" — `modl`: `'harvest\\containers\\XMSharvestUpperExecDesk01HiFi.nif'` → `'Furniture\\UpperClass\\UpperExecDesk01.NIF'`
- `ZOOOChestJewelry01NobleT100AlvaUlani` (FormID `001F48`) — "Exquisite Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestUpper01NobleTreasuryLesserT100AmAl` (FormID `001F4A`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestClutterMiddleSame01AsAt` (FormID `001F56`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOOChestClutterMiddleSame02AsAt` (FormID `001F57`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest02LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest02.NIF'`
- `ZOOOChestClutterUpper02AsAt` (FormID `001F58`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestJewelry01UpperT100Baer` (FormID `001F59`) — "Fine Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestMiddle02UpperArmoryPatneim` (FormID `001F7F`) — "Fine Banded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOOChestJewelry01MiddleCarandial` (FormID `001F80`) — "Common Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestJewelry01UpperT100DovynAren` (FormID `001F89`) — "Fine Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestJewelry01MiddleT100Droshanji` (FormID `001F8B`) — "Common Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestMiddle02UpperArmoryDynariAmnis` (FormID `001F8D`) — "Fine Banded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOOChestUpper02NobleClutterDynariAmnis` (FormID `001F8F`) — "Elaborate Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest01LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest01.NIF'`
- `ZOOOChestUpper01NobleAlchemyT100EidKee` (FormID `001F90`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestUpper01NobleArmoryT100EidKee` (FormID `001F92`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestUpper01NobleTreasuryT100EidKee` (FormID `001F93`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestMiddle02UpperArmoryLesserWizT100Glarthir` (FormID `001F98`) — "Rune Banded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOOChestMiddle01UpperTreasuryT100Glarthir` (FormID `001F99`) — "Studded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest02LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest02.NIF'`
- `ZOOOChestUpper01NobleTreasuryLesserT100Glarthir` (FormID `001F9A`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`

_…152 more changed omitted (see JSON for full list)_

### Script (SCPT) — +154 -0 ~0

**Added:**

- `3ContJewelAlvaUlvaniTrapYesCrimeYesHiFi01upgNR` (FormID `001F49`)
- `3ContJewelBaeralornTrapYesCrimeYesHiFi01upgNR` (FormID `001F5A`)
- `3ContAyleid02aTrapCrimeNoHifi01NRMS92` (FormID `001F5C`)
- `3ContJewelCarandialTrapNoCrimeYesHiFi01upgNR` (FormID `001F81`)
- `3ContJewelDovynArenTrapYesCrimeYesHiFi01upgNR` (FormID `001F8A`)
- `3ContJewelDroshanjiTrapYesCrimeYesHiFi01upgNR` (FormID `001F8C`)
- `3ContDrawTrapNoCrimeYesHifi01NRMG02` (FormID `001F94`)
- `3ContDrawTrapNoCrimeYesHifi01NRMG03` (FormID `001F95`)
- `3ContDrawUpgTrapNoCrimeYesHifi01NRMG03` (FormID `001F96`)
- `3DEJharvestMQ05CommentariesChestScriptOOO` (FormID `001F97`)
- `3ContJewelGreyThroatTrapNoCrimeYesHiFi01upgNR` (FormID `001FA0`)
- `3ContJewelHafidTrapNoCrimeYesHiFi01upgNR` (FormID `001FA2`)
- `3ContJewelHalLiurzTrapYesCrimeYesHiFi01upgNR` (FormID `001FA4`)
- `3ContJewelTravenTrapYesCrimeYesHiFi01upgNR` (FormID `002CD9`)
- `3ContUpgHelviusTrapNoCrimeYesHiFi01` (FormID `0032EC`)
- `3DEJharvestHifi01` (FormID `003D6F`)
- `3ContAyleid02bTrapCrimeNoHifi01NR` (FormID `003D70`)
- `3ContAyleid02bTrapCrimeYesHifi01NR` (FormID `003D73`)
- `3ContAyleid02bTrapNoCrimeNoHifi01NR` (FormID `003D74`)
- `3ContAyleid02bTrapNoCrimeYesHifi01NR` (FormID `003D75`)

_…134 more added omitted (see JSON for full list)_

## ESP changes — `OOO_NewChests.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChests03.esp`

### Container (CONT) — +5 -24 ~171

**Added:**

- `PCCupboardClutterUpperShelfSilverware01` (FormID `005130`) — "LOC_FN_PCCupboardClutterUpperShelfSilverware01"
- `PCCupboardClutterUpper` (FormID `00514E`) — "LOC_FN_PCCupboardClutterUpper"
- `PCCupboardClutterMiddle` (FormID `00516F`) — "LOC_FN_PCCupboardClutterMiddle"
- `PCCupboardClutterLower` (FormID `005171`) — "LOC_FN_PCCupboardClutterLower"
- `CupboardIngredientsRare` (FormID `0A4969`) — "Cupboard"

**Removed:**

- `VendorRindirsStaffsDefStaffsOOO` (FormID `0011E8`) — "Chest"
- `VendorMysticEmporiumDefStaffsOOO` (FormID `0011EA`) — "Chest"
- `LapBrewer` (FormID `001BA3`) — "Still"
- `LapSecretGrapeBarrel` (FormID `00208A`) — "Secret, No Lookie!"
- `LapGrapeSmushingBarrel` (FormID `002572`) — "Grape Barrel"
- `ChestDefStaffAlyeid` (FormID `0025A0`) — "Ayleid Reliquary"
- `ChestDefStaffAlyeidBoss3` (FormID `0025A3`) — "Ayleid Reliquary"
- `ChestDefStaffUpper4` (FormID `0025A6`) — "Chest"
- `ChestDefStaffUpper2` (FormID `0025A7`) — "Chest"
- `ChestDefStaffAlyeidBoss5` (FormID `0025A8`) — "Ayleid Reliquary"
- `ChestDefStaffLower1` (FormID `0025A9`) — "Chest"
- `LapWineMakingMachine` (FormID `002A6B`) — "Apple Press"
- `VendorArcaneUDefStaffOOO` (FormID `002AAE`) — "Chest"
- `LapKeg` (FormID `003479`) — "Keg"
- `XuniquerobechestrindirOOO` (FormID `006A3F`) — "Chest"
- `XRareRobeChestchednyhalOOO` (FormID `00AA0A`) — "Chest"
- `XuniquerobechestchedynhalOOO` (FormID `00AA0C`) — "Chest"
- `XRareRobeChestAnvilOOO` (FormID `00AEFA`) — "Chest"
- `XuniquerobechestskingradOOO` (FormID `00AEFB`) — "Chest"
- `XuniquerobechestsanvilOOO` (FormID `00AEFD`) — "Chest"

_…4 more removed omitted (see JSON for full list)_

**Changed:**

- `1grayfoxarmorychest` (FormID `0011D7`) — "Gray Fox's Armory" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest02LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest02.NIF'`
- `ZOOOChestJewelry01NobleT100AlvaUlani` (FormID `001F48`) — "Exquisite Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestUpper01NobleTreasuryLesserT100AmAl` (FormID `001F4A`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestClutterMiddleSame01AsAt` (FormID `001F56`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOOChestClutterMiddleSame02AsAt` (FormID `001F57`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest02LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest02.NIF'`
- `ZOOOChestClutterUpper02AsAt` (FormID `001F58`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestJewelry01UpperT100Baer` (FormID `001F59`) — "Fine Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestMiddle02UpperArmoryPatneim` (FormID `001F7F`) — "Fine Banded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOOChestJewelry01MiddleCarandial` (FormID `001F80`) — "Common Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestJewelry01UpperT100DovynAren` (FormID `001F89`) — "Fine Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestJewelry01MiddleT100Droshanji` (FormID `001F8B`) — "Common Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestMiddle02UpperArmoryDynariAmnis` (FormID `001F8D`) — "Fine Banded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOOChestUpper02NobleClutterDynariAmnis` (FormID `001F8F`) — "Elaborate Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest01LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest01.NIF'`
- `ZOOOChestUpper01NobleAlchemyT100EidKee` (FormID `001F90`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestUpper01NobleArmoryT100EidKee` (FormID `001F92`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestUpper01NobleTreasuryT100EidKee` (FormID `001F93`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestMiddle02UpperArmoryLesserWizT100Glarthir` (FormID `001F98`) — "Rune Banded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOOChestMiddle01UpperTreasuryT100Glarthir` (FormID `001F99`) — "Studded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest02LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest02.NIF'`
- `ZOOOChestUpper01NobleTreasuryLesserT100Glarthir` (FormID `001F9A`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestUpper02NobleClutterT100Glarthir` (FormID `001F9B`) — "Elaborate Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest01LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest01.NIF'`

_…151 more changed omitted (see JSON for full list)_

## ESP changes — `OOO_NewChests2.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChestsSkip.esp`

_Initial inventory (no prior version to compare against)._

- **Container (CONT):** 24 records

## ESP changes — `OOO_NewClothing04.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewClothingComps.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatureComps.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatures01.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatures02.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatures03.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatures04Special.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewDoors04.esp`

_Initial inventory (no prior version to compare against)._

- **Door (DOOR):** 5 records

## ESP changes — `OOO_NewGear04Amazon.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewGear04Bosmer.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewGear04Sylvan.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewMiscItems.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewNPCs03.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewNPCs04.esp`

### NPC (NPC_) — +68 -0 ~0

**Added:**

- `DefStaffGuardian` (FormID `0025C5`) — "Hrun Illmouth"
- `ImperialLegionForester5` (FormID `003993`) — "Imperial Legion Forester"
- `Pilgrim01` (FormID `0039D6`) — "Pilgrim of Akatosh"
- `BanditHighwayman05` (FormID `003A18`) — "Highwayman"
- `BanditHighwayman06` (FormID `003A19`) — "Highwayman"
- `SlaveTraderMeleeFemale1` (FormID `0071E0`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale2` (FormID `0071E1`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale3` (FormID `0071E2`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale4` (FormID `0071E3`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale5` (FormID `0071E4`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale6` (FormID `0071E5`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale7` (FormID `0071E6`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale8` (FormID `0071E7`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale9` (FormID `0071E8`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale9A` (FormID `0071E9`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale9B` (FormID `0071EA`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale9C` (FormID `0071EB`) — "Slave Trader Thug"
- `SlaveTraderMeleeMale1` (FormID `0071EC`) — "Slave Trader Thug"
- `SlaveTraderMeleeMale2` (FormID `0071ED`) — "Slave Trader Thug"
- `SlaveTraderMeleeMale3` (FormID `0071EE`) — "Slave Trader Thug"

_…48 more added omitted (see JSON for full list)_

## ESP changes — `OOO_NewNPCs04Seducer.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewNPCs04Special.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewQuestsAndRewards.esp`

_Initial inventory (no prior version to compare against)._

- **Creature (CREA):** 2 records

## ESP changes — `OOO_NewRobesComp.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewSigilStones04.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewWeaponComps.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewWeaponCompsBow.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewWeapons01.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewWeapons03.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewWeaponsNoble.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewWeaponsOdd.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewWeaponsUnused.esp`

_No record-level changes detected._

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Ammunition (AMMO) — +0 -0 ~27

**Changed:**

- `ArrowCloudOrnateOOO` (FormID `001F3B`) — "Ornate Cloudwood Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\cloudornate.nif'` → `'Weapons\\Glass\\Arrow.NIF'`
- `ArrowCloudSimpleOOO` (FormID `001F3C`) — "Cloudwood Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\cloudsimple.nif'` → `'Weapons\\Glass\\Arrow.NIF'`
- `ArrowEbonyOrnateOOO` (FormID `001F3D`) — "Ayleid Ornate Ebony Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\ebonyornate.nif'` → `'Weapons\\Ebony\\Arrow.NIF'`
- `ArrowEbonySimpleOOO` (FormID `001F3E`) — "Ayleid Ebony Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\ebonysimple.nif'` → `'Weapons\\Ebony\\Arrow.NIF'`
- `ArrowElmOrnateOOO` (FormID `001F3F`) — "Ornate Elmwood Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\elmwoodornate.nif'` → `'Weapons\\Elven\\Arrow.NIF'`
- `ArrowElmSimpleOOO` (FormID `001F40`) — "Elmwood Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\elmwoodsimple.nif'` → `'Weapons\\Elven\\Arrow.NIF'`
- `ArrowIvoryOrnateOOO` (FormID `001F41`) — "Ayleid Ornate Royal Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\ivoryornate.nif'` → `'Weapons\\Ebony\\Arrow.NIF'`
- `ArrowIvorySimpleOOO` (FormID `001F42`) — "Ayleid Royal Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\ivorysimple.nif'` → `'Weapons\\Ebony\\Arrow.NIF'`
- `ArrowTreeOrnateOOO` (FormID `001F43`) — "Ornate Sunwood Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\treeornate.nif'` → `'Weapons\\Elven\\Arrow.NIF'`
- `ArrowTreeSimpleOOO` (FormID `001F44`) — "Sunwood Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\treesimple.nif'` → `'Weapons\\Elven\\Arrow.NIF'`
- `ArrowWhiteOrnateOOO` (FormID `001F45`) — "Ornate White Oak Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\whiteleatherornate.nif'` → `'Weapons\\Silver\\Arrow.NIF'`
- `ArrowWhiteSimpleOOO` (FormID `001F46`) — "White Oak Arrows" — `modl`: `'Weapons\\Adonnay\\Quiver\\whiteleathersimple.nif'` → `'Weapons\\Silver\\Arrow.NIF'`
- `ArrowBraidedOOO` (FormID `013C57`) — "Braided Arrow" — `modl`: `'weapons\\Braided\\bquiver.nif'` → `'Weapons\\Ebony\\Arrow.NIF'`
- `TheDragonArrowOOO` (FormID `02566C`) — "The Dragon's Bites" — `modl`: `'Weapons\\TheSilverDragonOrder\\TheDragonArrow.nif'` → `'Weapons\\Silver\\Arrow.NIF'`
- `TheSilverDragonArrowsOOO` (FormID `02566E`) — "The Dragon's Teeth" — `modl`: `'Weapons\\TheSilverDragonOrder\\TheDragonQuiver.nif'` → `'Weapons\\Silver\\Arrow.NIF'`
- `WeaponsDraconicArmorarrowOOO` (FormID `02714B`) — "Draconic Arrow" — `modl`: `'Weapons\\DraconicArmor\\arrow.nif'` → `'Weapons\\Silver\\Arrow.NIF'`
- `KDWhiteRoseElvenOOO` (FormID `02714C`) — "White Rose Arrow" — `modl`: `'weapons\\KDwhiterosebow\\whiterosequiver.nif'` → `'Weapons\\Elven\\Arrow.NIF'`
- `ShadowMailArrowOOO` (FormID `038863`) — "Shadow Arrow" — `modl`: `'weapons\\ShadowMail\\arrow.nif'` → `'Weapons\\Steel\\Arrow.NIF'`
- `AyleidArrowEnchShock` (FormID `05138D`) — "Malatta Pilin" — `modl`: `'Weapons\\Meteoric\\metarrow1.nif'` → `'Weapons\\Elven\\Arrow.NIF'`
- `AyleidArrowEnchFireblast` (FormID `05138E`) — "Molagste Pilin" — `modl`: `'Weapons\\Meteoric\\metarrow1.nif'` → `'Weapons\\Elven\\Arrow.NIF'`

_…7 more changed omitted (see JSON for full list)_

### Armor (ARMO) — +10 -0 ~13

**Added:**

- `DreadBootsOOO` (FormID `002650`) — "Dread Boots"
- `DreadCuirassOOO` (FormID `002651`) — "Dread Cuirass"
- `DreadGauntletsOOO` (FormID `002652`) — "Dread Gauntlets"
- `DreadGreavesOOO` (FormID `002653`) — "Dread Greaves"
- `DreadHelmetOOO` (FormID `002654`) — "Dread Helmet"
- `DreadCuirassOOOv2L` (FormID `06EA3C`) — "Dread Cuirass"
- `DreadBootsOOOv2L` (FormID `06EA3D`) — "Dread Boots"
- `DreadGauntletsOOOv2L` (FormID `06EA3E`) — "Dread Gauntlets"
- `DreadGreavesOOOv2L` (FormID `06EA3F`) — "Dread Greaves"
- `DreadHelmetOOOv2L` (FormID `06EA40`) — "Dread Helmet"

**Changed:**

- `HeavenFuryBootsGold` (FormID `004C84`) — "Heaven's Fury Boots" — `modl`: `'armor\\hf2\\m\\boots.nif'` → `'Armor\\NDPelinal\\M\\NDBoots.NIF'`
- `HeavenFuryCuirassGold` (FormID `004C85`) — "Heaven's Fury Cuirass" — `modl`: `'armor\\hf2\\m\\cuirass.nif'` → `'Armor\\NDPelinal\\M\\NDCuirass.NIF'`
- `HeavenFuryGauntletsGold` (FormID `004C86`) — "Heaven's Fury Gauntlets" — `modl`: `'armor\\hf2\\m\\gauntlets.nif'` → `'Armor\\NDPelinal\\M\\NDGauntlets.NIF'`
- `HeavenFuryGreavesGold` (FormID `004C87`) — "Heaven's Fury Greaves" — `modl`: `'armor\\hf2\\m\\greaves.nif'` → `'Armor\\NDPelinal\\M\\NDGreaves.NIF'`
- `HeavenFuryHelmetGold` (FormID `004C88`) — "Heaven's Fury Helmet" — `modl`: `'armor\\hf2\\helmet.nif'` → `'Armor\\NDPelinal\\M\\NDHelmet.NIF'`
- `HeavenFuryShieldGold` (FormID `004C8A`) — "Heaven's Fury Shield" — `modl`: `'armor\\hf2\\shield.nif'` → `'Armor\\NDPelinal\\M\\NDShield.NIF'`
- `CMIronBattleShield03OOOBosmerGood` (FormID `0077A8`) — "Protector's Insignia Shield" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield003.nif'` → `'Armor\\TownguardBra\\Shield.NIF'`
- `CMIronBattleShield09OOO2` (FormID `00BE58`) — "Ranger's Insignia Shield" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield009.nif'` → `'Armor\\TownguardLe\\Shield.NIF'`
- `ArmorDraconicArmorbootsOOO` (FormID `027156`) — "Dragonborne Boots" — `modl`: `'Armor\\DraconicArmor\\boots.nif'` → `'Armor\\Chainmail\\M\\Boots.NIF'`
- `ArmorDraconicArmorcuirassOOO` (FormID `027157`) — "Dragonborne Cuirass" — `modl`: `'Armor\\DraconicArmor\\cuirass.nif'` → `'Armor\\Chainmail\\M\\Cuirass.NIF'`
- `ArmorDraconicArmorgauntletsOOO` (FormID `027158`) — "Dragonborne Gauntlets" — `modl`: `'Armor\\DraconicArmor\\gauntlets.nif'` → `'Armor\\Chainmail\\M\\Gauntlets.NIF'`
- `ArmorDraconicArmorgreavesOOO` (FormID `027159`) — "Dragonborne Greaves" — `modl`: `'Armor\\DraconicArmor\\greaves.nif'` → `'Armor\\Chainmail\\M\\Greaves.NIF'`
- `ArmorDraconicArmorshieldOOO` (FormID `02715A`) — "Dragonborne Shield" — `modl`: `'Armor\\DraconicArmor\\shield.nif'` → `'Armor\\Chainmail\\Shield.NIF'`

### Book (BOOK) — +35 -0 ~0

**Added:**

- `ZCloudRulerTempleBanditNote` (FormID `0010CB`) — "Recent Disturbances Near Bruma"
- `ZArcticBanditCamp1Note` (FormID `0010D7`) — "Betrayal Note From a Skyrim Bandit"
- `ZArcticBanditCamp4Note` (FormID `001151`) — "Vyka's Change of Plans"
- `ZBook2AnvilReportsFG` (FormID `0042C5`) — "Report on Bosmer Incursions"
- `ZBook4RareMagesGuildNecroInfo` (FormID `004B25`) — "Arch-Mage Traven's Notes"
- `ZMelusPetiliusDiary` (FormID `00677F`) — "A Path of Iron"
- `ZBosmerNoteAny` (FormID `00B5E3`) — "Note From the Brethren of Jephre"
- `ZBosmerCamp2Schedule` (FormID `00B5E4`) — "Smoke Hole Cave Ranger Camp Scroll"
- `ZBosmerCamp1Schedule` (FormID `00B5E5`) — "Strid River Ranger Camp Scroll"
- `ZBosmerCamp3Schedule` (FormID `00B5E6`) — "West Kvatch Ranger Camp Scroll"
- `ZLetterMillonaFromAzzan2b` (FormID `011633`) — "Azzan's Reports to Countess Umbranox"
- `ZNoteAnvilDisturbances` (FormID `011634`) — "Warning to Anvil Citizens and Visitors"
- `ZLetterMillonaToDairihill` (FormID `011B65`) — "Countess Umbranox's Message to Dairihill"
- `ZRaiderHlofortoFaran` (FormID `011BA8`) — "Hlofor's Mission for Faran Hestarius"
- `ZRaiderHlofortoSheil` (FormID `011BA9`) — "Hlofor's Letter to Sheil Hestarius"
- `ZRaiderDasekMoorClue` (FormID `013F7F`) — "Hlofor's Battle Plan"
- `ZNoteBrumaDisturbances` (FormID `014254`) — "Report to Bruma Citizens and Visitors"
- `ZNoteCheydinhallDisturbances` (FormID `01426A`) — "Announcement to Cheydinhal Citizens and Visitors"
- `ZNoteBravilDisturbances` (FormID `0147B2`) — "Warning to Bravil Citizens and Visitors"
- `ZSlaverDerahedFayluBook` (FormID `01ED69`) — "Slaver's Logbook"

_…15 more added omitted (see JSON for full list)_

### Cell (CELL) — +7 -0 ~0

**Added:**

- `SkingradTwoSistersLodgeUpstairs` (FormID `028C91`) — "Two Sisters Lodge Upstairs"
- `Rosulas` (FormID `003594`) — "Rosulas"
- `Rosulas02` (FormID `003769`) — "Rosulas Vasgedal"
- `Varastal` (FormID `003C34`) — "Varastal"
- `TestOOO` (FormID `01CC27`)
- `MarshPunk` (FormID `02EFE5`) — "Dummy cell so GetInCell function will work"
- `ThunderingStepsCave` (FormID `039FAD`) — "Thundering Steps Cave"

### Container (CONT) — +0 -6 ~171

**Removed:**

- `PCDeskClutterMiddle01` (FormID `005136`) — "Desk"
- `PCDeskClutterMiddle02` (FormID `005137`) — "Desk"
- `PCDeskClutterUpper01` (FormID `00514A`) — "Desk"
- `PCDeskClutterUpper02` (FormID `00514B`) — "Desk"
- `PCDeskExecClutter01` (FormID `00515E`) — "Desk"
- `DeskClutterMiddle01` (FormID `024457`) — "Desk"

**Changed:**

- `MG06DeskUpper01` (FormID `06DDA2`) — "LOC_FN_MG06DeskUpper01" — `full`: `'Desk'` → `'LOC_FN_MG06DeskUpper01'`; `modl`: `'harvest\\containers\\XMSharvestUpperDesk01HiFi.nif'` → `'Furniture\\UpperClass\\UpperDesk01.NIF'`
- `ZOOOChestJewelry01NobleT100AlvaUlani` (FormID `001F48`) — "Exquisite Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestUpper01NobleTreasuryLesserT100AmAl` (FormID `001F4A`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestClutterMiddleSame01AsAt` (FormID `001F56`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOOChestClutterMiddleSame02AsAt` (FormID `001F57`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest02LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest02.NIF'`
- `ZOOOChestClutterUpper02AsAt` (FormID `001F58`) — "Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestJewelry01UpperT100Baer` (FormID `001F59`) — "Fine Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestMiddle02UpperArmoryPatneim` (FormID `001F7F`) — "Fine Banded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOOChestJewelry01MiddleCarandial` (FormID `001F80`) — "Common Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestJewelry01UpperT100DovynAren` (FormID `001F89`) — "Fine Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestJewelry01MiddleT100Droshanji` (FormID `001F8B`) — "Common Jewelry Box" — `modl`: `'harvest\\containers\\XMSharvestJewelryChestHiFi.nif'` → `'Clutter\\MiddleClass\\MiddleChestJewelry.NIF'`
- `ZOOOChestMiddle02UpperArmoryDynariAmnis` (FormID `001F8D`) — "Fine Banded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOOChestUpper02NobleClutterDynariAmnis` (FormID `001F8F`) — "Elaborate Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest01LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest01.NIF'`
- `ZOOOChestUpper01NobleAlchemyT100EidKee` (FormID `001F90`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestUpper01NobleArmoryT100EidKee` (FormID `001F92`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestUpper01NobleTreasuryT100EidKee` (FormID `001F93`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestMiddle02UpperArmoryLesserWizT100Glarthir` (FormID `001F98`) — "Rune Banded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest01LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest01.NIF'`
- `ZOOOChestMiddle01UpperTreasuryT100Glarthir` (FormID `001F99`) — "Studded Chest" — `modl`: `'harvest\\containers\\XMSharvestMiddleChest02LoFi.nif'` → `'Clutter\\MiddleClass\\Middlechest02.NIF'`
- `ZOOOChestUpper01NobleTreasuryLesserT100Glarthir` (FormID `001F9A`) — "Elegant Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest02LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest02.NIF'`
- `ZOOOChestUpper02NobleClutterT100Glarthir` (FormID `001F9B`) — "Elaborate Chest" — `modl`: `'harvest\\containers\\XMSharvestUpperChest01LoFi.nif'` → `'Clutter\\UpperClass\\Upperchest01.NIF'`

_…151 more changed omitted (see JSON for full list)_

### Creature (CREA) — +2 -0 ~0

**Added:**

- `OOOGuarMount` (FormID `02EFD4`) — "Tamed Guar"
- `OOOGuarPropMount` (FormID `02EFE0`) — "Tamed Guar"

### Door (DOOR) — +5 -0 ~0

**Added:**

- `AyleidWeapDoor` (FormID `00353D`) — "Wooden Door"
- `OOOARDoor01bVarastal` (FormID `0173D6`) — "Stone Door"
- `DisplayCasePurple01DoorUmbacano` (FormID `02E2B4`) — "Display Case"
- `DisplayCasePurple02DoorUmbacano` (FormID `02E2B5`) — "Display Case"
- `RicketyFenceGateSlavers` (FormID `0356FE`) — "Stick Fence Gate"

### Light (LIGH) — +14 -0 ~0

**Added:**

- `CaveFire900Blue` (FormID `003107`)
- `CaveFire384Blue` (FormID `003108`)
- `Torch02light` (FormID `00341C`)
- `torch04` (FormID `003DEB`) — "Torch"
- `Torchkeyold` (FormID `00651E`) — "Old Torch Key"
- `zOOOTinyCandleLightYellow64flicker` (FormID `00767E`)
- `zOOOMelusPetiliusArmorLight` (FormID `0093B5`)
- `ARBlueGreenIntense800B` (FormID `01FFF3`)
- `ICLightHangIron01OOO` (FormID `024C01`)
- `zOOOLadyOblivionPropLight` (FormID `03494E`)
- `CommonLightRed200` (FormID `044370`)
- `Candelabra01Orange400` (FormID `0483A4`)
- `ARLightRedIntense400` (FormID `04EF3E`)
- `Torch03` (FormID `051331`) — "Torch"

### NPC (NPC_) — +67 -0 ~0

**Added:**

- `DefStaffGuardian` (FormID `0025C5`) — "Hrun Illmouth"
- `ImperialLegionForester5` (FormID `003993`) — "Imperial Legion Forester"
- `Pilgrim01` (FormID `0039D6`) — "Pilgrim of Akatosh"
- `BanditHighwayman05` (FormID `003A18`) — "Highwayman"
- `BanditHighwayman06` (FormID `003A19`) — "Highwayman"
- `SlaveTraderMeleeFemale1` (FormID `0071E0`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale2` (FormID `0071E1`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale3` (FormID `0071E2`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale4` (FormID `0071E3`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale5` (FormID `0071E4`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale6` (FormID `0071E5`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale7` (FormID `0071E6`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale8` (FormID `0071E7`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale9` (FormID `0071E8`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale9A` (FormID `0071E9`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale9B` (FormID `0071EA`) — "Slave Trader Thug"
- `SlaveTraderMeleeFemale9C` (FormID `0071EB`) — "Slave Trader Thug"
- `SlaveTraderMeleeMale1` (FormID `0071EC`) — "Slave Trader Thug"
- `SlaveTraderMeleeMale2` (FormID `0071ED`) — "Slave Trader Thug"
- `SlaveTraderMeleeMale3` (FormID `0071EE`) — "Slave Trader Thug"

_…47 more added omitted (see JSON for full list)_

### AI Package (PACK) — +19 -0 ~0

**Added:**

- `MG13HassildorTalktoPlayer` (FormID `009184`)
- `RegulusTerentiusThrone8x10` (FormID `00A1A9`)
- `DroNahrahDailyAudience` (FormID `00A1AD`)
- `SkingradJanusHassildorDefault` (FormID `02935F`)
- `SkingradJanusHassildorSleep` (FormID `02C465`)
- `MS40HassildorTalktoPlayer` (FormID `03E952`)
- `HannibalTravenAtHome` (FormID `049D1B`)
- `MQ11SkingradCountFindPlayer` (FormID `056E6D`)
- `DAMolagPetiliusSleep` (FormID `0579C0`)
- `TG06SkingradGuardMissing` (FormID `0838D1`)
- `HannibalTravenSleep` (FormID `084B47`)
- `HannibalTraveninCouncilChambers` (FormID `084B48`)
- `HannibalTravenEat` (FormID `084B49`)
- `MS40HassildorSitInChamber` (FormID `09815A`)
- `MS40HassildorTalktoPlayerEnd` (FormID `0A3DF1`)
- `SkingradGuardNightPost03Eat12x3` (FormID `0C9E89`)
- `SkingradGuardNightPost03Relief` (FormID `0C9E8A`)
- `SkingradGuardDayPost04Eat2x3` (FormID `0C9E8B`)
- `SkingradGuardDayPost04Relief` (FormID `0C9E8C`)

### Quest (QUST) — +1 -0 ~0

**Added:**

- `DAMolagBal` (FormID `0146B0`) — "LOC_FN_DAMolagBal"

### Script (SCPT) — +232 -0 ~0

**Added:**

- `3ContJewelAlvaUlvaniTrapYesCrimeYesHiFi01upgNR` (FormID `001F49`)
- `14ContTrapCrimeYesHiFi01NRAlAm` (FormID `001F4B`)
- `14ContTrapNoCrimeYesHiFi01NRArHo` (FormID `001F54`)
- `14ContTrapNoCrimeYesHiFi01AsAt` (FormID `001F55`)
- `3ContJewelBaeralornTrapYesCrimeYesHiFi01upgNR` (FormID `001F5A`)
- `14ContTrapNoCrimeYesHiFi01NRBaer` (FormID `001F5B`)
- `3ContAyleid02aTrapCrimeNoHifi01NRMS92` (FormID `001F5C`)
- `14ContTrapCrimeYesHiFi01NRStolenG` (FormID `001F5D`)
- `14ContTrapNoCrimeYesHiFi01NRPatneim` (FormID `001F7E`)
- `3ContJewelCarandialTrapNoCrimeYesHiFi01upgNR` (FormID `001F81`)
- `14ContTrapNoCrimeYesHiFi01NRClaudisArc` (FormID `001F82`)
- `14ContTrapCrimeYesHiFi01NRAntoinettaM` (FormID `001F84`)
- `14ContTrapNoCrimeYesHiFi01NRMraajDar` (FormID `001F85`)
- `14ContTrapNoCrimeYesHiFi01NRTeinaava` (FormID `001F86`)
- `14ContTrapCrimeYesHiFi01NRDNeville` (FormID `001F87`)
- `14ContTrapNoCrimeYesHiFi01NRTelaendril` (FormID `001F88`)
- `3ContJewelDovynArenTrapYesCrimeYesHiFi01upgNR` (FormID `001F8A`)
- `3ContJewelDroshanjiTrapYesCrimeYesHiFi01upgNR` (FormID `001F8C`)
- `14ContTrapNoCrimeYesHiFi01NRDynariAmnis` (FormID `001F8E`)
- `14ContTrapCrimeYesHiFi01NREidKee` (FormID `001F91`)

_…212 more added omitted (see JSON for full list)_

### Spell (SPEL) — +20 -0 ~0

**Added:**

- `OOODispositionEvilArmor01` (FormID `034954`) — "Disposition From Evil Armor"
- `OOODispositionEvilArmor02` (FormID `034955`) — "Disposition From Evil Armor"
- `OOODispositionEvilArmor03` (FormID `034957`) — "Disposition From Evil Armor"
- `OOODispositionEvilArmor04` (FormID `034959`) — "Disposition From Evil Armor"
- `OOODispositionGoodArmor01` (FormID `03495B`) — "Disposition From Good Armor"
- `OOODispositionGoodArmor02` (FormID `03495D`) — "Disposition From Good Armor"
- `OOODispositionGoodArmor03` (FormID `03495F`) — "Disposition From Good Armor"
- `OOODispositionGoodArmor04` (FormID `034961`) — "Disposition From Good Armor"
- `OOODispositionDreadArmor01` (FormID `03B338`) — "Disposition From Dread Armor"
- `OOODispositionDreadArmor02` (FormID `03B339`) — "Disposition From Dread Armor"
- `OOODispositionDreadArmor03` (FormID `03B33B`) — "Disposition From Dread Armor"
- `OOODispositionDreadArmor04` (FormID `03B33D`) — "Disposition From Dread Armor"
- `OOODispositionShadowArmor01` (FormID `03B345`) — "Disposition From Shadow Armor"
- `OOODispositionShadowArmor02` (FormID `03B850`) — "Disposition From Shadow Armor"
- `OOODispositionShadowArmor03` (FormID `03B851`) — "Disposition From Shadow Armor"
- `OOODispositionShadowArmor04` (FormID `03B853`) — "Disposition From Shadow Armor"
- `OOODispositionLawArmor01` (FormID `03F9B6`) — "Disposition From Law Armor"
- `OOODispositionLawArmor02` (FormID `03F9B7`) — "Disposition From Law Armor"
- `OOODispositionLawArmor03` (FormID `03F9B9`) — "Disposition From Law Armor"
- `OOODispositionLawArmor04` (FormID `03F9BB`) — "Disposition From Law Armor"

## ESP changes — `Oscuro's_Oblivion_Overhaul137.esp`

_No record-level changes detected._

## ESP changes — `Oscuro's_Oblivion_Overhaul137ESM.esp`

_No record-level changes detected._

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

