---
title: "Day function"
source_id: 8376
source_url: https://wiki.genexus.com/commwiki/wiki?8376
genexus_version: "18"
---

# Day function

Extracts the number that indicates the day in a given date. If the received parameter is null, the value returned is 0.

### [Syntax](#Syntax)

**Day(***date-expression* | *datetime-expression***)**  
  
**Type Returned:**   
Numeric(2)

### Scope

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### Samples

A company wants to implement the following discount policy: All debts paid before the 21st of every month will have a 15% discount.

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Payment 
{ 
   PaymentId* 
   PaymentDate 
   PaymentAmount     
}
```

The following code is defined inside an Event of the Payment Transaction or a Web Panel with base table:

```
If day(PaymentDate) < 21
   &Discount = PaymentAmount * 0.15
else
   &Discount = 0
EndIf
```

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[Day method](https://wiki.genexus.com/commwiki/wiki?12646)  
[Month function](https://wiki.genexus.com/commwiki/wiki?8379)  
[Year function](https://wiki.genexus.com/commwiki/wiki?8380)


|  |
| --- |
| **Backlinks** |
| [Date expressions](https://wiki.genexus.com/commwiki/wiki?24212) | [Day method](https://wiki.genexus.com/commwiki/wiki?12646) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Month function](https://wiki.genexus.com/commwiki/wiki?8379) |
| [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) | [Year function](https://wiki.genexus.com/commwiki/wiki?8380) |

---
