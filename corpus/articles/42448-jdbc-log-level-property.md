---
title: "JDBC Log level property"
source_id: 42448
source_url: https://wiki.genexus.com/commwiki/wiki?42448
genexus_version: "18"
---

# JDBC Log level property

It allows to create a log file per namespace, or one per each datastore or one per each connection. It is useful to make it easier to understand the execution path of an application.

### [Values](#Values)

|  |
| --- |
| **Namespace** |
| **Data Store** |
| **Connection** |

### [Description](#Description)

This option makes it easier to read the execution path of an application. For example, when trying to find an error caused by database locking. All connections are mixed in a single log, which makes it harder to follow the thread and ignore, for instance, connections that are not relevant to the problem.

Log names are written in this way: "gx\_" + MMDD + "\_" + HHMMSS + <namespace> + "\_" + <datastore> + "\_" + <connection> + ".log" where  
MMDD - Month Day  
HHMMSS - Hour Minutes Seconds  
namespace - Application package name  
datastore - Data store to which the connection is being made  
connection - Connection ID

Example: gx\_0129\_100352\_com.testlogjdbc\_DEFAULT\_24306159.log

### [Scope](#Scope)

**Platforms:** Web(Java)
