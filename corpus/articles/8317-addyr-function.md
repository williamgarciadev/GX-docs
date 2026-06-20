---
title: "AddYr function"
source_id: 8317
source_url: https://wiki.genexus.com/commwiki/wiki?8317
genexus_version: "18"
---

# AddYr function

Adds a given number of years to a given date.

### [Syntax](#Syntax)

**AddYr(***date-expression* | *datetime-expression* , *numeric-expression***)**

**Where:**  
  
*date-expression | datetime-expression*  
    Given date or datetime.

*numeric-expression*  
    The number of years added to the *date-expression | datetime-expression.*

**Type returned:**  
Date | DateTime

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), 
[Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Returns a value which results from adding numeric-expression years to date-expression or datetime-expression. When the type assigned is date, it returns a date value and when the type assigned is datetime, it returns a datetime.

### [Samples](#Samples)

```
Date1 = CtoD('29/02/2008')
Date2 = AddYr(Date1, 1)
// Result: Date2 = 28/02/2009 if Date2 is a date type attribute
```

```
Date3 = AddYr(Date1,-1)
// Result: Date3 = 28/02/2007 if Date3 is a date type attribute
```

```
Date4 = AddYr(Today(), 1)    //Today() = 18/12/2008
// Result: Date4 = 18/12/2009 00:00:00 if Date4 is a datetime type attribute
```

```
Date5 = AddYr(Now(), -2)   //Now() = 12/06/2008 10:30:00
// Result: Date5 = 12/06/2006 if Date5 is a date type attribute
// Result: Date5 = 12/06/2006 10:30:00 if Date5 is a datetime type attribute
```

### [See Also](#See+Also)

[AddMth function](https://wiki.genexus.com/commwiki/wiki?8314)  
[AddDays method](https://wiki.genexus.com/commwiki/wiki?8313)


|  |
| --- |
| **Backlinks** |
| [AddDays method](https://wiki.genexus.com/commwiki/wiki?8313) | [AddMth function](https://wiki.genexus.com/commwiki/wiki?8314) | [AddYears method](https://wiki.genexus.com/commwiki/wiki?12673) |
| [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |

---
