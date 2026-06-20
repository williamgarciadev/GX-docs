---
title: "SynchronizationEvents.MarkEventAsPending method"
source_id: 23965
source_url: https://wiki.genexus.com/commwiki/wiki?23965
genexus_version: "18"
---

# SynchronizationEvents.MarkEventAsPending method

Sometimes may occur errors when sending events to the server and it could be useful to mark as pending those events in order to try sending them again later.

### [Syntax](#Syntax)

*SynchronizationEvents.**MarkEventAsPending**(&EventGUID)*

**Where:**

*&EventGUID*  
    Is the GUID of an event that is in the GXPendingEvents table.

### [Description](#Description)

As explained in the [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) document, the GXPendingEvents table will be used to store all the changes made in the device in order to send them later to the server. With this method it is possible to set the events status to Pending.

### [Example](#Example)

```
Event 'Change To Pending'
    Composite
        &EventGUID = &GxSynchroEventsSDT.CurrentItem.EventId
        SynchronizationEvents.MarkEventAsPending(&EventGUID)
    EndComposite
EndEvent
```

Where *&GxSynchroEventsSDT* is the result of the [GetEvents method](https://wiki.genexus.com/commwiki/wiki?23966) .

### [Availability](#Availability)

As from [GeneXus Tilo Beta 2](https://wiki.genexus.com/commwiki/wiki?23074,,)

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087), Offline procedures |
| **Languages** | .NET, Java, Ruby |
| **Platforms** | [Android platform](https://wiki.genexus.com/commwiki/wiki?14453), [Apple platform](https://wiki.genexus.com/commwiki/wiki?14917) |

### [See also](#See+also)

* [SynchronizationEventsAPI external object](https://wiki.genexus.com/commwiki/wiki?23606,,)
* [SynchronizationEvents.GetEvents method](https://wiki.genexus.com/commwiki/wiki?23966)


|  |
| --- |
| **Backlinks** |
| [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) |

---
