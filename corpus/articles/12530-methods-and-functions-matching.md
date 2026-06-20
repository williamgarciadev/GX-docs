---
title: "Methods and Functions matching"
source_id: 12530
source_url: https://wiki.genexus.com/commwiki/wiki?12530
genexus_version: "18"
---

# Methods and Functions matching

Some GeneXus Functions have a Method with the same meaning and behavior.

### [Date and DateTime functions](#Date+and+DateTime+functions)

|  |  |
| --- | --- |
| **Function** | **Method** |
| [Day](https://wiki.genexus.com/commwiki/wiki?8376) | [Day](https://wiki.genexus.com/commwiki/wiki?12646) |
| [Month](https://wiki.genexus.com/commwiki/wiki?8379) | [Month](https://wiki.genexus.com/commwiki/wiki?12647) |
| [Year](https://wiki.genexus.com/commwiki/wiki?8380) | [Year](https://wiki.genexus.com/commwiki/wiki?12648) |
| [Hour](https://wiki.genexus.com/commwiki/wiki?8415) | [Hour](https://wiki.genexus.com/commwiki/wiki?12652) |
| [Minute](https://wiki.genexus.com/commwiki/wiki?8416) | [Minute](https://wiki.genexus.com/commwiki/wiki?12650) |
| [Second](https://wiki.genexus.com/commwiki/wiki?8417) | [Second](https://wiki.genexus.com/commwiki/wiki?12651) |
| [Eom](https://wiki.genexus.com/commwiki/wiki?8392) | [EndOfMonth](https://wiki.genexus.com/commwiki/wiki?12656) |
| [Dow](https://wiki.genexus.com/commwiki/wiki?8344) | [DayOfWeek](https://wiki.genexus.com/commwiki/wiki?12657) |
| [Addyr](https://wiki.genexus.com/commwiki/wiki?8317) | [AddYear](https://wiki.genexus.com/commwiki/wiki?12673) |
| [Addmth](https://wiki.genexus.com/commwiki/wiki?8314) | [AddMonths](https://wiki.genexus.com/commwiki/wiki?12674) |
| [Tadd](https://wiki.genexus.com/commwiki/wiki?8512) | [AddSeconds](https://wiki.genexus.com/commwiki/wiki?12676) |
| [Age](https://wiki.genexus.com/commwiki/wiki?8330) | [Age](https://wiki.genexus.com/commwiki/wiki?12687) |
| [Tdiff](https://wiki.genexus.com/commwiki/wiki?8513) | [Difference](https://wiki.genexus.com/commwiki/wiki?12677) |
| [Ymdtod](https://wiki.genexus.com/commwiki/wiki?7627) | [Set](https://wiki.genexus.com/commwiki/wiki?6810) |
| [Ymdhmstot](https://wiki.genexus.com/commwiki/wiki?7626) | [Set](https://wiki.genexus.com/commwiki/wiki?6810) |
| [Ttoc](https://wiki.genexus.com/commwiki/wiki?8361) | [ToString](https://wiki.genexus.com/commwiki/wiki?7090) |
| [Dtoc](https://wiki.genexus.com/commwiki/wiki?7475) | [ToString](https://wiki.genexus.com/commwiki/wiki?7090) |
| [Ctod](https://wiki.genexus.com/commwiki/wiki?7472) | [FromString](https://wiki.genexus.com/commwiki/wiki?12694) |
| [Ctot](https://wiki.genexus.com/commwiki/wiki?7473) | [FromString](https://wiki.genexus.com/commwiki/wiki?12694) |
| [CMonth](https://wiki.genexus.com/commwiki/wiki?8343) | [MonthName](https://wiki.genexus.com/commwiki/wiki?23930) |

### [Character functions](#Character+functions)

|  |  |  |
| --- | --- | --- |
| **Function** | **Method** | **Simplified Methods** |
| [Str](https://wiki.genexus.com/commwiki/wiki?7474) | [ToString](https://wiki.genexus.com/commwiki/wiki?7090) |  |
| [Strsearch](https://wiki.genexus.com/commwiki/wiki?8529) | [IndexOf](https://wiki.genexus.com/commwiki/wiki?12696) | [[StartsWith method](https://wiki.genexus.com/commwiki/wiki?53700)](#wiki%3F53700%2CStartsWith%2Bmethod+StartsWith+method)  ``` &character.StartsWith(&ParmCharacter1) ```   It is equivalent to:   ``` (&character.IndexOf(&ParmCharacter1)=1) ```    [Contains method](https://wiki.genexus.com/commwiki/wiki?53708) &character.**Contains**(&ParmCharacter1)  It is equivalent to:   ``` &character.IndexOf(&ParmCharacter1) > 0 ``` |
| [Strsearchrev](https://wiki.genexus.com/commwiki/wiki?8507) | [LastIndexOf](https://wiki.genexus.com/commwiki/wiki?12697) | [[EndsWith method](https://wiki.genexus.com/commwiki/wiki?53711)](#wiki%3F53711%2CEndsWith%2Bmethod+EndsWith+method)  ``` &character.EndsWith(&ParmCharacter1) ```   It is equivalent to:   ``` (&character.LastIndexOf(&ParmCharacter1) = &character.Length() - &ParmCharacter1.Length() + 1) ``` |
| [Len](https://wiki.genexus.com/commwiki/wiki?8436) | [Length](https://wiki.genexus.com/commwiki/wiki?12704) |  |
| [Padl](https://wiki.genexus.com/commwiki/wiki?8475) | [PadLeft](https://wiki.genexus.com/commwiki/wiki?12705) |  |
| [Padr](https://wiki.genexus.com/commwiki/wiki?8476) | [PadRight](https://wiki.genexus.com/commwiki/wiki?12706) |  |
| [Strreplace](https://wiki.genexus.com/commwiki/wiki?8505) | [Replace](https://wiki.genexus.com/commwiki/wiki?12710) |  |
| [Substr](https://wiki.genexus.com/commwiki/wiki?8527) | [Substring](https://wiki.genexus.com/commwiki/wiki?12713) | [[Substring method](https://wiki.genexus.com/commwiki/wiki?12713) with one parameter (since GeneXus 15 upgrade 7)](#wiki%3F12713%2CSubstring%2Bmethod+Substring+method+with+one+parameter+%28since+GeneXus+15+upgrade+7%29)  ``` &character.Substring(&Number) ```   It is equivalent to:   ``` &character.Substring(&Number,  &character.Length() - &Number + 1) ```    [CharAt method](https://wiki.genexus.com/commwiki/wiki?53716)  ``` &character.CharAt(&Number) ```   It is equivalent to:   ```  &character.Substring(&Number,1) ``` |
| [Lower](https://wiki.genexus.com/commwiki/wiki?8464) | [ToLower](https://wiki.genexus.com/commwiki/wiki?12714) |  |
| [Upper](https://wiki.genexus.com/commwiki/wiki?8466) | [ToUpper](https://wiki.genexus.com/commwiki/wiki?12716) |  |
| [Val](https://wiki.genexus.com/commwiki/wiki?8528) | [ToNumeric](https://wiki.genexus.com/commwiki/wiki?12717) |  |
| [Trim](https://wiki.genexus.com/commwiki/wiki?8424) | [Trim](https://wiki.genexus.com/commwiki/wiki?12718) |  |
| [Rtrim](https://wiki.genexus.com/commwiki/wiki?8425) | [TrimEnd](https://wiki.genexus.com/commwiki/wiki?12719) |  |
| [Ltrim](https://wiki.genexus.com/commwiki/wiki?8423) | [TrimStart](https://wiki.genexus.com/commwiki/wiki?12720) |  |
| [XSLTApply Function](https://wiki.genexus.com/commwiki/wiki?2167,,) | [XSLTApply](https://wiki.genexus.com/commwiki/wiki?12748) |  |
| [Toformattedstring](https://wiki.genexus.com/commwiki/wiki?8515) | [ToFormattedString](https://wiki.genexus.com/commwiki/wiki?12722) |  |

### [Numeric functions](#Numeric+functions)

|  |  |
| --- | --- |
| **Function** | **Method** |
| [Int](https://wiki.genexus.com/commwiki/wiki?8418) | [Integer](https://wiki.genexus.com/commwiki/wiki?12723) |
| [Round](https://wiki.genexus.com/commwiki/wiki?8486) | [Round](https://wiki.genexus.com/commwiki/wiki?12726) |
| [RoundToEven](https://wiki.genexus.com/commwiki/wiki?2086,,) | [RoundToEven](https://wiki.genexus.com/commwiki/wiki?12729) |
| [Trunc](https://wiki.genexus.com/commwiki/wiki?8488) | [Truncate](https://wiki.genexus.com/commwiki/wiki?12727) |

### [Nulls handling functions](#Nulls+handling+functions)

|  |  |
| --- | --- |
| **Function** | **Method** |
| [Null](https://wiki.genexus.com/commwiki/wiki?8421) | [IsEmpty](https://wiki.genexus.com/commwiki/wiki?9645) |
| [Nullvalue](https://wiki.genexus.com/commwiki/wiki?8226) | [SetNull](https://wiki.genexus.com/commwiki/wiki?12730), [SetEmpty](https://wiki.genexus.com/commwiki/wiki?9646) |
| [Isnull](https://wiki.genexus.com/commwiki/wiki?2357) | [IsNull](https://wiki.genexus.com/commwiki/wiki?12735) |
| [Old](https://wiki.genexus.com/commwiki/wiki?8472,,) | [GetOldValue](https://wiki.genexus.com/commwiki/wiki?12734) |


|  |
| --- |
| **Backlinks** |
| [CharAt method](https://wiki.genexus.com/commwiki/wiki?53716) | [Contains method](https://wiki.genexus.com/commwiki/wiki?53708) | [EndsWith method](https://wiki.genexus.com/commwiki/wiki?53711) |
| [StartsWith method](https://wiki.genexus.com/commwiki/wiki?53700) |

---
