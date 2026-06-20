---
title: "Azure Event Grid triggered functions"
source_id: 56742
source_url: https://wiki.genexus.com/commwiki/wiki?56742
genexus_version: "18"
---

# Azure Event Grid triggered functions

An [Azure Function](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview?pivots=programming-language-csharp) can be used as an [event handler](https://learn.microsoft.com/en-us/azure/event-grid/handler-functions) for [Event Grid](https://learn.microsoft.com/en-us/azure/event-grid/overview) events.

This document explains how to deploy Azure functions triggered by Event Grid events in GeneXus.

**Summary**

* [Deployment steps](#Deployment+steps)

+ [Deployment Settings](#Deployment+Settings)

* [Infrastructure setup](#Infrastructure+setup)
* [Requirements](#Requirements)
* [Function Inputs](#Function+Inputs)
* [Scope](#Scope)
* [Availability](#Availability)
* [See Also](#See+Also)

## [Deployment steps](#Deployment+steps)

First, read [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).  
To deploy the function, use the deployment tool. See [HowTo: Deploy as Azure Functions](https://wiki.genexus.com/commwiki/wiki?49351).

When using the deployment tool, the Azure functions use the [Event Grid trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid-trigger).

### [Deployment Settings](#Deployment+Settings)

The [Trigger type property](https://wiki.genexus.com/commwiki/wiki?51466) in the deployment unit should be "**Event Grid**" for this kind of function.

Then select the Event Schema used when the Event Grid was defined.

You can select one of these two values:

* [Cloud Event Schema](https://learn.microsoft.com/en-us/azure/event-grid/cloudevents-schema)
* [Event Grid Schema](https://learn.microsoft.com/en-us/azure/event-grid/event-schema)

The schema selection depends on the schema used by your Event Grid definition.

`[imagen omitida: wiki id 56745]`

## [Infrastructure setup](#Infrastructure+setup)

First, [Register the Event Grid resource provider](https://learn.microsoft.com/en-us/azure/event-grid/custom-event-quickstart-portal#register-the-event-grid-resource-provider).

Next, define an [Event Grid Custom Topic](https://learn.microsoft.com/en-us/azure/event-grid/custom-topics) or [System Topic](https://learn.microsoft.com/en-us/azure/event-grid/system-topics).

Afterwards, you have to configure a subscription for your Azure Function. Specify Azure Function as the endpoint type. Next, specify the function app and the function that will handle events.  
Check the Azure documentation [here](https://learn.microsoft.com/en-us/azure/event-grid/custom-event-quickstart-portal#subscribe-to-custom-topic).

`[imagen omitida: wiki id 56744]`

## [Requirements](#Requirements)

The Function App must be defined for NET 8.

`[imagen omitida: wiki id 56743]`

## [Function Inputs](#Function+Inputs)

The GeneXus procedure will have a signature as explained in [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729).

In this case, the EventMessage SDT will contain the following in each field:

* EventMessageId: Cloud Event Id or Event Grid Schema Id (depending on the schema used).
* EventMessageSourceType: Type of event related to the originating occurrence.
* EventMessageVersion: "" in the case of Cloud Event. Schema version of the data object in the case of Event Grid Schema.
* EventMessageDate: Time in UTC that the event was generated.
* EventMessageData: A Json string containing the event payload.
* EventMessageProperties: Properties of the event, including:
  + Subject and Topic: In the case of Event Grid Schema.
  + Subject and Source: In the case of Cloud Event Schema.

## [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

## [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) for .NET Generator.  
For Java, it's available since [GeneXus 18 Upgrade 12](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59446,,).

## [See Also](#See+Also)

[Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430)  
[Monitor Event Grid message delivery](https://learn.microsoft.com/en-us/azure/event-grid/monitor-event-delivery)  
[Enable diagnostic logs for Event Grid](https://learn.microsoft.com/en-us/azure/event-grid/enable-diagnostic-logs-topic)  
[Event Grid message delivery and retry](https://learn.microsoft.com/en-us/azure/event-grid/delivery-and-retry)


|  |
| --- |
| **Backlinks** |
| [Table of contents:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Azure Functions](https://wiki.genexus.com/commwiki/wiki?47430) | [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) |

---
