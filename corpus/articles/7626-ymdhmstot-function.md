---
title: "YMDHMStoT function"
source_id: 7626
source_url: https://wiki.genexus.com/commwiki/wiki?7626
genexus_version: "18"
---

# YMDHMStoT function

Returns a DateTime value representing the date and time received as parameters.

### [Syntax](#Syntax)

**YmdHmstoT(***numeric-expression*1 **,** *numeric-expression2* **,** *numeric-expression3* [ **,***numeric-expression4***,***numeric-expression5*, *numeric-expression6*] **)**  
  
**Where:**  
  
*numeric-expression1*  
   Represents the year. This value **does not** adjust according to the [First year of 20th century property](https://wiki.genexus.com/commwiki/wiki?7631).  
  
*numeric-expression2*  
   Represents the month.  
  
*numeric-expression3*  
   Represents the day.  
  
*numeric-expression4*  
   It is an optional value that represents the hour. The time value **must** be specified in 24-hour format.  
  
*numeric-expression5*  
    It is an optional value that represents the minutes.  
  
*numeric-expression6*  
   Represents the seconds and it is also an optional value.

Parameters that are omitted are assumed as zero.

**Type Returned:**  
DateTime

**Note**: If only one of the components (date or time) is invalid (is not a valid date or time) only this component will be considered invalid. For example: YMDHMStoT(1990, **31, 2**, 12, 10, 15) will return a valid DateTime value with a null date part. The time will be 12:10:15.

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[YMDtoD function](https://wiki.genexus.com/commwiki/wiki?7627)


|  |
| --- |
| **Backlinks** |
| [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [Set method](https://wiki.genexus.com/commwiki/wiki?6810) |
| [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) | [YMDtoD function](https://wiki.genexus.com/commwiki/wiki?7627) |

---
