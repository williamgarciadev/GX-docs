---
title: "Navigation Reports for Procedures, Web Panels and Data Providers"
source_id: 7178
source_url: https://wiki.genexus.com/commwiki/wiki?7178
genexus_version: "18"
---

# Navigation Reports for Procedures, Web Panels and Data Providers

Displays the course of action a [GeneXus object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1866,,) will take when generated. The Navigation diagram helps you analyze the performance and sequences of the object's operation.

### [For Each / Grid / Data Provider Group](#For+Each+%2F+Grid+%2F+Data+Provider+Group)

**FOR EACH Base Table Name:** [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) of the main [For each command](https://wiki.genexus.com/commwiki/wiki?24744) / [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) / Data Provider Group.

**Order:** List of Index Attributes, this order can be specified by the user or [inferred by GeneXus](https://wiki.genexus.com/commwiki/wiki?5100) to optimize navigation.

**Index:** Index name that will probably be used for Base Table access.

**Warning/Error:** Declares Warnings or Errors that have been detected in this Group.

**Navigation filter:** Inferred or specified conditions that act as a filter for the group.Table data retrieval when using the selected index.

**Constraint:** Data Retrieval Conditions.

Constraint can be classified between server constraint (DBMS) and client constraint (application server). The former will be included directly in the SQL sentence and in the latter, the filter will be applied in the generated program. Server constraint will lead in a database access optimization, so when a constraint can not be optimized, the condition is shown with a warning image that said : `[imagen omitida: wiki id 21326]` Constraint evaluated in the client. This may lead to poor performance.

### [See also](#See+also)

[Navigation Report for Transactions](https://wiki.genexus.com/commwiki/wiki?7177)


|  |
| --- |
| **Backlinks** |
| [Azure Cosmos DB execution errors](https://wiki.genexus.com/commwiki/wiki?53482) | [Database performance from the GeneXus perspective](https://wiki.genexus.com/commwiki/wiki?26285) | [Last Navigation](https://wiki.genexus.com/commwiki/wiki?7184) |

---
