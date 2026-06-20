---
title: "DtoC function"
source_id: 7475
source_url: https://wiki.genexus.com/commwiki/wiki?7475
genexus_version: "18"
---

# DtoC function

Returns the character string corresponding to a given date.

### [Syntax](#Syntax)

**Dtoc(***date-expression***)**  
  
**Where:**  
  
*date-expression*  
    Is the date to be converted.

**Type Returned:**  
Character C(8)

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), RPG, Visual FoxPro (up to GeneXus X Evolution 3), Cobol, [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Returns the String associated with the specified Date. The string “ / / “ is returned if the argument is a null Date expression.

The returned string has 2 digits for the year; to get 4 digits [TtoC function](https://wiki.genexus.com/commwiki/wiki?8361) has to be used.

### [Samples](#Samples)

You want to store a character string reading "Report date: 04/12/94" in the variable &String, where 04/12/94 is supposed to be the current date:

```
&string = concat(“Report date:”, dtoc(Today()), “ ”)
```

The result will be:  
Report date: 04/12/94

### [See Also](#See+Also)

[Ctod Function](https://wiki.genexus.com/commwiki/wiki?7472)  
[TtoC function](https://wiki.genexus.com/commwiki/wiki?8361)


|  |
| --- |
| **Backlinks** |
| [CtoD function](https://wiki.genexus.com/commwiki/wiki?7472) | [Date format in CTOD function property](https://wiki.genexus.com/commwiki/wiki?7632) | [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |
| [ToString method](https://wiki.genexus.com/commwiki/wiki?7090) |

---
