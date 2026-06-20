---
title: "Queue API MessageResult SDT"
source_id: 51740
source_url: https://wiki.genexus.com/commwiki/wiki?51740
genexus_version: "18"
---

# Queue API MessageResult SDT

The *MessageResult* structured data type is defined under the GeneXusMessagingQueue.SimpleQueue module and represents the message received when a message is sent to a Message Queue using the [Queue API](https://wiki.genexus.com/commwiki/wiki?51771).

`[imagen omitida: wiki id 51774]`

|  |  |
| --- | --- |
| MessageId | Message ID. |
| ServerMessageId | ID returned by the Queue when the message is sent. |
| MessageHandleId | Handle ID. |
| MessageStatus | Status after the message is sent. It can take the values of MessagesStatus. |
| MessageAtttributes | Collection of [MessageProperty](https://wiki.genexus.com/commwiki/wiki?51798). |

**Note**: The MessageAtttributes depend on the provider (Azure Queue or AWS SQS); both can return different metadata information after sending a message to the Queue.

### [Availability](#Availability)

This feature is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [HowTo: Send a message to an Azure Storage Queue](https://wiki.genexus.com/commwiki/wiki?51781) | [HowTo: Send and receive messages from SQS](https://wiki.genexus.com/commwiki/wiki?51926) |
| [Queue API MessageQueue external object](https://wiki.genexus.com/commwiki/wiki?51736) |

---
