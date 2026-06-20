---
title: "CtoT function"
source_id: 7473
source_url: https://wiki.genexus.com/commwiki/wiki?7473
genexus_version: "18"
---

# CtoT function

Returns a DateTime data type value representing the date and time in the parameter string.

### [Syntax](#Syntax)

**CtoT(***mm**/dd/yyyy HH* [ *:MM* [ *:SS*[.*lll* ] ] ] [ AM | PM ] **)**  
  
**Where:**  
  
*mm/dd/yyyy*  
     The first part of the parameter string represents the date.  
A fixed format can be set by the [Date format in CTOD function property](https://wiki.genexus.com/commwiki/wiki?7632).

*HH* [ *:MM* [ *:SS*[.*lll* ] ] ] [ AM | PM ]  
The second part of the parameter string represents the time (which can be up to 12 characters long).

* HH - hour
* MM - minutes
* SS - seconds
* lll - milliseconds

If AM | PM is specified, HH value range is 0-12; otherwise, the value range is 0-23. Suffix AM | PM is **not** case sensitive.

The first part of the parameter string represents the date and the second part represents the time.

**Type returned:**  
DateTime

### [Scope](#Scope)

**Objects:**

[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

**Notes:**

* The date and time parts of the parameter string must be separated by at least one blank space.
* If one part of the string (date and time) is omitted it is assumed null.
* If any part of the string is not valid, the resulting DateTime value is null.
* If neither AM nor PM is specified, the 24-hour format is assumed.  
  > {00:00:00AM} is equivalent to {12:00:00AM}, Midnight.  
  > {00:00:00PM} is equivalent to {12:00:00PM}, Noon.  
  > {00:00:00} to {11:59:59} is equivalent to {12:00:00AM} to {11:59:59AM}  
  > {12:00:00} to {23:59:59} is equivalent to {12:00:00PM} to {11:59:59PM}
* 24:00:00 is not a valid time.
* The year value in the string parameter is adjusted according to the [First year of 20th century property](https://wiki.genexus.com/commwiki/wiki?7631) if the year is specified with two digits.

### [Samples](#Samples)

24-hour format

```
&varDateTime = CtoT("25/06/2015 22:45")
```

12-hour format

```
&varDateTime = CtoT("25/06/15 10:45 PM")
```

Operations with milliseconds

```
&DT = CtoT('09/09/1999 14:35:30.450')
&STR = TtoC(&DT,10,8) //==> 09/09/1999 02:35:30 PM
&STR = TtoC(&DT,10,12) //  ==>  09/09/1999 02:35:30.450 PM
```

### [See Also](#See+Also)

[TtoC function](https://wiki.genexus.com/commwiki/wiki?8361)


|  |
| --- |
| **Backlinks** |
| [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) | [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [TtoC function](https://wiki.genexus.com/commwiki/wiki?8361) |

---
