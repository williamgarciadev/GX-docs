---
title: "HowTo: Connect to a Queue"
source_id: 51761
source_url: https://wiki.genexus.com/commwiki/wiki?51761
genexus_version: "18"
---

# HowTo: Connect to a Queue

The purpose of this article is to explain the necessary steps to connect to a Queue (for sending and receiving messages) using the [Queue API](https://wiki.genexus.com/commwiki/wiki?51771). For this, you have to use the *MessageQueueProvider* [External object](https://wiki.genexus.com/commwiki/wiki?5669).

The providers supported are [Azure Queue Storage](https://docs.microsoft.com/en-us/azure/storage/queues/storage-queues-introduction) and [AWS SQS](https://aws.amazon.com/sqs/?nc1=h_ls).

So, there is a different External Object for each one:

* [AWSQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51778)
* [AzureQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51737)

### [Samples](#Samples)

The following code is the one used to connect to AWS SQS:

```
&queueURL = !"https://sqs.us-east-1.amazonaws.com/xxxx/gxfullgx-test-queueapi"
&accessKey = !"xxxx"
&secretKey = !"xxxxx"
&region = !"us-east-1"

&AWSBasicCredentials.AccessKey = &accessKey //AWSBasicCredentials, AWSCore
&AWSBasicCredentials.SecretKey = &secretKey
&AWSBasicCredentials.Region = &region

&MessageQueue = AWSQueue.MessageQueueProvider.Connect(&AWSBasicCredentials,&queueURL,&errorMessages,&isOK)
```

To connect to the queue without hard coding the credentials and using [Environment](https://wiki.genexus.com/commwiki/wiki?7115) variables, click here: [Queue API domains](https://wiki.genexus.com/commwiki/wiki?51928).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [AWSQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51778) | [Queue API MessageQueue external object](https://wiki.genexus.com/commwiki/wiki?51736) |

---
