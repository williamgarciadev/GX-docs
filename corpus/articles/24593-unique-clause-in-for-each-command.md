---
title: "Unique clause in For Each command"
source_id: 24593
source_url: https://wiki.genexus.com/commwiki/wiki?24593
genexus_version: "18"
---

# Unique clause in For Each command

The  [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) [Unique Clause](https://wiki.genexus.com/commwiki/wiki?24592) is optional and is useful in scenarios where you need to process records with no duplicated values for a set of attributes.

Below are some examples where this clause could be used to solve the proposed problem. Suppose we have the following transaction structures:

```
Customer
{
   CustomerId*
   CustomerName
}

Product
{
   ProductId*
   ProductName
   ProductPrice
}

Invoice
{
   InvoiceId*
   InvoiceDate
   CustomerId
   CustomerName
   Line
   {
      InvoiceLineId*
      ProductId
      ProductName
      ProductPrice
      InvoiceLineQty
      InvoiceLineTotal = ProductPrice * InvoiceLineQty
   }
   InvoiceTotal = Sum( InvoiceLineTotal)
}
```

### [Example 1](#Example+1)

Get all the products that have ever been sold:

```
For each Invoice.Line Unique ProductName
   print PB //printblock with: ProductName
endfor
```

Note the for each base table is that of the [base transaction](https://wiki.genexus.com/commwiki/wiki?25418) Invoice.Line, that is: INVOICELINE. Without the unique clause all products that have ever been sold will be returned, repeatedly. With the unique, you avoid having duplicated values in the output.

Note unique attribute, ProductName, is in the extended table of the for each base table.

### [Example 2: sales by customer](#Example+2%3A+sales+by+customer)

Now we want to print the total amount spent by customer, for customers that have invoices from a certain date (&fromDate):

```
for each Invoice unique CustomerId
where InvoiceDate >= &fromDate
   &total = Sum( InvoiceTotal )
   print totalbycustomer //printblock with: CustomerName, &total
endfor
```

Note the aggregate [Sum](https://wiki.genexus.com/commwiki/wiki?6500) formula will have an implicit condition: the CustomerId "is given" by the context. That is, by the "group" of Invoice records that share the same CustomerId value, considered in each iteration of the for each.

Note the CustomerName attribute is allowed because given a CustomerId (the specified unique attribute), its value is unique as well (CustomerId is a foreign key, thus all the Customer extended table attributes will have a unique value from a CustomerId one).

Note Sum filter is only that of the group by (coming from the unique clause). The where clase filter is not applied, because it is only valid for the for each. Thus, for each customer with some invoice since &fromDate, he/she will be printed, with the total sum of his/her invoices (those after &fromDate and those before: all of them). If you want to sum only the invoices from that given date, you will have to make it explicit:

```
for each Invoice unique CustomerId
where InvoiceDate >= &fromDate
   &total = Sum( InvoiceTotal, InvoiceDate >= &fromDate )
   print totalbycustomer //printblock with: CustomerName, &total
endfor
```

### [Example 3: sales by year](#Example+3%3A+sales+by+year)

You need to group by not for an attribute but for an horizontal [inline formula](https://wiki.genexus.com/commwiki/wiki?6441) of some of them.

```
For each Invoice Unique InvoiceDate.Year()
   &total = Sum( InvoiceTotal )
   print totalbyyear //printblock with: InvoiceDate.Year(), &total
endfor
```

As a temporary limitation, this is not allowed. You can only use attributes in the unique clause (possibly [formula attributes](https://wiki.genexus.com/commwiki/wiki?6440)). Thus, the solution is to define a InvoiceDateYear attribute in the Invoice transaction structure level, as a formula, calculated as: "InvoiceDate.Year()".

### [See also](#See+also)

* [Unique Clause](https://wiki.genexus.com/commwiki/wiki?24592)
* [Unique clause in Data Providers](https://wiki.genexus.com/commwiki/wiki?24594)


|  |
| --- |
| **Backlinks** |
| [Unique Clause](https://wiki.genexus.com/commwiki/wiki?24592) | [Unique clause in Data Providers](https://wiki.genexus.com/commwiki/wiki?24594) |

---
