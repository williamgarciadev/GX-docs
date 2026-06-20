---
title: "Azure Event Grid: Infrastructure setup"
source_id: 55346
source_url: https://wiki.genexus.com/commwiki/wiki?55346
genexus_version: "18"
---

# Azure Event Grid: Infrastructure setup

Below is a summary of what you need to set up in the Azure cloud to start publishing events to [Azure Event Grid](https://learn.microsoft.com/en-us/azure/event-grid/overview) using the [Event Messaging API](https://wiki.genexus.com/commwiki/wiki?55334).

1. [Register the Event Grid resource provider](https://learn.microsoft.com/en-gb/azure/event-grid/custom-event-quickstart-portal#register-the-event-grid-resource-provider).  
2. [Create a Custom Topic](https://learn.microsoft.com/en-gb/azure/event-grid/create-custom-topic#create-a-custom-topic-or-domain).  
    Authentication: For now, the supported authentication is [local](https://learn.microsoft.com/en-gb/azure/event-grid/create-custom-topic#security-page).

`[imagen omitida: wiki id 55347]`

3. When you define the Event Grid resource, you are asked to select an [Event Schema](https://learn.microsoft.com/en-gb/azure/event-grid/create-custom-topic#advanced-page).  
All of the available schemas (CloudEvent, EventGridSchema, and Custom) are supported by the Event Messaging API.

## [CloudEvent Schema](#CloudEvent+Schema)

Use the [SendEvent](https://wiki.genexus.com/commwiki/wiki?55337) method by passing a [CloudEvent SDT](https://wiki.genexus.com/commwiki/wiki?55339) for the Event parameter.

## [EventGridSchema](#EventGridSchema)

Use the [SendCustomEvents](https://wiki.genexus.com/commwiki/wiki?55337) method by passing a JSON string of an [EventGridSchema SDT](https://wiki.genexus.com/commwiki/wiki?55344).

## [Custom Input Schema](#Custom+Input+Schema)

Use the [SendCustomEvents](https://wiki.genexus.com/commwiki/wiki?55337) method by passing a JSON string of an [EventGridSchema SDT](https://wiki.genexus.com/commwiki/wiki?55344).

Define the following as the mapping fields in the Topic creation (Advanced tab):

`[imagen omitida: wiki id 55348]`

4. Define a subscription for the Event Grid by following the Azure documentation. See [Event Handlers](https://learn.microsoft.com/en-us/azure/event-grid/event-handlers).

## [See Also](#See+Also)

[Delivery and retry](https://learn.microsoft.com/en-us/azure/event-grid/delivery-and-retry)


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) |

---
