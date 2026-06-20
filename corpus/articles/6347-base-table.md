---
title: "Base Table"
source_id: 6347
source_url: https://wiki.genexus.com/commwiki/wiki?6347
genexus_version: "18"
---

# Base Table

A **base table** is any table in the database where you are positioned and working at a certain time, for example for retrieving or modifying its data.

When you execute a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) with a single level, it has one associated **base table**.

When you work with a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) with more than one level, each level has an associated **base table**.

Also, when you define queries (a listing, for instance), you will be navigating a specific **base table**.

Some examples:

* **For each command:** The base table of a For Each is the table navigated, as determined by GeneXus. Even though a For Each doesn’t navigate only one table, but also an [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029), the For each has a **base table** that is navigated, and its Extended Table is accessed to retrieve or update data (or filter by an attribute that belong to the extended table, etc.).
* **New:** Every time GeneXus finds a “new” command, it must identify the table where the record will be inserted. The table identified to make the insertion in it is the **base table** in this case.
* **Data Provider:** The base table of a Data Provider is the table navigated to charge a collection, or an instance in memory, etc. Even though a Data Provider doesn’t navigate only one table, but also an [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029), the Data Provider has a **base table** that is navigated and its extended table is accessed (for the purpose of retrieving data or filtering by an attribute that belong to the extended table, etc.).
* **Grid:** The base table of a grid is the table navigated to retrieve and display in the grid the required attributes. Even though not only one table is browsed, but also an [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029), the grid has a base table that is navigated, and its extended table is accessed (for the purpose of retrieving data too or filtering by an attribute that belongs to the extended table, etc.).
* **Formula:** The **base table** of a formula is the table that is going to be navigated in order to evaluate it (to calculate its result value).
* **Subtype Group object:** The **base table** of a subtype group is the table whose complete primary key is included in the subtype group definition, as the key of the group (the subtype group must include a subtype attribute or a set of subtype attributes, whose corresponding supertype attributes make up the primary key of an existing table, which it is the base table of the group).

### [See Also](#See+Also)

[Extended Table](https://wiki.genexus.com/commwiki/wiki?6029)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Base and Extended table](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/base-and-extended-table)


|  |
| --- |
| **Backlinks** |
| [Attributes and Tables that can be Involved in Formulas](https://wiki.genexus.com/commwiki/wiki?6490) | [Automatic paging in Grid control](https://wiki.genexus.com/commwiki/wiki?6086) | [Base Transaction clause](https://wiki.genexus.com/commwiki/wiki?25418) |
| [Base Trn property](https://wiki.genexus.com/commwiki/wiki?36811) | [Conditions property](https://wiki.genexus.com/commwiki/wiki?9763) |
| [Conditions property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55966) | [Data Provider Group statement](https://wiki.genexus.com/commwiki/wiki?25082) | [Data Selectors in Aggregations](https://wiki.genexus.com/commwiki/wiki?5432) | [Data Selectors in For Each command](https://wiki.genexus.com/commwiki/wiki?5312) |
| [Delete command](https://wiki.genexus.com/commwiki/wiki?6828) | [Determining the Base Table for each Grid in a Web Panel](https://wiki.genexus.com/commwiki/wiki?6105) | [Determining the Base Table for the Form and Grid in Panels](https://wiki.genexus.com/commwiki/wiki?24807) |
| [Example: New Command](https://wiki.genexus.com/commwiki/wiki?6742) | [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029) | [FirstPage method](https://wiki.genexus.com/commwiki/wiki?8768) |
| [FirstPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55984) | [Formulas/Generating SQL](https://wiki.genexus.com/commwiki/wiki?3155) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [GotoPage method](https://wiki.genexus.com/commwiki/wiki?8772) |
| [GotoPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55994) | [Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064) | [Group Navigations that receive attributes as parameters](https://wiki.genexus.com/commwiki/wiki?18243) | [HowTo: Work with rows in a Transaction Grid](https://wiki.genexus.com/commwiki/wiki?6816) |
| [Inferred attribute](https://wiki.genexus.com/commwiki/wiki?22496) | [LastPage method](https://wiki.genexus.com/commwiki/wiki?8771) | [LastPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55989) |
| [Load command](https://wiki.genexus.com/commwiki/wiki?8196) | [Load event](https://wiki.genexus.com/commwiki/wiki?8188) | [Max, Min Formulas](https://wiki.genexus.com/commwiki/wiki?6502) |
| [Category:Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042) | [Navigation Reports for Procedures, Web Panels and Data Providers](https://wiki.genexus.com/commwiki/wiki?7178) | [Nested For Each commands to implement a Cartesian Product](https://wiki.genexus.com/commwiki/wiki?30876) | [Nested For Each commands to implement a Control Break](https://wiki.genexus.com/commwiki/wiki?30878) |
| [NextPage method](https://wiki.genexus.com/commwiki/wiki?8769) | [NextPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55985) | [Null function](https://wiki.genexus.com/commwiki/wiki?8421) | [Order clause](https://wiki.genexus.com/commwiki/wiki?6075) |
| [Category:Panel object](https://wiki.genexus.com/commwiki/wiki?24829) | [PreviousPage method](https://wiki.genexus.com/commwiki/wiki?8770) | [PreviousPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55992) |
| [Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863) | [Server-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24234) |
| [Category:Subtype Group object](https://wiki.genexus.com/commwiki/wiki?20206) | [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) | [Update rule](https://wiki.genexus.com/commwiki/wiki?21430) | [Category:Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) |
| [Where clause](https://wiki.genexus.com/commwiki/wiki?8578) |

---
