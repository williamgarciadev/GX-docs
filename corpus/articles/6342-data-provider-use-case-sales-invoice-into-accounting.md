---
title: "Data Provider Use Case: sales invoice into accounting"
source_id: 6342
source_url: https://wiki.genexus.com/commwiki/wiki?6342
genexus_version: "18"
---

# Data Provider Use Case: sales invoice into accounting

Let’s suppose we have the following invoice for which we want to obtain a corresponding accounting entry.

`[imagen omitida: wiki id 6343]`

Your accounting entry would be as follows:

`[imagen omitida: wiki id 6344]`

Before we go into the specific example, we need to make some observations:

Firstly, the transformation is considerably complex, that is, from a two-line invoice we need to generate a six-movement entry (four movements are fixed, and the other two vary according to the number of document lines).

The fixed movements are as follows:

* cash/bank: the invoice Grand Total goes to that account
* Sale: the invoice Sub-Total goes there
* Tax: the invoice taxes go there
* Total Item Costs: the sum of the cost of all products goes there. In our case, DVD: US$ 30 and mouse: US$ 10.

In addition, there is a movement per invoice line, with the individual cost corresponding to each line ( product cost \* line quantity )

Note that CR = 84+40 = DB = 70+14+30+10.

Secondly, the problem arises in the output, so Data Providers are a natural solution.

And lastly, we’ve declared our intention, and have specified no transformation process; we simply declare the output.

```
Entry
{
    EntryDate  = InvoiceDate
    EntryDescription = 'Invoice ' + InvoiceId
    Movements
    {
        Movement
        {
             AccountId = ObtainAccount.udp('Cash/Bank')
             MoveType = 'CR'
             MoveAmount = InvoiceTotal
        }
        Movement
        {
             AccountId = ObtainAccount.udp('Debtors')
             MoveType = 'DB'
             MoveAmount = InvoiceTotal
        }
        Movement
        {
             AccountId = ObtainAccount.udp('TAX')
             MoveType = 'CR'
             MoveAmount = InvoiceSubTotal * 0.20 	//corresponding to the Tax of 20%
        }
        Movement
        {
             AccountId   = AccountForProduct.udp(ProductId)
             MoveType    = 'DB'
             &MoveAmount = ProductCost.udp(ProductId) * InvoiceLineQuantity
             MoveAmount  = &MoveAmount
        }
        Movement
        {
             AccountId = ObtainAccount.udp('SaleCost')
             MoveType = 'CR'
             MoveAmount = &MoveAmount
        }
    }
}
```

This declaration is very simple, but that doesn’t make it less powerful in the Data Providers. Notice that the example uses formulas; you could also use filters, different types of outputs, and many other things that make Data Providers simple and powerful objects, something that is very difficult to achieve simultaneously.


|  |
| --- |
| **Backlinks** |
| [Category:Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) | [Data Providers philosophy](https://wiki.genexus.com/commwiki/wiki?6259) |

---
