---
title: "EndOfMonth method"
source_id: 12656
source_url: https://wiki.genexus.com/commwiki/wiki?12656
genexus_version: "18"
---

# EndOfMonth method

Returns the last date of the month of a given date.

### [Syntax](#Syntax)

*Date*| *DateTime***.****EndOfMonth()**

**Where:**

*Date*|*DateTime*Is an attribute or variable based on the Date/DateTime data type, to which the method will find its last date.

**Type Returned:**  
Date|DateTime

### [Scope](#Scope)

**Data Types:**[Date](https://wiki.genexus.com/commwiki/wiki?7373), [DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

This method returns the last date of the month in the data type received; that is, the result's data type will be the same as the given original value (Date or DateTime).

### [Samples](#Samples)

```
&Var = &Birthday.EndOfMonth()  // where &Birthday: 08/28/2009  The result is: 08/31/09
```

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[EoM function](https://wiki.genexus.com/commwiki/wiki?8392)


|  |
| --- |
| **Backlinks** |
| [EoM function](https://wiki.genexus.com/commwiki/wiki?8392) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) |

---
