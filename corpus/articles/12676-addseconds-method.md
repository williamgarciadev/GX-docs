---
title: "AddSeconds method"
source_id: 12676
source_url: https://wiki.genexus.com/commwiki/wiki?12676
genexus_version: "18"
---

# AddSeconds method

Adds seconds to a DateTime attribute or variable.

### [Syntax](#Syntax)

*Date* | *DateTime***.AddSeconds(***Numeric-expression***)**

**Where:**

*Date* | *DateTime*Is an attribute or variable based on the Date/DateTime data type, to which the method will add a certain number of seconds.

*Numeric-expression*  
     Is a Numeric [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) that indicates the number of seconds to be added to the *Date | DateTime.*

**Type Returned:**  
DateTime

### [Scope](#Scope)

**Data Types:**

[DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), RPG, Visual FoxPro (up to GeneXus X Evolution 3), Cobol

### [Description](#Description)

Returns a DateTime value, corresponding to adding a *Numeric-expression* to the seconds of  the *Date* | *DateTime* [expression](https://wiki.genexus.com/commwiki/wiki?51320,,).

### [Samples](#Samples)

```
&DateTime = &DateTime.AddSeconds(&Secs)
```

### [See Also](#See+Also)

[TAdd function](https://wiki.genexus.com/commwiki/wiki?8512)  
[Difference method](https://wiki.genexus.com/commwiki/wiki?12677)


|  |
| --- |
| **Backlinks** |
| [AddMilliseconds method](https://wiki.genexus.com/commwiki/wiki?39524) | [Difference method](https://wiki.genexus.com/commwiki/wiki?12677) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |
| [TAdd function](https://wiki.genexus.com/commwiki/wiki?8512) |

---
