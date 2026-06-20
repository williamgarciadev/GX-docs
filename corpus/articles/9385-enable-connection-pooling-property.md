---
title: "Enable connection pooling property"
source_id: 9385
source_url: https://wiki.genexus.com/commwiki/wiki?9385
genexus_version: "18"
---

# Enable connection pooling property

Enables the use of the GeneXus built-in connection pooling mechanism.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Description](#Description)

Enables or disables the use of the GeneXus built-in connection pooling.

The GeneXus built-in connection pooling is the default mechanism which is used to manage DBMS connections.

Each time an application attempts to access a database, it requires resources to create, maintain, and release a connection to that data store. The GeneXus built-in connection pooling establishes a pool of backend connections to be shared by the application. Connection pooling spreads the connection overhead across several user requests, thereby conserving application resources for future requests.

When this property is set to "true", the GeneXus built-in connection pooling is used and the following properties define the pooling behavior:

* [Unlimited size property](https://wiki.genexus.com/commwiki/wiki?9386)
* [Size property](https://wiki.genexus.com/commwiki/wiki?10585)
* [Create All Pool Connections at Startup Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18888,,)
* [Recycle Pool Connections Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?9387,,)
* [Recycle Type Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?9388,,)
* [Recycle Time (Minutes) Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?9389,,)

When this property is set to "false" the GeneXus built-in connection pooling is not used.

### [See Also](#See+Also)

* [Use Datasource for Web Based Applications Property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?9384,,)
* [Connection pooling and Datasource definitions](https://wiki.genexus.com/commwiki/wiki?18717)


|  |
| --- |
| **Backlinks** |
| [Connection pooling and Datasource definitions](https://wiki.genexus.com/commwiki/wiki?18717) | [Dameng](https://wiki.genexus.com/commwiki/wiki?50988) | [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) |
|

---
