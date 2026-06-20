---
title: "Age function"
source_id: 8330
source_url: https://wiki.genexus.com/commwiki/wiki?8330
genexus_version: "18"
---

# Age function

Calculates the difference, in years, between two date expressions.

### [Syntax](#Syntax)

**Age(***Date-expression1* | *DateTime-expression1* [ ,*Date-expression2* | *DateTime-expression2* ] **)**  
  
**Type returned:**  
Numeric(4)

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), 
[Panel](https://wiki.genexus.com/commwiki/wiki?24829)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Returns the difference, in years, between the two parameters (second parameter - first parameter). If the second parameter, which is optional, is omitted, then the default value depends on the first parameter’s data type:

1.  If it is **Date type,** then the default value is the value returned by the [Today function](https://wiki.genexus.com/commwiki/wiki?8334).  
2.  If it is **DateTime** **type**, then the default value is the value returned by the [Now function](https://wiki.genexus.com/commwiki/wiki?8335).

If the first parameter is prior to the second one, then Age function returns a positive value; otherwise, it returns a negative value.

### [Samples](#Samples)

```
&Nbr = Age(&DateOfBirth)
```

### [See Also](#See+Also)

[Age method](https://wiki.genexus.com/commwiki/wiki?12687)


|  |
| --- |
| **Backlinks** |
| [Age method](https://wiki.genexus.com/commwiki/wiki?12687) | [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |
|

---
