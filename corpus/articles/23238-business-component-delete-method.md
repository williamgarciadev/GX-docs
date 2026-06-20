---
title: "Business Component Delete method"
source_id: 23238
source_url: https://wiki.genexus.com/commwiki/wiki?23238
genexus_version: "18"
---

# Business Component Delete method

Executes the equivalent to the delete button in a [Transaction Form](https://wiki.genexus.com/commwiki/wiki?10043).

### [Syntax](#Syntax)

**&***VarBasedOnBC***.Delete()**

**Where:**  
*&VarBasedOnBC*  
      Is a variable defined in a GeneXus object, based on a Business Component.

### [Description](#Description)

When this method is executed, the data previously loaded into memory by using the [Load method](https://wiki.genexus.com/commwiki/wiki?23211) (\*) is deleted, but only if the referential integrity doesn't fail and if error rules don't occur.

(\*) This is indispensable, as the data to be deleted must be previously instantiated.

### [Samples](#Samples)

Suppose you define the following Transaction as Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True):

```
Customer
{
  CustomerId*     (Autonumber property = True)
  CustomerName
  CustomerAddress
  CustomerPhone
  CustomerEmail
  CustomerAddedDate
  CustomerTotalMiles
}
```

Customer rules:

```
Default(CustomerAddedDate,&today);
Error("The customer can't be deleted because he has miles to use") if delete and CustomerTotalMiles>0;
```

Accordingly, a Business Component data type of the Customer Transaction is automatically created in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and you can define a variable of the new type created in any object. Thus, in any object, you can define a variable named &Customer based on the Customer type.

The following code (defined for example in a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) or inside an Event in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)) tries to delete the customer whose [Primary Key](https://wiki.genexus.com/commwiki/wiki?1868) CustomerId=25:

```
 &Customer.Load(25)
 &Customer.Delete()
 if &Customer.success()
     commit
 else
     rollback
 endif
```

### Availability

This method is available since [GeneXus 9.0](https://wiki.genexus.com/commwiki/wiki?2813,,)

### See Also

[Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279)


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Business Component - Publication as Web Service](https://wiki.genexus.com/commwiki/wiki?2282) | [Business Component Fail method](https://wiki.genexus.com/commwiki/wiki?23402) |
| [Business Component GetMessages method](https://wiki.genexus.com/commwiki/wiki?23475) | [Business Component samples](https://wiki.genexus.com/commwiki/wiki?2278) | [Business Component Success method](https://wiki.genexus.com/commwiki/wiki?23404) | [Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279) |
| [GAM - Full Control Permissions and inheritance](https://wiki.genexus.com/commwiki/wiki?17664) | [Logically Deleted Attribute property](https://wiki.genexus.com/commwiki/wiki?37091) |

---
