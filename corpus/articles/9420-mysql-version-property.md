---
title: "MySQL version property"
source_id: 9420
source_url: https://wiki.genexus.com/commwiki/wiki?9420
genexus_version: "18"
---

# MySQL version property

Sets the MySQL version range for which the code is generated.

### [Values](#Values)

|  |  |
| --- | --- |
| **4.x to 5.0.2** | The MySQL version installed on the Server is between 4.x and 5.0.2. |
| **5.0.3 to 5.7.6** | The MySQL version installed on the Server is between 5.0.3 and 5.7.6. |
| **5.7.7 to 5.7.23** | The MySQL version installed on the Server is between 5.7.7 and 5.7.29. |
| **8.x or higher** | The MySQL version installed on the Server is 8.x or higher. |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** MySQL  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This property is used, for example, to determine the syntax for OUTER JOINs and for table creation/reorganization (i.e. syntax of CREATE TABLE, CREATE INDEX, etc.).

Notes related to MySQL 8 or higher:

* Java-specific: If date fields are read with one less day (e.g.: 1930-01-30 is returned as 1930-01-29), you may need to add the timezone of the application server to the connection string (eg.:&serverTimezone=America/Montevideo)
* As stated in the [Release Notes of MySQL 8](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-1.html), the default character\_set\_server, character\_set\_database, collation\_server, and collation\_database environment variables changed. In addition, "The pad attribute for Unicode 9.0.0 collations was changed from PAD SPACE to NO PAD." Consequently, spaces are treated at the end of strings like any other character, which means that comparing "A " with "A" does not return true by default. If you don't want this behavior, you should change those default values.
* .NET-specific: [SAC 43792 - MySQL 8.0 support in .NET](https://www.genexus.com/developers/websac?es,,,43792)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[PostgreSQL version property](https://wiki.genexus.com/commwiki/wiki?9419)  
[SQL server version property](https://wiki.genexus.com/commwiki/wiki?9114)  
[Oracle version property](https://wiki.genexus.com/commwiki/wiki?9112)  
[DB2 UDB Version property](https://wiki.genexus.com/commwiki/wiki?10479)  
[Informix Version property](https://wiki.genexus.com/commwiki/wiki?9399)


|  |
| --- |
| **Backlinks** |
| [DB2 UDB Version property](https://wiki.genexus.com/commwiki/wiki?10479) | [DB2UDB version property](https://wiki.genexus.com/commwiki/wiki?9397) | [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55768) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) |
| [GXflow Software Requirements](https://wiki.genexus.com/commwiki/wiki?18393) | [GXflow Software Requirements (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55579) | [Informix Version property](https://wiki.genexus.com/commwiki/wiki?9399) |
| [Oracle version property](https://wiki.genexus.com/commwiki/wiki?9112) | [SQL server version property](https://wiki.genexus.com/commwiki/wiki?9114) | [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) |

---
