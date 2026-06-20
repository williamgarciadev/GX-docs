---
title: "CMonth function"
source_id: 8343
source_url: https://wiki.genexus.com/commwiki/wiki?8343
genexus_version: "18"
---

# CMonth function

Returns the name of the month for a given date in the selected language. If no language is specified, the one selected in the Model Properties is used.

The value 'spaces' is returned if the received parameter is null.

### [Syntax](#Syntax)

CMonth(*Date-Expression* | *Datetime-Expression*[,*Language*])

**Where:**  
  
*Language*  must be one of the following:

Spanish  
English  
Portuguese  
Italian  
SimplifiedChinese  
TraditionalChinese  
Japanese  
Arabic  
German

**Type Returned:**  
Character(9)

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), 
[Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Samples](#Samples)

```
CMONTH(CTOD('01/01/2013')) // 'Enero' if Spanish is set as the default language.
```

```
CMONTH(CTOD('01/01/2013'), 'por') // Janeiro
```

```
CMONTH(CTOD('01/01/2013'), 'eng') // January
```

**Note**: Make sure the languages are installed on the KB.

### [See Also](#See+Also)

[MonthName method](https://wiki.genexus.com/commwiki/wiki?23930)  
[CDoW function](https://wiki.genexus.com/commwiki/wiki?8340)


|  |
| --- |
| **Backlinks** |
| [CDoW function](https://wiki.genexus.com/commwiki/wiki?8340) | [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [MonthName method](https://wiki.genexus.com/commwiki/wiki?23930) |
|

---
