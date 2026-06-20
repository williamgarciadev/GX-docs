---
title: "Event Messaging API: CloudEvent SDT"
source_id: 55339
source_url: https://wiki.genexus.com/commwiki/wiki?55339
genexus_version: "18"
---

# Event Messaging API: CloudEvent SDT

The *CloudEvent*[Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) is defined below the *GeneXusEventEventDrivenAPI*module and represents the event to be sent by an Event Router using the [Event Messaging API](https://wiki.genexus.com/commwiki/wiki?55334).  
It follows the [Cloud Events specification](https://cloudevents.io/).

`[imagen omitida: wiki id 55399]`

For more information, see [CloudEvents specification](https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md).

### [Considerations](#Considerations)

* The combination of "id" and "source" must be unique for each distinct event.
* If not explicitly set, the "id" defaults to a GUID.
* The data can be sent as binary using base64 (see [Handling of "data"](https://github.com/cloudevents/spec/blob/v1.0/json-format.md#31-handling-of-data)). To be sent as binary, the [SendEvent](https://wiki.genexus.com/commwiki/wiki?55337) method must receive the binaryData parameter with a TRUE value.

#### [Fields automatically assigned](#Fields+automatically+assigned)

* The time of the event will default to the time that the event is constructed.
* The SpecVersion will default to the spec version of the cloud event. It cannot be assigned.

### [Availability](#Availability)

This external object is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Azure Event Grid: Infrastructure setup](https://wiki.genexus.com/commwiki/wiki?55346) | [EventMessaging API: Send Events using CloudEvents Schema](https://wiki.genexus.com/commwiki/wiki?55400) |

---
