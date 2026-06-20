---
title: "EventMessaging API: Azure Event Grid"
source_id: 55354
source_url: https://wiki.genexus.com/commwiki/wiki?55354
genexus_version: "18"
---

# EventMessaging API: Azure Event Grid

[Azure Event Grid](https://learn.microsoft.com/en-us/azure/event-grid/overview) is a Publish/Subscribe message distribution serverless service that uses the MQTT and HTTP protocols.  
  
In addition to System events – where built-in Azure service events are the publishers (for example, by configuring Event Grid to receive an event when a new blob has been created) – you can have your own application events.  
In that case, Event Grid is used to route, filter, and reliably deliver custom events from your app.

This is the purpose of the [Event Messaging API](https://wiki.genexus.com/commwiki/wiki?55334) for Azure Event Grid.  
  
When configuring Event Grid for push delivery, Event Grid can send data to [destinations](https://learn.microsoft.com/en-us/azure/event-grid/overview#event-handlers) that include your own application webhooks and Azure services.

The covered scenario is similar to the image below:

`[imagen omitida: wiki id 55353]`

Events delivered to consumers by Event Grid are [delivered as JSON](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/eventgrid/Azure.Messaging.EventGrid/README.md#event-delivery).

### [See Also](#See+Also)

[Azure Event Grid concept](https://learn.microsoft.com/en-gb/azure/event-grid/concepts)s.


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Event Messaging API](https://wiki.genexus.com/commwiki/wiki?55334) | [EventMessaging API: Send Events using CloudEvents Schema](https://wiki.genexus.com/commwiki/wiki?55400) |
| [EventMessaging API: Send Events using EventGrid Schema](https://wiki.genexus.com/commwiki/wiki?55401) |

---
