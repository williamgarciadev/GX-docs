---
title: "PostgreSQL version property"
source_id: 9419
source_url: https://wiki.genexus.com/commwiki/wiki?9419
genexus_version: "18"
---

# PostgreSQL version property

Sets the PostgreSQL version that is installed in the Database Server.

### [Values](#Values)

|  |  |
| --- | --- |
| **7.x** | The PostgreSQL version installed in the Server is 7.x. Unique indexes are not generated. |
| **8.0** | The PostgreSQL version installed in the Server is 8.0. If this value is selected, Unique indexes are generated. |
| **8.1 or 8.2** | The PostgreSQL version installed in the Server is 8.1 or 8.2. If this value is selected, Unique indexes are generated. |
| **8.3 or higher** | The PostgreSQL version installed in the Server is 8.3 or higher. If this value is selected, Unique indexes are generated. |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** POSTGRESQL

### [Description](#Description)

It is used, for example, to determine the syntax for OUTER JOINs and for table creation/reorganization (i.e. syntax of CREATE TABLE, CREATE INDEX, etc.).

Every new version of the DBMS has new features that are used by GeneXus, which generates different SQL sentences or considers properties that can be applied to the new version.

**Note:**Unique indexes are not supported in PostgreSQL for versions prior to 7.3.11 (this is a restriction of the database engine itself).

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691). |

### [See Also](#See+Also)

* [ADO.NET drivers for PostgreSQL](https://wiki.genexus.com/commwiki/wiki?47954,,)


|  |
| --- |
| **Backlinks** |
| [DB2UDB version property](https://wiki.genexus.com/commwiki/wiki?9397) | [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55768) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) | [GXflow Software Requirements](https://wiki.genexus.com/commwiki/wiki?18393) |
| [GXflow Software Requirements (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55579) | [Lock time-out (seconds) property](https://wiki.genexus.com/commwiki/wiki?9116) | [MySQL version property](https://wiki.genexus.com/commwiki/wiki?9420) | [Oracle version property](https://wiki.genexus.com/commwiki/wiki?9112) |

---
