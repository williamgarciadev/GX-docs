---
title: "RSeed function"
source_id: 8481
source_url: https://wiki.genexus.com/commwiki/wiki?8481
genexus_version: "18"
---

# RSeed function

Sets the seed used by the Random function in order to generate the random numbers.

### [Syntax](#Syntax)

**&Res=RSeed(***Seed***)**

**Where:**  
  
*Seed*  
    The seed parameter is of the N(10.0) type.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

It can be set *n* times, and will affect the Randoms executed later. The value returned is not determined and it is not useful.

### [Samples](#Samples)

```
&var=RSeed(5)
Do While <Condition>
     …
     &SeedNro = Random( ) 
     ...
EndDo
```

It generates *n* pseudo-random numbers. Every time the application is run, it generates the same sequence of numbers because the seed always remains the same.

### [See Also](#See+Also)

[Random function](https://wiki.genexus.com/commwiki/wiki?8479)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Random function](https://wiki.genexus.com/commwiki/wiki?8479) |

---
