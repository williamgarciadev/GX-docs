---
title: "Assignment rule"
source_id: 6847
source_url: https://wiki.genexus.com/commwiki/wiki?6847
genexus_version: "18"
---

# Assignment rule

Updates the database by assigning a value that results from evaluating an expression, a fixed value or a value stored in an attribute/variable to an attribute or variable.

### [Syntax](#Syntax)

*att* | *&var* = *expression* [ If *condition* ]   [ on *triggering event*];

#### [**Where:**](#Where%3A)

*att* | *&var*  
    Is the attribute or variable to be assigned. In the case of being an attribute, it cannot be a formula.

*expression*  
    Is any valid expression that can involve constants, functions, [procedures](https://wiki.genexus.com/commwiki/wiki?6293), variables, or other attributes (the result must match the attribute or variable type definition).

*condition*  
    Is any valid logic condition (that can contain the "and", "or", and "not" logical operators).

*triggering event*  
    Is one of the predefined events available in GeneXus for transaction rules, which allows you to define the precise time for executing a rule.

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?38604),  [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Visual FoxPro (up to GeneXus X Evolution 3), Ruby (up to GeneXus X Evolution 3).

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Customer
{
  CustomerId*      
  CustomerName         
  CustomerAddress      
  CustomerPhone   
  CustomerAddedDate 
  CustomerLastUpdateDate
}
```

Now observe the following rules defined in that Transaction to assign values to certain attributes and variables:

```
CustomerAddedDate = today() if insert;
CustomerLastUpdateDate = today();
&DiscountPercentage=10 if CustomerAddedDate.year() < 2011;
```

### [See Also](#See+Also)

[Assignment command for variables](https://wiki.genexus.com/commwiki/wiki?8217)  
[Assignment command for attributes](https://wiki.genexus.com/commwiki/wiki?8215)


|  |
| --- |
| **Backlinks** |
| [Assignment command for attributes](https://wiki.genexus.com/commwiki/wiki?8215) | [Assignment Command for variables](https://wiki.genexus.com/commwiki/wiki?8217) | [Code Snippets](https://wiki.genexus.com/commwiki/wiki?10662) |
| [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Procedure rules](https://wiki.genexus.com/commwiki/wiki?8262) | [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) | [Web Panel rules](https://wiki.genexus.com/commwiki/wiki?8288) |
|

---
