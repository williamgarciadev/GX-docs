---
title: "Azure Service Bus: BrokerReceiverOptions SDT"
source_id: 51943
source_url: https://wiki.genexus.com/commwiki/wiki?51943
genexus_version: "18"
---

# Azure Service Bus: BrokerReceiverOptions SDT

When the [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782) is used, the *BrokerReceiverOptions*[Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) is defined under the *AzureServiceBus* module and represents the options that may be passed to the Connect method to configure the behavior of the receiver associated with this connection to the Service Bus.

`[imagen omitida: wiki id 52956]`

The BrokerReceiverOptions SDT is used

* at the [Connect methods](https://wiki.genexus.com/commwiki/wiki?51784) of the [MessageBrokerProvider EO](https://wiki.genexus.com/commwiki/wiki?51784), only for non-session enabled queues or topics.
* at the  [ReceiveMessage](https://wiki.genexus.com/commwiki/wiki?51786) and [ReceiveMessages](https://wiki.genexus.com/commwiki/wiki?51786) methods, for both, non-session, and session enabled queues or topics.  
  Passing the Session Id is mandatory for session-enabled queues and topics, for each Receive Operation.

|  |  |  |
| --- | --- | --- |
|  |  | **Notes** |
| **ReceiveMode** | 0: Specifies the PeekLock receive mode (default value). 1: Specifies the ReceiveAndDelete receive mode. | Click [here](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-queues-topics-subscriptions#receive-modes) for more information. |
| **PrefetchCount** | Sets the number of messages that will be eagerly requested from Queues or Subscriptions and queued locally without regard to whether the receiver is actively receiving, intended to help maximize throughput by allowing the receiver to receive from a local cache rather than waiting on a service request. | It corresponds to [this](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.servicebus.servicebusreceiver.prefetchcount?view=azure-dotnet) property. |
| **Identifier** | To set the ID to identify the client for the receive operations. This can be used to correlate logs and exceptions. If null or empty, a random unique value will be used | It corresponds to [this](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.servicebus.servicebusreceiver.identifier?view=azure-dotnet) property. |
| **SessionId** | The Session ID for receive operations, only for [session-enabled](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions) queues or topics. | The Session ID has to be established at the [ReceiveMessage](https://wiki.genexus.com/commwiki/wiki?51786) and [ReceiveMessages](https://wiki.genexus.com/commwiki/wiki?51786) method, using the [ReceiveMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51952). |

### [Availability](#Availability)

This feature is available since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Azure Service Bus: ReceiveMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51952) | [AzureServiceBus.MessageBrokerProvider external object](https://wiki.genexus.com/commwiki/wiki?51784) |
| [AzureServiceBus.MessageBrokerProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55677) | [HowTo: Complete a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51980) | [HowTo: Connect to a Message Broker](https://wiki.genexus.com/commwiki/wiki?51972) | [HowTo: Defer a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51981) |
| [HowTo: Receive messages from a Message Broker](https://wiki.genexus.com/commwiki/wiki?51977) | [HowTo: Receive messages from a session-enabled Message Broker](https://wiki.genexus.com/commwiki/wiki?51984) | [HowTo: Send messages to a Message Broker](https://wiki.genexus.com/commwiki/wiki?51973) |

---
