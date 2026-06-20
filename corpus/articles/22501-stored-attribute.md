---
title: "Stored attribute"
source_id: 22501
source_url: https://wiki.genexus.com/commwiki/wiki?22501
genexus_version: "18"
---

# Stored attribute

Stored attributes are those that physically belong to a table in the Database as fields.

Attributes defined as [Global Formulas](https://wiki.genexus.com/commwiki/wiki?6440) aren't stored attributes.

[Inferred attributes](https://wiki.genexus.com/commwiki/wiki?22496) aren't stored attributes either, but only in the context where they are retrieved. They are stored in certain tables and inferred in a context where they aren't stored.

The following example shows a set of transactions where attributes InvoiceId, InvoiceDate and CustomerId are examples of stored attributes in the physical table associated with the first level of the Invoice transaction.

```
Invoice                                                Customer                        Product
{                                                      {                               {
  InvoiceId*                                              CustomerId*                      ProductId*
  InvoiceDate                                             CustomerName                     ProductName
  CustomerId                                              CustomerPhone                    ProductPrice
  CustomerName                                         }                               }
  InvoiceTotal -> f(x): Sum(InvoiceDetailAmmount)
  Detail
  {
       ProductId*
       ProductName
       ProductPrice
       InvoiceDetailQuantity 
       InvoiceDetailAmount -> f(x): ProductPrice * InvoiceDetailAmount 
  }
}
```

On the other hand, InvoiceTotal isn't a stored attribute (it's a virtual attribute). The same occurs with the InvoiceDetailAmount attribute because both are defined as global formulas.

CustomerName, ProductName and ProductPrice are inferred attributes in the Invoice Transaction. This means that they aren't stored in the base tables associated with the Invoice transaction. They are stored in other tables and inferred in the Invoice transaction.


|  |
| --- |
| **Backlinks** |
| [Inferred attribute](https://wiki.genexus.com/commwiki/wiki?22496) |

---
