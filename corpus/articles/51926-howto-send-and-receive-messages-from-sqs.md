---
title: "HowTo: Send and receive messages from SQS"
source_id: 51926
source_url: https://wiki.genexus.com/commwiki/wiki?51926
genexus_version: "18"
---

# HowTo: Send and receive messages from SQS

This article contains an example that shows how to send and consume messages from a [Message queue](https://wiki.genexus.com/commwiki/wiki?6912,,) with the [Queue API](https://wiki.genexus.com/commwiki/wiki?51771), using [AWS SQS](https://aws.amazon.com/sqs/?nc1=h_ls).

### [Steps](#Steps)

The code consists of the following:

**1.** Connect to the AWS SQS using the [AWSQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51778).  
**2.** It returns a [MessageQueue EO](https://wiki.genexus.com/commwiki/wiki?51736) which should be used to send the message to the Queue.  
**3.** The result is returned in a variable of type [MessageResult SDT](https://wiki.genexus.com/commwiki/wiki?51740).

Next, create a GeneXus object and define the following:

#### [To connect](#To+connect)

```
&queueURL = !"https://sqs.us-east-1.amazonaws.com/xxxxx/gxfullgx-test-queueapi"
&accessKey = !"xxxxxxxxxxxxxxxx"
&secretKey = !"xxxxxxxxxxxxxxxxxxxxxxxx"
&region = !"us-east-1"

&AWSBasicCredentials.AccessKey = &accessKey //AWSBasicCredentials SDT is under AWSCore module
&AWSBasicCredentials.SecretKey = &secretKey
&AWSBasicCredentials.Region = &region

&MessageQueue = AWSQueue.MessageQueueProvider.Connect(&AWSBasicCredentials,&queueURL,&errorMessages,&isOK) //GeneXusMessagingQueue.SimpleQueue.MessageQueue
```

#### [To Send Messages](#To+Send+Messages+)

```
&Message = new()
&Message.MessageId = GUID.NewGuid().ToString().Trim()
&Message.MessageBody = !"test1 send one message"

&MessageProperty = new() //GeneXusMessagingQueue.SimpleQueue.MessageProperty
&MessageProperty.PropertyKey = !"key1"
&MessageProperty.PropertyValue = !"Value1"
&Message.MessageAttributes.Add(&MessageProperty)

&MessageProperty = new()
&MessageProperty.PropertyKey = !"key2"
&MessageProperty.PropertyValue = !"Value2"
&Message.MessageAttributes.Add(&MessageProperty)

&Messages.Add(&Message)

&MessageOptions.MaxNumberOfMessages = 10 //GeneXusMessagingQueue.SimpleQueue.MessageOptions

&MessageResultCollection = &MessageQueue.SendMessages(&Messages,&MessageOptions,&errorMessages,&success) //GeneXusMessagingQueue.SimpleQueue.MessageResult Collection
```

#### [To Receive Messages](#To+Receive+Messages)

```
&MessageCollection = &MessageQueue.ReceiveMessages(&errorMessages,&success) //GeneXusMessagingQueue.SimpleQueue.Message Collection
//Process &MessageCollection
```


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Queue API MessageQueue external object](https://wiki.genexus.com/commwiki/wiki?51736) |

---
