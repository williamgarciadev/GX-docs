---
title: "Synchronization.Send method"
source_id: 23604
source_url: https://wiki.genexus.com/commwiki/wiki?23604
genexus_version: "18"
---

# Synchronization.Send method

Sends pending modifications from the local database to the server and synchronizes changes made via a Business Component.

### [Syntax](#Syntax)

```
&SynchResult = Synchronization.Send()
```

**Where:**

*SynchResult*  
Is a numeric variable. Stores the result of the send method.

### [Description](#Description)

This method sends to the server the pending modifications made in the local database. All these modifications are stored as events in the GxPendingEvents table in the device's local database.

**Note**: Only changes made via a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) are sent to the server.

Once the Send process ends, all pending events that have been successfully applied on the server are removed from the GxPendingEvents table. On the other hand, all events that could not be applied on the server remain in the GxPendingEvents table, and their status is changed to "RejectedServer".  
The [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) has methods to query the pending events as well as any synchronization error.

### [Type returned](#Type+returned)

Returns one of the following values:

| Send message code | Send message | Send message causes |
| --- | --- | --- |
| 0 | Send OK. | Data has been successfully sent. |
| 1 | Error opening Transactions. | An error has occurred while opening the Transactions. |
| 2 | Unknown error. | Unknown error. |
| 3 | Replicator not found. | The application could not find the replicator services. Try checking if the [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146) is correct or test if the replicator services are correctly published. |
| 8 | Send is already running | The replicator will not be executed because another send is already running. |

**Note:** If you are invoking the Send method directly, avoid using the [Send Changes property](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?23392,,) = When connected simultaneously.

### [Sample](#Sample)

Here is an example of calling the Send method when pressing a button:

```
Event "MyAction"
    &SynchResult = Synchronization.Send()
EndEvent
```

### [Scope](#Scope)

**Object:**  [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087)  
**Generator:**  [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Availability](#Availability)

As from [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?20247,,).

### [See Also](#See+Also)

[Synchronization.Receive method](https://wiki.genexus.com/commwiki/wiki?23603)  
[Synchronization.ServerStatus method](https://wiki.genexus.com/commwiki/wiki?25839)  
[Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602)  
[SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341)


|  |
| --- |
| **Backlinks** |
| [Advanced Concepts of Offline Applications architecture](https://wiki.genexus.com/commwiki/wiki?25536) | [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) | [Error handling in Synchronization.Send() operations](https://wiki.genexus.com/commwiki/wiki?25454) |
| [HowTo: Use the Synchronization API](https://wiki.genexus.com/commwiki/wiki?23605) | [Table of contents:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [Offline Native Mobile applications using GAM](https://wiki.genexus.com/commwiki/wiki?23400) | [OfflineEventReplicator procedure](https://wiki.genexus.com/commwiki/wiki?26218) |
| [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602) | [Synchronization.Receive method](https://wiki.genexus.com/commwiki/wiki?23603) | [Synchronization.ServerStatus method](https://wiki.genexus.com/commwiki/wiki?25839) |

---
