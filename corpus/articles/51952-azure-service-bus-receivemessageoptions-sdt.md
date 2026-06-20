---
title: "Azure Service Bus: ReceiveMessageOptions SDT"
source_id: 51952
source_url: https://wiki.genexus.com/commwiki/wiki?51952
genexus_version: "18"
---

# Azure Service Bus: ReceiveMessageOptions SDT

When the [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782) is used, the *ReceiveMessageOptions*[Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) is defined under the *AzureServiceBus* module and represents the options that may be passed to the [ReceiveMessage](https://wiki.genexus.com/commwiki/wiki?51786) and [ReceiveMessages](https://wiki.genexus.com/commwiki/wiki?51786) methods.

`[imagen omitida: wiki id 52955]`

|  |  |  |
| --- | --- | --- |
|  |  | **Notes** |
| **MaxMessages** | The maximum number of messages that will be received. Defaults to 10. | Used by the [ReceiveMessages](https://wiki.genexus.com/commwiki/wiki?51786) method. |
| **MaxWaitTime** | An optional TimeSpan (seconds) specifying the maximum time to wait for a message before returning null if no messages are available.  **\*\***Consider this option to avoid your app to being hang waiting for a message to arrive to the service bus when no messages are available. | Used by the [ReceiveMessage](https://wiki.genexus.com/commwiki/wiki?51786)method. If not specified, the [TryTimeout](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.servicebus.servicebusretryoptions.trytimeout?view=azure-dotnet-preview#azure-messaging-servicebus-servicebusretryoptions-trytimeout) will be used. |
| **SessionId** | The Session ID associated with the receiver (for [session enabled](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions) queue or topic). | Used by *ReceiveMessages* and *ReceiveMessage* methods. |
| **(PeekReceive)**   * **Peek** * **PeekFromSequenceNumber** | Peeking a message does not require the message to be locked. Because the message is not locked to a specific receiver, the message will not be able to be settled.  PeekFromSequenceNumber:An optional sequence number from where to peek the message. This corresponds to the [SequenceNumber](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.servicebus.servicebusreceivedmessage.sequencenumber?view=azure-dotnet-preview#remarks). | Used by the *ReceiveMessage* method, fetches the next active message without changing the state of the receiver or the message source. It corresponds to [this](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.servicebus.servicebusreceiver.peekmessageasync?view=azure-dotnet) method in the Azure Service Bus SDK. |
| **(ReceiveDeferredSequenceNumber) SequenceNumber** | Options to receive deferred messages identified by [sequence number](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.servicebus.servicebusreceivedmessage.sequencenumber?view=azure-dotnet-preview#remarks). | Used by the [ReceiveMessage](https://wiki.genexus.com/commwiki/wiki?51786)method for a deferred message. See [HowTo: Defer a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51981). |
| **BrokerReceiverOptions** | Options for initializing the receiver. See [BrokerReceiverOptions SDT](https://wiki.genexus.com/commwiki/wiki?51943). | For non session-enabled queues or topics, the broker receiver can be initialized at the connection also, and will be used until disposed.  Nevertheless, the BrokerReceiverOptions settings can be changed for each receive operation.   For session-enabled queues or topics the session receiver is initialized for each receive operation so the *Session Id* is mandatory in this case. |

### [Availability](#Availability)

This feature is available since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Azure Service Bus: BrokerReceiverOptions SDT](https://wiki.genexus.com/commwiki/wiki?51943) | [Azure Service Bus: ConsumeMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51945) |
| [HowTo: Complete a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51980) | [HowTo: Defer a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51981) | [HowTo: Receive messages from a Message Broker](https://wiki.genexus.com/commwiki/wiki?51977) | [HowTo: Receive messages from a session-enabled Message Broker](https://wiki.genexus.com/commwiki/wiki?51984) |
| [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786) |

---
