---
title: "YMDtoD function"
source_id: 7627
source_url: https://wiki.genexus.com/commwiki/wiki?7627
genexus_version: "18"
---

# YMDtoD function

Returns a date from three given numbers: year, month and day

### [Syntax](#Syntax)

**YMDtoD(***Numeric-expression*1**,** *Numeric-expression*2**,** *Numeric-expression*3**)**  
  
**Where:**  
*Numeric-expression1*  
    Represents the year.  
  
*Numeric-expression2*  
    Represents the month.  
  
*Numeric-expression3*  
    Represents the day.

**Type Returned:**  
Date

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), Ruby (up to GeneXus X Evolution 3), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Visual FoxPro (up to GeneXus X Evolution 3), Cobol

### [Description](#Description)

Returns a date from three given numbers: year, month and day.  
  
The year will be set according to the [First year of 20th century property](https://wiki.genexus.com/commwiki/wiki?7631):

```
0 = YEAR ................... year 2000
0 < YEAR < YEAR-LIMIT ...... year in the 21st. century
YEAR-LIMIT≤ YEAR < 100 ..... year in the 20th. century
```

If the resulting date is not valid, a null date will be returned.  
  
The date format returned depends on the selected language:  
- English: "mm/dd/yy"  
- Portuguese: "dd/mm/yy"  
- Spanish: "dd/mm/yy"  
- Italian: "dd/mm/yy"

**Note**: We suggest the use of this function instead of [CtoD function](https://wiki.genexus.com/commwiki/wiki?7472). It does not vary with the language.

### [Samples](#Samples)

1. Using two digits for the year

```
&YY = 91
&MM = 10
&DD = 15
YMDTOD(&YY, &MM, &DD)
```

Result: 10/15/91 if English is set as the default Language.  
  
2. Using four digits for the year

```
&YY = 1999
&MM = 08
&DD = 15
YMDTOD(&YY, &MM, &DD)
```

Result: 08/15/1999 if English is set as the default Language.

### [See Also](#See+Also)

* [Set method](https://wiki.genexus.com/commwiki/wiki?6810)
* [CtoD function](https://wiki.genexus.com/commwiki/wiki?7472)
* [YMDHMStoT function](https://wiki.genexus.com/commwiki/wiki?7626)


|  |
| --- |
| **Backlinks** |
| [CtoD function](https://wiki.genexus.com/commwiki/wiki?7472) | [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |
| [Set method](https://wiki.genexus.com/commwiki/wiki?6810) | [YMDHMStoT function](https://wiki.genexus.com/commwiki/wiki?7626) |

---
