---
title: "Truncate method"
source_id: 12727
source_url: https://wiki.genexus.com/commwiki/wiki?12727
genexus_version: "18"
---

# Truncate method

Truncates the value of a given numeric expression.

### [Syntax](#Syntax)

*Numeric-expression***.****Truncate(***nK***)**

**Where:**  
  
*Numeric-expression*  
     Is a Numeric [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) that indicates the number the method will be applied to.  
  
*nK*  
    Must be a non negative numeric constant.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Data Types:**

[Numeric](https://wiki.genexus.com/commwiki/wiki?6793)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Truncates the value of *Numeric-expression*  to *nK* decimals.

### [Samples](#Samples)

```
&Val = 1.5
&Val.Truncate(0)      // Result: 1

&Val = 1.4
&Val.Truncate(0)      // Result: 1

&Val = 1.25
&Val.Truncate(1)      // Result: 1.2

&Val = 1.24
&Val.Truncate(1)      // Result: 1.2
```

### [See Also](#See+Also)

[Trunc function](https://wiki.genexus.com/commwiki/wiki?8488)  
[Round function](https://wiki.genexus.com/commwiki/wiki?8486)  
[Round method](https://wiki.genexus.com/commwiki/wiki?12726)


|  |
| --- |
| **Backlinks** |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Round function](https://wiki.genexus.com/commwiki/wiki?8486) | [Round method](https://wiki.genexus.com/commwiki/wiki?12726) |
| [Trunc function](https://wiki.genexus.com/commwiki/wiki?8488) |

---
