---
title: "Query Object Compatibility"
source_id: 11032
source_url: https://wiki.genexus.com/commwiki/wiki?11032
genexus_version: "18"
---

# Query Object Compatibility

## [Changes in GeneXus 18 Upgrade 1](#Changes+in+GeneXus+18+Upgrade+1)

This section details changes made since GeneXus 18.

### [Edition & Build improvements](#Edition+%26+Build+improvements)

* GeneXus provides a set of built-in [Domains](https://wiki.genexus.com/commwiki/wiki?7221) and [Structured data types](https://wiki.genexus.com/commwiki/wiki?10021) to interact with [QueryViewer](https://wiki.genexus.com/commwiki/wiki?9075) and [DashboardViewer](https://wiki.genexus.com/commwiki/wiki?36770) controls with GeneXus 18 they are read-only and encapsulated in the [GeneXusReporting module](https://wiki.genexus.com/commwiki/wiki?51178).
* The context menu of the dashboard has more commands such as open, copy, paste and delete.
* With GeneXus 18 only the maps most used by our clients are distributed, the rest of the maps are available in a repository on Github. For more information read [How to use maps that are not provided by QueryViewer](https://wiki.genexus.com/commwiki/wiki?49859)

### [UX improvements](#UX+improvements)

* The queries and dashboards adopt the Unanimo's design (Default style of the KB)

### [Modeling improvements](#Modeling+improvements)

* GeneXus 18 provides methods to improve data analysis such as Rolling Average, Difference and Running Total. For more information about this, you can read [Show values as property](https://wiki.genexus.com/commwiki/wiki?50338).
* With GeneXus 18 it is possible that the elements of a query do not have a description, they only show the value.
* Full support for the GeoPoint data type is added. It is very useful when we work with [Maps](https://wiki.genexus.com/commwiki/wiki?48199).
* Also added the [Title property](https://wiki.genexus.com/commwiki/wiki?7234) for the output types Table and Pivot Table.
* The [TotalForRows](https://wiki.genexus.com/commwiki/wiki?49723) and [TotalForColumns](https://wiki.genexus.com/commwiki/wiki?49724) properties are provided for those indicators that are not summarizable in the outputs Pivot Table and Table.
* The [ItemClick Event](https://wiki.genexus.com/commwiki/wiki?19570) is now also available for [Maps](https://wiki.genexus.com/commwiki/wiki?48199), with which it is possible to do things like clicking on a territory to display information about that territory or go to a more detailed query about it.

### [Security improvements](#Security+improvements)

* As of [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853) Queries and Dashboards have the [Integrated Security Level](https://wiki.genexus.com/commwiki/wiki?15214) and [Permission Prefix](https://wiki.genexus.com/commwiki/wiki?17571) properties so that authentication and authorization is checked server-side in a per query or per dashboard basis.

### [Software Requirements](#Software+Requirements)

* Since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238), it is necessary to have the [.NET SDK 6](https://dotnet.microsoft.com/es-es/download/dotnet/6.0) installed, for the [Query Preview](https://wiki.genexus.com/commwiki/wiki?9026) and the Dashboard editor.

## [Changes in GeneXus 17 Upgrade 1](#Changes+in+GeneXus+17+Upgrade+1)

The [Query Object](https://wiki.genexus.com/commwiki/wiki?9026) [Axis](https://wiki.genexus.com/commwiki/wiki?19577) and [Visible](https://wiki.genexus.com/commwiki/wiki?43697,,) properties were completely refactored since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,). Check [here](https://wiki.genexus.com/commwiki/wiki?47094) for more information.

## [Changes in GeneXus 16](#Changes+in+GeneXus+16)

This section details changes made to the [Query Object](https://wiki.genexus.com/commwiki/wiki?9026) since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,).

In case of using[GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,) and [Query Objects](https://wiki.genexus.com/commwiki/wiki?9026), it is mandatory to update GeneXus Server to the same upgrade; check the [compatibility section](https://wiki.genexus.com/commwiki/wiki?11032) for further detail.

### [Grammar changes](#Grammar+changes)

The grammar associated to the [Query Object](https://wiki.genexus.com/commwiki/wiki?9026) was updated and improved. The following sections detail the associated changes.

#### [IN](#IN)

The *IN* operator with straight brackets changes to curved brackets; it applies to a list of values ​​with parentheses, for example the expression

```
att in [value1, value2, value3, ...]
```

changes automatically to:

```
att in (value1, value2, value3, ...)
```

#### [By](#By)

The *By (att1, att2, att3, ...)* with parentheses clause is no longer mandatory; to add an attribute but before grouping by another one (for example, to calculate the monthly average of the invoices) use the *By* clause. The expression:

```
Average (att1) By (att2, att3, ...)
```

changes to:

```
Average (att1) by att2, att3, ...
```

The same criteria is followed as for the [for each clause](https://wiki.genexus.com/commwiki/wiki?33957).

#### [DefinedBy](#DefinedBy)

The *DefinedBy (att1, att2, att3, ...)* with parentheses clause is no longer mandatory and is separated into 2 words. To change the base table (for example to count not all Customers but Customers with Invoices) use the *defined by* clause. The expression:

```
Count (att1) DefinedBy (att2, att3, ...)
```

changes to:

```
Count (att1) defined by att2, att3, ...
```

#### [WeightedBy](#WeightedBy)

The *WeightedBy (att)* with parentheses clause is no longer mandatory and separated into 2 words. To do a weighted average use the *weighted by* clause. The expression:

```
Average (att1) WeightedBy (numericAtt2)
```

changes to:

```
Average (att1) weighted by numericAtt2
```

#### [Not](#Not)

Expressions with the *NOT* clause (used in the middle of expressions) is moved to the beginning. These expressions:

```
att not like "xxx"
att not in ["a", "b", "c"]
att not in [1 to 10]
```

changes to:

```
not att like "xxx"
not att in ("a", "b", "c")
not att in (1 to 10)
```

#### [Is Null](#Is+Null)

Expressions with the *IS NULL* clause changes to use the *IsNull()* function:

```
att is null
att is not null
```

changes to

```
att.IsNull ()
not att.IsNull ()
```

#### [Filters in aggregations](#Filters+in+aggregations)

Filters within an aggregation function are removed; the expressions:

```
Sum (att1 where att2 = "xxx")
Sum (att1) where (> 1)
```

change to:

```
Sum (att1) where att2 = "xxx"
Sum (att1) where Sum (att1)> 1
```

### [New Constructions](#New+Constructions)

The following new language constructions were added.

#### [Enumerated Domain](#Enumerated+Domain)

Enumerated Domain values can be used in filters and also formula fields, example

```
# Formula
Att + Domain.Element1
# Filter
CustomerSex = Sex.Female
```

#### [Boolean Expressions](#Boolean+Expressions)

The use of booleans is less verbose, you can directly reference a boolean attribute in a filter, insted of using

```
Att = true
Att = false
```

simply write:

```
Att
not Att
```

#### [Conditional Expressions](#Conditional+Expressions)

Support for conditional expressions, such as

```
<expr1> if <cond1>; <expr2> if <cond2>; <expr3> otherwise
```

#### [Nullvalue](#Nullvalue)

Use of the *Nullvalue()* function in query elements and filters:

```
# Edition
Nullvalue(att)
# Filter
Att <> Nullvalue (Att)
```

### [Miscellaneous](#Miscellaneous)

* Each expression is fully validated in edition time to prevent errors later on while generating the SQL statement.
* Better Undo support (query edition).
* Better intellisense support, suggestions for attributes, method names, parameter names, enumerations and other clauses applicable to aggregations (*by*, *defined by*, *weighted by*).

## [Changes in GeneXus X](#Changes+in+GeneXus+X)

This section details changes made to the [Query Object](https://wiki.genexus.com/commwiki/wiki?9026) since [GeneXus X](https://wiki.genexus.com/commwiki/wiki?3146,,).

When upgrading [GeneXus X](https://wiki.genexus.com/commwiki/wiki?3146,,), if you are using [queries](https://wiki.genexus.com/commwiki/wiki?9026) check the following compatibility section:

### [Upgrading from GeneXus X Upgrade #3 to GeneXus X Upgrade #4](#Upgrading+from+GeneXus+X+Upgrade+%233+to+GeneXus+X+Upgrade+%234)

#### [Filter Section Breaking Change](#Filter+Section+Breaking+Change)

Several changes have been done to the [query filter section](https://wiki.genexus.com/commwiki/wiki?9026) making the new specification (upgrade #4 or higher) incompatible with the old one (upgrade #3 or lower).

If you are using filters in your queries; you will need to delete all the filters section and add them again using the new specification.

#### [Query Viewer Control](#Query+Viewer+Control)

The [Query Viewer control](https://wiki.genexus.com/commwiki/wiki?9075) has been improved supporting Java and .Net environments.


|  |
| --- |
| **Backlinks** |
| [Query Object - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?9105) | [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) | [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |

---
