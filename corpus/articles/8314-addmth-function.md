---
title: "AddMth function"
source_id: 8314
source_url: https://wiki.genexus.com/commwiki/wiki?8314
genexus_version: "18"
---

# AddMth function

Adds a specific number of months to a given date.

### [Syntax](#Syntax)

**AddMth(***date-expression* | *datetime-expression* **,** numeric-e*xpression***)**  
  
**Where:**  
  
*date-expression* | *datetime-expression*  
   Given date or datetime.

numeric-e*xpression*  
   The number of months added to the *date-expression* | *datetime-expression*.

**Type Returned:**  
Date | Datetime

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), 
[Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)

### [Description](#Description)

Returns a value that results from adding numeric-e*xpression* months to *date-expression* or *datetime-expression*. When the type assigned is date, it returns a date value, and when the type assigned is datetime it returns a datetime.

If the numeric expression is negative, the months are subtracted from the given date.

### [Samples](#Samples)

```
Date1 = ADDMTH(Today(),2) // Today() = 31/03/2008
// Result: Date1 = 31/05/2008 if Date1 is a date type attribute

Date2 = ADDMTH(Today(),1) // Today() = 31/03/2008
// Result: Date2 = 30/04/2008 00:00:00 if Date2 is a datetime type attribute

Date3 = ADDMTH(Date2,1) // Date2 = 30/04/2008
// Result: Date3 = 30/05/2008 if Date3 is a date type attribute

Date4 = ADDMTH(Today(),-2) // Today() = 21/09/2008
// Result: Date4 = 21/07/2008 if Date2 is a date type attribute

Date5 = ADDMTH(Now(),1) // Now() = 21/08/2008 16:30:12
// Result: Date5 = 21/09/2008 if Date5 is a date type attribute 
// Result: Date5 = 21/09/2008 16:30:12 if Date5 is a datetime type attribute
```

Note that the resulting value corresponding to Date1 is different from the result in Date 3, so different results may be obtained when adding two months to a date (Date1 case), or adding one month twice (Date2, Date3 case). You can also subtract months from a given date (e.g. Date4).

### 

### [See Also](#See+Also)

[AddMonths method](https://wiki.genexus.com/commwiki/wiki?12674)  
[AddYr function](https://wiki.genexus.com/commwiki/wiki?8317)  
[AddDays method](https://wiki.genexus.com/commwiki/wiki?8313)


|  |
| --- |
| **Backlinks** |
| [AddMonths method](https://wiki.genexus.com/commwiki/wiki?12674) | [AddYr function](https://wiki.genexus.com/commwiki/wiki?8317) | [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [GeneXus deprecated functions, methods, and rules](https://wiki.genexus.com/commwiki/wiki?6620) |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |

---
