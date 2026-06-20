---
title: "AddDays method"
source_id: 8313
source_url: https://wiki.genexus.com/commwiki/wiki?8313
genexus_version: "18"
---

# AddDays method

Adds a given number of days to a given date.

### [Syntax](#Syntax)

*Date*| *DateTime***.AddDays(***Numeric-*e*xpression***)**

**Where:**  
  
*Date*| *DateTime*  
   Is a Date or DateTime [expression](https://wiki.genexus.com/commwiki/wiki?51320,,), to which the method will add a certain number of days.

*Numeric-expression*  
    Is a Numeric [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) that indicates the number of days to be added to the *Date | DateTime.*

**Type Returned:**  
Date | DateTime

### [Scope](#Scope)

**Data Types:**[Date](https://wiki.genexus.com/commwiki/wiki?7373), 
[DateTime](https://wiki.genexus.com/commwiki/wiki?7370)

### [Description](#Description)

Returns a value that results from adding a number of days to a given date or date with time.

The result data type will be the same as the given original value (Date or DateTime).

If the numeric [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) is negative, the days are subtracted from the given date.

**Notes:**

* GeneXus verifies the resulting date in order to obtain a valid one.
* In Microsoft SQL Server, this function takes part of the SQL sentence send to the database manager.

### [Samples](#Samples)

```
&Date1 = &Date1.AddDays(7) // Adds one week to Date1 variable
```

You can also add days to a given date just by using the '+' operator:

```
&Date1 = &Date1 + 7 // Adds one week to Date1 variable
```

### [Availability](#Availability+)

This method is available since [GeneXus X Evolution 2](https://wiki.genexus.com/commwiki/wiki?15152,,).

### [See Also](#See+Also)

[AddYr function](https://wiki.genexus.com/commwiki/wiki?8317)  
[AddHours method](https://wiki.genexus.com/commwiki/wiki?19209)  
[AddMinutes method](https://wiki.genexus.com/commwiki/wiki?19205)


|  |
| --- |
| **Backlinks** |
| [AddHours method](https://wiki.genexus.com/commwiki/wiki?19209) | [AddMinutes method](https://wiki.genexus.com/commwiki/wiki?19205) | [AddMonths method](https://wiki.genexus.com/commwiki/wiki?12674) |
| [AddMth function](https://wiki.genexus.com/commwiki/wiki?8314) | [AddYears method](https://wiki.genexus.com/commwiki/wiki?12673) | [AddYr function](https://wiki.genexus.com/commwiki/wiki?8317) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |

---
