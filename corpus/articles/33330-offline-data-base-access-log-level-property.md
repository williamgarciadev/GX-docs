---
title: "Offline Data Base Access Log Level property"
source_id: 33330
source_url: https://wiki.genexus.com/commwiki/wiki?33330
genexus_version: "18"
---

# Offline Data Base Access Log Level property

Set the log level desired related to the database access on the device.

### [Values](#Values)

|  |  |
| --- | --- |
| **Debug** | Info level plus useful information for the developer is saved. |
| **Error** | Show issues that have caused errors. |
| **Info** | Error, warnings and any other relevant information is saved. |
| **Off** | Default value. Logging is disabled. |
| **Warning** | Error and warnings are saved. |

### [Samples](#Samples)

#### [Android Examples](#Android+Examples)

**Info**

```
I/System.out(3323): Creating table t002 .
I/System.out(3323): Creating index IT002 ...
I/System.out(3323): Creating table GxPendingEvent .
I/System.out(3323): Creating index IPENDINGEVENT ..
```

**Debug**

```
D/SQLDroid(3763): sqlite setAutoCommit beginTransaction 
D/SQLDroid(3763): sqlite setAutoCommit setTransactionSuccessful endTransaction
D/SQLDroid(3763): sqlite setAutoCommit beginTransaction 
D/SQLDroid(3763): sqlite setAutoCommit setTransactionSuccessful endTransaction
D/SQLDroid(3763): sqlite setAutoCommit beginTransaction 
D/SQLDroid(3763): new SqlDRoid prepared statement from org.sqldroid.SQLDroidConnection@21c5819 sql SELECT [PendingEventStatus], [PendingEventId], [PendingEventBC], [PendingEventAction], [PendingEventData], [PendingEventErrors], [PendingEventFiles], [PendingEventTimestamp] FROM [GxPendingEvent] WHERE  ([PendingEventStatus] = ?) ORDER BY [PendingEventTimestamp]
D/SQLDroid(3763): executeQuery SELECT [PendingEventStatus], [PendingEventId], [PendingEventBC], [PendingEventAction], [PendingEventData], [PendingEventErrors], [PendingEventFiles], [PendingEventTimestamp] FROM [GxPendingEvent] WHERE  ([PendingEventStatus] = ?) ORDER BY [PendingEventTimestamp]
D/SQLDroid(3763): sqlite endTransaction
D/SQLDroid(3763): sqlite beginTransaction
D/SQLDroid(3763): new SqlDRoid prepared statement from org.sqldroid.SQLDroidConnection@21c5819 sql INSERT INTO [t002]([t002Id], [t002Dsc], [t002Date], [t002Int1]) VALUES(?, ?, ?, ?)
D/SQLDroid(3763): execute INSERT INTO [t002]([t002Id], [t002Dsc], [t002Date], [t002Int1]) VALUES(?, ?, ?, ?)
D/SQLDroid(3763): sqlite commit setTransactionSuccessful endTransaction beginTransaction
D/SQLDroid(3763): sqlite endTransaction
D/SQLDroid(3763): sqlite beginTransaction
D/SQLDroid(3763): executeQuery SELECT [PendingEventStatus], [PendingEventId], [PendingEventBC], [PendingEventAction], [PendingEventData], [PendingEventErrors], [PendingEventFiles], [PendingEventTimestamp] FROM [GxPendingEvent] WHERE  ([PendingEventStatus] = ?) ORDER BY [PendingEventTimestamp]
D/SQLDroid(3763): sqlite endTransaction
```

### [Scope](#Scope)

**Platforms:** Smart Devices(Android, IOS)


|  |
| --- |
| **Backlinks** |
| [Default Log Level property](https://wiki.genexus.com/commwiki/wiki?33333) | [Enable Logging property](https://wiki.genexus.com/commwiki/wiki?37876) | [HowTo: Enable logging for Native Mobile](https://wiki.genexus.com/commwiki/wiki?37846) |
| [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
