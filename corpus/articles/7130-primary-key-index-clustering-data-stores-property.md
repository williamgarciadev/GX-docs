---
title: "Primary key Index Clustering Data Stores Property"
source_id: 7130
source_url: https://wiki.genexus.com/commwiki/wiki?7130
genexus_version: "18"
---

# Primary key Index Clustering Data Stores Property

Define whether the primary key index is created ‘clustered’ or ‘not clustered’ at the DBMS Options level.

### [Values](#Values)

|  |  |
| --- | --- |
| **Clustered** | The index is created with the following syntax:  “CREATE UNIQUE CLUSTERED INDEX …”. This is the default value. |
| **Not clustered** | The index is created with the following syntax:  “CREATE UNIQUE NONCLUSTERED INDEX …” |

### [Description](#Description)

This DBMS Option applies when the [Primary key Definition property](https://wiki.genexus.com/commwiki/wiki?7826,,) is ‘Index’. Clustered means that the index order at a physical level matches the logical order.

### [Scope](#Scope)

**Languages:** .NET, Java, Visual Basic, Visual FoxPro

**DBMS:** Informix and SQL Server

### [See Also](#See+Also)

[Primary Key Definition Data Stores Property](https://wiki.genexus.com/commwiki/wiki?7826,,)
