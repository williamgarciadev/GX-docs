---
title: "Difference method"
source_id: 12677
source_url: https://wiki.genexus.com/commwiki/wiki?12677
genexus_version: "18"
---

# Difference method

Returns the seconds elapsed between two DateTime data type values.

### [Syntax](#Syntax)

*DateTime-expression1****.*****Difference(***DateTime-expression2***)**

**Where:**

*DateTime-expression1*Is an [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) that returns a value based on the [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370).

*DateTime-expression**2*  
      Is an [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) that returns a value based on the [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370). This is the value subtracted from *DateTime-expression1.*

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Data Types:**

[DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258),
[Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

Returns the amount of seconds elapsed between the two DateTime values received as parameters (*DateTime-expression1*– *DateTime-expression**2*). If *DateTime-expression**2* is greater than *DateTime-expression1*, a negative value is returned.

**Notes:**

* If the arguments [support Milliseconds](https://wiki.genexus.com/commwiki/wiki?39306), the resulting numeric value will contain decimals that represent the milliseconds.
* If some parameters have null value, then the return value will be zero.

### Samples

```
&Nbr = &DateTime1.Difference(&DateTime2)
```

Being &DateTime1= 09/13/22 09/07/22 12:00:30 and &DateTime2= 09/13/22 09/07/22 12:00:00 ==>> &Nbr = 30  
Being &DateTime1= 09/13/22 09/07/22 12:00:00 and &DateTime2= 09/13/22 09/07/22 12:00:50 ==>> &Nbr = -50

```
&Nbr=&DateTime1.Difference(&DateTime2.AddMinutes(30))
```

```
&Nbr=&DateTime1.AddDays(5).Difference(&DateTime2.AddMinutes(30))
```

### [See Also](#See+Also)

[TDiff function](https://wiki.genexus.com/commwiki/wiki?8513)  
[AddSeconds method](https://wiki.genexus.com/commwiki/wiki?12676)


|  |
| --- |
| **Backlinks** |
| [AddSeconds method](https://wiki.genexus.com/commwiki/wiki?12676) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [TDiff function](https://wiki.genexus.com/commwiki/wiki?8513) |

---
