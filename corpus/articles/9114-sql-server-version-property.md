---
title: "SQL server version property"
source_id: 9114
source_url: https://wiki.genexus.com/commwiki/wiki?9114
genexus_version: "18"
---

# SQL server version property

Indicates which SQL Server version is installed on the Database Server.

### [Values](#Values)

|  |  |
| --- | --- |
| **2012 or higher** | The SQL Server version installed on the Server is 2012 or higher. |
| **Azure** | The SQL Server is an Azure SQL Database or an Azure SQL Managed Instance. |
| **2000** | The SQL Server version installed on the Server is 2000. |
| **2005 to 2008 R2** | The SQL Server version installed on the Server is between 2005 and 2008 R2. |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** SQL Server

### [Description](#Description)

**Note**: Since GeneXus 17 update 10, the SQL Server 2000 value has been discontinued. Read more at [SAC #51285](https://www.genexus.com/en/developers/websac?data=51285;;).

**Note**: Since GeneXus 17 update 11, the Azure value has been discontinued. Instead, you can use the value 2012 or higher when generating for SQL Azure. Read more at [SAC#51502](https://www.genexus.com/developers/websac?en,,,51502).

It is used, for example, to determine the syntax for OUTER JOINs and for table creation/reorganizations (i.e., the syntax of CREATE TABLE, CREATE INDEX, etc.).

When the SQL Server version Azure is selected, the code is generated as if SQL Server 2012 or higher is selected. The exception to this is, that the temporary tables that are created during the reorganization process are created with a clustered index given related restrictions of SQL Azure.

Every new version of the DBMS has new features that are used by GeneXus, which generates different SQL sentences or considers properties that can be applied to the new version.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Lock time-out (seconds) property](https://wiki.genexus.com/commwiki/wiki?9116)  
[Oracle version property](https://wiki.genexus.com/commwiki/wiki?9112)


|  |
| --- |
| **Backlinks** |
| [DB2UDB version property](https://wiki.genexus.com/commwiki/wiki?9397) | [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) | [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900) |
| [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54300) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54649) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55768) | [GeneXus 18 hardware and software requirements (GeneXus 18 Upgrade 6)](https://wiki.genexus.com/commwiki/wiki?56187) |
| [GXflow Software Requirements](https://wiki.genexus.com/commwiki/wiki?18393) | [GXflow Software Requirements (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55579) | [Informix Version property](https://wiki.genexus.com/commwiki/wiki?9399) |
| [Lock time-out (seconds) property](https://wiki.genexus.com/commwiki/wiki?9116) | [MySQL version property](https://wiki.genexus.com/commwiki/wiki?9420) | [Oracle version property](https://wiki.genexus.com/commwiki/wiki?9112) |

---
