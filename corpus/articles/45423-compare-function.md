---
title: "Compare function"
source_id: 45423
source_url: https://wiki.genexus.com/commwiki/wiki?45423
genexus_version: "18"
---

# Compare function

Compares two values using the indicated [relational operator](https://wiki.genexus.com/commwiki/wiki?6882) ('=', '>', '>=', '<', '<=', '<>', 'like') which can be dynamic (for example, entered by the end user at runtime).

### [Syntax](#Syntax)

**Compare(**<value1>,<operator>,<value2>**)**

**Where:**  
  
*<value1>*  
    Is an attribute, variable, or fixed value.

*<operator>*  
    Is a specific value of the predefined CompareKind [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207).

*<value2>*  
    Is an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,), [variable](https://wiki.genexus.com/commwiki/wiki?7375) or fixed value.

**Type returned:**  
Boolean

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

To compare two values using the operator entered by the end user at runtime, you may define filters (for example, Conditions) as follows:

```
Compare(&value1,&operator &value2);   //&operator is a variable based on the CompareKind Enumerated domain. It's included in the screen and entered by the end user.
```

CompareKind is a predefined [Enumerated Domain](https://wiki.genexus.com/commwiki/wiki?2207), whose [Enum Values](https://wiki.genexus.com/commwiki/wiki?7379) are:

```
CompareKind
{
    .Equal - '='
    .Greater - '>'
    .GreaterOrEqual -'>=' 
    .Less - '<'
    .LessOrEqual - '<='
    .NotEqual -'<>'
    .Like -'like'
}
```

#### [**Context of use**](#Context+of+use)

You can use the function anywhere an expression is supported.

#### [**Runtime features**](#Runtime+features)

* If the operator value entered by the end user at runtime is not valid, the value used is =.
* Performing this construction at runtime is the same as writing the operator to send the SQL statements to the DBMS.
* The like operator only makes sense for Character types and their variants. If you use it for other data types, it may give an execution error depending on whether the DBMS / version supports it or not.

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
Product
{
   ProductId*
   ProductName
   ProductPrice
}
```

Also, consider the 'ProducList' [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) whose Web Layout, Variables, and Conditions are shown below:

#### [**Web Layout**](#Web+Layout)

`[imagen omitida: wiki id 58760]`

#### [**Variables**](#Variables)

```
&ProductId - Data type based on Attribute: ProductId
&ProductName - Data type based on Attribute: ProductName
&ProductPrice - Data type based on Attribute: ProductPrice
&Op1 - Data type CompareKind, GeneXus
&Op2 - Data type CompareKind, GeneXus
&Op3 - Data type CompareKind, GeneXus
```

#### [**Conditions**](#Conditions)

```
Compare(ProductId, &Op1, &ProductId)
when not &ProductId.IsEmpty();

Compare(ProductName, &Op2, &ProductName)
when not &ProductName.IsEmpty();

Compare(ProductPrice, &Op3, &ProductPrice)
when not &ProductPrice.IsEmpty();
```

At runtime, when executing the 'ProducList' Web Panel object, the end user can select a predefined operator value for &Op1, &Op2, and/or &Op3.

`[imagen omitida: wiki id 58922]`

For example, if the end user selects Greater for the &op3 variable and enters 9 for the &ProductPrice variable, only products with a price greater than 9 will be displayed in the Grid:

`[imagen omitida: wiki id 58918]`

## [See Also](#See+Also)

[Operators](https://wiki.genexus.com/commwiki/wiki?6882)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [Category:Operators](https://wiki.genexus.com/commwiki/wiki?6882) |

---
