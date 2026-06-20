---
title: "DoW function"
source_id: 8344
source_url: https://wiki.genexus.com/commwiki/wiki?8344
genexus_version: "18"
---

# DoW function

Returns the number (1...7) of the day of the week. This number is associated with a day of the week (Sunday = 1).

### [Syntax](#Syntax)

DoW(*date-expression* | *datetime-expression*)

**Type Returned:**  
Numeric N(1)

The value 0 is returned if the parameter received is null.

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), 

[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Samples](#Samples)

You only want to obtain the today's day from a datetime (or date)  variable or attribute.

```
&DayNbr = DoW(Now())
// Now = 11/24/2010 02:42 PM
// &DayNbr = 4
```

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[DayOfWeek method](https://wiki.genexus.com/commwiki/wiki?12657)  
[CDoW function](https://wiki.genexus.com/commwiki/wiki?8340)


|  |
| --- |
| **Backlinks** |
| [CDoW function](https://wiki.genexus.com/commwiki/wiki?8340) | [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) | [DayOfWeek method](https://wiki.genexus.com/commwiki/wiki?12657) |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |
| [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) |

---
