---
title: "Unique clause in Data Providers"
source_id: 24594
source_url: https://wiki.genexus.com/commwiki/wiki?24594
genexus_version: "18"
---

# Unique clause in Data Providers

The [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) [Unique Clause](https://wiki.genexus.com/commwiki/wiki?24592) is optional, and allows you to determine which attributes should not have duplicated values in the output.

It is the equivalent of [Unique clause in For Each command](https://wiki.genexus.com/commwiki/wiki?24593). Thus, for further examples see there.

Below are some examples where this clause could be used to solve the proposed problem.

### [Example 1](#Example+1)

Get the sales by date. The output will be a collection SDT, SalesByDay, where each item, named Day, is a simple SDT with two elements: Day and Total.

```
SalesByDay from Invoice Unique InvoiceDate
{
   Day 
   {
      Day = InvoiceDate
      Total = sum(InvoiceTotal)
   }
}
```

Remember in Data providers repetitive groups loaded from database, it is exactly the same to declare the group base transaction, order, where, etc. at the outer group name (the collection one) or at the inner group name (the item itself). That is:

```
SalesByDay 
{
   Day from Invoice Unique InvoiceDate
   {
      Day = InvoiceDate
      Total = sum(InvoiceTotal)
   }
}
```

### [Example 2](#Example+2)

Another example, adding order clause and using clause.

```
SalesByDay
{
   Day FROM invoice
   order InvoiceDescription
   USING dataSelector1(InvoiceDate)
   Unique InvoiceDate
   {
      Day4 = InvoiceDate
      Total4 = sum(InvoiceTotal)
   }
}
```

### [See Also](#See+Also)

* [Unique Clause](https://wiki.genexus.com/commwiki/wiki?24592)
* [Unique clause in For Each command](https://wiki.genexus.com/commwiki/wiki?24593)


|  |
| --- |
| **Backlinks** |
| [Unique Clause](https://wiki.genexus.com/commwiki/wiki?24592) | [Unique clause in For Each command](https://wiki.genexus.com/commwiki/wiki?24593) |

---
