---
title: "Business Component Mode method"
source_id: 23790
source_url: https://wiki.genexus.com/commwiki/wiki?23790
genexus_version: "18"
---

# Business Component Mode method

Shows the present first [level](https://wiki.genexus.com/commwiki/wiki?42569) [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) mode of a variable based on a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846).

### [Syntax](#Syntax)

*&varBasedOnBC***.Mode()**

**Where:**  
  
*&varBasedOnBC*  
     Is a variable defined in a GeneXus object, based on a Business Component.

### [Description](#Description)

The result returned by this method is a string that indicates the mode. The result can be assigned to a character variable or showed using [Msg function](https://wiki.genexus.com/commwiki/wiki?31635) as the following example shows, etc.

It only applies for reading purposes, to obtain the present first level mode of a Transaction executed as Business Component.

When you work with a Business Component variable, the default mode is Insert ('INS'). Then, suppose you assign values to the Business Component variable [properties](https://wiki.genexus.com/commwiki/wiki?2276). Before applying the [Save method](https://wiki.genexus.com/commwiki/wiki?23229) the mode is Insert, but after saving, the mode changes to Update ('UPD') and the record keeps instantiated in memory.

In the case you apply the [Load method](https://wiki.genexus.com/commwiki/wiki?23211) to a Business Component variable in order to retrieve information from the database, the mode is set to Update and it keeps after invoking the Save method.

### [Samples](#Samples)

Suppose you define the Customer Transaction as Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True):

```
Customer
{
  CustomerId*     (Autonumber property = True)
  CustomerName
  CustomerAddress
  CustomerPhone
  CustomerEmail
  CustomerAddedDate
}

Rule:
Default(CustomerAddedDate,&today);
```

Accordingly, a Business Component data type of the Customer Transaction is automatically created in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and you can define a variable of the new type created in any object. Thus, you can define a variable named &Customer based on the Customer type in any object.

The following code can be defined in that object, for example, for testing what the method provides. If the object is a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), the code can be included in its source:

```
   &Customer = new()
   msg(&Customer.Mode())                         //The mode is 'INS'
   &Customer.CustomerName  = 'Susan Brown'
   &Customer.CustomerEmail  = 'SBrown@mail.com'
   &Customer.Save()
   msg(&Customer.Mode())                         //The mode is 'UPD'
   commit
```

### See Also

[Business Components Methods](https://wiki.genexus.com/commwiki/wiki?2277)


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) |

---
