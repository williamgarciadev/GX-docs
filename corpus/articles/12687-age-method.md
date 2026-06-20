---
title: "Age method"
source_id: 12687
source_url: https://wiki.genexus.com/commwiki/wiki?12687
genexus_version: "18"
---

# Age method

Calculates the difference in years between two date expressions.

### [Syntax](#Syntax)

*Date1* | *DateTime1* **.Age(**[ ,*Date2* | *DateTime2* ]**)**  
  
**Type Returned:**  
Numeric N(4)

### [Scope](#Scope)

**Data Types:** [Date](https://wiki.genexus.com/commwiki/wiki?7373), [DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Visual FoxPro (up to GeneXus X Evolution 3), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

This method returns the difference in years between the two parameters (second parameter - first parameter).

The second parameter is optional. If it is omitted, the default value depends on the first parameter’s data type:

1.  if it is of **Date type**, the default value is the one returned by the [Today function](https://wiki.genexus.com/commwiki/wiki?8334).  
2.  if it is of **DateTime** **type**, the default value is the one returned by the [Now function](https://wiki.genexus.com/commwiki/wiki?8335).

If the first parameter is less than the second parameter, the Age function returns a positive value. Otherwise, it returns a negative value.

### [Samples](#Samples)

```
&Nbr = &DateOfBirth.Age()
```

### [See Also](#See+Also)

[Age function](https://wiki.genexus.com/commwiki/wiki?8330)


|  |
| --- |
| **Backlinks** |
| [Age function](https://wiki.genexus.com/commwiki/wiki?8330) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |

---
