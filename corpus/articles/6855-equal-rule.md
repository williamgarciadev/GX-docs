---
title: "Equal rule"
source_id: 6855
source_url: https://wiki.genexus.com/commwiki/wiki?6855
genexus_version: "18"
---

# Equal rule

Assigns a value to an attribute in insert mode, and works as a filter when using the navigation buttons.

### [Syntax](#Syntax)

**Equal(***att* , *expression***);**  
  
**Where:**  
  
*att*  
     Is the attribute to which a value will be assigned.  
  
*expression*  
     Is the expression that will be assigned to the attribute (*att*). It can be any variable, attribute or constant, and must be the same type as that given to the attribute (*att*)*.*

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Description](#Description)

This rule assigns an expression to an attribute in insert mode. For Update and Delete mode the rule will be generated as *att = expression* condition to filter records when using the navigation buttons or receiving the transaction primary key as parameter. The Equal rule first parameter (*att*) will be read-only in all Transaction modes.

### [Samples](#Samples)

Considering the following *Invoice* Transaction:

Structure:

```
Invoice
{
    InvoiceNumber*
    InvoiceDate
    InvoiceType
    InvoiceTotal
}
```

Rules:

```
Equal(InvoiceDate, Today());
```

InvoiceDate will be read-only in all transaction modes. The Equal rule will automatically assign the current date to the Invoice Date attribute when the Transaction is in Insert mode. When navigating transaction records using [Navigation Buttons](https://wiki.genexus.com/commwiki/wiki?22882,,), only those records where "InvoiceDate = Today()" will be retrieved, skipping the records different than Today().

**Notes:**

* When using the Update mode, the Equal rule is generated as a filter so it will never update the Equal rule first parameter (att).
* If you try to access a record that does not match the filter (by manually entering the primary key), you will get a "Record not found" message.
* The [Prompt](https://wiki.genexus.com/commwiki/wiki?21635) does not take Equal rule as a filter.

###


|  |
| --- |
| **Backlinks** |
| [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) |

---
