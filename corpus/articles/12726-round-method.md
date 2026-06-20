---
title: "Round method"
source_id: 12726
source_url: https://wiki.genexus.com/commwiki/wiki?12726
genexus_version: "18"
---

# Round method

Rounds the value of a given numeric expression.

### [Syntax](#Syntax)

*Numeric-expression****.*Round(***nK***)**  
  
**Where:**  
  
*Numeric-expresion*  
     Is a Numeric [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) that indicates the number the method will be applied to.  
  
*nK*  
   Must be a numeric constant.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Data Types:**

[Numeric](https://wiki.genexus.com/commwiki/wiki?6793)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This function rounds the value of *N**umeric-expression1* to *nK* decimals. The rounding threshold is 5. That is, below 5 is rounded downwards, otherwise the value is rounded upwards.

*nK* must be a Numeric Constant. If *nK* is a negative number, the Round function apply to the integer part of the number.

### [Samples](#Samples)

```
&NewVal = &Val.Round(0)    // &Val=1.5    then &NewVal = 2
&NewVal = &Val.Round(0)    // &Val=1.4    then &NewVal = 1
&NewVal = &Val.Round(1)    // &Val=1.25   then &NewVal = 1.3
&NewVal = &Val.Round(1)    // &Val=1.24   then &NewVal = 1.2
&NewVal = &Val.Round(-1)   // &Val=125.11 then &NewVal = 130 
```

### [See Also](#See+Also)

[Round function](https://wiki.genexus.com/commwiki/wiki?8486)  
[Trunc function](https://wiki.genexus.com/commwiki/wiki?8488)  
[Truncate method](https://wiki.genexus.com/commwiki/wiki?12727)


|  |
| --- |
| **Backlinks** |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Round function](https://wiki.genexus.com/commwiki/wiki?8486) | [RoundToEven function](https://wiki.genexus.com/commwiki/wiki?12728) |
| [RoundToEven method](https://wiki.genexus.com/commwiki/wiki?12729) | [Truncate method](https://wiki.genexus.com/commwiki/wiki?12727) |

---
