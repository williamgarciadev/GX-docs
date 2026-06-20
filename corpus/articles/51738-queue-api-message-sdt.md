---
title: "Queue API Message SDT"
source_id: 51738
source_url: https://wiki.genexus.com/commwiki/wiki?51738
genexus_version: "18"
---

# Queue API Message SDT

The *Message* [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) is defined under the GeneXusMessagingQueue.SimpleQueue module and represents the message to be sent to a Message Queue using the [Queue API](https://wiki.genexus.com/commwiki/wiki?51771).

`[imagen omitida: wiki id 51772]`

|  |  |
| --- | --- |
| MessageId | ID of the message. |
| MessageBody | Message to send. |
| MessageAttributes | Collection of [MessageProperty](https://wiki.genexus.com/commwiki/wiki?51798). |
| MessageHandleId | Every time you receive a message from a queue, you receive a handle ID for that message (also called a receipt handle). This handle is associated with the action of receiving the message, not with the message itself. To delete the message, you must provide the HandleId (not the message ID). |

**Note**: In the case of AWS SQS, it lets you include structured metadata with messages using MessageAttributes. For more information, visit this [link](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes).

### [Availability](#Availability)

This feature is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Queue API MessageQueue external object](https://wiki.genexus.com/commwiki/wiki?51736) |

---
