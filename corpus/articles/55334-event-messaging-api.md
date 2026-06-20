---
title: "Event Messaging API"
source_id: 55334
source_url: https://wiki.genexus.com/commwiki/wiki?55334
genexus_version: "18"
---

# Event Messaging API

Event Messaging API is an approach to building Event driven applications.

For now, this functionality is implemented for [Azure Event Grid](https://wiki.genexus.com/commwiki/wiki?55354).

## [How to use the API](#How+to+use+the+API)

You must import the following modules into your KB:

* GeneXusEventMessaging
  + GeneXusEventDrivenAPI
* AzureEventGrid

To import each module, in the GeneXus menu you need to select: Knowledge Manager > Manage Module References.

### [Support](#Support)

Azure Event Grid API support is provided by the [.NET Generator](https://wiki.genexus.com/commwiki/wiki?38604)

### [Terminology](#Terminology)

* What is an Event? An event is the smallest amount of information that fully describes something that happened in a system.
* [CloudEvents 1.0](https://github.com/cloudevents/spec) is a [CNCF](https://www.cncf.io/)’s open standard specification using the HTTP protocol binding with the JSON format.

### [Availabilty](#Availabilty)

Since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239)


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Azure Event Grid: Infrastructure setup](https://wiki.genexus.com/commwiki/wiki?55346) | [AzureEventGrid.EventGridRouterProvider external object](https://wiki.genexus.com/commwiki/wiki?55341) |
| [Event Messaging API: CloudEvent SDT](https://wiki.genexus.com/commwiki/wiki?55339) | [EventMessaging API: Azure Event Grid](https://wiki.genexus.com/commwiki/wiki?55354) | [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239) |
| [Microservices systems](https://wiki.genexus.com/commwiki/wiki?55526) |

---
