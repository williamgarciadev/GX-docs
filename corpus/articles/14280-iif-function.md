---
title: "iif function"
source_id: 14280
source_url: https://wiki.genexus.com/commwiki/wiki?14280
genexus_version: "18"
---

# iif function

Assigns a value depending on the evaluation of an expression. **iif** is an abbreviation for **Immediate if**.

### [Syntax](#Syntax)

**iif (***Expression, TruePart, FalsePart***)**

**Where:**  
*Expression*  
    The returned value is of Boolean type. It is the expression you want to evaluate. Expression can be a formula, a Udp, etc.

*TruePart*  
    Return value if the evaluation of Expression is True.

*FalsePart*  
    Return value if the evaluation of Expression is False.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Cobol

### [Samples](#Samples)

This example uses the iif function to evaluate if &PageName1 is not equal to &PageName2.

```
&PageNameChanged = iif(&PageName1 <> &PageName2, true , false)
```

It is exactly the same to:

```
if &PageName1 <> &PageName2
   &PageNameChange = 1
else
   &PageNameChange = 0
endif
```

### [See Also](#See+Also)

[If command](https://wiki.genexus.com/commwiki/wiki?8608)


|  |
| --- |
| **Backlinks** |
| [Expression data type](https://wiki.genexus.com/commwiki/wiki?6631) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |

---
