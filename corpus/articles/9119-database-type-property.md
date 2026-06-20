---
title: "Database type property"
source_id: 9119
source_url: https://wiki.genexus.com/commwiki/wiki?9119
genexus_version: "18"
---

# Database type property

Enables the generator know the type of INFORMIX database it is connecting to.

### [Values](#Values)

|  |  |
| --- | --- |
| **ANSI** | Indicate this value if the database was created with the “WITH LOG MODE ANSI” option from the CREATE DATABASE command. |
| **Logged** | Specify this value if you wish to create the database that uses the “WITH {BUFFERED} LOG” (the reserved word BUFFERED is optional) with the CREATE DATABASE command. |
| **Not Logged** | Specify this value if no LOG specification options where indicated when the database was created. |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** INFORMIX  
**Level:** [Data Store](https://wiki.genexus.com/commwiki/wiki?7117)

### [Description](#Description)

With ANSI value, transactions are automatically triggered by INFORMIX (in this case it is not possible to avoid transactional integrity and as a consequence the value of the ‘Transactional integrity’ property will be ignored. So, Yes will always be considered). As a consequence, all processes including the reorganization are executed with transactional integrity control.

With Logged value, the program (BEGIN WORK command) explicitly initializes transactions. The reorganization, in this case, executes without transactional integrity.

With Not Logged value, transactional integrity cannot be activated and as a consequence the value specified by the ‘Transactional Integrity’ property is ignored and the value will always be considered as No). No process (including the reorganization) executes with transactional integrity.

**DBMS:** Informix.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build any object. |

### [See Also](#See+Also)

[Lock Mode property](https://wiki.genexus.com/commwiki/wiki?9091,,)


|  |
| --- |
| **Backlinks** |
| [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) |

---
