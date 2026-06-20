---
title: "Query object: Filters"
source_id: 12250
source_url: https://wiki.genexus.com/commwiki/wiki?12250
genexus_version: "18"
---

# Query object: Filters

Diagrams are used here to show the **filters** that can be applied in a query through the Query object's **Filters** node, as illustrated by the example below:

`[imagen omitida: wiki id 46208]`

## [Filters](#Filters)

Valid *filter:*

The following diagram represents a valid entry for the Filters node. In other words: a valid filter will be composed of:

**Filter:**  
`[imagen omitida: wiki id 46217]`

**logical expression:**  
`[imagen omitida: wiki id 46218]`

**logical operator:**  
`[imagen omitida: wiki id 46219]`

Based on the previous initial definition and the following detail, possible filters values are:

```
CustomerId = 1
CustomerId > 5
CustomerId <> 10
CustomerId in (1 to 5)
not CustomerId in (1 to 5)
CustomerId in (1,2,5,17,30)
not CustomerId in (1,2,5,17,30)
CustomerName like "Peter Pan"
not CustomerName like "Peter Pan"
CustomerId in (CustomerId where (ProductId = 10))
not CustomerId in (CustomerId where (ProductId = 10))
Sum( InvoiceAmount ) > 10000
not Count( CustomerId ) in (4, 500, 1000)
Average( InvoiceAmount) by InvoiceDate > 1000
```

## [Values](#Values)

#### [Valid values](#Valid+values)

`[imagen omitida: wiki id 46222]`

### [Examples](#Examples)

|  |  |
| --- | --- |
| 1 | Numeric Constant |
| "Peter" | Character Constant |
| #2009-12-31# | Date Constant |
| #2009-12-31 08:55:00# | DateTime Constant |
| &Balance | Parameter defined in the Query object's Parameter node |
| Sum(InvoiceAmount) | Sum |
| Count(CustomerId) | Count |
| Average(InvoiceAmount) | Average |
| Sum(Average(InvoiceAmount) by InvoiceDate) | Sum |

### [Date and Datetime](#Date+and+Datetime)

When using a *Date* or *Datetime* attribute, the filter format is #YYYY-MM-DD# for Date and #YYYY-MM-DD HH:MM:SS# for Datetime; otherwise the following error will occur:

*invalid date constant; ANSI format expected: YYYY-MM-DD HH:MM:SS.*

## [Subqueries](#Subqueries)

Valid *subqueries*:

They're used to specify a filter that is not a constant or a list of constant values, but in which values are drawn from the database.

`[imagen omitida: wiki id 46220]`  
**where:**  
`[imagen omitida: wiki id 46221]`

### [Example](#Example)

Suppose we have a table that relates Supplier with Product sold.

```
SupplierId*
ProductId*
```

We need to have a query that shows all the suppliers that sell product 5, and the amount of product that each supplier sells. To do that, we have to specify the query as follows:

```
# Attributes
SupplierName
ProductDescription
# Filters
SupplierId in (SupplierId where ProductId = 5)
```

Observations

The subquery has to return one or more values, as applicable. If either a relational operator is used (=, >, >=, <, <=, <>), it must return a single value. E.g.: **att=(subquery)**.  
If the query returns N values instead of the single value it should return, then the first value will be taken as the result of the subquery.

It should also return a single value when it is used with the **in** operator and a list of values that includes the subquery as one of those values. E.g.: **att in (value1, value2, subquery, value3)**. The list can be a list of clients 1, 2 and 3 plus the client that bought the most products (this client is obtained through a subquery). A single value is also returned when a range is established.

The only case in which the subquery can return N values is when it is used with an **in** operator that has a single element: the subquery. It's the example that returns all the suppliers that sold product 5 and the amount of product sold by these suppliers. That is: **att in (subquery)**.

## [Logical Operators](#Logical+Operators)

#### [*Filters* made up of logical operators:](#Filters+made+up+of+logical+operators%3A)

`[imagen omitida: wiki id 46217]`

**logical expression:**  
`[imagen omitida: wiki id 46218]`

**logical operator:**  
`[imagen omitida: wiki id 46219]`

An example of different kind of filters can be the following:

`[imagen omitida: wiki id 46223]`

If you need to combine AND and OR will need to specify it explicitly for example link them by OR and both results are joined by AND:

```
(filter1 or filter2, or... or filterN) and (anotherFilter1 or anotherFilter2 or ... or anotherFilterM)
```

example:

```
(CustomerId > 5 or CustomerId <> 10 or CustomerId in (1 to 5) or CustomerId in (CustomerId where CustomerName <> "Peter Pan")) and (not CustomerName like "Hook" or CustomerId in (1,2,3,4))
```

## [Aggregations](#Aggregations)

Valid *Sum | Count | Average | Min | Max*:

`[imagen omitida: wiki id 46209]`

**by:**  
`[imagen omitida: wiki id 46212]`

**defined by:**  
`[imagen omitida: wiki id 46213]`

**weighted by:**  
`[imagen omitida: wiki id 46214]`

**arithmetic expression:**  
`[imagen omitida: wiki id 46216]`

Nesting is possible using *Sum*, *Count*, *Average*, *Max* and *Min*. Remember that the Where conditions the elements that are to be added; that is, it is applied before aggregating. For example, if you have

```
Sum(InvoiceAmount) where InvoiceAmount > 1000
```

only the invoices with amount > 1000 will be added together.

## [Considerations](#Considerations)

Some differences of the Query object filters with filters specified in other GeneXus objects (procedures, web panels, data providers, etc.):

* Filters in the Query object must be resolved in the server, so no client logic invocations, such as an invocation to a data provider, can be made.
* Data Selectors cannot be used yet.

### [Availability](#Availability)

This behavior is available since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,).


|  |
| --- |
| **Backlinks** |
| [Category:Query object](https://wiki.genexus.com/commwiki/wiki?9026) |
| [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |

---
