---
title: "Error handling in Synchronization.Send() operations"
source_id: 25454
source_url: https://wiki.genexus.com/commwiki/wiki?25454
genexus_version: "18"
---

# Error handling in Synchronization.Send() operations

In the [Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?20286), when there is a [Synchronization.Send()](https://wiki.genexus.com/commwiki/wiki?23604) operation, the device sends to the server a list of [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) (BC) operations which were performed localy. The server then applies these operations to the central database.

There are some cases where a BC operation can result in an error for several reasons: business rules which succeded in the device but failed on the server database, referential integrity, etc.

### [How changes are applied to the server](#How+changes+are+applied+to+the+server)

There is a procedure, called "[OfflineEventReplicator](https://wiki.genexus.com/commwiki/wiki?26218)", which handles the list of operations sent from the device.

The signature of this procedure is as follows:

```
parm(in:&GxPendingEvents, in:&GxSyncroInfo, out:&EventResults);
```

Where

* &GxPendingEvents are the events sent by the device,
* &GxSyncroInfo contains additional information required by the synchronization process, and
* &EventResults is a collection of the results of each pending event processed by the server.

### [How errors are handled](#How+errors+are+handled)

The GeneXus developer might need to have control over the behavior of the application whenever there is an error in a Send operation.

There are two procedures, called automatically from the [OfflineEventReplicator procedure](https://wiki.genexus.com/commwiki/wiki?26218), which notify the application of any error and allows the programmer to take any required action.

These procedures are located in the GeneXus\SD\Synchronization folder under the [Root module](https://wiki.genexus.com/commwiki/wiki?22439) of the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836). Note that they are not inside the [GeneXus Module](https://wiki.genexus.com/commwiki/wiki?31268), because they may be modified locally in the KB.

#### [GxOnPendingEventFailed](#GxOnPendingEventFailed)

This procedure is called on every BC operation that finishes with an error.

The signature of this procedure is:

```
parm(in:&PendingEvent, in:&BCName, in:&BCJson, in:&EventResult, in:&GxSyncroInfo, out:&Continue);
```

where

* &PendingEvent is based on GxSynchroEventSDT.GxSynchroEventSDTItem and has the information about the failed event,
* &BCName is a VarChar(128) and contains the name of the business component,
* &BCJSon is based on EventData and contains the BC's JSON representation associated with the failed event,
* &EventResult is based on GxSynchroEventResultSDT.GxSynchroEventResultSDTItem and has the information about the nature of the failed event (fields: EventStatus and EventErrors),
* &GxSynchroInfo is passed along from the [OfflineEventReplicator procedure](https://wiki.genexus.com/commwiki/wiki?26218), and
* &Continue is a Boolean which indicates if the [OfflineEventReplicator procedure](https://wiki.genexus.com/commwiki/wiki?26218) should continue processing the next items (return True) or if it must abort the synchronization (return False).

By default, this procedure is empty (except for the assignment &Continue = True) so that the GeneXus developer can indicate the action to take under each circumstance.

#### [GxBeforeEventReplicator](#GxBeforeEventReplicator)

This procedure is called by the OfflineEventReplicator before processing any of the BC operations.

Its signature is the same than the one of the OfflineEventReplicator.

You can change this procedure by adding log information or even change, with caution, the list of events to be processed.

**Note**: This procedure is available since [GeneXus 16 upgrade 1](https://wiki.genexus.com/commwiki/wiki?40782,,).

**Warning**: For already existing KBs, migrated from previous GeneXus versions, this procedure must be imported from <genexus\_installation\_directory>\Packages\Patterns\WorkWithDevices\Resources\SDApi.xml .

#### [GxAfterEventReplicator](#GxAfterEventReplicator)

This procedure is called after processing all the BC operations, whether all operations completed successfully or there were any errors. It is called even if a call to the GxOnPendingEventFailed procedure finished with &Continue = False.

The signature of this procedure is:

```
parm(in:&EventResults, in:&GxSyncroInfo);
```

where

* &EventResults is based on GxSynchroEventResultSDT, which is, the collection returned to the device and has all the information about the synchronization result, and
* &GxSynchroInfo is passed along from the [OfflineEventReplicator procedure](https://wiki.genexus.com/commwiki/wiki?26218).


|  |
| --- |
| **Backlinks** |
| [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [OfflineEventReplicator procedure](https://wiki.genexus.com/commwiki/wiki?26218) | [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) |

---
