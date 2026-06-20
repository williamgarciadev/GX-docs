---
title: "Event Messaging API: EventGridSchema SDT"
source_id: 55344
source_url: https://wiki.genexus.com/commwiki/wiki?55344
genexus_version: "18"
---

# Event Messaging API: EventGridSchema SDT

The *EventGridSchema*[Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) is defined below the *AzureEventGrid*module and allows you to publish Events to Azure Event Grid using the [Event Grid Schema](https://learn.microsoft.com/en-us/azure/event-grid/event-schema).  
This is an alternative format to using the [CloudEvents schema](https://learn.microsoft.com/en-us/azure/event-grid/cloud-event-schema).

`[imagen omitida: wiki id 55398]`

### [Considerations](#Considerations)

* The subject, data, eventType, and dataVersion cannot be empty. Otherwise, you'll get an error at runtime.
* If not explicitly set, the Id defaults to a GUID.
* The topic must be set when publishing the event to a [domain](https://learn.microsoft.com/en-us/azure/event-grid/event-domains), and must not be set when publishing the event to a [topic](https://learn.microsoft.com/en-us/azure/event-grid/custom-topics). Otherwise, you'll get an error at runtime.

#### [Fields automatically assigned](#Fields+automatically+assigned)

* The time of the event will default to the time that the event is constructed.
* metadataversion: Event Grid defines the schema of the top-level properties. Event Grid provides this value.

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Azure Event Grid: Infrastructure setup](https://wiki.genexus.com/commwiki/wiki?55346) | [EventMessaging API: Send Events using EventGrid Schema](https://wiki.genexus.com/commwiki/wiki?55401) |

---
