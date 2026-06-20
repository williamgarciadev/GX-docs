---
title: "SynchronizationEvents.GetEvents method"
source_id: 23966
source_url: https://wiki.genexus.com/commwiki/wiki?23966
genexus_version: "18"
---

# SynchronizationEvents.GetEvents method

The GetEvents method gives the developer the ability to access the stored events for processing.  
This is useful for example when there are events that returned with errors from the server, to get the error messages.

### [Syntax](#Syntax)

*&**SynchronizationEventList* *= SynchronizationEvents.**GetEvents**(&EventStatus)*

**Type returned**  
SynchronizationEventList

**Where:**  
*&EventStatus*  
    Is a variable based on the EventStatus domain and it represents the status of the events to filter. Its possible values are:

|  |  |
| --- | --- |
| Values | **Name** |
| 1 | Pending |
| 2 | ProcessingServer |
| 3 | ConfirmedServer |
| 4 | RejectedServer |
| 5 | CanceledUser |

**Note**: If *&EventStatus* equals 0, then the GetEvents method does not filter by the status of the events.

### [Values](#Values)

Returns a SynchronizationEvent value that represents the collection of events with status &EventStatus stored in the GXPendingEvents table.

### [Description](#Description)

As explained in the [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) document, the GXPendingEvents table will be used to store all the changes made in the device in order to send them later to the server. With this method it is possible to access those registries and optionaly filter by the EventStatus of those events.

### [Examples](#Examples)

```
Event refresh
   &SynchronizationEventList = SynchronizationEvents.GetEvents(EventStatus.Pending)
EndEvent
```

Where &SynchronizationEventList is based on SynchronizationEventList SDT and this variable is going to be displayed in a panel's layout as a SD Grid.

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


|  |
| --- |
| **Backlinks** |
| [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) | [SynchronizationEvents.MarkEventAsPending method](https://wiki.genexus.com/commwiki/wiki?23965) | [SynchronizationEvents.RemoveEvent method](https://wiki.genexus.com/commwiki/wiki?23967) |

---
