---
title: "SynchronizationEvents.RemoveEvent method"
source_id: 23967
source_url: https://wiki.genexus.com/commwiki/wiki?23967
genexus_version: "18"
---

# SynchronizationEvents.RemoveEvent method

If it is needed to remove some registry of the GXPendingEvents table for some reason, it is possible to do that using the RemoveEvent method.

### [Syntax](#Syntax)

*SynchronizationEvents.**RemoveEvent**(&EventGUID)*

**Where:**

*&EventGUID*  
    Is the Identifier of an event that is in the GXPendingEvents table.

### [Description](#Description)

As explained in the [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) document, the GXPendingEvents table will be used to store all the changes made in the device in order to send them later to the server. With this method it is possible to remove a specific event from the GXPendingEvents table.

### [Example](#Example)

```
Event 'Remove Event'
    Composite
        &EventGUID = &SynchronizationEvent.CurrentItem.EventId
        SynchronizationEvents.RemoveEvent(&EventGUID)
    EndComposite
EndEvent
```

Where *&SynchronizationEvent* is the result of the [GetEvents method](https://wiki.genexus.com/commwiki/wiki?23966) .

### [Availability](#Availability)

As from [GeneXus Tilo Beta 2](https://wiki.genexus.com/commwiki/wiki?23074,,)

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087), Offline procedures |
| **Languages** | .NET, Java, Ruby |
| **Platforms** | [Android platform](https://wiki.genexus.com/commwiki/wiki?14453), [Apple platform](https://wiki.genexus.com/commwiki/wiki?14917) |

### [See also](#See+also)

* [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341)
* [SynchronizationEvents.GetEvents method](https://wiki.genexus.com/commwiki/wiki?23966)


|  |
| --- |
| **Backlinks** |
| [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) |

---
