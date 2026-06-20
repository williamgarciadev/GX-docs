---
title: "Inferred attribute"
source_id: 22496
source_url: https://wiki.genexus.com/commwiki/wiki?22496
genexus_version: "18"
---

# Inferred attribute

In the context of a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), inferred attributes are those whose value is not stored in any transaction level [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) but in a table related to the transaction base tables.

The **inferred** term means "obtained" or "retrieved". Attributes can be inferred, given the value of a foreign key.

The following example shows a set of transactions where attributes CustomerName, ProductName and ProductPrice are inferred attributes in the first and second levels of the Invoice transaction.

```
Invoice                                  Customer                        Product
{                                        {                               {
  InvoiceId*                                CustomerId*                      ProductId*
  InvoiceDate                               CustomerName                     ProductName
  CustomerId                                CustomerPhone                    ProductPrice
  CustomerName                           }                               }
  InvoiceTotal
  Detail
  {
       ProductId*
       ProductName
       ProductPrice
       InvoiceDetailQuantity
       InvoiceDetailAmmount
  }
}
```

We say that the CustomerName attribute is an inferred attribute in the Invoice transaction, because its value is not stored in any of its associated tables, but inferred – that is to say, it is obtained – from the Customer table, given the value of the CustomerId attribute. In a similar way, the ProductName and ProductPrice attributes are also inferred in the Invoice transaction, because they are not stored in its associated tables; instead, its values are inferred from the Product table in order to, for example, show them in the form.

**See Also**

[Stored attribute](https://wiki.genexus.com/commwiki/wiki?22501)


|  |
| --- |
| **Backlinks** |
| [Redundant property - Attribute](https://wiki.genexus.com/commwiki/wiki?6661) | [Stored attribute](https://wiki.genexus.com/commwiki/wiki?22501) |

---
