---
title: "Connection pooling and Datasource definitions"
source_id: 18717
source_url: https://wiki.genexus.com/commwiki/wiki?18717
genexus_version: "18"
---

# Connection pooling and Datasource definitions

Both properties [Enable Connection Pooling Property](https://wiki.genexus.com/commwiki/wiki?9385) and [Use Datasource for Web Based Applications Property](https://wiki.genexus.com/commwiki/wiki?9384,,) are closely related to each other as they work with DBMS Connections.

Behavior proceeds as follows:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Use Datasource for Web Based Application Property** | **Enable Connection Pooling Property** | **DBMS connection** | **Connection Pool** | **Connections recycle** |
| True | True (Not Apply) | Uses the Application Server Datasource configuration | Application Server Datasource dependant | Application Server Datasource dependant |
| False (Not Apply) | Uses the Application Server Datasource configuration | Application Server Datasource dependant | Application Server Datasource dependant |
| False | True | Managed by a set of classes included in [GeneXus Standard Classes](https://wiki.genexus.com/commwiki/wiki?18859) | Managed by GeneXus built-in connection pooling | Managed by GeneXus built-in connection pooling |
| False | Managed by a set of classes included in [GeneXus Standard Classes](https://wiki.genexus.com/commwiki/wiki?18859) | Not applied | Not applied |


|  |
| --- |
| **Backlinks** |
| [Enable connection pooling property](https://wiki.genexus.com/commwiki/wiki?9385) |

---
