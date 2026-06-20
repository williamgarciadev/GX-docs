---
title: "Location property"
source_id: 7956
source_url: https://wiki.genexus.com/commwiki/wiki?7956
genexus_version: "18"
---

# Location property

Indicate the location in which the object will be run. This information is used in 3 tiers models, in an RPC call with C generator, or in an object with SOAP call protocol.

### [Description](#Description)

In [Data Views](https://wiki.genexus.com/commwiki/wiki?1914) specifies the location where GeneXus can find the file. The property applies to the following platforms:

| **Platform** | **Description** |
| --- | --- |
| DB2 for iSeries | Library name only if you want GeneXus to hardcode the name of the library in generated programs 1. |
| Informix, Oracle, PostgreSQL, SQL Server | Here the database name is stored. |

1 If you choose this, then you will have to re-generate all programs if the file is moved to a different library, or if different libraries are used or each different working environment (development and production). Remember, you can use the iSeries library list to search for files.

### [Scope](#Scope)

**Objects:** Data View, Procedure, Transaction, Web Panel

### [See Also](#See+Also)

[Main program property](https://wiki.genexus.com/commwiki/wiki?7407)  
[Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947)
