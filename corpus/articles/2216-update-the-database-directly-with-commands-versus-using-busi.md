---
title: "Update the database directly with commands VERSUS using Business Components"
source_id: 2216
source_url: https://wiki.genexus.com/commwiki/wiki?2216
genexus_version: "18"
---

# Update the database directly with commands VERSUS using Business Components

There are two ways to update a database in a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293):

1. Directly with commands.  
2. Using [Business Components](https://wiki.genexus.com/commwiki/wiki?5846).

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Customer
{
  CustomerId*
  CustomerName
}
```

Below are two possible alternatives to solve an insertion (similarly, there are two alternatives to update and delete).

1. A direct insertion using the [New command](https://wiki.genexus.com/commwiki/wiki?6714) (this code can only be included in a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664)):

```
       Procedure Rules:
       Parm(&CustomerId,&CustomerName);

       Procedure Source:
       New 
          CustomerId = &CustomerId
          CustomerName = &CustomerName
       Endnew
```

2. An insertion using the [business components](https://wiki.genexus.com/commwiki/wiki?5846) concept (this code can be included in a Procedure Source and/or in other [GeneXus objects](https://wiki.genexus.com/commwiki/wiki?1866) in their events section):

```
       Procedure Rules:
       Parm(&CustomerId,&CustomerName);

       Procedure Source:
       &Customer.CustomerId = &CustomerId      
       &Customer.CustomerName = &CustomerName
       &Customer.Save()  //&Customer is a variable based on the Transaction Customer defined as a Business Component
       Commit
```

**Note**: Since GeneXus 15 you can use the [Business Component Insert method](https://wiki.genexus.com/commwiki/wiki?31695).

The question is, which of these two methods is better?

The answer, as often happens, is that it depends! From the point of view of performance, the first method is preferred, since there are no controls involved and the generated SQL sentence will be optimized for bulk updates. On the other hand, from the point of view of consistency, the second method is best, since all the controls will be enforced independently if data comes from a screen or a Procedure.  
  
So, a good rule of thumb would be to always use Business Components unless performance is critical.

### [See Also](#See+Also)

[Business Components - Differences between the Save method and the Insert and Update methods](https://wiki.genexus.com/commwiki/wiki?31703)  
[Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279)


|  |
| --- |
| **Backlinks** |
| [Category:Database update through procedures](https://wiki.genexus.com/commwiki/wiki?6826) | [New command](https://wiki.genexus.com/commwiki/wiki?6714) | [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) |

---
