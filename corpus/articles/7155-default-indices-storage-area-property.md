---
title: "Default indices storage area property"
source_id: 7155
source_url: https://wiki.genexus.com/commwiki/wiki?7155
genexus_version: "18"
---

# Default indices storage area property

Controls the generation of the TABLESPACE clause when creating indices in the database.

### [Description](#Description)

If this property is not used, GeneXus will not generate the TABLESPACE clause when the indices are created. This means that the indices will be created, by default, in the current user's tablespace.

The specified value applies to all application indices (except for the case when specific tablespaces are indicated for particular indices) including those specified for the primary key, in any of its configuration options, see the [Primary Key Definition Property](https://wiki.genexus.com/commwiki/wiki?7826,,).

#### [Notes:](#Notes%3A)

* Applies when generating for SQL Server, Oracle, Informix and DB2 Universal Servers.
* A change in this configuration option (moving indices to other tablespaces) will not force the entire reorganization of the database. The change affects the creation/reorganization processes that are carried out later on, and they are only performed over the indices that these processes can manipulate. In other words, a change in this configuration option will gradually be noticed by the database as these indices are created.
* GeneXus does not create the tablespace. If an index is created and the Tablespace does not exist, an error will take place.

#### [Values](#Values)

The Index Storage Area Name; this property is not related to a default value.

#### [How to apply changes](#How+to+apply+changes)

Create database

### [Scope](#Scope)

**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[Storage Area Property](https://wiki.genexus.com/commwiki/wiki?7144,,)  
[Default Temporary Storage Area Property](https://wiki.genexus.com/commwiki/wiki?9087)


|  |
| --- |
| **Backlinks** |
| [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) | [Default Tables Storage Area property](https://wiki.genexus.com/commwiki/wiki?9088) | [Default Temporary Storage Area Property](https://wiki.genexus.com/commwiki/wiki?9087) |
|

---
