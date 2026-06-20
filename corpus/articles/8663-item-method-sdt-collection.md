---
title: "Item method - SDT Collection"
source_id: 8663
source_url: https://wiki.genexus.com/commwiki/wiki?8663
genexus_version: "18"
---

# Item method - SDT Collection

Returns a reference to the element located at a certain position in a collection.

### [Syntax](#Syntax)

*&VariableBasedOnSDTCollection***.Item(***Position***)**

**Where:**

*&VariableBasedOnSDTCollection* Is a variable name based on an SDT that is a collection.  
  
*Position*  
    Is the position of the desired element in the collection. This parameter must be Numeric (between 1 and the *Count* property value).

### Description

This method returns a reference to the element located at a certain position (specified by you as the argument) in a collection.

The first possible position is 1. If the specified position is less than 1 or greater than the number of elements, the program fails.

**Note:** It is not possible to assign a value to the syntax. In other words, the following code is wrong:    
  
*&VariableBasedOnSDTCollection***.Item**(1)= AttValue

### [Samples](#Samples)

Consider the following [SDT](https://wiki.genexus.com/commwiki/wiki?10021):

`[imagen omitida: wiki id 50841]`

The following code is defined in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916):

```
Event 'Show customer names'
   &Customers=DPLoadCustomers()
   for &i = 1 to &Customers.Count
      &Customer = &Customers.Item(&i)
      msg(&Customer.CustomerName)
   endfor
Endevent 

Variables:
- &Customers: Customers
- &Customer: Customers.Customer
- &i: Numeric(4)
```

The DPLoadCustomers [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270) definition is as follows:

`[imagen omitida: wiki id 50843]`

### [See Also](#See+Also)

[Structured Data Type methods](https://wiki.genexus.com/commwiki/wiki?24589)


|  |
| --- |
| **Backlinks** |
| [MailRecipientCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6996) | [Structured Data Type methods](https://wiki.genexus.com/commwiki/wiki?24589) |

---
