---
title: "Business Component GetOldValues method"
source_id: 23804
source_url: https://wiki.genexus.com/commwiki/wiki?23804
genexus_version: "18"
---

# Business Component GetOldValues method

Obtains the previous value from a [property](https://wiki.genexus.com/commwiki/wiki?2276) of a variable based on a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) from the database.

### [Syntax](#Syntax)

*&varBasedOnBC*.PropertyName.**Getoldvalue()**

**Where:**  
*&varBasedOnBC*  
      Is a variable defined in a GeneXus object, based on a Business Component.

### [Description](#Description)

The objective of applying this method to a [property](https://wiki.genexus.com/commwiki/wiki?2276) of a variable based on a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), is to obtain the previous value that the property still has in store. It retrieves the value despite having modified it in memory; for example, by having assigned another value to it.

The result returned by the method is a value that can be assigned to a variable or showed using [Msg function](https://wiki.genexus.com/commwiki/wiki?31635), etc.

### [Samples](#Samples)

Suppose you define the Customer [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) as Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True):

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

Rules:
Default(CustomerAddedDate,&today);
Error("The customer can't be deleted because he has miles to use") if delete and CustomerTotalMiles>0;
```

Accordingly, a Business Component data type of the Customer Transaction is automatically created in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and you can define a variable of the new type created in any object. Thus, you can define a variable named &Customer based on the Customer type in any object. The following code can be defined in that object for example (if the object is a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), the code can be included in its source):

```
&Customer.Load(1)                  
&Customer.CustomerTotalMiles += 500
msg('The customer has' + str(&Customer.CustomerTotalMiles.Getoldvalue()) + ' miles and now is going to have ' + str(&Customer.CustomerTotalMiles))
&Customer.Save()
commit
```

### See Also

[Business Components Methods](https://wiki.genexus.com/commwiki/wiki?2277)


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) |

---
