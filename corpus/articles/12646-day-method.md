---
title: "Day method"
source_id: 12646
source_url: https://wiki.genexus.com/commwiki/wiki?12646
genexus_version: "18"
---

# Day method

Extracts the number that indicates the day in a given date. If the received parameter is null, the value returned is 0.

### [Syntax](#Syntax)

*Date*| *DateTime***.Day()**  
  
**Where:**

*Date*| *DateTime*Is a Date or DateTime [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) to which the day number is extracted.

**Type returned:**   
Numeric(2)

### [Scope](#Scope)

**Data Types:**[Date](https://wiki.genexus.com/commwiki/wiki?7373), [DateTime](https://wiki.genexus.com/commwiki/wiki?7370)

### [Samples](#Samples)

Suppose a company wants to implement the following discount policy: "All debts paid before the 21st of every month, will have a 15% discount".

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
If PaymentDate.Day() < 21
   &Discount = PaymentAmount * 0.15
else
   &Discount = 0
EndIf
```

The Day method may be also applied  to the result returned by an [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) as follows:

```
&Nbr = PaymentDate.AddDays(&NbrOfDays).Day()
```

In this example, first the AddDays method is applied to the PaymentDate attribute (&NbrOfDays is a Numeric variable received by parameter using the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862)). The result is a new Date with some days added and the Day method is applied to that new date, returning the number that indicates the day.

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[Day function](https://wiki.genexus.com/commwiki/wiki?8376)  
[Month method](https://wiki.genexus.com/commwiki/wiki?12647)  
[Year method](https://wiki.genexus.com/commwiki/wiki?12648)


|  |
| --- |
| **Backlinks** |
| [Day function](https://wiki.genexus.com/commwiki/wiki?8376) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Month method](https://wiki.genexus.com/commwiki/wiki?12647) |
| [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) | [Year method](https://wiki.genexus.com/commwiki/wiki?12648) |

---
