---
title: "Create Database"
source_id: 7877
source_url: https://wiki.genexus.com/commwiki/wiki?7877
genexus_version: "18"
---

# Create Database

To create a complete Database when editing the connection.

When you press F5 to prototype the application, or when you are creating the Database tables, GeneXus checks the login connection with the selected DBMS. If it fails, the following message is displayed:

`[imagen omitida: wiki id 7878]`

As mentioned, you can create the entire Database by clicking on the Create Database link as shown below.

`[imagen omitida: wiki id 7879]`

So, the Database and tables will be created immediately.

### [Considerations](#Considerations)

When using Java generator, the class path is set using the folder *GeneXus\_Installation/gxjava/drivers*. If you use a non standard JDBC driver make sure to copy it to the \drivers location; otherwise the Test connection option will detail

```
java.sql.SQLException: No suitable driver found for jdbc:protocol://server:port/db
```

When using C# generator, make sure to install the correct Ado.Net driver on the machine and copy the assembly to the genexus installation folder.

* *SQLServer*: the .net framework installs the driver; no action is needed.
* *MySQL*: make sure to install the ado.net MySQLDriverCS driver.
* *Oracle*: the .net framework installs the driver; no action is needed.
* *Db2 UDB*: make sure to install the associated driver and copy the IBM.Data.DB2.dll file to the GeneXus installation folder.
* *Db2 for iSeries*: make sure to install the associated driver and copy the IBM.Data.DB2.iSeries.dll file to the GeneXus installation folder.
* *Informix*: make sure to install the associated driver and copy the IBM.Data.Informix.dll file to the GeneXus installation folder.
* *PostgreSQL*: the driver (npgsql.dll file) is distributed with GeneXus; no action is needed.

To use double byte characters please see this sac <https://www.genexus.com/en/developers/websac?data=15602;;>


|  |
| --- |
| **Backlinks** |
| [Default KB language and Database Collation](https://wiki.genexus.com/commwiki/wiki?42336) | [Default KB language and Database Collation (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?53433) |

---
