---
title: "Business Component GetMessages method"
source_id: 23475
source_url: https://wiki.genexus.com/commwiki/wiki?23475
genexus_version: "18"
---

# Business Component GetMessages method

Gets the collection of errors(\*) that occurred after executing the [Save](https://wiki.genexus.com/commwiki/wiki?23229), [Check](https://wiki.genexus.com/commwiki/wiki?23401), [Load](https://wiki.genexus.com/commwiki/wiki?23211) or [Delete](https://wiki.genexus.com/commwiki/wiki?23238) methods.

(\*) Those automatically checked by GeneXus as well as the [Msg](https://wiki.genexus.com/commwiki/wiki?6854) and [Error](https://wiki.genexus.com/commwiki/wiki?6852) rules defined in the [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908).

### [Syntax](#Syntax)

**&***messages*=**&***VarBasedOnBC*.**GetMessages()**

**Where:**  
  
*&messages*  
     Is a variable defined in a GeneXus object, based on the [Messages structured data type](https://wiki.genexus.com/commwiki/wiki?40335) which is automatically defined by GeneXus in every [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836):

`[imagen omitida: wiki id 23254]`

*&VarBasedOnBC*  
      Is a variable defined in a GeneXus object, based on a Business Component.

### [Samples](#Samples)

Suppose you define the following [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) as Business Component (by setting its [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) = True):

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

Accordingly, a Business Component data type of the Customer Transaction is automatically created in the Knowledge Base and you can define a variable of the new type created in any object. Thus, you can define a variable named &Customer based on the Customer type.

In the same object, the following two variables are also indicated:

```
&Messages: of the Messages data type, collection
&oneMessage: of the Messages.Message data type, which is 1 element in the collection
```

Then, specify the following code in the object (for example in [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664)):

```
&Customer.Load(18)
&Customer.Delete()
if &Customer.success()
   commit
else
   &Messages = &customer.GetMessages()
   for &oneMessage in &Messages
       msg(&oneMessage.Description)
   endfor   
endif
```

### [See Also](#See+Also)

[Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279)  
[Business Components Methods](https://wiki.genexus.com/commwiki/wiki?2277)


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) | [Error rule](https://wiki.genexus.com/commwiki/wiki?6852) | [Messages structured data type](https://wiki.genexus.com/commwiki/wiki?40335) |

---
