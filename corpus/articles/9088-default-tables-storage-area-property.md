---
title: "Default Tables Storage Area property"
source_id: 9088
source_url: https://wiki.genexus.com/commwiki/wiki?9088
genexus_version: "18"
---

# Default Tables Storage Area property

Allows you to indicate the name of the tablespace where GeneXus will create/reorganize the tables.

### [Values](#Values)

The Tablespace Storage Area Name, this property is not related to a default value.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

Create database

If this option is not used, GeneXus will not generate the TABLESPACE clause when the tables are created/reorganized. This means that the tables will be created, by default, in the current user's tablespace.

### [**Notes**](#Notes)

* A change in this configuration option (moving tables to other tablespaces) will not force the entire reorganization of the database. The change affects the creation/reorganization processes that are carried out later on, and they are only performed over the tables that these processes can manipulate. In other words, a change in this configuration option will gradually be noted by the database as these tables are created.
* GeneXus does not create the tablespace. If a table is created and the Tablespace does not exist then an error will occur.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Languages** | .Net, Java, Visual FoxPro |
| **DBMS** | SQL Server, Oracle, Informix |

### [See also](#See+also)

[Default indices storage area property](https://wiki.genexus.com/commwiki/wiki?7155)  
[Default Temporary Storage Area Property](https://wiki.genexus.com/commwiki/wiki?9087)  
[Storage Area Property](https://wiki.genexus.com/commwiki/wiki?7144,,)


|  |
| --- |
| **Backlinks** |
| [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) | [Default Temporary Storage Area Property](https://wiki.genexus.com/commwiki/wiki?9087) |

---
