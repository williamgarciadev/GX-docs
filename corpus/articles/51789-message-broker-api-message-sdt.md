---
title: "Message Broker API: Message SDT"
source_id: 51789
source_url: https://wiki.genexus.com/commwiki/wiki?51789
genexus_version: "18"
---

# Message Broker API: Message SDT

The *Message*[Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) is defined under the *GeneXusMessagingMessageBroker* module and represents the message to be sent and received by a Message Broker using the [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782).

`[imagen omitida: wiki id 51971]`

|  |  |
| --- | --- |
| MessageId | ID of the message |
| MessageBody | The message to send |
| MessageAttributes | Collection of [MessageProperty SDT](https://wiki.genexus.com/commwiki/wiki?51969) (PropertyKey / PropertyValue pairs which allow setting attributes to the message) |
| MessageHandleId |  |

**Note**: The MessageAttributes depend on the Message Broker.

### [Availability](#Availability)

This feature is available since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).

### [See Also](#See+Also)

[Message attributes for Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51791).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [HowTo: Complete a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51980) | [HowTo: Defer a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51981) |
| [HowTo: Receive messages from a Message Broker](https://wiki.genexus.com/commwiki/wiki?51977) | [HowTo: Receive messages from a session-enabled Message Broker](https://wiki.genexus.com/commwiki/wiki?51984) | [HowTo: Schedule a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51982) | [Message attributes for Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51791) |
| [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786) |

---
