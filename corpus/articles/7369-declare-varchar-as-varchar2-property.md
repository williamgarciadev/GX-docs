---
title: "Declare Varchar as Varchar2 property"
source_id: 7369
source_url: https://wiki.genexus.com/commwiki/wiki?7369
genexus_version: "18"
---

# Declare Varchar as Varchar2 property

Only applies to GeneXus Varchar data types. It allows controling if, in ORACLE, this data type is defined as Varchar2 or Varchar.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | Varchar data type attributes are not declared as Oracle’s Varchar2 |
| **Yes** | Varchar data type attributes are declared as Oracle’s Varchar2 |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** ORACLE  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

If the value for this property is modified, then the reorganization of tables that use Varchar attributes will not be forced. The change in an attribute’s definition will take place the next time a reorganization is required.

### [See Also](#See+Also)

* [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778)


|  |
| --- |
| **Backlinks** |
| [Data types of attributes in the DBMS](https://wiki.genexus.com/commwiki/wiki?3297) | [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) | [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) |

---
