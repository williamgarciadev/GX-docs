---
title: "Queue API"
source_id: 51771
source_url: https://wiki.genexus.com/commwiki/wiki?51771
genexus_version: "18"
---

# Queue API

Allows defining the way to send, receive, and consume a  [Message queue](https://wiki.genexus.com/commwiki/wiki?6912,,).  
This functionality is implemented for  [Azure Queue Storage](https://docs.microsoft.com/en-us/azure/storage/queues/storage-queues-introduction) and [AWS SQS](https://aws.amazon.com/sqs/?nc1=h_ls).  
Depending on the provider, you must import the following modules into your [KB](https://wiki.genexus.com/commwiki/wiki?1836):

Azure Storage Queue

* AzureCore
* AzureQueue
* GeneXusMessagingQueue

AWS SQS

* AWSCore
* AWSQueue
* GeneXusMessagingQueue

To import each module, in the GeneXus menu you need to select: **Knowledge Manager > Manage Module References**.

### [Support](#Support)

Azure Storage Queue support is provided by the  [.NET](https://wiki.genexus.com/commwiki/wiki?38604) generator.  
AWS SQS is supported by both the [Java](https://wiki.genexus.com/commwiki/wiki?12258) generator and by the [.NET](https://wiki.genexus.com/commwiki/wiki?38604) generator.

### [Availability](#Availability)

This feature is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [AWSQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51778) | [AzureQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51737) |
| [AzureQueue.MessageQueueProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55673) | [HowTo: Connect to a Queue](https://wiki.genexus.com/commwiki/wiki?51761) | [HowTo: Send a message to an Azure Storage Queue](https://wiki.genexus.com/commwiki/wiki?51781) | [HowTo: Send and receive messages from SQS](https://wiki.genexus.com/commwiki/wiki?51926) |
| [Queue API domains](https://wiki.genexus.com/commwiki/wiki?51928) | [Queue API Message SDT](https://wiki.genexus.com/commwiki/wiki?51738) | [Queue API MessageQueue external object](https://wiki.genexus.com/commwiki/wiki?51736) | [Queue API MessageResult SDT](https://wiki.genexus.com/commwiki/wiki?51740) |

---
