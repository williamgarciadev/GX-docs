---
title: "Message Broker API"
source_id: 51782
source_url: https://wiki.genexus.com/commwiki/wiki?51782
genexus_version: "18"
---

# Message Broker API

Modern applications rely on asynchronous message exchange to establish boundaries between components, which ensures low coupling.

[Message brokers](https://en.wikipedia.org/wiki/Message_broker) facilitate the implementation of this feature of modern applications, since:

* They can validate, store, route, and deliver messages. This enables asynchronous communication between applications, systems, and services.
* They act as an intermediary between applications, so that senders can send messages without knowing where the receivers are and whether they are active or not. In other words, Message Brokers effectively implement decoupling between components.

For now, this functionality is implemented for [Azure Service Bus](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-queues-topics-subscriptions)

You must import the following modules into your KB:

* GeneXusMessagingMessageBroker
* AzureServiceBus

To import each module, in the GeneXus menu you need to select: **Knowledge Manager > Manage Module References**.

### [Support](#Support)

* Azure Service Bus support is provided by the  [.NET](https://wiki.genexus.com/commwiki/wiki?38604) generator.

### [Availability](#Availability)

This feature is available since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Azure Service Bus: BrokerReceiverOptions SDT](https://wiki.genexus.com/commwiki/wiki?51943) | [Azure Service Bus: ConsumeMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51945) |
| [Azure Service Bus: ReceiveMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51952) | [Azure Service Bus: ScheduleMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51950) | [AzureServiceBus.MessageBrokerProvider external object](https://wiki.genexus.com/commwiki/wiki?51784) | [AzureServiceBus.MessageBrokerProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55677) |
| [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081) | [HowTo: Connect to a Message Broker](https://wiki.genexus.com/commwiki/wiki?51972) | [HowTo: Receive messages from a Message Broker](https://wiki.genexus.com/commwiki/wiki?51977) | [HowTo: Receive messages from a session-enabled Message Broker](https://wiki.genexus.com/commwiki/wiki?51984) |
| [HowTo: Send messages to a Message Broker](https://wiki.genexus.com/commwiki/wiki?51973) | [HowTo: Settle messages from a Message Broker](https://wiki.genexus.com/commwiki/wiki?51978) | [Message attributes for Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51791) | [Message Broker API: Message SDT](https://wiki.genexus.com/commwiki/wiki?51789) |
| [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786) |

---
