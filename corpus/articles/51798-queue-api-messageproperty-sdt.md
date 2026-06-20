---
title: "Queue API MessageProperty SDT"
source_id: 51798
source_url: https://wiki.genexus.com/commwiki/wiki?51798
genexus_version: "18"
---

# Queue API MessageProperty SDT

The *MessageProperty*[Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) is defined under the GeneXusMessagingQueue.SimpleQueue module and represents the attributes of a message (Key and Value pairs) that are sent as part of the message, or returned when a message is received.

`[imagen omitida: wiki id 51799]`

The attributes depend on the provider (Azure Queue or AWS SQS), both can return different metadata information after sending a message to the Queue.

In the case of AWS SQS, it lets you include structured metadata with messages using message attributes. For more information see this [link](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Queue API Message SDT](https://wiki.genexus.com/commwiki/wiki?51738) | [Queue API MessageResult SDT](https://wiki.genexus.com/commwiki/wiki?51740) |

---
