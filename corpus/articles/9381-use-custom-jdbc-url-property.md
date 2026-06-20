---
title: "Use Custom JDBC URL Property"
source_id: 9381
source_url: https://wiki.genexus.com/commwiki/wiki?9381
genexus_version: "18"
---

# Use Custom JDBC URL Property

It allows typing the specific JDBC URL in the Custom JDBC URL property.

### [Values](#Values)

|  |  |
| --- | --- |
| **False** | It does not enable the Custom JDBC URL property. This is the default value. |
| **True** | It enables the Custom JDBC URL property. |

### [Description](#Description)

By choosing Use Custom JDBC URL = “True” you'll be able to type the specific JDBC URL in the Custom JDBC URL property. However, if you choose Use Custom JDBC URL = “False,” GeneXus will put together the JDBC URL, and do that the following properties will be enabled:

* **Database Name**, so that the name of the database may be entered.
* **Server Name**, so that the server's name or IP address may be entered.
* **Server TCP/IP Port**, so that the port for connection with the DBMS is entered. We recommend using the default port for connection with each DBMS.

With these three properties, GeneXus will automatically put together the JDBC URL. In order to do that, it takes into account not only the value of these three properties but also the value selected in the **JDBC Driver** and **DBMS Version** properties.

For instance, for SQL Server, if the value of the **JDBC Driver** property is "jTDS Driver (Type 4)," GeneXus will put together the following URL:

```
jdbc:jtds:sqlserver://database_host:1433/database_name
```

If the value of the JDBC Driver were "Microsoft JDBC Driver (Type 4)," it would put together this other URL:

```
jdbc:sqlserver://database_host:1433;databaseName=database_name
```

Other sample JDBC URL strings

```
// mySQL
jdbc:mysql://hostname/databaseName
// Oracle
jdbc:oracle:thin:@hostname:portNumber:databaseName
// DB2
jdbc:db2:hostname:portNumber/databaseName
```

### [Notes](#Notes)

* The URL generated depends on each DBMS version.
* Modifying the **Use Custom JDBC URL** property depends on the value of the [JDBC Driver](https://wiki.genexus.com/commwiki/wiki?10391,,) property, which must be other than "Custom Driver."

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

Build any object

### [Scope](#Scope)

**Drivers:** JDBC  
**DBMSs:** SQL Server, Oracle, iSeries Native, DB2 Universal Database, Informix, PostgreSQL, MySQL

### [See Also](#See+Also)

[JDBC Driver Property](https://wiki.genexus.com/commwiki/wiki?10391,,)  
[Database name property](https://wiki.genexus.com/commwiki/wiki?9080)  
[Server Name Property](https://wiki.genexus.com/commwiki/wiki?9117)  
[Server TCP/IP Port Property](https://wiki.genexus.com/commwiki/wiki?9382,,)


|  |
| --- |
| **Backlinks** |
| [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) | [Deploy to SAP Cloud Foundry - SAP BTP](https://wiki.genexus.com/commwiki/wiki?49572) | [Deploy to SAP Cloud Foundry - SAP BTP (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54602) |
|

---
