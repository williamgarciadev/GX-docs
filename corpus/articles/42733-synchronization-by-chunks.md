---
title: "Synchronization by Chunks"
source_id: 42733
source_url: https://wiki.genexus.com/commwiki/wiki?42733
genexus_version: "18"
---

# Synchronization by Chunks

In GeneXus-generated [Smart Devices offline applications](https://wiki.genexus.com/commwiki/wiki?20286), when the [data synchronization](https://wiki.genexus.com/commwiki/wiki?22269) is executed, all the pending synchronization events are processed and sent to the server as a whole, that means in a single request to the server.

This functionality has its justification: it allows the correct processing of primary and foreign keys, assuring the consistency between server-side and device database information. For example, if in an application we perform these actions:

* Insert a new record in Customer table with CustomerId = 1
* Insert a new record in Invoice table, with an association (FK) to CustomerId = 1
* Insert another record in Invoice table, also with an association (FK) to CustomerId = 1

When all this information is synchronized to the server, the data will keep its consistency. If the CustomerId for the Customer record in the server changes (because of the application of an auto numbering function), the Invoice table records are modified to have the correct reference to the Customer. In addition, this data change information is sent back to the client in the response of the synchronization request to be applied at the device's offline database.

Sending all the pending information at once has a drawback, nevertheless. If we have an application that performs several offline database operations (creating many synchronization events), this synchronization method may present some problems and negatively affect the application's user experience, because a very big synchronization request to the server is needed and if it fails (due to network connection problems, for instance) it has to be repeated.

The solution to this problem is to send the database events data in a group of smaller requests, instead of executing a very big one. It is important to know that we need to be sure that the consistency of the data will be maintained. For example, in the scenario we explained before for the Customer and the Invoices, we cannot split the actions in different requests, because if we sent the Customer in one request and the Invoices in another, if the CustomerId is changed in server-side processing the first request, when the second one is processed we do not have this CustomerId change information, and the Invoices will remain referencing CustomerId = 1 which is not the Customer record selected at the beginning.

### [How to perform batch synchronization in GeneXus?](#How+to+perform+batch+synchronization+in+GeneXus%3F)

The [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602) has a new method called **SetSendCheckpoint** which allows inserting "checkpoints" in the pending events table. These checkpoints will be inserted along with the other synchronization events (inserts, updates, and deletes) and then, when the Send operation is performed (automatically or manually), the pending events are processed by its date and included in the request until a checkpoint is found. At that moment, the request is sent to the server and the same process is repeated for the remaining pending events.

Following this, the data synchronization can be executed using more that one request to the server, avoiding performance or network problems associated to the request size.

Note: As a developer, you only need to perform the Send operation once. This mechanism of sending the events in chunks is handled internally by the platform's flexible client.

### [When should the checkpoints be included?](#When+should+the+checkpoints+be+included%3F)

This decision corresponds entirely to the application developer. Depending on the application's functionality and the data processed, the checkpoints should be added in the code in order to create reasonable-size synchronization requests.

Note: Please pay special attention when using checkpoints in an application that has autonumbered primary keys, because that is the case where the problem described above may arise.

### [Example](#Example)

Suppose we need to track the device location and save it in the device's database every 5 minutes. We want to put a checkpoint after 100 inserts to be sure of not generating huge synchronization requests. The code could be as follows:

```
Event 'LocationChanged'
    composite
        SaveCurrentLocation()
        do 'SetCheckpointIfNeeded'
    endcomposite
EndEvent

Sub 'SetCheckpointIfNeeded'
    composite
        &countStr = ClientStorage.Get('SyncEventsCount')
        &count = Int(&countStr) + 1
        if &count = 100
            Synchronization.SetSendCheckpoint()
            &count = 0
        endif
        &countStr = &count.ToString()
        ClientStorage.Set('SyncEventsCount', &countStr)
    endcomposite
EndSub
```

### [Availability](#Availability)

This synchronization method is available as of [GeneXus 16 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,)

### [See also](#See+also)

* [The Data Synchronization Problem](https://wiki.genexus.com/commwiki/wiki?22240)
* [GeneXus applications data synchronization](https://wiki.genexus.com/commwiki/wiki?22269)
* [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602)


|  |
| --- |
| **Backlinks** |
| [Advanced Concepts of Offline Applications architecture](https://wiki.genexus.com/commwiki/wiki?25536) | [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |
| [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602) | [Synchronization.SetSendCheckpoint method](https://wiki.genexus.com/commwiki/wiki?42735) |

---
