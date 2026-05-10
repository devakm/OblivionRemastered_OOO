# alpha73 — release notes

_Compared against `alpha71`._

## File-level changes

- Added: 0
- Removed: 0
- Changed: 9

### Changed

- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_ARMO.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_BOOK.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_MISC.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_SGST.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/MagicLoader/Oscuro's_Oblivion_Overhaul_WEAP.json`
- `OblivionRemastered/Content/Dev/ObvData/Data/OptionalPatches/OOO_DeluxeEdition.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/OptionalPatches/SyncMap - DeluxeEdition/Oscuro's_Oblivion_Overhaul.ini`
- `OblivionRemastered/Content/Dev/ObvData/Data/Oscuro's_Oblivion_Overhaul.esp`
- `OblivionRemastered/Content/Dev/ObvData/Data/SyncMap/Oscuro's_Oblivion_Overhaul.ini`

## ESP changes — `Oscuro's_Oblivion_Overhaul.esp`

### Armor (ARMO) — +12 -0 ~0

**Added:**

- `UniqueHarbingerBootsOOO` (FormID `00DE56`) — "LOC_FN_UniqueHarbingerBootsOOO"
- `UniqueHarbingerCuirassOOO` (FormID `00DE57`) — "LOC_FN_UniqueHarbingerCuirassOOO"
- `UniqueHarbingerGauntletsOOO` (FormID `00DE58`) — "LOC_FN_UniqueHarbingerGauntletsOOO"
- `UniqueHarbingerGreavesOOO` (FormID `00DE59`) — "LOC_FN_UniqueHarbingerGreavesOOO"
- `UniqueHarbingerHelmetOOO` (FormID `00DE5A`) — "LOC_FN_UniqueHarbingerHelmetOOO"
- `UniqueHarbingerShieldOOO` (FormID `00DE5B`) — "LOC_FN_UniqueHarbingerShieldOOO"
- `UniqueAncestralBootsOOO` (FormID `00DE61`) — "LOC_FN_UniqueAncestralBootsOOO"
- `UniqueAncestralCuirassOOO` (FormID `00DE62`) — "LOC_FN_UniqueAncestralCuirassOOO"
- `UniqueAncestralGauntletsOOO` (FormID `00DE63`) — "LOC_FN_UniqueAncestralGauntletsOOO"
- `UniqueAncestralGreavesOOO` (FormID `00DE64`) — "LOC_FN_UniqueAncestralGreavesOOO"
- `UniqueAncestralHelmetOOO` (FormID `00DE65`) — "LOC_FN_UniqueAncestralHelmetOOO"
- `UniqueAncestralShieldOOO` (FormID `00DE66`) — "LOC_FN_UniqueAncestralShieldOOO"

### Enchantment (ENCH) — +2 -0 ~0

**Added:**

- `EnAppResistMagickaEpicOOO` (FormID `00DE5C`)
- `PegasusShieldOOO` (FormID `00DE7F`)

### Leveled Item List (LVLI) — +9 -0 ~103

**Added:**

- `SELL0NPCDarkSeducerWeaponLvl100` (FormID `041518`)
- `LL0LootAGoodieGoodie3ArmorHarbinger` (FormID `00DE5D`)
- `LL0LootAGoodieGoodie3weapDark` (FormID `00DE70`)
- `LL0LootAGoodieGoodie4weapMithril` (FormID `00DE7A`)
- `LL0LootAGoodieGoodie4ArmorAncestral` (FormID `00DE7B`)
- `LL0LootAGoodieGoodieCombo` (FormID `00DE82`)
- `LL0LootAGoodieGoodieCombo50` (FormID `00DE83`)
- `LL0LootAGoodieGoodieComboWeap` (FormID `00DE84`)
- `AyleidEnchantmentStones` (FormID `00DE88`)

**Changed:**

- `LL1LootWeapon0Magic100` (FormID `03C7F8`) — + entry: level 1 × 1 → `03C7F6`; + entry: level 1 × 1 → `045EE1`; + entry: level 5 × 1 → `045EE2`; + entry: level 10 × 1 → `045EE1`; + entry: level 10 × 1 → `045EE2`; + entry: level 10 × 1 → `045EE3`; + entry: level 15 × 1 → `045EE3`; + entry: level 15 × 1 → `045EE4`; + entry: level 20 × 1 → `03C7F1`; + entry: level 20 × 1 → `03C7F5`; + entry: level 20 × 1 → `03C7F6`; + entry: level 20 × 1 → `045EE3`; + entry: level 20 × 1 → `045EE4`; + entry: level 20 × 1 → `045EE5`; + entry: level 25 × 1 → `03C7F1`; + entry: level 25 × 1 → `045EE4`; + entry: level 25 × 1 → `045EE5`; + entry: level 25 × 1 → `045EE6`; + entry: level 30 × 1 → `03C7F3`; + entry: level 30 × 1 → `03C7F7`; + entry: level 30 × 1 → `045EE4`; + entry: level 30 × 1 → `045EE5`; + entry: level 30 × 1 → `045EE6`; + entry: level 30 × 1 → `045EE7`; - entry: level 3 × 1 → `03C7F6`; - entry: level 18 × 1 → `03C7F1`; - entry: level 18 × 1 → `03C7F5`; - entry: level 18 × 1 → `03C7F6`; - entry: level 23 × 1 → `03C7F1`; - entry: level 23 × 1 → `03C7F4`; - entry: level 29 × 1 → `03C7F3`; - entry: level 29 × 1 → `03C7F7`
- `SELL1LootWeapon0Magic10` (FormID `045EEA`) — + entry: level 1 × 1 → `03C7F6`; + entry: level 5 × 1 → `03C7F7`; + entry: level 5 × 1 → `045EE2`; + entry: level 10 × 1 → `03C7F5`; + entry: level 10 × 1 → `03C7F6`; + entry: level 10 × 1 → `03C7F7`; + entry: level 10 × 1 → `045EE3`; + entry: level 15 × 1 → `03C7F1`; + entry: level 15 × 1 → `045EE3`; + entry: level 15 × 1 → `045EE4`; + entry: level 20 × 1 → `03C7F1`; + entry: level 20 × 1 → `03C7F3`; + entry: level 20 × 1 → `03C7F5`; + entry: level 20 × 1 → `03C7F6`; + entry: level 20 × 1 → `03C7F7`; + entry: level 20 × 1 → `045EE3`; + entry: level 20 × 1 → `045EE4`; + entry: level 20 × 1 → `045EE5`; + entry: level 25 × 1 → `03C7F1`; + entry: level 25 × 1 → `03C7F4`; + entry: level 25 × 1 → `03C7F5`; + entry: level 25 × 1 → `03C7F6`; + entry: level 25 × 1 → `045EE4`; + entry: level 25 × 1 → `045EE5`; + entry: level 25 × 1 → `045EE6`; + entry: level 30 × 1 → `03C7F1`; + entry: level 30 × 1 → `03C7F2`; + entry: level 30 × 1 → `03C7F3`; + entry: level 30 × 1 → `03C7F7`; + entry: level 30 × 1 → `045EE4`; + entry: level 30 × 1 → `045EE5`; + entry: level 30 × 1 → `045EE6`; + entry: level 30 × 1 → `045EE7`; + entry: level 32 × 1 → `03C7F0`; + entry: level 32 × 1 → `045EE8`; - entry: level 1 × 1 → `045EE2`; - entry: level 5 × 1 → `045EE3`; - entry: level 10 × 1 → `045EE4`; - entry: level 14 × 1 → `045EE3`; - entry: level 14 × 1 → `045EE5`; - entry: level 18 × 1 → `045EE6`; - entry: level 24 × 1 → `045EE4`; - entry: level 24 × 1 → `045EE5`; - entry: level 24 × 1 → `045EE7`; - entry: level 27 × 1 → `045EE4`; - entry: level 27 × 1 → `045EE5`; - entry: level 27 × 1 → `045EE6`; - entry: level 27 × 1 → `045EE7`; - entry: level 30 × 1 → `045EE8`
- `SELL1LootWeapon0Magic100` (FormID `045EEB`) — + entry: level 1 × 1 → `03C7F6`; + entry: level 5 × 1 → `03C7F7`; + entry: level 5 × 1 → `045EE2`; + entry: level 10 × 1 → `03C7F5`; + entry: level 10 × 1 → `03C7F6`; + entry: level 10 × 1 → `03C7F7`; + entry: level 15 × 1 → `03C7F1`; + entry: level 15 × 1 → `045EE3`; + entry: level 15 × 1 → `045EE4`; + entry: level 20 × 1 → `03C7F1`; + entry: level 20 × 1 → `03C7F3`; + entry: level 20 × 1 → `03C7F5`; + entry: level 20 × 1 → `03C7F6`; + entry: level 20 × 1 → `03C7F7`; + entry: level 20 × 1 → `045EE3`; + entry: level 20 × 1 → `045EE4`; + entry: level 20 × 1 → `045EE5`; + entry: level 25 × 1 → `03C7F1`; + entry: level 25 × 1 → `03C7F4`; + entry: level 25 × 1 → `03C7F5`; + entry: level 25 × 1 → `03C7F6`; + entry: level 25 × 1 → `045EE4`; + entry: level 25 × 1 → `045EE5`; + entry: level 25 × 1 → `045EE6`; + entry: level 30 × 1 → `03C7F1`; + entry: level 30 × 1 → `03C7F2`; + entry: level 30 × 1 → `03C7F3`; + entry: level 30 × 1 → `03C7F7`; + entry: level 30 × 1 → `045EE4`; + entry: level 30 × 1 → `045EE5`; + entry: level 30 × 1 → `045EE6`; + entry: level 30 × 1 → `045EE7`; + entry: level 32 × 1 → `03C7F0`; + entry: level 32 × 1 → `045EE8`; - entry: level 1 × 1 → `045EE2`; - entry: level 1 × 1 → `045EE3`; - entry: level 6 × 1 → `045EE4`; - entry: level 12 × 1 → `045EE5`; - entry: level 15 × 1 → `045EE6`; - entry: level 17 × 1 → `045EE4`; - entry: level 19 × 1 → `045EE3`; - entry: level 20 × 1 → `045EE7`; - entry: level 21 × 1 → `045EE5`; - entry: level 24 × 1 → `045EE6`; - entry: level 26 × 1 → `045EE4`; - entry: level 27 × 1 → `045EE4`; - entry: level 27 × 1 → `045EE5`; - entry: level 27 × 1 → `045EE6`; - entry: level 27 × 1 → `045EE7`; - entry: level 27 × 1 → `045EE8`
- `SQ02LL0NPCWeapon0MagicClaymoreLvl100` (FormID `181C66`) — + entry: level 20 × 1 → `03CD01`; + entry: level 30 × 1 → `03CCFE`
- `OOOViDropGolemEbonyHeart` (FormID `00080A`) — + entry: level 1 × 1 → `00225A`
- `OOOViDropGolemGlassHeart` (FormID `00080B`) — + entry: level 1 × 1 → `00225B`
- `OOOViDropGolemIronHeart` (FormID `00080C`) — + entry: level 1 × 1 → `002265`
- `OOOViDropGolemMagmaHeart` (FormID `00080D`) — + entry: level 1 × 1 → `002269`
- `OOOViDropGolemMudHeart` (FormID `00080E`) — + entry: level 1 × 1 → `002270`
- `OOOViDropGolemFleshHeart` (FormID `000816`) — + entry: level 1 × 1 → `002253`
- `OOOViDropGolemMithrilHeart` (FormID `000817`) — + entry: level 1 × 1 → `00226F`
- `OOOViDropGolemGoldHeart` (FormID `000818`) — + entry: level 1 × 1 → `002261`
- `OOOLootJewelry25All` (FormID `0026E4`) — + entry: level 1 × 1 → `00342F`
- `OOOLootJewelry50All` (FormID `0026E9`) — + entry: level 1 × 1 → `00342F`
- `OOOLootGoldSilverNuggets50` (FormID `0026EA`) — + entry: level 1 × 1 → `00D838`
- `OOOLootRing50All` (FormID `0026EB`) — + entry: level 1 × 1 → `038011`; + entry: level 1 × 1 → `038012`; + entry: level 1 × 1 → `038013`; + entry: level 1 × 1 → `038014`; + entry: level 1 × 1 → `038015`; + entry: level 1 × 1 → `038016`; + entry: level 1 × 1 → `038017`; + entry: level 1 × 1 → `038018`; + entry: level 1 × 1 → `038019`; + entry: level 1 × 1 → `03801A`; + entry: level 1 × 1 → `03801B`; + entry: level 1 × 1 → `03801C`; + entry: level 1 × 1 → `03801D`; + entry: level 1 × 1 → `03801E`; + entry: level 1 × 1 → `03801F`; + entry: level 1 × 1 → `038020`; + entry: level 1 × 1 → `038021`; + entry: level 1 × 1 → `038022`; + entry: level 1 × 1 → `038023`; + entry: level 1 × 1 → `038024`; + entry: level 1 × 1 → `038025`; + entry: level 1 × 1 → `038026`; + entry: level 1 × 1 → `00342F`
- `OOOLootRing25All` (FormID `0026EC`) — + entry: level 1 × 1 → `038011`; + entry: level 1 × 1 → `038012`; + entry: level 1 × 1 → `038013`; + entry: level 1 × 1 → `038014`; + entry: level 1 × 1 → `038015`; + entry: level 1 × 1 → `038016`; + entry: level 1 × 1 → `038017`; + entry: level 1 × 1 → `038018`; + entry: level 1 × 1 → `038019`; + entry: level 1 × 1 → `03801A`; + entry: level 1 × 1 → `03801B`; + entry: level 1 × 1 → `03801C`; + entry: level 1 × 1 → `03801D`; + entry: level 1 × 1 → `03801E`; + entry: level 1 × 1 → `03801F`; + entry: level 1 × 1 → `038020`; + entry: level 1 × 1 → `038021`; + entry: level 1 × 1 → `038022`; + entry: level 1 × 1 → `038023`; + entry: level 1 × 1 → `038024`; + entry: level 1 × 1 → `038025`; + entry: level 1 × 1 → `038026`; + entry: level 1 × 1 → `00342F`
- `OOOLootScroll25` (FormID `0026F3`) — + entry: level 1 × 1 → `08C254`; + entry: level 1 × 1 → `08C255`; + entry: level 1 × 1 → `08C256`; + entry: level 1 × 1 → `08C257`; + entry: level 1 × 1 → `08C258`
- `OOOLootScroll10` (FormID `0026F4`) — + entry: level 1 × 1 → `08C254`; + entry: level 1 × 1 → `08C255`; + entry: level 1 × 1 → `08C256`; + entry: level 1 × 1 → `08C257`; + entry: level 1 × 1 → `08C258`
- `OOOLootWeapon100High` (FormID `0026FC`) — + entry: level 1 × 1 → `00DE70`; + entry: level 1 × 1 → `00DE7A`

_…83 more changed omitted (see JSON for full list)_

### Misc Item (MISC) — +0 -0 ~2

**Changed:**

- `WolfPeltWargGiant2` (FormID `029824`) — "LOC_FN_WolfPeltWargGiant2" — `full`: `'Giant Shadow Wolf Pelt'` → `'LOC_FN_WolfPeltWargGiant2'`
- `WolfPelt01Giant` (FormID `02F9FB`) — "LOC_FN_WolfPelt01Giant" — `full`: `'Giant Wolf Pelt'` → `'LOC_FN_WolfPelt01Giant'`

### Script (SCPT) — +1 -0 ~0

**Added:**

- `zOOOFlamingEffectScript` (FormID `00DE81`)

### Sigil Stone (SGST) — +3 -0 ~0

**Added:**

- `AyleidFireDmgFireShld` (FormID `00DE85`) — "LOC_FN_AyleidFireDmgFireShld"
- `AyleidFrostDmgFrostShld` (FormID `00DE86`) — "LOC_FN_AyleidFrostDmgFrostShld"
- `AyleidShockDmgShockShld` (FormID `00DE87`) — "LOC_FN_AyleidShockDmgShockShld"

### Weapon (WEAP) — +18 -0 ~11

**Added:**

- `WeapHarbingerShortswordOOO` (FormID `00DE67`) — "LOC_FN_WeapHarbingerShortswordOOO"
- `WeapHarbingerDaggerOOO` (FormID `00DE68`) — "LOC_FN_WeapHarbingerDaggerOOO"
- `WeapHarbingerLongswordOOO` (FormID `00DE69`) — "LOC_FN_WeapHarbingerLongswordOOO"
- `WeapHarbingerClaymoreOOO` (FormID `00DE6A`) — "LOC_FN_WeapHarbingerClaymoreOOO"
- `WeapHarbingerMaceOOO` (FormID `00DE6B`) — "LOC_FN_WeapHarbingerMaceOOO"
- `WeapHarbingerWarAxeOOO` (FormID `00DE6C`) — "LOC_FN_WeapHarbingerWarAxeOOO"
- `WeapHarbingerBattleAxeOOO` (FormID `00DE6D`) — "LOC_FN_WeapHarbingerBattleAxeOOO"
- `WeapHarbingerWarhammerOOO` (FormID `00DE6E`) — "LOC_FN_WeapHarbingerWarhammerOOO"
- `WeapHarbingerBowOOO` (FormID `00DE6F`) — "LOC_FN_WeapHarbingerBowOOO"
- `WeapRoyalBattleAxeOOO` (FormID `00DE71`) — "LOC_FN_WeapRoyalBattleAxeOOO"
- `WeapRoyalBowOOO` (FormID `00DE72`) — "LOC_FN_WeapRoyalBowOOO"
- `WeapRoyalClaymoreOOO` (FormID `00DE73`) — "LOC_FN_WeapRoyalClaymoreOOO"
- `WeapRoyalDaggerOOO` (FormID `00DE74`) — "LOC_FN_WeapRoyalDaggerOOO"
- `WeapRoyalLongswordOOO` (FormID `00DE75`) — "LOC_FN_WeapRoyalLongswordOOO"
- `WeapRoyalMaceOOO` (FormID `00DE76`) — "LOC_FN_WeapRoyalMaceOOO"
- `WeapRoyalShortswordOOO` (FormID `00DE77`) — "LOC_FN_WeapRoyalShortswordOOO"
- `WeapRoyalWarAxeOOO` (FormID `00DE78`) — "LOC_FN_WeapRoyalWarAxeOOO"
- `WeapRoyalWarhammerOOO` (FormID `00DE79`) — "LOC_FN_WeapRoyalWarhammerOOO"

**Changed:**

- `WeapSODZ` (FormID `018338`) — "LOC_FN_WeapSODZ" — `modl`: `'Weapons\\Dragonsword\\longsword.NIF'` → `'Weapons\\Glass\\MS18Chillrend.NIF'`
- `WeapSeverianBlackHandDaikatana` (FormID `033EF1`) — "LOC_FN_WeapSeverianBlackHandDaikatana" — `modl`: `'Weapons\\SeverianKatana\\blackhanddaikatana.nif'` → `'Weapons\\Akaviri weapon\\Claymore.NIF'`
- `WeapSeverianBlackHandKatana` (FormID `033EF2`) — "LOC_FN_WeapSeverianBlackHandKatana" — `modl`: `'Weapons\\SeverianKatana\\blackhandkatana.nif'` → `'Weapons\\Akaviri weapon\\LongSword.NIF'`
- `WeapSeverianDaedricDaikatana` (FormID `033EF3`) — "LOC_FN_WeapSeverianDaedricDaikatana" — `modl`: `'Weapons\\SeverianKatana\\daedricdaikatana.nif'` → `'Weapons\\Akaviri weapon\\Claymore.NIF'`
- `WeapSeverianDwarvenDaikatana` (FormID `033EF5`) — "LOC_FN_WeapSeverianDwarvenDaikatana" — `modl`: `'Weapons\\SeverianKatana\\dwarvendaikatana.nif'` → `'Weapons\\Akaviri weapon\\Claymore.NIF'`
- `WeapSeverianEbonyDaikatana` (FormID `033EF7`) — "LOC_FN_WeapSeverianEbonyDaikatana" — `modl`: `'Weapons\\SeverianKatana\\ebonydaikatana.nif'` → `'Weapons\\Akaviri weapon\\Claymore.NIF'`
- `WeapSeverianElvenDaikatana` (FormID `033EF9`) — "LOC_FN_WeapSeverianElvenDaikatana" — `modl`: `'Weapons\\SeverianKatana\\elvendaikatana.nif'` → `'Weapons\\Akaviri weapon\\Claymore.NIF'`
- `WeapSeverianGlassDaikatana` (FormID `033EFB`) — "LOC_FN_WeapSeverianGlassDaikatana" — `modl`: `'Weapons\\SeverianKatana\\glassdaikatana.nif'` → `'Weapons\\Akaviri weapon\\Claymore.NIF'`
- `WeapSeverianIronDaikatana` (FormID `033EFD`) — "LOC_FN_WeapSeverianIronDaikatana" — `modl`: `'Weapons\\SeverianKatana\\irondaikatana.nif'` → `'Weapons\\Akaviri weapon\\Claymore.NIF'`
- `WeapSeverianSilverDaikatana` (FormID `033EFF`) — "LOC_FN_WeapSeverianSilverDaikatana" — `modl`: `'Weapons\\Akaviri weapon\\LongSword.NIF'` → `'Weapons\\Akaviri weapon\\Claymore.NIF'`
- `WeapSeverianSteelDaikatana` (FormID `033F01`) — "LOC_FN_WeapSeverianSteelDaikatana" — `modl`: `'Weapons\\SeverianKatana\\steeldaikatana.nif'` → `'Weapons\\Akaviri weapon\\Claymore.NIF'`

## ESP changes — `OOO_DeluxeEdition.esp`

### Faction (FACT) — +2 -0 ~0

**Added:**

- `MythicDawn` (FormID `029F82`) — "LOC_FN_MythicDawn"
- `ZOOOBoars` (FormID `00CD9D`) — "LOC_FN_ZOOOBoars"

### Weapon (WEAP) — +26 -0 ~0

**Added:**

- `DEMShortswordCataclysm1` (FormID `014EC5`) — "LOC_FN_DEMShortswordCataclysm1"
- `DEMShortswordCataclysm2` (FormID `014EC6`) — "LOC_FN_DEMShortswordCataclysm2"
- `DEMDaggerCataclysm3` (FormID `014ECF`) — "LOC_FN_DEMDaggerCataclysm3"
- `DEMLongswordCataclysm2` (FormID `014ED6`) — "LOC_FN_DEMLongswordCataclysm2"
- `DEMMaceCataclysm3` (FormID `014EE7`) — "LOC_FN_DEMMaceCataclysm3"
- `DEMMaceCataclysm5` (FormID `014EE9`) — "LOC_FN_DEMMaceCataclysm5"
- `DEMMaceCataclysm6` (FormID `014EEA`) — "LOC_FN_DEMMaceCataclysm6"
- `DEMMaceCataclysm7` (FormID `014EEB`) — "LOC_FN_DEMMaceCataclysm7"
- `DEMWarAxeCataclysm2` (FormID `014EEE`) — "LOC_FN_DEMWarAxeCataclysm2"
- `DEMBowCataclysm1` (FormID `014F05`) — "LOC_FN_DEMBowCataclysm1"
- `DEMBowCataclysm4` (FormID `014F08`) — "LOC_FN_DEMBowCataclysm4"
- `DEMBowCataclysm5` (FormID `014F09`) — "LOC_FN_DEMBowCataclysm5"
- `DEMBowCataclysm6` (FormID `014F0A`) — "LOC_FN_DEMBowCataclysm6"
- `DEAShortswordOrder1` (FormID `014F0D`) — "LOC_FN_DEAShortswordOrder1"
- `DEAShortswordOrder2` (FormID `014F0E`) — "LOC_FN_DEAShortswordOrder2"
- `DEADaggerOrder3` (FormID `014F17`) — "LOC_FN_DEADaggerOrder3"
- `DEALongswordOrder2` (FormID `014F1E`) — "LOC_FN_DEALongswordOrder2"
- `DEAMaceOrder3` (FormID `014F2F`) — "LOC_FN_DEAMaceOrder3"
- `DEAMaceOrder5` (FormID `014F31`) — "LOC_FN_DEAMaceOrder5"
- `DEAMaceOrder6` (FormID `014F32`) — "LOC_FN_DEAMaceOrder6"

_…6 more added omitted (see JSON for full list)_

## ESP changes — `OOO_OOMC_Compatibility_Patch.esp`

_No record-level changes detected._

## ESP changes — `OOO_UnlimitedRingsReduxPatch.esp`

_No record-level changes detected._

## ESP changes — `OOO_UORP.esp`

_No record-level changes detected._

