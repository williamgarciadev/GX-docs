---
title: "Unlimited size property"
source_id: 9386
source_url: https://wiki.genexus.com/commwiki/wiki?9386
genexus_version: "18"
---

# Unlimited size property

Defines whether the GeneXus built-in connection pool size will allow an unlimited number of connections.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** Iseries, DB2 UDB, INFORMIX, MYSQL, ORACLE, POSTGRESQL, SQLSERVER

### [Description](#Description)

When enabled, the GeneXus built-in connection pool is unlimited. Every time a client requests a database connection, a new one is created if no connections are available. This is the default value.

When disabled, the GeneXus built-in connection pool size is limited. Every time a client requests a new database connection, when there's no availability and the maximum number of pool connections has been reached, then the client remains waiting for one to be released. This value enables the following properties: [Size](https://wiki.genexus.com/commwiki/wiki?10585) and [Create all pool connections at startup](https://wiki.genexus.com/commwiki/wiki?18888,,).

The limited number of connections in the GeneXus built-in connection pool is configured with the [Size](https://wiki.genexus.com/commwiki/wiki?10585) property.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [See Also](#See+Also)

[Size property](https://wiki.genexus.com/commwiki/wiki?10585)  
[Create All Pool Connections at Startup Property](https://wiki.genexus.com/commwiki/wiki?18888,,)


|  |
| --- |
| **Backlinks** |
| [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) | [Enable connection pooling property](https://wiki.genexus.com/commwiki/wiki?9385) |
| [Size property](https://wiki.genexus.com/commwiki/wiki?10585) |

---
