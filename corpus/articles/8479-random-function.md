---
title: "Random function"
source_id: 8479
source_url: https://wiki.genexus.com/commwiki/wiki?8479
genexus_version: "18"
---

# Random function

Returns a pseudo-random number.

### [Syntax](#Syntax)

**Random()**  
  
**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

It returns a value of the numeric type with decimals N(11.9) in the range 0 to 1. The seed can be indicated through the [RSeed function](https://wiki.genexus.com/commwiki/wiki?8481)*.* If it is not explicitly initialized before calling the Random function, then it will be automatically initialized with a different value every time the application is run.

### [Samples](#Samples)

```
Do While <Condition>
   ...
   &SesNro = Random() // Example: 0.11, 0.98, 0.54, etc.
   ...
EndDo
```

It generates N pseudo-random numbers. Every time the application is run, it generates a different sequence of numbers because the seed will always change.

### [See Also](#See+Also)

[RSeed function](https://wiki.genexus.com/commwiki/wiki?8481)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [RSeed function](https://wiki.genexus.com/commwiki/wiki?8481) | [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) |
| [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |

---
