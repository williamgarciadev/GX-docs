---
title: "EoM function"
source_id: 8392
source_url: https://wiki.genexus.com/commwiki/wiki?8392
genexus_version: "18"
---

# EoM function

Returns the last date of the month in the given date parameter, i.e. when the type received is date, it returns a date value, and when the type received is datetime, it returns a datetime.

### [Syntax](#Syntax)

**EoM(***date-expression* | *datetime-expression***)**  
  
**Type Returned:**  
Date|DateTime

### [Scope](#Scope)

**Objects:**

[Procedure](https://wiki.genexus.com/commwiki/wiki?6293),
[Transaction](https://wiki.genexus.com/commwiki/wiki?1908),
[Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Samples](#Samples)

Supposing the Language is set to English:

```
EoM(CToD('01/01/08')) 
Result: 01/31/08
```

```
EoM(CToD('02/05/91')) 
Result: 02/28/91
```

```
EoM(Now())
Result: 01/31/98 10:30:12 if Now() = 01/10/98 10:30:12
```

```
Date1 = EoM(Now()) 
Result: 01/31/98 if Now() = 01/10/98 10:30:12 and Date1 is a date type attribute
```

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[EndOfMonth method](https://wiki.genexus.com/commwiki/wiki?12656)


|  |
| --- |
| **Backlinks** |
| [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) | [EndOfMonth method](https://wiki.genexus.com/commwiki/wiki?12656) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |
| [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) |

---
