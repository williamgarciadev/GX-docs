---
title: "Round function"
source_id: 8486
source_url: https://wiki.genexus.com/commwiki/wiki?8486
genexus_version: "18"
---

# Round function

#### [Rounds the value of a given numeric expression](#Rounds+the+value+of+a+given+numeric+expression)

### [Syntax](#Syntax)

**Round(** *nExp1* **,** *nK***)**  
  
**Where:**  
  
*nExp1*  
   Must be a numeric expression.  
  
*nK*  
   Must be a numeric constant o variable.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

This function rounds the value of *nExp1* to *nK* decimals. The rounding threshold is 5. That is, values below 5 are rounded downwards, otherwise the value is rounded upwards.

*nK* must be a numeric constant or variable. If *nK* is a negative number, the Round function applies to the integer part of the number.

### [Samples](#Samples)

```
Round(1.5, 0) = 2 
Round(1.4, 0) = 1 
Round(1.25, 1) = 1.3

&value = 1
Round(1.24, &value) = 1.2 
Round(125.11, -1) = 130 

&sum = 146 
&count = 10 
&avg = Round(&sum / &count, 0) // Result &avg: 15
```

### [See Also](#See+Also)

[Round method](https://wiki.genexus.com/commwiki/wiki?12726)  
[Trunc function](https://wiki.genexus.com/commwiki/wiki?8488)  
[Truncate method](https://wiki.genexus.com/commwiki/wiki?12727)


|  |
| --- |
| **Backlinks** |
| [Expression data type](https://wiki.genexus.com/commwiki/wiki?6631) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [Round method](https://wiki.genexus.com/commwiki/wiki?12726) |
| [RoundToEven function](https://wiki.genexus.com/commwiki/wiki?12728) | [RoundToEven method](https://wiki.genexus.com/commwiki/wiki?12729) | [Trunc function](https://wiki.genexus.com/commwiki/wiki?8488) | [Truncate method](https://wiki.genexus.com/commwiki/wiki?12727) |
| [Use decimal arithmetic property](https://wiki.genexus.com/commwiki/wiki?10324) |

---
