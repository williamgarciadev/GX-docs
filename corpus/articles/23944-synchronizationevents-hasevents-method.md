---
title: "SynchronizationEvents.HasEvents method"
source_id: 23944
source_url: https://wiki.genexus.com/commwiki/wiki?23944
genexus_version: "18"
---

# SynchronizationEvents.HasEvents method

Sometimes the application needs to check if there are any pending changes to submit to the server, or whether there was any error when sending the data to the server.

The HasEvent method performs this checks.

### [Syntax](#Syntax)

*&HasEvents = SynchronizationEvents.**HasEvents**(&EventStatus)*

**Type returned**  
Boolean

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

**Note**: If *&EventStatus* equals 0, then the HasEvents method does not filter by the status of the events.

### Values

|  |  |
| --- | --- |
| **False** | Returns false if there are no events with status &EventStatus in the GXPendingEvents table. |
| **True** | Returns true if there are any event with status &EventStatus in the GXPendingEvents table. |

### [Description](#Description)

As explained in the [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) document, the GXPendingEvents table will be used to store all the changes made in the device in order to send them later to the server. With this method it is possible to check whether there are events in the GXPendingEvents table.

### [Examples](#Examples)

```
Event refresh
    Composite
        &HasEvents = SynchronizationEvents.HasEvents(1)
        If &HasEvents
           Msg("You have events to send!")
        EndIf
    EndComposite
EndEvent
```

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
| [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) |

---
