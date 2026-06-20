---
title: "HowTo: Send a message to an Azure Storage Queue"
source_id: 51781
source_url: https://wiki.genexus.com/commwiki/wiki?51781
genexus_version: "18"
---

# HowTo: Send a message to an Azure Storage Queue

This article contains an example that shows how to send and consume messages from a [Message queue](https://wiki.genexus.com/commwiki/wiki?6912,,) with the [Queue API](https://wiki.genexus.com/commwiki/wiki?51771), using an [Azure Storage Queue](https://docs.microsoft.com/en-us/azure/storage/queues/storage-queues-introduction).

### [Steps](#Steps)

The code consists of the following:

**1.** Connect to the Azure Storage Queue using the [AzureQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51737).  
**2.** It returns a [MessageQueue EO](https://wiki.genexus.com/commwiki/wiki?51736) which should be used to send the message to the Queue.  
**3.** The result is returned in a variable of [MessageResult SDT](https://wiki.genexus.com/commwiki/wiki?51740) type.

Next, create a GeneXus object and define the following:

```
////////Connect to Azure Storage Queue //////

&queueURL = !"DefaultEndpointsProtocol=https;AccountName=azapiqueuetest;AccountKey=xxxxxxxxxxx;EndpointSuffix=core.windows.net" //storage Account Connection String
&queueName = !"gxqueue"

&MessageQueue = AzureQueue.MessageQueueProvider.Connect(&queueName,&queueURL,&errorMessages,&isOK) //&MessageQueue is MessageQueue external object

//////Send a message ///////

&Message = new()  //Message SDT, GeneXusMessagingQueue.SimpleQueue
&Message.MessageId = !"1"   //Id of the message to send
&Message.MessageBody = !"test1 send one message" //Message to be sent

//Message metadata
&MessageProperty = new() //MessageProperty SDT, GeneXusMessagingQueue.SimpleQueue
&MessageProperty.PropertyKey = !"key1"  
&MessageProperty.PropertyValue = !"Value1"
&Message.MessageAttributes.Add(&MessageProperty) //Add the metadata to the message you want to send

&MessageProperty = new()
&MessageProperty.PropertyKey = !"key2"
&MessageProperty.PropertyValue = !"Value2"
&Message.MessageAttributes.Add(&MessageProperty)

&MessageResult = &MessageQueue.SendMessage(&Message,&errorMessages,&success) //Sends the message and captures whether it was sent successfully or error obtained. 

//Here process the &errorMessages
```


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Queue API MessageQueue external object](https://wiki.genexus.com/commwiki/wiki?51736) |

---
