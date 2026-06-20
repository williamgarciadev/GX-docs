---
title: "Year function"
source_id: 8380
source_url: https://wiki.genexus.com/commwiki/wiki?8380
genexus_version: "18"
---

# Year function

Returns the year number in a given date. If the received parameter is null, zero is returned.

### [Syntax](#Syntax)

**Year(***Date-expression* | *DateTime-expression***)**

**Where:**

*Date-expression* | *DateTime-expression*  
   Is any valid expression that can involve constants, functions, methods, [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), variables, attributes, [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441). The result must match the [Date data type](https://wiki.genexus.com/commwiki/wiki?7373) or [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370).

**Type returned:**  
Numeric(4)

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Samples](#Samples)

To obtain the current year and assign it to a variable:

```
&ThisYear = Year(Today())
```

And next year:

```
&NextYear = Year(Now()) + 1
```

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[Year method](https://wiki.genexus.com/commwiki/wiki?12648)  
[Month function](https://wiki.genexus.com/commwiki/wiki?8379)  
[Day function](https://wiki.genexus.com/commwiki/wiki?8376)


|  |
| --- |
| **Backlinks** |
| [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) | [Day function](https://wiki.genexus.com/commwiki/wiki?8376) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Month function](https://wiki.genexus.com/commwiki/wiki?8379) |
| [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) | [Year method](https://wiki.genexus.com/commwiki/wiki?12648) |

---
