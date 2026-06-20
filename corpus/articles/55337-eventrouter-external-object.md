---
title: "EventRouter external object"
source_id: 55337
source_url: https://wiki.genexus.com/commwiki/wiki?55337
genexus_version: "18"
---

# EventRouter external object

The *EventRouter*External Object is below the *GeneXusEventMessaging*module and allows you to publish events to an Event Router.

`[imagen omitida: wiki id 55443]`

## [Methods](#Methods+)

### [SendEvent](#SendEvent)

Sends an event using the [CloudEvents](https://github.com/cloudevents/spec/blob/v1.0/spec.md) specification.

**Return value:**   Boolean  
**Parameters:**     Event:CloudEvent, binaryData:Boolean, ErrorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335)

The binaryData parameter indicates whether the data item of the Event will be [sent as binary](https://github.com/cloudevents/spec/blob/v1.0/json-format.md#json-event-format-for-cloudevents---version-10).

### [SendEvents](#SendEvents)

Sends events using the [CloudEvents](https://github.com/cloudevents/spec/blob/v1.0/spec.md) specification.

**Return value:**   Boolean  
**Parameters:**     Event:CloudEvent (Collection), binaryData:Boolean, ErrorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335)

The binaryData parameter indicates whether the data item of the Events will be [sent as binary](https://github.com/cloudevents/spec/blob/v1.0/json-format.md#json-event-format-for-cloudevents---version-10).

### [SendCustomEvents](#SendCustomEvents)

Sends events using a specific proprietary format.   
To send the Event using any other format valid for any specific provider, use this method.

**Return value:**   Boolean  
**Parameters:**     Event:varchar, binaryData: Boolean, ErrorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), success: Boolean

The event is passed to the method as a JSON.  
The JSON string passed to the method must have a valid format according to the Event Schema supported by the event router provider.  
For example, Azure Event Grid supports Azure [Event Grid Schema](https://learn.microsoft.com/en-us/azure/event-grid/event-schema).  
Therefore, the JSON can be obtained using the AzureEventGrid.EventGridSchema SDT.

### [Availability](#Availability)

This external object is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Azure Event Grid: Infrastructure setup](https://wiki.genexus.com/commwiki/wiki?55346) | [AzureEventGrid.EventGridRouterProvider external object](https://wiki.genexus.com/commwiki/wiki?55341) |
| [Event Messaging API: CloudEvent SDT](https://wiki.genexus.com/commwiki/wiki?55339) | [EventMessaging API: Send Events using CloudEvents Schema](https://wiki.genexus.com/commwiki/wiki?55400) | [EventMessaging API: Send Events using EventGrid Schema](https://wiki.genexus.com/commwiki/wiki?55401) |

---
