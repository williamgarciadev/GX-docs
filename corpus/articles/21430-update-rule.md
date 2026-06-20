---
title: "Update rule"
source_id: 21430
source_url: https://wiki.genexus.com/commwiki/wiki?21430
genexus_version: "18"
---

# Update rule

Edits/updates attributes that are not stored in any of the base tables of a Transaction object.

### [Syntax](#Syntax)

**Update(**att1, ..., *attn***)**;

**Where:**  
  
*att1*, ..., *attn*: attributes belonging to the [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029).

### [Scope](#Scope)

**Objects:** [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)

### [Description](#Description)

This rule allows you to edit or update attributes that are not stored in any of the base tables of a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908).

Given a Transaction level, the only attributes that can be edited are the ones stored in its [Base Table](https://wiki.genexus.com/commwiki/wiki?6347). For example, in an Invoice Transaction you can have the CustomerName in the form, but it isn't editable; the only Customer attribute that can be edited in the Invoice form is CustomerId, because it is stored in the Invoice table.

The Update() rule is introduced in case you need to edit CustomerName anyway in the Invoice form.

This rule is unconditional. Therefore, to conditionally allow the edition of a particular attribute, you should combine it with the [NoAccept rule](https://wiki.genexus.com/commwiki/wiki?6856).

### [Samples](#Samples)

The following example explains the canonical use of the Update rule. Suppose you have a Customer Transaction, an attribute called CustomerAddressLastShipment inside it, and an Invoice Transaction, too.

```
Invoice
{
    InvoiceNumber*
    InvoiceDate
    CustomerId
    CustomerName
    CustomerRUT
    CustomerAddressLastShipment
    InvoiceLastNumber
    }
         ProductId*
         ProductDescription
         ProductPrice
         InvoiceLineQtty
         InvoiceLineTotal
    }
}
```

```
Customer
{
    CustomerId*
    CustomerName
    CustomerRUT
    CustomerAddress
    CustomerAddressLastShipment
    CustomerMail
    CustomerBalance
    CustomerPhone
}
```

The CustomerAddressLastShipment attribute is inferred from the Customer table and it is displayed on the screen in a read-only mode. However, if the shipping address changed, this rule could solve it.

```
Update(CustomerAddressLastShipment);
```

The operator may change the address, and this new information will be stored in the Customer table.

`[imagen omitida: wiki id 21437]`

**Considerations:**

* Transactions may have either one or more Update rules. There is no preferred method for writing them.

* No errors or warnings are raised for this rule (i.e. reference to attributes that can already be accepted).

* Some considerations about the rule's behavior in Update mode:

If the foreign key determining the inferred attribute can be changed (i.e. it does not belong to the primary key of the base table) and it is changed in different transactions (work units), the value of the inferred attribute for the "original" foreign key value is not restored. An example may clarify the concept:

Suppose you have two Transactions: Customer and Invoice, which are related. CustomerCod is a Foreign Key (FK) in the Invoice and it has this rule:

```
Update(CustomerName);
```

It has an Invoice #1 with CustomerCod = 1 whose CustomerName = "Customer\_x". The CustomerName value is changed (in fact, CustomerName is updated in the Customer's table) in Invoice #1 to "Customer\_new" and the Invoice is confirmed.

After that (in a new [LUW](https://wiki.genexus.com/commwiki/wiki?2424)) the CustomerCod for invoice #1 is changed to another value, for example, CustomerCod = 2. This change doesn't mean the Customer #1 Name is restored to its original value.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Category:Grid control](https://wiki.genexus.com/commwiki/wiki?24817) | [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) |

---
