---
title: "Data Selectors in Aggregations"
source_id: 5432
source_url: https://wiki.genexus.com/commwiki/wiki?5432
genexus_version: "18"
---

# Data Selectors in Aggregations

It is possible to use [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271)s in [Aggregate Formulas](https://wiki.genexus.com/commwiki/wiki?5868).

### [Syntax](#Syntax)

Data Selectors can be referenced in Aggregate formulas, with the USING clause according to the following grammar:

```
<AggFormulaName> (<Expression>, [<AggregationCondition>], [<DefaultValue>])
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*AggFormulaName*  
   Could be one of the following: Find, Max, Min, Sum, Count, or Average.

*Expression*  
   Is an expression to be found, maximized, minimized, summed, or averaged. It can be an attribute (stored or formula), or an expression that involves attributes, variables, and constants.

*AggregationCondition*   
   Is composed of [<Condition>] [**USING** <DataSelector> **'('** <Parameters...> **')'**]

*DefaultValue*  
   Is the returned value when no records match the AggregateCondition. It is a constant and it is optional.

**Notes**

* For Count formulas, the first parameter can't be an expression. It must be an attribute.
* For Sum and Count formulas, the result of evaluating the expression must be a numeric value.
* When using a Data Selector (USING clause):
  + The use of Procedures is not supported in the formula definition. Otherwise, the message [spc0026](https://wiki.genexus.com/commwiki/wiki?6431) is shown and the formula cannot be solved.
  + What will be taken into account is the [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) Condition (not its Order or anything else).
* User variables can only be used in inline formulas.

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
Country
{
  CountryId*
  CountyName
}

Customer
{
  CustomerId*
  CustomerName
  CustomerStatus
  CountryId
  CountyName
}
```

Consider the "ActiveCustomers" Data Selector definition as follows:

`[imagen omitida: wiki id 54801]`

**1)** To count the total number of active customers, you can define inside an event, source, etc. the following code:

```
  &NumberActiveCustomers = Count(CustomerName, USING ActiveCustomers())
```

**2)** To count the number of active customers per country, you can define the following code:

```
For Each Country
   &NumberActiveCustomers = Count(CustomerName, USING ActiveCustomers())
EndFor
```

Remember that the *CustomerName* attribute –the first parameter in the count formula– is not taken into account by GeneXus to determine the [For Each](https://wiki.genexus.com/commwiki/wiki?24744) [Base Table](https://wiki.genexus.com/commwiki/wiki?6347). The *CustomerName* attribute belongs to the Formula definition.

The For Each base table is COUNTRY (because *Country* is mentioned as [Base Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?23945,,)).

The table navigated by the Formula (in which the calculation is made) is CUSTOMER (because the attributes mentioned in the formula and in the Data Selector definitions belong to the CUSTOMER table).

Finally, the two tables navigated –COUNTRY and CUSTOMER– have a common attribute: *CountryId.* So, for each navigated country (by the For Each command), the Aggregate Formula defined inside the For Each (inline) considers only the **active** customers **that belong to the country being navigated in the For Each query, at the moment of triggering the formula**.

### [See Also](#See+Also)

[Data Selectors in Grids](https://wiki.genexus.com/commwiki/wiki?5386)  
[Data Selectors in Data Providers](https://wiki.genexus.com/commwiki/wiki?6501)  
[Data Selectors in For Each command](https://wiki.genexus.com/commwiki/wiki?5312)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Data Selectors](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/data-selectors-v16?p=5414)


|  |
| --- |
| **Backlinks** |
| [Category:Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) | [Data Selector property](https://wiki.genexus.com/commwiki/wiki?5361) | [Data Selector property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57171) |
| [Data Selectors in Data Providers](https://wiki.genexus.com/commwiki/wiki?6501) | [Data Selectors in For Each command](https://wiki.genexus.com/commwiki/wiki?5312) | [Data Selectors in Grids](https://wiki.genexus.com/commwiki/wiki?5386) | [Data Selectors in Grids (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57179) |
| [Examples of Using Formulas](https://wiki.genexus.com/commwiki/wiki?5882) | [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Specification Codes from spc0050 to spc0099](https://wiki.genexus.com/commwiki/wiki?6432) |

---
