---
title: "AddMilliseconds method"
source_id: 39524
source_url: https://wiki.genexus.com/commwiki/wiki?39524
genexus_version: "18"
---

# AddMilliseconds method

Adds milliseconds to a DateTime attribute or variable.

### [Syntax](#Syntax)

*DateTime-expression***.AddMilliseconds(***Numeric-expression***)**

**Where:**

*DateTime-expression*Is a DateTime [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) to which the method will add a certain number of milliseconds.

*Numeric-expression*  
     Is a Numeric [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) that indicates the number of milliseconds to be added to the DateTime-expression*.*

**Type Returned:**  
DateTime

### [Scope](#Scope)

**Data Types:**

[DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

Returns a DateTime value, corresponding to adding a *Numeric-expression* to themilliseconds of the *DateTime* [expression](https://wiki.genexus.com/commwiki/wiki?51320,,).

### [Samples](#Samples)

Consider the &DateTime1 and &DateTime2 variables with their [Precision property](https://wiki.genexus.com/commwiki/wiki?39306) set to Milliseconds.

```
msg(&DateTime1.ToString()) // ==> 09/09/22 02:35:30.400 PM
&DateTime2 = &DateTime1.AddMilliseconds(45) // ==> &DT2 = 09/09/22 02:35:30.445 PM
```

```
&DateTime2 = &DateTime1.AddDays(5).AddMilliseconds(45)
```

### [See Also](#See+Also)

[Precision property](https://wiki.genexus.com/commwiki/wiki?39306)  
[AddSeconds method](https://wiki.genexus.com/commwiki/wiki?12676)


|  |
| --- |
| **Backlinks** |
| [MilliSecond method](https://wiki.genexus.com/commwiki/wiki?39523) |

---
