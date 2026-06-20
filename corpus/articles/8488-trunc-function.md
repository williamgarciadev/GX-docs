---
title: "Trunc function"
source_id: 8488
source_url: https://wiki.genexus.com/commwiki/wiki?8488
genexus_version: "18"
---

# Trunc function

Truncates the value of a given numeric expression.

### [Syntax](#Syntax)

**Trunc(***numeric-expression*, *nK***)**

**Where:**  
*numeric-expression*  
    Must be a numeric expression containing constants, attributes, GeneXus functions or variables.

*nK*  
    Must be a non-negative numeric constant or variable.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3),RPG, Cobol

### [Description](#Description)

Truncates the value of *numeric-expression*  to *nK* decimals.

### [Samples](#Samples)

```
Trunc(1.5, 0) = 1
Trunc(1.4, 0) = 1
Trunc(1.25, 1) = 1.2
Trunc(1.24, 1) = 1.2

&var = 0 
&sum = 146
&count = 10
&avg = Trunc(&sum / &count , &var) // Result: &avg = 14
```

### [See Also](#See+Also)

[Round function](https://wiki.genexus.com/commwiki/wiki?8486)  
[Truncate method](https://wiki.genexus.com/commwiki/wiki?12727)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [Round function](https://wiki.genexus.com/commwiki/wiki?8486) | [Round method](https://wiki.genexus.com/commwiki/wiki?12726) |
| [Truncate method](https://wiki.genexus.com/commwiki/wiki?12727) |

---
