---
title: "Data Provider Variable statement"
source_id: 25413
source_url: https://wiki.genexus.com/commwiki/wiki?25413
genexus_version: "18"
---

# Data Provider Variable statement

It is one of the three main components of the [Data Provider output-based declarative language](https://wiki.genexus.com/commwiki/wiki?5309).

Sometimes it is necessary to make internal calculations that do not necessarily have to go into the Output itself. Variables are used in this case, in a [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082).

## [Syntax](#Syntax)

```
 &var = <Formula>
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

***&**var*  
     Is the name of the variable.

*Formula*  
     Is a conditional [Formula](https://wiki.genexus.com/commwiki/wiki?5861) ([horizontal](https://wiki.genexus.com/commwiki/wiki?5864) as well as [aggregate](https://wiki.genexus.com/commwiki/wiki?5868) or [Compound](https://wiki.genexus.com/commwiki/wiki?5879)). That is, it could be several conditional expressions. This includes either an isolate attribute, or an invocation to a procedure with output or a Data Provider, a constant, as well as the typical formulas.

### [Samples](#Samples)

```
Customers
{
   &TotalCustomers = 0
   Customer
   {
      CustomerId = CustomerId
      CustomerName = CustomerName
      &TotalCustomers = &TotalCustomers + 1
   }
   Summary
   {
      Total = &TotalCustomers 
   }
}
```


|  |
| --- |
| **Backlinks** |
| [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [Toc:Data Provider language](https://wiki.genexus.com/commwiki/wiki?5309) | [Data Provider: Input](https://wiki.genexus.com/commwiki/wiki?6292) |

---
