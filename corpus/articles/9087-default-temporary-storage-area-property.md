---
title: "Default Temporary Storage Area Property"
source_id: 9087
source_url: https://wiki.genexus.com/commwiki/wiki?9087
genexus_version: "18"
---

# Default Temporary Storage Area Property

Lets you name the tablespace where GeneXus will create temporary tables and indexes required during the reorganization.

### [Values](#Values)

This property is not related to a default value, this implies that tables and indexes will be created in tablespaces for tables and indexes specified in their respective properties.

### [Notes](#Notes)

* This property does not apply to Informix DBMS as it supports the renaming of tables. So, temporary tables are created in the indicated space and thus ‘moving’ tables between different tablespaces and rename them is avoided. Tablespaces (for both indexes and tables) need to have been defined before you can actually refer to them. GeneXus does NOT create them.

There is a configuration setting (in the config.gx) that lets you specify a tablespace for each table in a model. The keyword is xxxxx\_TBLSPACE=tblspacename, where xxxxx is the name of the table for the tablespace you wish to specify. If you specify the property Default Tables Storage Area and the keyword is specified in the config.gx file then the keyword has priority.

There is another method you can use to make sure the change of these property values are considered by the database in its entirety instead of physically reorganizing each individual table. This option consists of backing up the database, creating a new GeneXus database and copying the backup data to the new database manually.

You will NOT need to generate application programs if there happens to be a change in tablespaces (whether the change be via the property or the config.gx).

* In DB2 Common Servers DBMS GXAnnnn tables are used as temporary tablespaces.

Tablespaces (for both indexes and tables) need to have been defined before you can actually refer to them. GeneXus does NOT create them.

There is a configuration setting (in the config.gx) that lets you specify a tablespace for each table in a model. The keyword is xxxxx\_TBLSPACE=tblspacename, where xxxxx is the name of the table for the tablespace you wish to specify. If you specify the property Default Tables Storage Area and the keyword is specified in the config.gx file then the keyword has priority.

There is another method you can use to make sure the change of these property values are considered by the database in its entirety instead of physically reorganizing each individual table. This option consists of backing up the database, creating a new GeneXus database and copying the backup data to the new database manually.

You will NOT need to generate application programs if there happens to be a change in tablespaces (whether the change be via the property or the config.gx).

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Languages** | .Net, Java, Visual FoxPro |
| **DBMS** | DB2 Universal Database, Informix, SQL Server, Oracle |
| **Interfaces** | Web |

### [See also](#See+also)

[Default Tables Storage Area property](https://wiki.genexus.com/commwiki/wiki?9088)  
[Default indices storage area property](https://wiki.genexus.com/commwiki/wiki?7155)


|  |
| --- |
| **Backlinks** |
| [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) | [Default indices storage area property](https://wiki.genexus.com/commwiki/wiki?7155) | [Default Tables Storage Area property](https://wiki.genexus.com/commwiki/wiki?9088) |
|

---
