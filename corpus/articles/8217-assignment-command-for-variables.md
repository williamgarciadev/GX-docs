---
title: "Assignment Command for variables"
source_id: 8217
source_url: https://wiki.genexus.com/commwiki/wiki?8217
genexus_version: "18"
---

# Assignment Command for variables

Assigns a value to a variable or a variable property.

### [Syntax](#Syntax)

***&**var | **&**var.property* operator expression  
  
**Where:**  
  
***&**var | **&**var.property*  
    Is the variable or variable property to be assigned.  
  
*operator*  
     One of the following assignment operators: = , +=, -=, \*=, /=.  
  
e*xpression*  
     Is any valid expression that can involve constants, functions, methods, [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), variables, attributes, arithmetic calculations, [Inline Formulas](https://wiki.genexus.com/commwiki/wiki?6441). The result must match the variable data type definition.

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908)

### [Description](#Description)

You may want to assign a value to a variable or a variable property, within the definition of an object.

The object section where the assignment may be defined depends on the object (Rules and Events in [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s, Rules and Source in [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)s, etc.).

The value type to be assigned must match the variable or variable property type. Otherwise, the navigation report will display a warning message.

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
Customer
{
   CustomerId*
   CustomerName
   CustomerAddress
   CustomerPhone
}

Invoice
{
   InvoiceId*    (Autonumber property = Yes)
   InvoiceDate
   CustomerId
   CustomerName
   InvoiceAmount
}
```

**1)** The following example assigns, to a variable, the result of all invoice total amounts (this code may be included, for example, in a Procedure Source or Web Panel Event):

```
&InvoicesTotalAmount = Sum(InvoiceAmount)
```

**2)**The following example assigns the True or False value to a variable, depending on whether a specific customer has invoices or not  (this code may be included in a Procedure source or Web Panel event, upon considering if the context of the Web Panel has base table or not):

```
For each Customer
    where CustomerId=15                        
          &CustomerHasInvoice=True
when none
          &CustomerHasInvoice=False
EndFor
```

**Note**: Instead of filtering by a fixed value of CustomerId, the object may receive a variable as a parameter (for example &CustomerId in the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862)) and use it in the where clause.

**3)** Suppose you have configured the Invoice Transaction [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True, and you define in a Web Panel the &Invoice variable based on the Invoice BC data type.  
The following code assigns a value to each &Invoice variable property. Following such assignments, it inserts the customer record:

```
&Invoice.InvoiceDate=&today
&Invoice.CustomerId=10
&Invoice.InvoiceAmount=100
&Invoice.save()
Commit
```

### [See also](#See+also)

[Assignment command for attributes](https://wiki.genexus.com/commwiki/wiki?8215)  
[Assignment rule](https://wiki.genexus.com/commwiki/wiki?6847)


|  |
| --- |
| **Backlinks** |
| [Assignment command for attributes](https://wiki.genexus.com/commwiki/wiki?8215) | [Assignment rule](https://wiki.genexus.com/commwiki/wiki?6847) | [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) |
| [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) |

---
