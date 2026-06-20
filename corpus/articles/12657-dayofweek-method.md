---
title: "DayOfWeek method"
source_id: 12657
source_url: https://wiki.genexus.com/commwiki/wiki?12657
genexus_version: "18"
---

# DayOfWeek method

Returns the number associated to a day of the week. (Sunday = 1). The value 0 is returned if the received parameter is null.

### [Syntax](#Syntax)

*Date* | *DateTime***.****DayOfWeek()**

**Type returned:**  
Numeric(1)

### [Scope](#Scope)

**Data Types:** [Date](https://wiki.genexus.com/commwiki/wiki?7373), [DateTime](https://wiki.genexus.com/commwiki/wiki?7370)

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Purchase
{
  PurchaseId*
  PurchaseDate
  Line
  {
    PurchaseLineId*
    PurchaseLineDescription
    PurchaseLineOriginalPrice
    PurchaseLinePriceWithDiscount
  }
}
```

If you want to apply a 15% discount for purchases made on Monday or Tuesday, you can define the following Rule in the Purchases Transaction:

```
PurchaseLinePriceWithDiscount = PurchaseLineOriginalPrice * 0.85 if  &Today.DayOfWeek()=2 or &Today.DayOfWeek()=3;
```

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[Dow function](https://wiki.genexus.com/commwiki/wiki?8344)  
[CDoW function](https://wiki.genexus.com/commwiki/wiki?8340)


|  |
| --- |
| **Backlinks** |
| [Dow function](https://wiki.genexus.com/commwiki/wiki?8344) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) |

---
