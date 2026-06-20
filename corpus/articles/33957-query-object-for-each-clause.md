---
title: "Query Object: for each clause"
source_id: 33957
source_url: https://wiki.genexus.com/commwiki/wiki?33957
genexus_version: "18"
---

# Query Object: for each clause

The For each clause in a [Query object](https://wiki.genexus.com/commwiki/wiki?9026) allows splitting a data element into more than one by using one axis to perform the separation.

In other words, it allows displaying the Query's result separated by the differents values, if you want it is similar to a SQL *group by* operation. The syntax is composed of the following elements:

`[imagen omitida: wiki id 46252]`  
**for each:**  
`[imagen omitida: wiki id 46215]`  
**argument:**  
`[imagen omitida: wiki id 46253]`  
**arithmetic expression:**  
`[imagen omitida: wiki id 46216]`

which in short translates to:

```
<Expression1> for each <Expression2>
```

where:

* *<arithmetic expression>* is the data to split. It can be defined by a simple expression or with an aggregated formula.
* *<argument>* is the axis used to separate the values. It must be defined using a simple expression (no aggregated formulas are allowed).

### [Usage example](#Usage+example)

There are many scenarios where this clause can be applied, so let's focus in two of them, a simple case and a more complex one.

Let's suppose a Car Dealer reality.

#### [Simple case](#Simple+case)

In this case, we will focus on each Car Brand's total sales. We want to show the differents values separated by country; to do so, we define the following Query structure:

```
# Attributes
Sum(InvoiceTotal) for each CountryName
CarBrandName
```

After the Query's execution, the following values are displayed:

`[imagen omitida: wiki id 33972]`

Notice that this type of syntax is also useful when:

* the Attribute's values change dynamically over time.
* it's values are unknown when the Query's structure is defined.

#### [Complex case](#Complex+case)

In this case, we want to compare the total sale's average with each Car Brand's total over time and separated by countries. So, the following structure is defined:

```
# Attributes
Sum(InvoiceTotal) for each CountryName
Average(InvoiceTotal) by CountryName
Year(InvoiceDate)
```

The result is as follows:

`[imagen omitida: wiki id 33975]`

### [See also](#See+also)

* [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075)

### [Availability](#Availability)

This behavior is available since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,).


|  |
| --- |
| **Backlinks** |
| [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |

---
