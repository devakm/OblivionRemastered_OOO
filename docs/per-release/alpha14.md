# alpha14 — release notes

_Compared against `alpha13`._

## File-level changes

- Added: 2
- Removed: 0
- Changed: 14

### Added

- `Content/Dev/ObvData/Data/OOO_FGD09HistPatch.esp`
- `Content/Dev/ObvData/Data/OOO_NewArmorUnused.esp`

### Changed

- `Content/Dev/ObvData/Data/OOO_NewAmmo04.esp`
- `Content/Dev/ObvData/Data/OOO_NewArmor03.esp`
- `Content/Dev/ObvData/Data/OOO_NewArmor04Amazon.esp`
- `Content/Dev/ObvData/Data/OOO_NewArmorComps.esp`
- `Content/Dev/ObvData/Data/OOO_NewArmorOdds.esp`
- `Content/Dev/ObvData/Data/OOO_NewCreatureComps.esp`
- `Content/Dev/ObvData/Data/OOO_NewQuestsAndRewards.esp`
- `Content/Dev/ObvData/Data/OOO_NewWeaponComps.esp`
- `Content/Dev/ObvData/Data/OOO_NewWeaponCompsBow.esp`
- `Content/Dev/ObvData/Data/OOO_NewWeapons03.esp`
- `Content/Dev/ObvData/Data/OOO_NewWeaponsNoble.esp`
- `Content/Dev/ObvData/Data/OOO_NewWeaponsOdd.esp`
- `Content/Dev/ObvData/Data/OOO_NewWeaponsUnused.esp`
- `Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`

## ESP changes — `OOO_FGD09HistPatch.esp`

_Initial inventory (no prior version to compare against)._

- **Quest (QUST):** 1 records
- **Weapon (WEAP):** 1 records

## ESP changes — `OOO_GameSettings.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewAmmo04.esp`

### Ammunition (AMMO) — +1 -0 ~0

**Added:**

- `drarrowsOOO` (FormID `02714D`) — "Blood Thorn Arrows"

## ESP changes — `OOO_NewAmmoComps.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewArmor.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewArmor03.esp`

### Armor (ARMO) — +40 -1 ~0

**Added:**

- `CMIronBattleShield09OOO` (FormID `001254`) — "Ranger's Insignia Shield"
- `BikCuirassOOO` (FormID `00126C`) — "Amazon Light Cuirass"
- `BikGreavesOOO` (FormID `00126E`) — "Amazon Light Greaves"
- `OOOSEUniqueSunShield` (FormID `00534D`) — "Shield of the Sun"
- `NoblebootsOOO` (FormID `0072EF`) — "Noble Boots"
- `NoblecuirassOOO` (FormID `0072F0`) — "Noble Cuirass"
- `NoblegauntletsOOO` (FormID `0072F1`) — "Noble Gauntlets"
- `NoblegreavesOOO` (FormID `0072F2`) — "Noble Greaves"
- `NobleHelmetOOO` (FormID `0072F3`) — "Noble Helmet"
- `NobleshieldOOO` (FormID `0072F4`) — "Noble Shield"
- `00GRASA01OOO` (FormID `00790C`) — "Amazon's Bronze Armor"
- `00GRASA02OOO` (FormID `00790D`) — "Amazon's Cobalt Armor"
- `00GRASA03OOO` (FormID `00790E`) — "Amazon's Leather Armor"
- `TheSilverDragonArmorPlateOOO` (FormID `02566F`) — "The Dragon's Savior"
- `TheSilverDragonBootsOOO` (FormID `025670`) — "The Dragon's Pace"
- `TheSilverDragonGauntletsOOO` (FormID `025671`) — "The Dragon's Iron Fist"
- `TheSilverDragonGreavesOOO` (FormID `025672`) — "The Dragon's Spellshards"
- `TheSilverDragonHelmetOOO` (FormID `025673`) — "The Dragon's Companion"
- `TheSilverDragonShieldOOO` (FormID `025675`) — "The Dragon's Guardian"
- `SkullShieldHeavyOOO` (FormID `025BBD`) — "Embrace of Doom"

_…20 more added omitted (see JSON for full list)_

**Removed:**

- `CMIronBattleShield09OOO2` (FormID `00BE58`) — "Ranger's Insignia Shield"

### Leveled Item List (LVLI) — +2 -0 ~0

**Added:**

- `LL0CrWeapDremora6Valkynaz100` (FormID `03E9DC`)
- `LL0CrWeapDremora6ValkynazBow100` (FormID `0872B1`)

## ESP changes — `OOO_NewArmor04Amazon.esp`

### Armor (ARMO) — +32 -0 ~5

**Added:**

- `TownguardCuirassSk` (FormID `01DC4B`) — "LOC_FN_TownguardCuirassSk"
- `FurGreaves` (FormID `024764`) — "LOC_FN_FurGreaves"
- `FurGauntlets` (FormID `024765`) — "LOC_FN_FurGauntlets"
- `FurCuirass` (FormID `024766`) — "LOC_FN_FurCuirass"
- `FurBoots` (FormID `024767`) — "LOC_FN_FurBoots"
- `FurHelmet` (FormID `024768`) — "LOC_FN_FurHelmet"
- `FurShield` (FormID `025056`) — "LOC_FN_FurShield"
- `TownguardCuirassAn` (FormID `02766D`) — "LOC_FN_TownguardCuirassAn"
- `TownguardCuirassBra` (FormID `027673`) — "LOC_FN_TownguardCuirassBra"
- `TownguardCuirassBru` (FormID `027677`) — "LOC_FN_TownguardCuirassBru"
- `TownguardCuirassChe` (FormID `027678`) — "LOC_FN_TownguardCuirassChe"
- `TownguardCuirassCho` (FormID `027679`) — "LOC_FN_TownguardCuirassCho"
- `TownguardCuirassKv` (FormID `02767A`) — "LOC_FN_TownguardCuirassKv"
- `TownguardCuirassLe` (FormID `02767B`) — "LOC_FN_TownguardCuirassLe"
- `TownguardHelmet` (FormID `02767C`) — "LOC_FN_TownguardHelmet"
- `TownguardAnShield` (FormID `0352C3`) — "LOC_FN_TownguardAnShield"
- `TownguardBraShield` (FormID `0352C5`) — "LOC_FN_TownguardBraShield"
- `TownguardBruShield` (FormID `0352C7`) — "LOC_FN_TownguardBruShield"
- `TownguardCheShield` (FormID `0352C9`) — "LOC_FN_TownguardCheShield"
- `TownguardChoShield` (FormID `0352CB`) — "LOC_FN_TownguardChoShield"

_…12 more added omitted (see JSON for full list)_

**Changed:**

- `drbootsOOO` (FormID `02714E`) — "Blood Thorn Boots" — `modl`: `'armor\\darkrose\\drboots.nif'` → `'Armor\\Fur\\M\\Boots.NIF'`
- `drgauntOOO` (FormID `027150`) — "Blood Thorn Gauntlets" — `modl`: `'armor\\darkrose\\drgaunt.nif'` → `'Armor\\Fur\\M\\Gauntlets.NIF'`
- `drhelmOOO` (FormID `027152`) — "Blood Thorn Helm" — `modl`: `'armor\\darkrose\\drhelmet.nif'` → `'Armor\\TownguardCho\\Helmet.NIF'`
- `drshieldOOO` (FormID `027154`) — "Dark Thorn Shield" — `modl`: `'armor\\darkrose\\drshield.nif'` → `'Armor\\TownguardKv\\Shield.NIF'`
- `drshield2OOO` (FormID `027155`) — "Blood Thorn Shield" — `modl`: `'armor\\darkrose\\drshield2.nif'` → `'Armor\\TownguardAn\\Shield.NIF'`

## ESP changes — `OOO_NewArmor04Bosmer.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewArmorComps.esp`

### Armor (ARMO) — +35 -16 ~3

**Added:**

- `ArenaRaimentHeavyYellow` (FormID `0236EF`) — "LOC_FN_ArenaRaimentHeavyYellow"
- `ArenaRaimentLightYellow` (FormID `0236F0`) — "LOC_FN_ArenaRaimentLightYellow"
- `ArenaRaimentHeavy` (FormID `029921`) — "LOC_FN_ArenaRaimentHeavy"
- `EbonyCuirass` (FormID `02AD85`) — "LOC_FN_EbonyCuirass"
- `SEGoldenSaintShield1Iron` (FormID `04121C`) — "LOC_FN_SEGoldenSaintShield1Iron"
- `SEGoldenSaintShield2Steel` (FormID `0414FC`) — "LOC_FN_SEGoldenSaintShield2Steel"
- `SEGoldenSaintShield3Dwarven` (FormID `0414FF`) — "LOC_FN_SEGoldenSaintShield3Dwarven"
- `SEGoldenSaintShield4Orcish` (FormID `041502`) — "LOC_FN_SEGoldenSaintShield4Orcish"
- `SEGoldenSaintShield5Ebony` (FormID `041505`) — "LOC_FN_SEGoldenSaintShield5Ebony"
- `SEGoldenSaintShield6Daedric` (FormID `041508`) — "LOC_FN_SEGoldenSaintShield6Daedric"
- `CMIronBattleShield01OOO` (FormID `00124C`) — "Crownblood Iron Shield"
- `CMIronBattleShield02OOO` (FormID `00124D`) — "Nightblood Iron Shield"
- `CMIronBattleShield03OOO` (FormID `00124E`) — "Green and Gold"
- `CMIronBattleShield04OOO` (FormID `00124F`) — "Blue and Red"
- `CMIronBattleShield05OOO` (FormID `001250`) — "Ice Dragon Clan Insignia"
- `CMIronBattleShield06OOO` (FormID `001251`) — "Arctic Wolves' Clan Insignia"
- `CMIronBattleShield07OOO` (FormID `001252`) — "Skyrim Ornate Shield"
- `CMIronBattleShield08OOO` (FormID `001253`) — "Knotblood Iron Shield"
- `CMIronBattleShield10OOO` (FormID `001255`) — "Red and Green Decorative"
- `CMIronBattleShield11OOO` (FormID `001256`) — "Three Wolves' Clan Insignia"

_…15 more added omitted (see JSON for full list)_

**Removed:**

- `TheSilverDragonArmorPlateOOO` (FormID `02566F`) — "The Dragon's Savior"
- `TheSilverDragonBootsOOO` (FormID `025670`) — "The Dragon's Pace"
- `TheSilverDragonGauntletsOOO` (FormID `025671`) — "The Dragon's Iron Fist"
- `TheSilverDragonGreavesOOO` (FormID `025672`) — "The Dragon's Spellshards"
- `TheSilverDragonHelmetOOO` (FormID `025673`) — "The Dragon's Companion"
- `TheSilverDragonMaskOOO` (FormID `025674`) — "The Dragon's Breath"
- `TheSilverDragonShieldOOO` (FormID `025675`) — "The Dragon's Guardian"
- `SkullShieldHeavyOOO` (FormID `025BBD`) — "Embrace of Doom"
- `SkullShieldLightOOO` (FormID `025BBE`) — "Light Silver Skull Shield"
- `HeavyBraidedBootsOOO` (FormID `03DDF3`) — "Heavy Braided Boots"
- `HeavyBraidedCuirassOOO` (FormID `03DDF4`) — "Heavy Braided Cuirass"
- `HeavyBraidedGauntletsOOO` (FormID `03DDF5`) — "Heavy Braided Gauntlets"
- `HeavyBraidedGreavesOOO` (FormID `03DDF6`) — "Heavy Braided Greaves"
- `HeavyBraidedHelmetOOO` (FormID `03DDF7`) — "Heavy Braided Helmet"
- `HeavyBraidedShieldOOO` (FormID `03DDF8`) — "Heavy Braided Shield"
- `TornesBlockadeOOO` (FormID `043D9D`) — "Torne's Blockade"

**Changed:**

- `OOOSEUniqueSunShield` (FormID `00534D`) — "Shield of the Sun" — `modl`: `'OOOSE\\Armor\\Other\\sunshield.nif'` → `'Armor\\GoldenSaint\\Shield.NIF'`
- `ShadowMailHoodOOO` (FormID `038860`) — "Shadowmail Hood" — `modl`: `'armor\\ShadowMail\\hood.nif'` → `'Clothes\\RobeMCBlack\\Hood.NIF'`
- `ShadowMailTunicOOO` (FormID `038862`) — "Shadowmail Tunic" — `modl`: `'armor\\ShadowMail\\m\\rangerarmor.nif'` → `'Armor\\TownguardChe\\M\\Cuirass.NIF'`

## ESP changes — `OOO_NewArmorOdds.esp`

### Armor (ARMO) — +3 -44 ~0

**Added:**

- `ArenaRaimentHeavyYellow` (FormID `0236EF`) — "LOC_FN_ArenaRaimentHeavyYellow"
- `ArenaRaimentLightYellow` (FormID `0236F0`) — "LOC_FN_ArenaRaimentLightYellow"
- `ArenaRaimentHeavy` (FormID `029921`) — "LOC_FN_ArenaRaimentHeavy"

**Removed:**

- `HeavenFuryBoots` (FormID `0046DB`) — "Heaven's Fury Boots"
- `HeavenFuryCuirass` (FormID `0046DC`) — "Heaven's Fury Cuirass"
- `HeavenFuryGauntlets` (FormID `0046DD`) — "Heaven's Fury Gauntlets"
- `HeavenFuryGreaves` (FormID `0046DE`) — "Heaven's Fury Greaves"
- `HeavenFuryHelmet` (FormID `0046DF`) — "Heaven's Fury Helmet"
- `HeavenFuryShield` (FormID `0046E0`) — "Heaven's Fury Shield"
- `HeavenFuryHelmetAlt` (FormID `0046E1`) — "Heaven's Fury Helmet"
- `HeavenFuryHelmetGoldAlt` (FormID `004C89`) — "Heaven's Fury Helmet"
- `NoblebootsOOO` (FormID `0072EF`) — "Noble Boots"
- `NoblecuirassOOO` (FormID `0072F0`) — "Noble Cuirass"
- `NoblegauntletsOOO` (FormID `0072F1`) — "Noble Gauntlets"
- `NoblegreavesOOO` (FormID `0072F2`) — "Noble Greaves"
- `NobleHelmetOOO` (FormID `0072F3`) — "Noble Helmet"
- `NobleshieldOOO` (FormID `0072F4`) — "Noble Shield"
- `1greyfoxsboots` (FormID `0073E7`) — "Gray Fox's Boots"
- `CMIronBattleShield03OOOBosmerGood` (FormID `0077A8`) — "Protector's Insignia Shield"
- `00GRASA01OOO` (FormID `00790C`) — "Amazon's Bronze Armor"
- `00GRASA02OOO` (FormID `00790D`) — "Amazon's Cobalt Armor"
- `00GRASA03OOO` (FormID `00790E`) — "Amazon's Leather Armor"
- `NoblebootsOOOz` (FormID `007D04`) — "Fine Noble Plate Boots"

_…24 more removed omitted (see JSON for full list)_

## ESP changes — `OOO_NewArmorUnused.esp`

_Initial inventory (no prior version to compare against)._

- **Armor (ARMO):** 24 records

## ESP changes — `OOO_NewChestComps.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChests.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChests03.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChests2.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewChestsSkip.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewClothing04.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewClothingComps.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatureComps.esp`

### Creature (CREA) — +9 -0 ~0

**Added:**

- `CreatureHorseBay` (FormID `015B90`) — "LOC_FN_CreatureHorseBay"
- `CreatureHorsePaint` (FormID `015B93`) — "LOC_FN_CreatureHorsePaint"
- `CreatureHorseChestnut` (FormID `01F11C`) — "LOC_FN_CreatureHorseChestnut"
- `CreatureHorseBay1` (FormID `0084EC`) — "Wild Bay Horse"
- `CreatureHorseBay2` (FormID `0084ED`) — "Wild Bay Horse"
- `CreatureHorseChestnut1` (FormID `0084EF`) — "Wild Chestnut Horse"
- `CreatureHorseChestnut2` (FormID `0084F1`) — "Wild Chestnut Horse"
- `CreatureHorsePaint1` (FormID `0084F2`) — "Wild Paint Horse"
- `CreatureHorsePaint2` (FormID `0084F3`) — "Wild Paint Horse"

## ESP changes — `OOO_NewCreatures01.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatures02.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatures03.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewCreatures04Special.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewDoors04.esp`

_No record-level changes detected._

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

_No record-level changes detected._

## ESP changes — `OOO_NewNPCs04Seducer.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewNPCs04Special.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewQuestsAndRewards.esp`

**Master list changed:**

- before: ['Oblivion.esm', "Oscuro's_Oblivion_Overhaul.esp"]
- after:  ['Oblivion.esm', 'DLCHorseArmor.esp', 'Knights.esp', 'AltarDeluxe.esp', "Oscuro's_Oblivion_Overhaul.esp"]

### Creature (CREA) — +4 -0 ~2

**Added:**

- `HorsePCArmoredMehrunesShadowmere` (FormID `014DDF`) — "LOC_FN_HorsePCArmoredMehrunesShadowmere"
- `HorsePCArmoredMehrunesWhiteAnvil` (FormID `014DE0`) — "LOC_FN_HorsePCArmoredMehrunesWhiteAnvil"
- `HorsePCArmoredSteelOldNag` (FormID `0034CA`) — "LOC_FN_HorsePCArmoredSteelOldNag"
- `HorsePCBayBravil` (FormID `04DE8E`) — "LOC_FN_HorsePCBayBravil"

**Changed:**

- `OOOGuarMount` (FormID `02EFD4`) — "Guaroache" — `full`: `'Tamed Guar'` → `'Guaroache'`; `modl`: `'creatures\\OOO_guar\\skeleton.nif'` → `'Creatures\\Horse\\Skeleton.NIF'`
- `OOOGuarPropMount` (FormID `02EFE0`) — "Guaroache" — `full`: `'Tamed Guar'` → `'Guaroache'`; `modl`: `'creatures\\OOO_guar\\skeleton.nif'` → `'Creatures\\Horse\\Skeleton.NIF'`

### Script (SCPT) — +1 -0 ~0

**Added:**

- `HorsePCBayBravilScript` (FormID `04DE92`)

## ESP changes — `OOO_NewRobesComp.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewSigilStones04.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewWeaponComps.esp`

**Master list changed:**

- before: ['Oblivion.esm', 'DLCThievesDen.esp', "Oscuro's_Oblivion_Overhaul.esp"]
- after:  ['Oblivion.esm', 'DLCBattlehornCastle.esp', 'DLCThievesDen.esp', "Oscuro's_Oblivion_Overhaul.esp"]

### Weapon (WEAP) — +53 -27 ~0

**Added:**

- `DLCBattlehornDragonsword05` (FormID `0147F0`) — "LOC_FN_DLCBattlehornDragonsword05"
- `WeapIronShortsword` (FormID `000C0D`) — "LOC_FN_WeapIronShortsword"
- `WeapSteelShortsword` (FormID `0229BC`) — "LOC_FN_WeapSteelShortsword"
- `WeapSteelWarAxe` (FormID `0229BD`) — "LOC_FN_WeapSteelWarAxe"
- `WeapSilverBow` (FormID `025227`) — "LOC_FN_WeapSilverBow"
- `WeapIronBow` (FormID `025231`) — "LOC_FN_WeapIronBow"
- `WeapDaedricBattleAxe` (FormID `035E77`) — "LOC_FN_WeapDaedricBattleAxe"
- `WeapSteelShortswordFine` (FormID `03A85C`) — "LOC_FN_WeapSteelShortswordFine"
- `WeapSteelWarAxeFine` (FormID `03A85D`) — "LOC_FN_WeapSteelWarAxeFine"
- `WeapIronBattleAxeFine` (FormID `03A85F`) — "LOC_FN_WeapIronBattleAxeFine"
- `WeapIronBowFine` (FormID `03A860`) — "LOC_FN_WeapIronBowFine"
- `WeapIronShortswordFine` (FormID `03A865`) — "LOC_FN_WeapIronShortswordFine"
- `WeapClub` (FormID `03B375`) — "LOC_FN_WeapClub"
- `WeapIronShortswordRusty` (FormID `090615`) — "LOC_FN_WeapIronShortswordRusty"
- `rdMithrilWarAxeOOOHoar` (FormID `0010BF`) — "Hang'em"
- `rdKukriOOOBellamont` (FormID `001630`) — "Vengeance"
- `WeapSpiritBattleAxe2` (FormID `00363E`) — "Spectral Battle Axe"
- `WeapSpiritClaymore2` (FormID `00363F`) — "Spectral Claymore"
- `WeapSpiritDagger2` (FormID `003640`) — "Spectral Dagger"
- `WeapSpiritLongsword2` (FormID `003641`) — "Spectral Longsword"

_…33 more added omitted (see JSON for full list)_

**Removed:**

- `WeaponSabreBrightwood1hOOO` (FormID `000D59`) — "Sunwood Shining"
- `WeaponSabreBrightwood1hShortOOO` (FormID `000D5A`) — "Sunwood Whisper"
- `WeaponSabreBrightwood2hOOO` (FormID `000D5B`) — "Sunwood Fury"
- `WeaponSabreBrightwood2hlongOOO` (FormID `000D5C`) — "Sunwood Glory"
- `WeaponSabreEbony1hOOO` (FormID `0083F1`) — "Ebony Shining"
- `WeaponSabreEbony1hShortOOO` (FormID `0083F2`) — "Ebony Whisper"
- `WeaponSabreEbony2hOOO` (FormID `0083F3`) — "Ebony Fury"
- `WeaponSabreEbony2hlongOOO` (FormID `0083F4`) — "Ebony Glory"
- `WeaponSabreElmwood1hOOO` (FormID `0083F5`) — "Elmwood Shining"
- `WeaponSabreElmwood1hShortOOO` (FormID `0083F6`) — "Elmwood Whisper"
- `WeaponSabreElmwood2hOOO` (FormID `0083F7`) — "Elmwood Fury"
- `WeaponSabreElmwood2hlongOOO` (FormID `0083F8`) — "Elmwood Glory"
- `WeaponSabreIvory1hOOO` (FormID `0083F9`) — "Royal Shining"
- `WeaponSabreIvory1hShortOOO` (FormID `0083FA`) — "Royal Whisper"
- `WeaponSabreIvory2hOOO` (FormID `0083FB`) — "Royal Fury"
- `WeaponSabreIvory2hlongOOO` (FormID `0083FC`) — "Royal Glory"
- `WeaponSabreWhiteleather1hOOO` (FormID `0083FD`) — "White Oak Shining"
- `WeaponSabreWhiteleather1hShortOOO` (FormID `0083FE`) — "White Oak Whisper"
- `WeaponSabreWhiteleather2hOOO` (FormID `0083FF`) — "White Oak Fury"
- `WeaponSabreWhiteleather2hlongOOO` (FormID `008400`) — "White Oak Glory"

_…7 more removed omitted (see JSON for full list)_

## ESP changes — `OOO_NewWeaponCompsBow.esp`

### Weapon (WEAP) — +4 -1 ~0

**Added:**

- `WeapSteelBow` (FormID `0229B7`) — "LOC_FN_WeapSteelBow"
- `WeapIronBow` (FormID `025231`) — "LOC_FN_WeapIronBow"
- `WeapSteelBowFine` (FormID `03A857`) — "LOC_FN_WeapSteelBowFine"
- `WeapIronBowFine` (FormID `03A860`) — "LOC_FN_WeapIronBowFine"

**Removed:**

- `drbowOOO` (FormID `02716D`) — "Blood Thorn Bow"

## ESP changes — `OOO_NewWeapons01.esp`

_No record-level changes detected._

## ESP changes — `OOO_NewWeapons03.esp`

### Weapon (WEAP) — +57 -1 ~4

**Added:**

- `WeaponSabreBrightwood1hOOO` (FormID `000D59`) — "Sunwood Shining"
- `WeaponSabreBrightwood1hShortOOO` (FormID `000D5A`) — "Sunwood Whisper"
- `WeaponSabreBrightwood2hOOO` (FormID `000D5B`) — "Sunwood Fury"
- `WeaponSabreBrightwood2hlongOOO` (FormID `000D5C`) — "Sunwood Glory"
- `WeapCommonShortbow02OOO` (FormID `001F18`) — "Worn Shortbow"
- `WeapCommonShortbow01OOO` (FormID `001F19`) — "Shortbow"
- `WeapSpiritBattleAxe2` (FormID `00363E`) — "Spectral Battle Axe"
- `WeapSpiritClaymore2` (FormID `00363F`) — "Spectral Claymore"
- `WeapSpiritDagger2` (FormID `003640`) — "Spectral Dagger"
- `WeapSpiritLongsword2` (FormID `003641`) — "Spectral Longsword"
- `WeapSpiritMace2` (FormID `003642`) — "Spectral Mace"
- `WeapSpiritShortSword2` (FormID `003643`) — "Spectral Shortsword"
- `WeapSpiritWarAxe2` (FormID `003644`) — "Spectral War Axe"
- `WeapSpiritWarhammer2` (FormID `003645`) — "Spectral Warhammer"
- `rdTemplarSwordOOO3` (FormID `003E9E`) — "Worn Templar Longsword"
- `WeapWelkyndSwordShrine` (FormID `004976`) — "Welkynd Sword"
- `WeapHeavenFuryClaymore01` (FormID `007AE6`) — "Heaven's Fury Claymore"
- `WeapHeavenFuryLongsword01` (FormID `007AE7`) — "Heaven's Fury Longsword"
- `WeaponSabreEbony1hOOO` (FormID `0083F1`) — "Ebony Shining"
- `WeaponSabreEbony1hShortOOO` (FormID `0083F2`) — "Ebony Whisper"

_…37 more added omitted (see JSON for full list)_

**Removed:**

- `DAClavicusUmbraSwordOOO` (FormID `044564`) — "Umbra"

**Changed:**

- `TG11WeapAyleidLongswordEnchShock` (FormID `008BA6`) — "Arce Lango" — `modl`: `'weapons\\Meteoric\\metscimitar.nif'` → `'Weapons\\Elven\\LongSword.NIF'`
- `TG11WeapAyleidMaceEnchShock` (FormID `008BA7`) — "Arce Volenbal" — `modl`: `'weapons\\Meteoric\\metmace.nif'` → `'Weapons\\Elven\\Mace.NIF'`
- `TheSilverDragonBowOOO` (FormID `025677`) — "The Dragon's Purification" — `modl`: `'Weapons\\TheSilverDragonOrder\\TheDragonBow.nif'` → `'Weapons\\Silver\\Bow.NIF'`
- `TheSilverDragonSwordOOO` (FormID `025679`) — "The Dragon's Hunger" — `modl`: `'Weapons\\TheSilverDragonOrder\\TheDragonBlade.nif'` → `'Weapons\\Silver\\LongSword.NIF'`

## ESP changes — `OOO_NewWeaponsNoble.esp`

### Weapon (WEAP) — +0 -18 ~0

**Removed:**

- `WeapElvenLongSword` (FormID `0229B3`) — "LOC_FN_WeapElvenLongSword"
- `WeapElvenBow` (FormID `0229BF`) — "LOC_FN_WeapElvenBow"
- `WeapElvenDagger` (FormID `035E63`) — "LOC_FN_WeapElvenDagger"
- `WeapElvenShortsword` (FormID `035E64`) — "LOC_FN_WeapElvenShortsword"
- `WeapElvenWarAxe` (FormID `035E65`) — "LOC_FN_WeapElvenWarAxe"
- `WeapElvenMace` (FormID `035E66`) — "LOC_FN_WeapElvenMace"
- `WeapElvenBattleAxe` (FormID `035E67`) — "LOC_FN_WeapElvenBattleAxe"
- `WeapElvenClaymore` (FormID `035E68`) — "LOC_FN_WeapElvenClaymore"
- `WeapElvenWarHammer` (FormID `035E69`) — "LOC_FN_WeapElvenWarHammer"
- `WeapEbonyDagger` (FormID `035E6A`) — "LOC_FN_WeapEbonyDagger"
- `WeapEbonyShortsword` (FormID `035E6B`) — "LOC_FN_WeapEbonyShortsword"
- `WeapEbonyWarAxe` (FormID `035E6C`) — "LOC_FN_WeapEbonyWarAxe"
- `WeapEbonyMace` (FormID `035E6D`) — "LOC_FN_WeapEbonyMace"
- `WeapEbonyLongsword` (FormID `035E6E`) — "LOC_FN_WeapEbonyLongsword"
- `WeapEbonyBattleAxe` (FormID `035E6F`) — "LOC_FN_WeapEbonyBattleAxe"
- `WeapEbonyClaymore` (FormID `035E70`) — "LOC_FN_WeapEbonyClaymore"
- `WeapEbonyWarHammer` (FormID `035E71`) — "LOC_FN_WeapEbonyWarHammer"
- `WeapEbonyBow` (FormID `035E7B`) — "LOC_FN_WeapEbonyBow"

## ESP changes — `OOO_NewWeaponsOdd.esp`

### Weapon (WEAP) — +0 -46 ~0

**Removed:**

- `WeapCommonShortbow02OOO` (FormID `001F18`) — "Worn Shortbow"
- `WeapCommonShortbow01OOO` (FormID `001F19`) — "Shortbow"
- `WeapSpiritBattleAxe2` (FormID `00363E`) — "Spectral Battle Axe"
- `WeapSpiritClaymore2` (FormID `00363F`) — "Spectral Claymore"
- `WeapSpiritDagger2` (FormID `003640`) — "Spectral Dagger"
- `WeapSpiritLongsword2` (FormID `003641`) — "Spectral Longsword"
- `WeapSpiritMace2` (FormID `003642`) — "Spectral Mace"
- `WeapSpiritShortSword2` (FormID `003643`) — "Spectral Shortsword"
- `WeapSpiritWarAxe2` (FormID `003644`) — "Spectral War Axe"
- `WeapSpiritWarhammer2` (FormID `003645`) — "Spectral Warhammer"
- `rdTemplarSwordOOO3` (FormID `003E9E`) — "Worn Templar Longsword"
- `WeapWelkyndSwordShrine` (FormID `004976`) — "Welkynd Sword"
- `WeapHeavenFuryClaymore01` (FormID `007AE6`) — "Heaven's Fury Claymore"
- `WeapHeavenFuryLongsword01` (FormID `007AE7`) — "Heaven's Fury Longsword"
- `AyleidStaffEnchMasterOpen` (FormID `00BB55`) — "Latar Andavar"
- `WeapDaedricScimitarOOO` (FormID `00BFFA`) — "Daedric Scimitar"
- `WeapDwarvenScimitarOOO` (FormID `00BFFB`) — "Dwemer Scimitar"
- `WeapGlassScimitarOOO` (FormID `00BFFE`) — "Glass Scimitar"
- `WeapIronScimitarOOO` (FormID `00BFFF`) — "Iron Scimitar"
- `WeapSilverScimitarOOO` (FormID `00C000`) — "Silver Scimitar"

_…26 more removed omitted (see JSON for full list)_

## ESP changes — `OOO_NewWeaponsUnused.esp`

### Weapon (WEAP) — +1 -0 ~0

**Added:**

- `DAClavicusUmbraSwordOOO` (FormID `044564`) — "Umbra"

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Ammunition (AMMO) — +0 -0 ~1

**Changed:**

- `drarrowsOOO` (FormID `02714D`) — "Blood Thorn Arrows" — `modl`: `'weapons\\drbow\\drquiver.nif'` → `'Weapons\\Silver\\Arrow.NIF'`

### Armor (ARMO) — +0 -0 ~38

**Changed:**

- `CMIronBattleShield09OOO` (FormID `001254`) — "Ranger's Insignia Shield" — `modl`: `'Armor\\CMBattleShields\\CMBattleShield009.nif'` → `'Armor\\TownguardLe\\Shield.NIF'`
- `OOOSEUniqueSunShield` (FormID `00534D`) — "Shield of the Sun" — `modl`: `'OOOSE\\Armor\\Other\\sunshield.nif'` → `'Armor\\GoldenSaint\\Shield.NIF'`
- `NoblebootsOOO` (FormID `0072EF`) — "Noble Boots" — `modl`: `'armor\\Noble Plate\\m\\nobleboots.nif'` → `'Armor\\Ebony\\M\\Boots.NIF'`
- `NoblecuirassOOO` (FormID `0072F0`) — "Noble Cuirass" — `modl`: `'armor\\Noble Plate\\m\\noblecuirass.nif'` → `'Armor\\Ebony\\M\\Cuirass.NIF'`
- `NoblegauntletsOOO` (FormID `0072F1`) — "Noble Gauntlets" — `modl`: `'armor\\Noble Plate\\m\\noblegauntlets.nif'` → `'Armor\\Ebony\\M\\Gauntlets.NIF'`
- `NoblegreavesOOO` (FormID `0072F2`) — "Noble Greaves" — `modl`: `'armor\\Noble Plate\\m\\noblegreaves.nif'` → `'Armor\\Ebony\\M\\Greaves.NIF'`
- `NobleHelmetOOO` (FormID `0072F3`) — "Noble Helmet" — `modl`: `'armor\\Noble Plate\\m\\noblehelmet.nif'` → `'Armor\\Ebony\\M\\Helmet.NIF'`
- `NobleshieldOOO` (FormID `0072F4`) — "Noble Shield" — `modl`: `'armor\\Noble Plate\\nobleshield.nif'` → `'Armor\\Ebony\\Shield.NIF'`
- `00GRASA01OOO` (FormID `00790C`) — "Amazon's Bronze Armor" — `modl`: `'armor\\growlf\\Sexychamp\\fullbody\\gold\\sexychamp.nif'` → `'Armor\\ArenaHeavyYellow\\M\\Cuirass.NIF'`
- `00GRASA02OOO` (FormID `00790D`) — "Amazon's Cobalt Armor" — `modl`: `'armor\\growlf\\Sexychamp\\fullbody\\iron\\sexychamp.nif'` → `'Armor\\ArenaHeavyBlue\\M\\Cuirass.NIF'`
- `00GRASA03OOO` (FormID `00790E`) — "Amazon's Leather Armor" — `modl`: `'armor\\growlf\\Sexychamp\\fullbody\\leather\\sexychamp.nif'` → `'Armor\\ArenaLightYellow\\M\\Cuirass.NIF'`
- `TheSilverDragonArmorPlateOOO` (FormID `02566F`) — "The Dragon's Savior" — `modl`: `'armor\\TheSilverDragonOrder\\m\\cuirass.nif'` → `'Armor\\Orcish\\M\\Cuirass.NIF'`
- `TheSilverDragonBootsOOO` (FormID `025670`) — "The Dragon's Pace" — `modl`: `'armor\\TheSilverDragonOrder\\m\\boots.nif'` → `'Armor\\Orcish\\M\\Boots.NIF'`
- `TheSilverDragonGauntletsOOO` (FormID `025671`) — "The Dragon's Iron Fist" — `modl`: `'armor\\TheSilverDragonOrder\\m\\gauntlets.nif'` → `'Armor\\Orcish\\M\\Gauntlets.NIF'`
- `TheSilverDragonGreavesOOO` (FormID `025672`) — "The Dragon's Spellshards" — `modl`: `'armor\\TheSilverDragonOrder\\m\\greaves.nif'` → `'Armor\\Orcish\\M\\Greaves.NIF'`
- `TheSilverDragonHelmetOOO` (FormID `025673`) — "The Dragon's Companion" — `modl`: `'armor\\TheSilverDragonOrder\\helmet2.nif'` → `'Armor\\Orcish\\Helmet.NIF'`
- `TheSilverDragonShieldOOO` (FormID `025675`) — "The Dragon's Guardian" — `modl`: `'armor\\TheSilverDragonOrder\\shield.nif'` → `'Armor\\Orcish\\Shield.NIF'`
- `SkullShieldHeavyOOO` (FormID `025BBD`) — "Embrace of Doom" — `modl`: `'armor\\skull\\shield.nif'` → `'Armor\\TownguardSk\\Shield.NIF'`
- `drbootsOOO` (FormID `02714E`) — "Blood Thorn Boots" — `modl`: `'armor\\darkrose\\drboots.nif'` → `'Armor\\Fur\\M\\Boots.NIF'`
- `drgauntOOO` (FormID `027150`) — "Blood Thorn Gauntlets" — `modl`: `'armor\\darkrose\\drgaunt.nif'` → `'Armor\\Fur\\M\\Gauntlets.NIF'`

_…18 more changed omitted (see JSON for full list)_

### Book (BOOK) — +1 -0 ~0

**Added:**

- `Book4RareChildrenoftheSky` (FormID `024587`) — "LOC_FN_Book4RareChildrenoftheSky"

### Creature (CREA) — +0 -0 ~2

**Changed:**

- `OOOGuarMount` (FormID `02EFD4`) — "Guaroache" — `full`: `'Tamed Guar'` → `'Guaroache'`; `modl`: `'creatures\\OOO_guar\\skeleton.nif'` → `'Creatures\\Horse\\Skeleton.NIF'`
- `OOOGuarPropMount` (FormID `02EFE0`) — "Guaroache" — `full`: `'Tamed Guar'` → `'Guaroache'`; `modl`: `'creatures\\OOO_guar\\skeleton.nif'` → `'Creatures\\Horse\\Skeleton.NIF'`

### Dialogue Topic (DIAL) — +16 -0 ~0

**Added:**

- `zOOOFollow` (FormID `007B53`) — "Follow"
- `zOOOCrackedWood` (FormID `00833D`) — "Cracked Wood Cave"
- `zOOOFatback` (FormID `00833F`) — "Fatback Cave"
- `zOOOYes` (FormID `008341`) — "Sure!"
- `zOOONo` (FormID `008342`) — "No, I don't think so."
- `zOOOJim` (FormID `008345`) — "Brother Jim"
- `zOOODBRingElite` (FormID `0097CD`) — "Dragonborne Elite Ring"
- `zOOODBRing` (FormID `0097CE`) — "Dragonborne Ring"
- `zOOOGoblinJim` (FormID `00C0C6`) — "He joined a goblin tribe"
- `zOOOKnight` (FormID `00C0C8`) — "Knight of the Dragonborne"
- `zOOOQuestStill` (FormID `00C0CD`) — "I'm working on it"
- `zOOOQuestDone` (FormID `00C0CE`) — "The goblin tribes are no more!"
- `zOOOShields` (FormID `0119D9`) — "Goblin Shield"
- `zOOOTotem` (FormID `0120AD`) — "Goblin Totem"
- `GuarMountTopic` (FormID `02EFE3`) — "Purchase Guar for 3000 drakes, "
- `zOOORandomGoblins` (FormID `06E9FF`) — "Goblin menace"

### Faction (FACT) — +0 -0 ~38

**Changed:**

- `AmazonFaction` (FormID `00491B`) — "Amazons" — `full`: `''` → `'Amazons'`
- `ValenBosmer` (FormID `004E16`) — "ValenWood Bosmer" — `full`: `''` → `'ValenWood Bosmer'`
- `OscuroUOPHackdirtVillagers` (FormID `005D78`) — "UOP-added Hackdirt Villagers (non-Brethren)" — `full`: `''` → `'UOP-added Hackdirt Villagers (non-Brethren)'`
- `SlaveTraderFaction` (FormID `007064`) — "Slave Traders" — `full`: `''` → `'Slave Traders'`
- `ArgonianBlackMarshFaction` (FormID `00722E`) — "Black Marsh Smuggler Faction" — `full`: `''` → `'Black Marsh Smuggler Faction'`
- `ValenBosmerGood` (FormID `00779E`) — "Bosmer Protectors" — `full`: `''` → `'Bosmer Protectors'`
- `zzOOODragonborneKnights` (FormID `00831F`) — "Knights of the Dragonborne" — `full`: `''` → `'Knights of the Dragonborne'`
- `ZOOOBears` (FormID `00CD9C`) — "Yogi Faction" — `full`: `''` → `'Yogi Faction'`
- `ZOOOBoars` (FormID `00CD9D`) — "Cochino Faction" — `full`: `''` → `'Cochino Faction'`
- `ZOOODeers` (FormID `00CD9E`) — "Bambi Faction" — `full`: `''` → `'Bambi Faction'`
- `ZOOOCougars` (FormID `00CD9F`) — "Puma Faction" — `full`: `''` → `'Puma Faction'`
- `ZOOOMinotaurs` (FormID `00CDA0`) — "King Minos Faction" — `full`: `''` → `'King Minos Faction'`
- `ZOOOOgres` (FormID `00CDA1`) — "Ann Coulter Faction" — `full`: `''` → `'Ann Coulter Faction'`
- `ZOOOSpriggan` (FormID `00CDA2`) — "Eeeeeeeennt Faction" — `full`: `''` → `'Eeeeeeeennt Faction'`
- `ZOOOSlaughterfish` (FormID `00CDA3`) — "Jaws Faction" — `full`: `''` → `'Jaws Faction'`
- `ZOOORats` (FormID `00CDA4`) — "Micky's Faction" — `full`: `''` → `"Micky's Faction"`
- `ZOOOWillowisps` (FormID `00CDA5`) — "Greater Lightstone Faction" — `full`: `''` → `'Greater Lightstone Faction'`
- `ZOOOSheep` (FormID `00CDA6`) — "Hill-Billies' Consolation Faction" — `full`: `''` → `"Hill-Billies' Consolation Faction"`
- `ZOOOMudcrabs` (FormID `00CDA7`) — "STD Scare Faction" — `full`: `''` → `'STD Scare Faction'`
- `ZOOOWolves` (FormID `00CDA8`) — "Kevin's Faction" — `full`: `''` → `"Kevin's Faction"`

_…18 more changed omitted (see JSON for full list)_

### Leveled Item List (LVLI) — +3 -0 ~43

**Added:**

- `LL0CrWeapDremora6Valkynaz100` (FormID `03E9DC`)
- `SE39LLAllSkillBooks` (FormID `07DE9E`)
- `LL0CrWeapDremora6ValkynazBow100` (FormID `0872B1`)

**Changed:**

- `LL0NPCArmorHeavyHelmet100` (FormID `033EAD`) — + entry: level 1 × 1 → `001C54`; + entry: level 4 × 1 → `021BC5`; + entry: level 6 × 1 → `021BC5`; + entry: level 8 × 1 → `021BC5`; + entry: level 24 × 1 → `00CFD2`; + entry: level 25 × 1 → `0025F4`; + entry: level 27 × 1 → `001210`; + entry: level 27 × 1 → `0025F4`; + entry: level 27 × 1 → `021BC5`; + entry: level 32 × 1 → `00CFD2`; - entry: level 1 × 1 → `01C6CE`; - entry: level 4 × 1 → `0229A4`; - entry: level 25 × 1 → `03634B`; - entry: level 32 × 1 → `036351`
- `LL0NPCArmorHeavyGreaves50` (FormID `033EB6`) — + entry: level 1 × 1 → `001C52`; + entry: level 4 × 1 → `01C6D0`; + entry: level 4 × 1 → `021BC4`; + entry: level 6 × 1 → `01C6D0`; + entry: level 6 × 1 → `0229A3`; + entry: level 6 × 1 → `021BC4`; + entry: level 8 × 1 → `01C6D0`; + entry: level 8 × 1 → `0229A3`; + entry: level 8 × 1 → `021BC4`; + entry: level 10 × 1 → `0229A3`; + entry: level 10 × 1 → `003288`; + entry: level 12 × 1 → `001205`; + entry: level 12 × 1 → `003287`; + entry: level 12 × 1 → `021BC4`; + entry: level 15 × 1 → `036348`; + entry: level 16 × 1 → `0229A3`; + entry: level 16 × 1 → `003286`; + entry: level 17 × 1 → `002AF0`; + entry: level 18 × 1 → `036348`; + entry: level 18 × 1 → `003285`; + entry: level 20 × 1 → `0229A3`; + entry: level 20 × 1 → `03634E`; + entry: level 20 × 1 → `001205`; + entry: level 20 × 1 → `021BC4`; + entry: level 22 × 1 → `036348`; + entry: level 24 × 1 → `003284`; + entry: level 24 × 1 → `00CFD1`; + entry: level 25 × 1 → `002AF0`; + entry: level 27 × 1 → `0229A3`; + entry: level 27 × 1 → `036348`; + entry: level 27 × 1 → `03634E`; + entry: level 27 × 1 → `001205`; + entry: level 27 × 1 → `002AF0`; + entry: level 27 × 1 → `021BC4`; + entry: level 29 × 1 → `036354`; + entry: level 29 × 1 → `003283`; + entry: level 32 × 1 → `00CFD1`; + entry: level 34 × 1 → `036354`; + entry: level 35 × 1 → `03635A`; + entry: level 35 × 1 → `003282`; - entry: level 1 × 1 → `033EAC`
- `LL0NPCArmorHeavyShield100` (FormID `03405D`) — + entry: level 32 × 1 → `00CFD3`
- `LL0NPCArmorHeavyShield25` (FormID `034060`) — + entry: level 32 × 1 → `00CFD3`
- `LL0NPCArmorHeavyShieldLvl100` (FormID `034061`) — + entry: level 24 × 1 → `00CFD3`
- `LL0NPCArmorHeavyShieldLvl25` (FormID `034062`) — + entry: level 24 × 1 → `00CFD3`
- `LL0NPCArmorHeavyShieldLvl50` (FormID `034063`) — + entry: level 24 × 1 → `00CFD3`
- `LL0NPCArmorHeavyShieldLvl75` (FormID `034064`) — + entry: level 24 × 1 → `00CFD3`
- `LL0Book4Rare50` (FormID `0A497F`) — + entry: level 1 × 1 → `003FBC`; + entry: level 1 × 1 → `051315`; - entry: level 1 × 1 → `024587`
- `LL0NPCArmorHeavyHelmet100at35` (FormID `00327A`) — + entry: level 1 × 1 → `001210`; + entry: level 1 × 1 → `0025F4`; + entry: level 1 × 1 → `00CFD2`; + entry: level 1 × 1 → `021BC5`
- `LL0NPCArmorHeavyHelmet100at29` (FormID `00327B`) — + entry: level 1 × 1 → `001210`; + entry: level 1 × 1 → `0025F4`; + entry: level 1 × 1 → `00CFD2`; + entry: level 1 × 1 → `021BC5`
- `LL0NPCArmorHeavyHelmet100at24` (FormID `00327C`) — + entry: level 1 × 1 → `001210`; + entry: level 1 × 1 → `0025F4`; + entry: level 1 × 1 → `00CFD2`; + entry: level 1 × 1 → `021BC5`
- `LL0NPCArmorHeavyHelmet100at18` (FormID `00327D`) — + entry: level 1 × 1 → `001210`; + entry: level 1 × 1 → `0025F4`; + entry: level 1 × 1 → `021BC5`
- `LL0NPCArmorHeavyHelmet100at16` (FormID `00327E`) — + entry: level 1 × 1 → `001210`; + entry: level 1 × 1 → `0025F4`; + entry: level 1 × 1 → `021BC5`
- `LL0NPCArmorHeavyHelmet100at12` (FormID `00327F`) — + entry: level 1 × 1 → `001210`; + entry: level 1 × 1 → `021BC5`
- `LL0NPCArmorHeavyHelmet100at10` (FormID `003280`) — + entry: level 1 × 1 → `001210`; + entry: level 1 × 1 → `021BC5`
- `LL0NPCArmorHeavyGreaves100at35` (FormID `003282`) — + entry: level 1 × 1 → `001205`; + entry: level 1 × 1 → `002AF0`; + entry: level 1 × 1 → `00CFD1`; + entry: level 1 × 1 → `021BC4`
- `LL0NPCArmorHeavyGreaves100at29` (FormID `003283`) — + entry: level 1 × 1 → `001205`; + entry: level 1 × 1 → `002AF0`; + entry: level 1 × 1 → `00CFD1`; + entry: level 1 × 1 → `021BC4`
- `LL0NPCArmorHeavyGreaves100at24` (FormID `003284`) — + entry: level 1 × 1 → `001205`; + entry: level 1 × 1 → `002AF0`; + entry: level 1 × 1 → `00CFD1`; + entry: level 1 × 1 → `021BC4`
- `LL0NPCArmorHeavyGreaves100at18` (FormID `003285`) — + entry: level 1 × 1 → `001205`; + entry: level 1 × 1 → `002AF0`; + entry: level 1 × 1 → `021BC4`

_…23 more changed omitted (see JSON for full list)_

### Quest (QUST) — +1 -0 ~0

**Added:**

- `FGD09Hist` (FormID `0356CA`) — "LOC_FN_FGD09Hist"

### Weapon (WEAP) — +0 -0 ~60

**Changed:**

- `WeaponSabreBrightwood1hOOO` (FormID `000D59`) — "Sunwood Shining" — `modl`: `'Weapons\\Adonnay\\sabre_1h.nif'` → `'Weapons\\Elven\\LongSword.NIF'`
- `WeaponSabreBrightwood1hShortOOO` (FormID `000D5A`) — "Sunwood Whisper" — `modl`: `'Weapons\\Adonnay\\sabre_1h_short.nif'` → `'Weapons\\Elven\\ShortSword.NIF'`
- `WeaponSabreBrightwood2hOOO` (FormID `000D5B`) — "Sunwood Fury" — `modl`: `'Weapons\\Adonnay\\sabre_2h.nif'` → `'Weapons\\Elven\\Claymore.NIF'`
- `WeaponSabreBrightwood2hlongOOO` (FormID `000D5C`) — "Sunwood Glory" — `modl`: `'Weapons\\Adonnay\\sabre_2h_long.nif'` → `'Weapons\\Elven\\Claymore.NIF'`
- `WeapCommonShortbow02OOO` (FormID `001F18`) — "Worn Shortbow" — `modl`: `'Weapons\\Adonnay\\Bows\\shortbow02.nif'` → `'Weapons\\Iron\\Bow.NIF'`
- `WeapCommonShortbow01OOO` (FormID `001F19`) — "Shortbow" — `modl`: `'Weapons\\Adonnay\\Bows\\shortbow01.nif'` → `'Weapons\\Steel\\Bow.NIF'`
- `WeapSpiritBattleAxe2` (FormID `00363E`) — "Spectral Battle Axe" — `modl`: `'Weapons\\SpiritWeapons\\battleaxefine.nif'` → `'Weapons\\Steel\\BattleAxeFine.NIF'`
- `WeapSpiritClaymore2` (FormID `00363F`) — "Spectral Claymore" — `modl`: `'Weapons\\SpiritWeapons\\claymorefine.nif'` → `'Weapons\\Steel\\ClaymoreFine.NIF'`
- `WeapSpiritDagger2` (FormID `003640`) — "Spectral Dagger" — `modl`: `'Weapons\\SpiritWeapons\\daggerfine.nif'` → `'Weapons\\Steel\\DaggerFine.NIF'`
- `WeapSpiritLongsword2` (FormID `003641`) — "Spectral Longsword" — `modl`: `'Weapons\\SpiritWeapons\\longswordfine.nif'` → `'Weapons\\Steel\\LongswordFine.NIF'`
- `WeapSpiritMace2` (FormID `003642`) — "Spectral Mace" — `modl`: `'Weapons\\SpiritWeapons\\macefine.nif'` → `'Weapons\\Steel\\MaceFine.NIF'`
- `WeapSpiritShortSword2` (FormID `003643`) — "Spectral Shortsword" — `modl`: `'Weapons\\SpiritWeapons\\shortswordfine.nif'` → `'Weapons\\Steel\\ShortswordFine.NIF'`
- `WeapSpiritWarAxe2` (FormID `003644`) — "Spectral War Axe" — `modl`: `'Weapons\\SpiritWeapons\\waraxefine.nif'` → `'Weapons\\Steel\\WarAxeFine.NIF'`
- `WeapSpiritWarhammer2` (FormID `003645`) — "Spectral Warhammer" — `modl`: `'Weapons\\SpiritWeapons\\warhammerfine.nif'` → `'Weapons\\Steel\\WarhammerFine.NIF'`
- `rdTemplarSwordOOO3` (FormID `003E9E`) — "Worn Templar Longsword" — `modl`: `'Weapons\\RD\\rdtemplarsword.nif'` → `'Weapons\\Steel\\LongswordFine.NIF'`
- `WeapWelkyndSwordShrine` (FormID `004976`) — "Welkynd Sword" — `modl`: `'RD\\rdwelkynd.nif'` → `'Weapons\\Elven\\LongSword.NIF'`
- `ArcticBowOOO` (FormID `005BCC`) — "Arctic Bow" — `modl`: `'weapons\\arctic\\bow.nif'` → `'Weapons\\Silver\\Bow.NIF'`
- `WeapHeavenFuryClaymore01` (FormID `007AE6`) — "Heaven's Fury Claymore" — `modl`: `'Weapons\\hf2\\claymorefine.nif'` → `'Weapons\\Silver\\Claymore.NIF'`
- `WeapHeavenFuryLongsword01` (FormID `007AE7`) — "Heaven's Fury Longsword" — `modl`: `'Weapons\\hf2\\longswordfine.nif'` → `'Weapons\\Silver\\LongSword.NIF'`
- `WeaponSabreEbony1hOOO` (FormID `0083F1`) — "Ebony Shining" — `modl`: `'Weapons\\Adonnay\\ebony_sabre_1h.nif'` → `'Weapons\\Elven\\LongSword.NIF'`

_…40 more changed omitted (see JSON for full list)_

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

