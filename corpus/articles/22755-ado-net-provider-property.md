---
title: "ADO.NET provider property"
source_id: 22755
source_url: https://wiki.genexus.com/commwiki/wiki?22755
genexus_version: "18"
---

# ADO.NET provider property

Sets the ADO.NET provider used to connect with the DBMS.

### [Values](#Values)

|  |
| --- |
| **HIS Data Provider** |
| **IBM Data Provider** |
| **Oracle Managed Driver** |
| **Microsoft Data Provider** |
| **MySQL Connector** |
| **MySQLDriverCS** |
| **Oracle Data Provider** |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** Oracle, iSeries, MySQL  
**Generators:** [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)

### [Description](#Description)

The offered values depend on the [Data Store](https://wiki.genexus.com/commwiki/wiki?7117) set for the [Environment](https://wiki.genexus.com/commwiki/wiki?7115).

**Oracle-specific**

In particular, the 'Oracle Managed Driver' value offered when the Data Store is Oracle has been available since GeneXus 15 U12. It allows you to connect to 10g Release 2 (or later) from .Net applications without having the Oracle client installed.

It is useful when you want to upload the application to a PAAS and nothing can be installed on the server.

The dll must be copied to the web\bin directory or put in the GAC to work at runtime. It can be downloaded from https://www.nuget.org/packages/Oracle.ManagedDataAccess/

You must also copy the Oracle tnsnames.ora to the web or web\bin directory for command-line programs.

If [Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) is set to True, copy the dll and Oracle tnsnames.ora to the corresponding GAM platform installation directory (<GeneXus path>\Library\GAM\Platforms\netOracle)

**MySQL-specific**

MySQL Connector (<http://www.nuget.org/packages/MySqlConnector/>) is a fully managed ADO.NET provider.

MySQLDriverCS (<http://sourceforge.net/projects/mysqldrivercs>) is not fully managed; it requires an extra dlls (see [MySQL driver for .NET installation](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?2041,,) for Mysql 4.x to 5.x and [SAC #43792](https://www.genexus.com/en/developers/websac?data=43792) for Mysql 8).

More information at [ADO.NET drivers for MySQL](https://wiki.genexus.com/commwiki/wiki?47458).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.


|  |
| --- |
| **Backlinks** |
| [ADO.NET drivers for MySQL](https://wiki.genexus.com/commwiki/wiki?47458) |

---
