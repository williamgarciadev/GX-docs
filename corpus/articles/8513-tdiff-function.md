---
title: "TDiff function"
source_id: 8513
source_url: https://wiki.genexus.com/commwiki/wiki?8513
genexus_version: "18"
---

# TDiff function

Returns the seconds elapsed between two DateTime data type values.

### [Syntax](#Syntax)

**TDiff(***DateTime-expression1* **,** *DateTime-expression2***)**  
  
**Where:**

*DateTime-expression1* **,** *DateTime-expression2:*   
     Are valid [expressions](https://wiki.genexus.com/commwiki/wiki?51320,,) that can involve constants, functions, methods, [variables](https://wiki.genexus.com/commwiki/wiki?7375), [attributes](https://wiki.genexus.com/commwiki/wiki?7240), [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441).  
     Both results must match the [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) or [Data data type](https://wiki.genexus.com/commwiki/wiki?44237).

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Returns the seconds elapsed between the two DateTime values received as parameters (*DateTime-expression1* - *DateTime-expression2*).  
*DateTime-expression2* can be greater than *DateTime-expression1*. In this case, a negative value is returned.

**Notes**:

* If the arguments [support Milliseconds](https://wiki.genexus.com/commwiki/wiki?39306), the resulting numeric value contains decimals that represent the milliseconds.
* This function calculates the time difference even when any of the parameters have null values.

### [Samples](#Samples)

```
&Diff = TDiff(&LastTime, Now())

&Diff = TDiff(&VarFinalDateTime, &VarInitialDateTime)
```

### [See Also](#See+Also)

* [Difference method](https://wiki.genexus.com/commwiki/wiki?12677)


|  |
| --- |
| **Backlinks** |
| [Difference method](https://wiki.genexus.com/commwiki/wiki?12677) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [TAdd function](https://wiki.genexus.com/commwiki/wiki?8512) |

---
