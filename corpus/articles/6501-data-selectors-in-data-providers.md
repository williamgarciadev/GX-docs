---
title: "Data Selectors in Data Providers"
source_id: 6501
source_url: https://wiki.genexus.com/commwiki/wiki?6501
genexus_version: "18"
---

# Data Selectors in Data Providers

A [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) can be used in a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) in the same way as in a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744).

Some examples already seen in [Data Selectors in For Each command](https://wiki.genexus.com/commwiki/wiki?5312) show this.

If you have the following Data Selector:

`[imagen omitida: wiki id 6216]`

From a Data Provider you can return the list of customers having an invoice in a given range (for example, taken from parameters):

#### [1) 'USING' clause](#1%29+%27USING%27+clause)

```
Clients
{
     Client USING InvoicesByDate( &FromDate, &ToDate )
     {
        Code = CustomerId
        Name = CustomerName
     }
}
```

When invoking a Data Selector through the "USING" clause in a group (same as a For each), the Data Selector doesn't have an associated navigation (it doesn't have a base table by itself). At specification time, the Data Selector definition is combined with the Group definition to determine the table that will be navigated, taking into account the attributes of both definitions. So, the base table associated with the 'Client' group will be INVOICE.

#### [2) 'IN' operator in the Where clause](#2%29+%27IN%27+operator+in+the+Where+clause)

```
Clients
{
    Client
    where CustomerName IN InvoicesByDate( &FromDate, &ToDate )
    {
       Code = CustomerId
       Name = CustomerName
    }
}
```

The Data Selector query will return a collection of values corresponding to the same definition as the attribute that precedes the IN operator. In the above example, the Data Selector returns 'a customer list' with invoices in the given range.

For further information, see [Data Selectors in For Each command](https://wiki.genexus.com/commwiki/wiki?5312)

### [See also](#See+also)

[Data Selectors in Grids](https://wiki.genexus.com/commwiki/wiki?5386)  
[Data Selectors in Aggregations](https://wiki.genexus.com/commwiki/wiki?5432)  
[Data Selectors in For Each command](https://wiki.genexus.com/commwiki/wiki?5312)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Data Selectors](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/data-selectors-v16?p=5414)


|  |
| --- |
| **Backlinks** |
| [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [Category:Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) | [Data Selector property](https://wiki.genexus.com/commwiki/wiki?5361) |
| [Data Selector property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57171) | [Data Selectors in Aggregations](https://wiki.genexus.com/commwiki/wiki?5432) | [Data Selectors in For Each command](https://wiki.genexus.com/commwiki/wiki?5312) | [Data Selectors in Grids](https://wiki.genexus.com/commwiki/wiki?5386) |
| [Data Selectors in Grids (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57179) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Order Clause Specification](https://wiki.genexus.com/commwiki/wiki?5100) |

---
