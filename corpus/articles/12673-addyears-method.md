---
title: "AddYears method"
source_id: 12673
source_url: https://wiki.genexus.com/commwiki/wiki?12673
genexus_version: "18"
---

# AddYears method

Adds a given number of years to a given date.

### [Syntax](#Syntax)

*Date*| *DateTime***.AddYears(***Numeric-expression***)**

**Where:**

*Date*| *DateTime*Is an attribute or variable based on the Date/DateTime data type, to which the method will add a certain number of years.

*Numeric-expression*  
     Is a Numeric [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) that indicates the number of years to be added to the *Date | DateTime.*

**Type returned:**  
Date | DateTime

### [Scope](#Scope)

**Data Types:**[Date](https://wiki.genexus.com/commwiki/wiki?7373), [DateTime](https://wiki.genexus.com/commwiki/wiki?7370)

### [Description](#Description)

Returns a value which results from adding a number of years to a given date or date with time.

The result's data type will be the same as the given original value (Date or DateTime).

If the numeric expression is negative, the years are subtracted from the given date.

### [Samples](#Samples)

```
If &Today.Month() = 12
   &ExpiryDate = &Today.AddYears(1)
EndIf  
```

### [See Also](#See+Also)

[AddYr function](https://wiki.genexus.com/commwiki/wiki?8317)  
[AddMonths method](https://wiki.genexus.com/commwiki/wiki?12674)  
[AddDays method](https://wiki.genexus.com/commwiki/wiki?8313)


|  |
| --- |
| **Backlinks** |
| [AddMonths method](https://wiki.genexus.com/commwiki/wiki?12674) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |

---
