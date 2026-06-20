---
title: "Minute function"
source_id: 8416
source_url: https://wiki.genexus.com/commwiki/wiki?8416
genexus_version: "18"
---

# Minute function

Returns a numeric value, representing the minutes of a DateTime argument.

### [Syntax](#Syntax)

**Minute(***DateTime-Expression***)**  
  
**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), Ruby (up to GeneXus X Evolution 3), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Returns a numeric value representing the minutes, given a DateTime argument.

### [Samples](#Samples)

You only want to obtain the minute part of a datetime variable or attribute.

```
&Min= Minute(Now())
// Now = 11/24/2010 02:42 PM
// &Min = 42
```

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[Minute method](https://wiki.genexus.com/commwiki/wiki?12650)  
[Hour Function](https://wiki.genexus.com/commwiki/wiki?8415)  
[Second Function](https://wiki.genexus.com/commwiki/wiki?8417)


|  |
| --- |
| **Backlinks** |
| [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Hour function](https://wiki.genexus.com/commwiki/wiki?8415) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Minute method](https://wiki.genexus.com/commwiki/wiki?12650) |
| [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [Second function](https://wiki.genexus.com/commwiki/wiki?8417) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) |

---
