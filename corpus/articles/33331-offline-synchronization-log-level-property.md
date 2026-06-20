---
title: "Offline Synchronization Log Level property"
source_id: 33331
source_url: https://wiki.genexus.com/commwiki/wiki?33331
genexus_version: "18"
---

# Offline Synchronization Log Level property

Sets the desired log level related to the offline database synchronization.

### [Values](#Values)

|  |  |
| --- | --- |
| **Debug** | Info level plus useful information for the developer is saved. |
| **Error** | Only errors are saved. |
| **Info** | Errors, warnings, and any other relevant information is saved. |
| **Off** | Default value. No log is saved. |
| **Warning** | Errors and warnings are saved. |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

#### [Android](#Android)

```
D/SyncHelper(3308): jsonParameters[]
D/SyncHelper(3308): Start invoke local sync proc
D/SyncHelper(3308): End invoke local sync proc
D/SyncHelper(3308): Local sync commit changes
D/SyncHelper(3308): jsonParameters ...
D/SyncHelper(3308): DATABASE SYNCHRONIZATION FINISHED
D/SyncHelper(3308): Database file: /data/user/0/com.artech.sdv15u3offline.sd15u3toff/files/db/sd15u3toff.sqlite
D/SyncHelper(3308): Hashes file: /data/user/0/com.artech.sdv15u3offline.sd15u3toff/files/db/sd15u3toff_hashes.json
D/SyncHelper(3308): callSynchronizer dismissIndicator progressDialog is null.
...
D/SyncSendHelper(3308): Call OfflineEventReplicator.
D/SyncSendHelper(3308): OfflineEventReplicator sending 1 events.
D/SyncSendHelper(3308): Call ProcedureReplicator. input: 1
D/SyncSendHelper(3308): Uploading blob : 1 of 1
...
D/SyncSendHelper(3308): Save sucessfully 2dee2965-2d91-4bfb-9af1-3104fb029b68 , 3 , 
D/SyncSendHelper(3308): End Call ProcedureReplicator.
```

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [See Also](#See+Also)

[Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228)

[HowTo: Enable logging for Native Mobile](https://wiki.genexus.com/commwiki/wiki?37846)


|  |
| --- |
| **Backlinks** |
| [Android - FAQ and Common Issues](https://wiki.genexus.com/commwiki/wiki?14575) | [Default Log Level property](https://wiki.genexus.com/commwiki/wiki?33333) | [Enable Logging property](https://wiki.genexus.com/commwiki/wiki?37876) |
| [HowTo: Enable logging for Native Mobile](https://wiki.genexus.com/commwiki/wiki?37846) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
