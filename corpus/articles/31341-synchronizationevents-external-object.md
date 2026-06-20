---
title: "SynchronizationEvents external object"
source_id: 31341
source_url: https://wiki.genexus.com/commwiki/wiki?31341
genexus_version: "18"
---

# SynchronizationEvents external object

Every time an offline application generated with GeneXus is installed in the device, an auxiliary table called "GXPendingEvents" is created automatically in the local database. The GXPendingEvents table will store all Business Component modifications made offline (Inserts, Deletes, Updates) as events to replicate the same changes later to the server. Each event has an attribute that represents the status of the event (based on EventStatus domain).

​​​​​The SynchronizationEvents external object has methods that make possible to access and manipulate the GXPendingEvents data.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

It does not have any.

## [Methods](#Methods)

### [HasEvents method](#HasEvents+method)

Checks if there are any pending changes to submit to the server, or whether there was any error when sending the data to the server. Detailed information in [SynchronizationEvents.HasEvents method](https://wiki.genexus.com/commwiki/wiki?23944).

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | EventStatus:EventStatus |
|  |  |

### [GetEvents method](#GetEvents+method)

Accesses the stored events for processing. Detailed information in [SynchronizationEvents.GetEvents method](https://wiki.genexus.com/commwiki/wiki?23966).

|  |  |
| --- | --- |
| **Return value** | SynchronizationEventList |
| **Parameters** | EventStatus:EventStatus |
|  |  |

### [MarkEventAsPending method](#MarkEventAsPending+method)

Marks as pending an events in order to try sending it again later. Detailed information in [SynchronizationEvents.MarkEventAsPending method](https://wiki.genexus.com/commwiki/wiki?23965).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | EventGUID:[GUID](https://wiki.genexus.com/commwiki/wiki?31772) |
|  |  |

### [RemoveEvent method](#RemoveEvent+method)

Removes some registry of the GXPendingEvents table. Detailed information in [SynchronizationEvents.RemoveEvent method](https://wiki.genexus.com/commwiki/wiki?23967).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | EventGUID:[GUID](https://wiki.genexus.com/commwiki/wiki?31772) |
|  |  |

## [Events](#Events)

It does not have any.

## [Domains](#Domains)

### [EventStatus domain](#EventStatus+domain)

Numeric based enumerated domain with the possible event status values.

|  |  |  |
| --- | --- | --- |
| **Pending** | 1 | Events with this status are ready to be sent by the device to the server. Also, these events are created every time a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) transaction is executed. |
| **ProcessingServer** | 2 | This is a temporary status of an event while it is being processed on the server side. |
| **ConfirmedServer** | 3 | This status means that the event was successfully replicated in the server side. Because there is no need to store all confirmed events, they are removed from the GXPendingEvents table instantly. |
| **RejectedServer** | 4 | Events with this status could not be replicated on the server side because some error happened. From the device, it is possible to access the error code and messages by using the [GetEvents method](https://wiki.genexus.com/commwiki/wiki?23966) and the "EventErrors" property of the "GxSynchroEventSD". |
| **CanceledUser** | 5 | Means that the event was canceled by the user. |
| **RejectedFK** | 6 | When at least two insertion events are sent and one of them has a foreign key to some of the other events if that event fails (with status RejectedServer), the event with the foreign key fails as well but with the status RejectedFK. For instance, if we have a Customer-Invoice model, and we insert a Customer with one Invoice, if for some reason the event associated with the Customer is rejected by the server when replicating, the Invoice event is made as RejectedFK |

**Note**: Statuses *"ProcessingServer"*, *"ConfirmedServer"* and *"CanceledUser"* are temporary states of an event, and, in addition, every event with some of these statuses is removed from the GXPendingEvents table; which means that only events with status *"Pending"*, *"RejectedServer"* or *"RejectedFK"* remains in the GXPendingEvents table.

### [EventAction domain](#EventAction+domain)

Possible event actions.

|  |  |
| --- | --- |
| **INS** | Insertion |
| **UPD** | Modification (or update) |
| **DLT** | Deletion |
|  |  |

### [EventData domain](#EventData+domain)

Event data information. It is based on [LongVarChar data type](https://wiki.genexus.com/commwiki/wiki?7371).

### [EventError domain](#EventError+domain)

Event error information. It is based on [LongVarChar data type](https://wiki.genexus.com/commwiki/wiki?7371).

## [Structured Data Types](#Structured+Data+Types)

### [SyncrhonizationEventList](#SyncrhonizationEventList)

A collection of synchronization event information.

* EventId:[GUID](https://wiki.genexus.com/commwiki/wiki?31772)  
  The event identifier.
* EventTimestamp:[DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
  The event timestamp.
* EventBC:[VarChar(128)](https://wiki.genexus.com/commwiki/wiki?6778)  
  The event business component.
* EventAction:EventAction  
  The event action.
* EventData:EventData  
  The event associated data.
* EventStatus:EventStatus  
  The event status.
* EventErrors:EventErrors  
  The event associated errors.

## [Notes](#Notes)

* Events with status "RejectedFK" are only supported by [Apple platform](https://wiki.genexus.com/commwiki/wiki?14917) offline applications as of [GeneXus X Evolution 3 Upgrade 1](https://wiki.genexus.com/commwiki/wiki?25965,,).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | Smart Devices (iOS, Android) |

## [Availability](#Availability)

This external object is available as of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

## [See also](#See+also)

* [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602)
* [HowTo: Use the Synchronization API](https://wiki.genexus.com/commwiki/wiki?23605)
* [Error handling in Synchronization.Send() operations](https://wiki.genexus.com/commwiki/wiki?25454)


|  |
| --- |
| **Backlinks** |
| [Advanced Concepts of Offline Applications architecture](https://wiki.genexus.com/commwiki/wiki?25536) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) |
| [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) | [Synchronization.Send method](https://wiki.genexus.com/commwiki/wiki?23604) |
| [SynchronizationEvents.GetEvents method](https://wiki.genexus.com/commwiki/wiki?23966) | [SynchronizationEvents.HasEvents method](https://wiki.genexus.com/commwiki/wiki?23944) | [SynchronizationEvents.MarkEventAsPending method](https://wiki.genexus.com/commwiki/wiki?23965) | [SynchronizationEvents.RemoveEvent method](https://wiki.genexus.com/commwiki/wiki?23967) |

---
