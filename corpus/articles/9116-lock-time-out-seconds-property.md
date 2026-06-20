---
title: "Lock time-out (seconds) property"
source_id: 9116
source_url: https://wiki.genexus.com/commwiki/wiki?9116
genexus_version: "18"
---

# Lock time-out (seconds) property

When accessing a locked record, it indicates the time in seconds to try to obtain the record.
The value is defined in seconds; the default value is zero for all DBMS except for Oracle, which is one.

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** AS400, INFORMIX, ORACLE, POSTGRESQL, SQLSERVER

### [Description](#Description)

In the case of an object with an interface, once this time has elapsed, the control is returned to the program and a message is displayed to the user for him/her to decide whether to retry or cancel the time-out.

In the case of an object without an interface, such as SQL Server, PostgreSQL, it waits until the record is released. With iSeries handler, it retries for up to ten times the specified time-out and then sends a message to the system's operator.

### [Notes](#Notes)

* This property can only be configured for iSeries, when it is used as ‘iSeries native' access technology (i.e.: generating RPG or Cobol, but not in the SQL accesses), and for SQL Server with version 7.0 or higher, with the access technologies employed by all the Client/Server generators (.NET, Java, and Visual FoxPro).
* If the handler is iSeries, the value 0 indicates that it takes the value configured in the properties of the physical file (WAITRCD); if the handler is SQL Server, it indicates that attempts will be made indefinitely.
* When the property is set to 0, the *NoWait* clause in SQL generators is not generated; it applies to objects without an interface (Procedures and Business Components).
* PostgreSQL support is added in Xev2 Upgrade #4 (Java generator), for PostgreSQL 8.1 or higher.
* If the handler is PostgreSQL, an [optimized For Each command](https://wiki.genexus.com/commwiki/wiki?26286) ignores this property.
* For more details on Oracle default values, read [SAC#21696](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,21696)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [See Also](#See+Also)

* [Lock retry count property](https://wiki.genexus.com/commwiki/wiki?9400)
* [SQL server version property](https://wiki.genexus.com/commwiki/wiki?9114)
* [PostgreSQL version property](https://wiki.genexus.com/commwiki/wiki?9419)


|  |
| --- |
| **Backlinks** |
| [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) | [Lock retry count property](https://wiki.genexus.com/commwiki/wiki?9400) |
| [SQL server version property](https://wiki.genexus.com/commwiki/wiki?9114) |

---
