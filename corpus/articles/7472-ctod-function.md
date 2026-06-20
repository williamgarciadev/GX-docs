---
title: "CtoD function"
source_id: 7472
source_url: https://wiki.genexus.com/commwiki/wiki?7472
genexus_version: "18"
---

# CtoD function

Converts a date-string into a date value.

### [Syntax](#Syntax)

**Ctod(***mm/dd/yy* | *dd/mm/yy* | *yy/mm/dd***)**  
  
**Where:**  
  
*mm/dd/yy | dd/mm/yy | yy/mm/dd*  
    Must be a string. It depends on the [Date format in CTOD function property](https://wiki.genexus.com/commwiki/wiki?7632).

**Type returned:**  
Date

**Note**: *mm*represents the month in 2 digits, *dd*represents the day in 2 digits and *yy*represents the year, which can be of 2 or 4 digits. In case 2 digits are used, the year limit is applied ([First year of 20th century property](https://wiki.genexus.com/commwiki/wiki?7631))

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Sample](#Sample)

```
Event Start
    &Date=CtoD('08/21/14')   //The &Date variable is based on the Date data type
Endevent
```

### [See Also](#See+Also)

[FromString method](https://wiki.genexus.com/commwiki/wiki?12694)  
[DtoC function](https://wiki.genexus.com/commwiki/wiki?7475)  
[YMDtoD function](https://wiki.genexus.com/commwiki/wiki?7627)  
[Date format in CTOD function property](https://wiki.genexus.com/commwiki/wiki?7632)


|  |
| --- |
| **Backlinks** |
| [Date format in CTOD function property](https://wiki.genexus.com/commwiki/wiki?7632) | [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) | [DtoC function](https://wiki.genexus.com/commwiki/wiki?7475) |
| [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [YMDtoD function](https://wiki.genexus.com/commwiki/wiki?7627) |

---
