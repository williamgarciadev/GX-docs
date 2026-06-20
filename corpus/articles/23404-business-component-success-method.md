---
title: "Business Component Success method"
source_id: 23404
source_url: https://wiki.genexus.com/commwiki/wiki?23404
genexus_version: "18"
---

# Business Component Success method

Evaluates whether the execution of  the [Save](https://wiki.genexus.com/commwiki/wiki?23229), [Check](https://wiki.genexus.com/commwiki/wiki?23401), [Load](https://wiki.genexus.com/commwiki/wiki?23211) or [Delete](https://wiki.genexus.com/commwiki/wiki?23238) methods,succeeded or not. It returns True if the operation was successful. Otherwise, it returns False.

### [Syntax](#Syntax)

**&***VarBasedOnBC***.Success()**

**Where:**  
*&VarBasedOnBC*  
     Is a variable defined in a GeneXus object, based on a Business Component.

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
  CustomerBirthDate
  CustomerAddedDate
}

Rules:

Default(CustomerAddedDate,&today);
error('The customer must be 18 years old or more') if CustomerBirthDate.Age()<18;
```

Accordingly, a Business Component data type of the Customer Transaction is automatically created in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and you can define a variable of the new type created in any object.

You can define a variable named &Customer based on the Customer type in any object.

The following code (defined for example in a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) or inside an Event in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)) tries to insert a customer younger than 18 years old:

```
&Customer.CustomerName='Tina Parker'
&Customer.CustomerAddress='18001 Collins Avenue'
&Customer.CustomerPhone= '877-219-8890'
&Customer.CustomerEmail= 'tinaparker@mail.com'
&Customer.CustomerBirthDate= ymdtod(2010,10,08)
&Customer.save()
If &Customer.success()
   commit
else
   &Messages = &customer.GetMessages()
   for &oneMessage in &Messages
       msg(&oneMessage.Description)
   endfor
endif

Variables defined in this object:

- &messagges: Messages data type (collection)
- &onemessage: Messages.message data type (1 element of the messages collection)
```

When the Success method is evaluated, it returns False because the error rule was triggered and the save wasn't successful, so the code included in the else, will be executed.

### [Availability](#Availability)

Available in 
[Android](https://wiki.genexus.com/commwiki/wiki?14453) since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).

### [See Also](#See+Also)

[Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279)  
[Business Components Methods](https://wiki.genexus.com/commwiki/wiki?2277)


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) |

---
