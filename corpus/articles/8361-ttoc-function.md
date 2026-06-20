---
title: "TtoC function"
source_id: 8361
source_url: https://wiki.genexus.com/commwiki/wiki?8361
genexus_version: "18"
---

# TtoC function

Returns a character type value representing the DateTime parameter, which format is specified by *DateDigits*and *HourDigits*.

### [Syntax](#Syntax)

**TtoC(***D**ateTime-expression* [, *DateDigits*[, *HourDigits*]] **)**

**Where:**  
  
*D**ateTime-expression*  
      Is any valid expression that can involve constants, functions, methods, [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), variables, attributes, [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441). The result must match the [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370).

*DateDigits*and *HourDigits*  
     Their possible values are the same used for the DateTime data type definition.

**Type returned:**  
Character

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Values](#Values)

Possible values for *DateDigits* are:

|  |  |
| --- | --- |
| **DateDigits** | **Description** |
| **0** | The date part is not included in the resulting string. |
| **8** | The date part is included in the resulting string in 8 digits (99/99/99) following the date format rules. |
| **10** | The date part is included in the resulting string in 10 digits (99/99/9999) following the date format rules. |

|  |  |
| --- | --- |
| **HourDigits** | **Description** |
| **0** | Only the date part is obtained |
| **2** | Only the time part is displayed in 24-hour format |
| **5** | Hour and minutes are included in the resulting string separated by the time separator symbol. The 24-hour format is used |
| **8** | Hour, minutes and seconds are included in the resulting string with the hour/minute and minute/second separator. The 24-hour format is used |
| **12** | The complete time is included in the resulting string (including milliseconds) with the hour/minute, minute/second and second/millisecond separator. The 24-hour format is used |

**Notes:**

* In case *DateDigits*and/or *HourDigits* are omitted, their default values are the ones used for the DateTime parameter definition (first parameter).
* In case the *m*/*n* combination is not valid, these values are assumed: *DateDigits*=10 and *HourDigits*=8.
* The returned string format is the same one expected by [CtoT function](https://wiki.genexus.com/commwiki/wiki?7473). That is, the date part depends on the [Date format in CTOD function property](https://wiki.genexus.com/commwiki/wiki?7632) and the time part is always in 24-hour format.

### [Samples](#Samples)

If you need to obtain the date part of a DateTime expression you can simply assign it to a Date expression (Date = DateTime).

For instance, you can define:

```
&Date = &Timestamp
```

You can also get a DateTime from a previously stored record, convert it to the character data type and show it:

```
new
    CustomerName = "John Smith"
    CustomerDateOfBirth = ymdhmstot(82,03,24,13,25,10) // This function creates a DateTime value = 24/03/82 13:25:10
endnew

for each Customer
   where CustomerName = "John Smith"
      &CharVar = TtoC(CustomerDateOfBirth)
      msg(&CharVar)       //this will show "24/03/82 13:25:10"
endfor
```

Sample using [Milliseconds precision](https://wiki.genexus.com/commwiki/wiki?39306):

```
&DT = CtoT('09/09/1999 14:35:30.450')
&STR = TtoC(&DT,10,8) //==> 09/09/1999 02:35:30 PM
&STR = TtoC(&DT,10,12) //==> 09/09/1999 02:35:30.450 PM
```

### [See Also](#See+Also)

[CtoT function](https://wiki.genexus.com/commwiki/wiki?7473)


|  |
| --- |
| **Backlinks** |
| [CtoT function](https://wiki.genexus.com/commwiki/wiki?7473) | [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) | [DtoC function](https://wiki.genexus.com/commwiki/wiki?7475) |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |
| [TimeZone Support - DateTime handling](https://wiki.genexus.com/commwiki/wiki?21990) | [ToString method](https://wiki.genexus.com/commwiki/wiki?7090) |

---
