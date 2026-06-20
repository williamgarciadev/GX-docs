---
title: "Paging clauses in Data Provider Group Statement"
source_id: 25410
source_url: https://wiki.genexus.com/commwiki/wiki?25410
genexus_version: "18"
---

# Paging clauses in Data Provider Group Statement

In order to handle a potentially large number of records, the Count and Skip clauses let you control how many records will go to the Output.

### [Syntax](#Syntax)

```
['['Count = <NumericExpression>']' ] [ '['Skip = <NumericExpression>']']
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*Count*  
         Determines the number of records that will go to the output. If Count takes the value 0 or less, it means no limit.

*NumericExpression  
     S*pecifies the number of records in each block.

*Skip*  
        Determines the number of records omitted from the output. Skip takes positive values. If negative values are assigned, you may get an exception, which you will have to handle with [error\_handler](https://wiki.genexus.com/commwiki/wiki?6853).

### [Samples](#Samples)

The following will skip the first 100 customers and Output the next 20.

```
Customers 
{
   Customer [Count = 20] [Skip = 100]
   {
      Code = CustomerId
      Name = CustomerName
   }
}
```

This is the clause used to handle all the paging, for example:

```
parm(&PageNumber, &PageSize)
```

```
Customers 
{ 
   Customer [Count = &PageSize] [Skip = (&PageNumber - 1) * &PageSize] 
   {
     Code = CustomerId
     Name = CustomerName
   }
}
```

This will handle any number of page lines and any page size.


|  |
| --- |
| **Backlinks** |
| [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [Toc:Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) | [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) |
| [Maximum workFile lines property](https://wiki.genexus.com/commwiki/wiki?8966) |

---
