---
title: "Hour function"
source_id: 8415
source_url: https://wiki.genexus.com/commwiki/wiki?8415
genexus_version: "18"
---

# Hour function

Returns a numeric value representing the time in 24-hour format.

### [Syntax](#Syntax)

**Hour(***DateTime-expression***)**  
  
**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), RPG, Visual FoxPro (up to GeneXus X Evolution 3), Cobol, [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Returns a numeric value representing the time, in 24-hour format, given a DateTime argument.

### [Samples](#Samples)

Supose you only want to obtain the hour part of a DateTime variable or attribute.

```
&Hour = Hour(Now())
// Now = 11/24/2010 02:32 PM
// &Hour = 14
```

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[Hour method](https://wiki.genexus.com/commwiki/wiki?12652)  
[Minute function](https://wiki.genexus.com/commwiki/wiki?8416)  
[Second function](https://wiki.genexus.com/commwiki/wiki?8417)


|  |
| --- |
| **Backlinks** |
| [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Hour method](https://wiki.genexus.com/commwiki/wiki?12652) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Minute function](https://wiki.genexus.com/commwiki/wiki?8416) |
| [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [Second function](https://wiki.genexus.com/commwiki/wiki?8417) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) |

---
