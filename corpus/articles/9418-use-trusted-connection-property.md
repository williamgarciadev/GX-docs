---
title: "Use trusted connection property"
source_id: 9418
source_url: https://wiki.genexus.com/commwiki/wiki?9418
genexus_version: "18"
---

# Use trusted connection property

Connects to the Database using the Windows authentication method when the Database engine is SQL Server or Oracle.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | DBMS authentication is used to connect to the Database. |
| **Yes** | Windows authentication is used to connect to the Database. This is the default value. |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** ORACLE, SQLSERVER  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

When the value is Yes, the programs do not require a username and password to connect to the DBMS.

A connection is automatically established (by the DBMS) through the user logged on to the operating system.

For Web applications in particular, the value "Yes" will take the default user used to run web objects (for example, in IIS the user is known as IUSR\_MASTER). It must have access rights to the database; otherwise, another username must be configured with the necessary rights.

If the value is No, the programs require a username and password to establish a connection with the DBMS. To this end, the username and password dialog is enabled in the [DBMS Options](https://wiki.genexus.com/commwiki/wiki?9067). You will have to enter a valid username previously defined at the database level.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.


|  |
| --- |
| **Backlinks** |
| [.NET Generator Troubleshooting](https://wiki.genexus.com/commwiki/wiki?50588) | [Deploy to GeneXus Prototyping Cloud - FAQ](https://wiki.genexus.com/commwiki/wiki?18292) |
| [User Properties](https://wiki.genexus.com/commwiki/wiki?25111) |

---
