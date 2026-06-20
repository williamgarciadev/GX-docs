---
title: "Business Component Fail method"
source_id: 23402
source_url: https://wiki.genexus.com/commwiki/wiki?23402
genexus_version: "18"
---

# Business Component Fail method

Evaluates whether the execution of  the [Save](https://wiki.genexus.com/commwiki/wiki?23229), [Check](https://wiki.genexus.com/commwiki/wiki?23401), [Load](https://wiki.genexus.com/commwiki/wiki?23211) or [Delete](https://wiki.genexus.com/commwiki/wiki?23238) methods failed or not. It returns True if the operation failed. Otherwise, it returns False.

### [Syntax](#Syntax)

**&***VarBasedOnBC*.**Fail()**

**Where:**  
*&VarBasedOnBC*  
     Is a -temporary and local- variable defined in a GeneXus object, based on a Business Component.

### [Samples](#Samples)

Suppose you define the following [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) as Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True):

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

Accordingly, a Business Component data type of the Customer Transaction is automatically created in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and you can define a variable of the new type created in any object.

You can define a variable named &Customer based on the Customer type in any object.

The following code (defined for example in a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) or inside an Event in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)) tries to delete a customer who has some miles to use:

```
&Customer.Load(15)
&Customer.Delete()
if &Customer.fail()
   &Messages = &customer.GetMessages()
   for &oneMessage in &Messages
         msg(&oneMessage.Description)
  endfor
else
  commit
endif

Variables defined in this object:

- &messagges: Messages data type (collection)
- &onemessage: Messages.message data type (1 element of the messages collection)
```

When the fail method is evaluated, it returns True because the error rule was triggered and the deletion couldn't be performed, so the code included in the if body, will be executed.

### [Availability](#Availability)

Available in 
[Android](https://wiki.genexus.com/commwiki/wiki?14453) since  [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).

### See Also

[Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279)  
[Business Components Methods](https://wiki.genexus.com/commwiki/wiki?2277)


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) |

---
