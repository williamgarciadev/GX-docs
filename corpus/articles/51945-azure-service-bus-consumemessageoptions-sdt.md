---
title: "Azure Service Bus: ConsumeMessageOptions SDT"
source_id: 51945
source_url: https://wiki.genexus.com/commwiki/wiki?51945
genexus_version: "18"
---

# Azure Service Bus: ConsumeMessageOptions SDT

When the [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782) is used, the *ConsumeMessageOptions*[Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) is defined under the *AzureServiceBus* module and represents the options that may be passed to the [ConsumeMessage](https://wiki.genexus.com/commwiki/wiki?51786) method.

`[imagen omitida: wiki id 51947]`

After executing the Receive method, you decide what to do with the message using the Consume method.  
Message settlement can only be used when using the [PeekLock](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-transfers-locks-settlement#peeklock) receive mode, which is the default behavior. For the settlement operation to be successful, the message must be locked.   
To understand the behavior, the recommendation is to check the [Azure documentation](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-transfers-locks-settlement#settling-receive-operations).

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ConsumeMode** | When a consumer receives a message from the broker, the consumer decides what to do with the message. | |  |  | | --- | --- | | **ConsumeModeOptions Domain** |  | | *Complete* | Completes a message. This will delete the message from the service. | | *Abandon* | Abandons a message. This will make the message available again for immediate processing as the lock on the message held by the receiver will be released. | | *DeadLetter* | Moves a message to the dead-letter subqueue. | | *Defer* | Indicates that the receiver wants to defer the processing for the message. In order to receive this message again in the future, you will need to get the [SequenceNumber](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sequencing) (which is an [attribute](https://wiki.genexus.com/commwiki/wiki?51791) of the received Message) and receive it using the [ReceiveMessage method](https://wiki.genexus.com/commwiki/wiki?51786), passing to it the ReceiveDeferredSequenceNumbers.SequenceNumber of the [Azure Service Bus: ReceiveMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51952). | | *RenewMessageLock* | Renews the lock on the message. The lock will be renewed based on the setting specified on the queue. | |

### [Availability](#Availability)

This feature is available since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).

### [See Also](#See+Also)

[Message settlement with peek lock mode.](https://medium.com/event-driven-utopia/azure-service-bus-essentials-message-settlement-with-peek-lock-mode-cc2e5917e92b)  
[Message deferral](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-deferral)


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [HowTo: Complete a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51980) | [HowTo: Defer a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51981) |
| [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786) |

---
