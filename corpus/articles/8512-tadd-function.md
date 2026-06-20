---
title: "TAdd function"
source_id: 8512
source_url: https://wiki.genexus.com/commwiki/wiki?8512
genexus_version: "18"
---

# TAdd function

Adds seconds (and optionally milliseconds) to a DateTime value.

### [Syntax](#Syntax)

**TAdd(***DateTime-expression***,** *Numeric-expression***)**  
  
**Where:**

*DateTime-expression*  
Is any valid expression that can involve constants, functions, methods, [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), variables, attributes, [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441). The result must match the [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370).

*Numeric-expression*It corresponds to the number of seconds (and optionally milliseconds) to be added. It can be any valid expression that can involve constants, functions, methods, [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), variables, attributes, [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441). The result must match the Numeric data type.

**Type Returned:**  
DateTime

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Returns a DateTime value after adding a *numeric-expression* seconds and milliseconds to a *DateTime-expression.*

### [Samples](#Samples)

Suppose you want to add 10 seconds to the current date and time:

```
&FinalDateTime = TAdd(now(), 10)
```

Now, suppose you want to add 10 seconds with 230 milliseconds to a DateTime variable that [supports Milliseconds](https://wiki.genexus.com/commwiki/wiki?39306):

```
&FinalDateTime = TAdd(now(), 10.230)
```

### [See Also](#See+Also)

[TDiff function](https://wiki.genexus.com/commwiki/wiki?8513)  
[AddSeconds method](https://wiki.genexus.com/commwiki/wiki?12676)


|  |
| --- |
| **Backlinks** |
| [AddSeconds method](https://wiki.genexus.com/commwiki/wiki?12676) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |

---
