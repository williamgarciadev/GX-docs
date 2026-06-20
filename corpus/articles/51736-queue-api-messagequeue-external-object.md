---
title: "Queue API MessageQueue external object"
source_id: 51736
source_url: https://wiki.genexus.com/commwiki/wiki?51736
genexus_version: "18"
---

# Queue API MessageQueue external object

The *MessageQueue* External Object is under the GeneXusMessagingQueue.SimpleQueue module, and allows you to send and process messages of a [Message queue](https://wiki.genexus.com/commwiki/wiki?6912,,) using the [Queue API](https://wiki.genexus.com/commwiki/wiki?51771).

`[imagen omitida: wiki id 51776]`

## [Properties](#Properties)

It doesn't have any.

## [Methods](#Methods)

### [GetQueueLength](#GetQueueLength)

Gets the approximate number of messages in the queue.

**Return value**   None  
**Parameters**     ErrorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), Success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

### [SendMessage](#SendMessage)

Sends a message to the queue.

**Return value**   [MessageResult](https://wiki.genexus.com/commwiki/wiki?51740)  
**Parameters**     Message:[Message](https://wiki.genexus.com/commwiki/wiki?51738), ErrorMessages: [GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), Success:Boolean.

### [SendMessages](#SendMessages)

 Sends a list of messages to the queue, using options.

**Return value**   [MessageResult](https://wiki.genexus.com/commwiki/wiki?51740) (Collection)  
**Parameters**     Message:[Message](https://wiki.genexus.com/commwiki/wiki?51738) (Collection), Options:[MessageOptions](https://wiki.genexus.com/commwiki/wiki?51743),  ErrorMessages: [GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), Success:Boolean.

### [Clear](#Clear)

Clears the queue.

**Return value**   None  
**Parameters**     ErrorMessages: [GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), Success:Boolean.

### [DeleteMessage](#DeleteMessage)

Deletes the message.

**Return value**   [MessageResult](https://wiki.genexus.com/commwiki/wiki?51740)  
**Parameters**     Message: [Message](https://wiki.genexus.com/commwiki/wiki?51738), ErrorMessages: [GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), Succes:Boolean.

### [ReceiveMessages](#ReceiveMessages)

Receives one or more messages from the front of the queue.

**Return value**   [MessageResult](https://wiki.genexus.com/commwiki/wiki?51740) (Collection)  
**Parameters**     ErrorMessages: [GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), Success:Boolean.

Receives one or more messages from the front of the queue with advanced options.

**Return value**   None  
**Parameters**     Options: [MessagesOptions](https://wiki.genexus.com/commwiki/wiki?51743), ErrorMessages: [GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), Success:Boolean.

### [DeleteMessages](#DeleteMessages)

Deletes a list of messages.

**Return value**   [MessageResult](https://wiki.genexus.com/commwiki/wiki?51740)  
**Parameters**     Messages: [Message](https://wiki.genexus.com/commwiki/wiki?51738) (Collection), ErrorMessages: [GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), Success:Boolean

## [Events](#Events)

It doesn't have any.

## [See Also](#See+Also)

[HowTo: Send a message to an Azure Storage Queue](https://wiki.genexus.com/commwiki/wiki?51781)  
[HowTo: Connect to a Queue](https://wiki.genexus.com/commwiki/wiki?51761)  
[HowTo: Send and receive messages from SQS](https://wiki.genexus.com/commwiki/wiki?51926)

## [Availability](#Availability)

This feature is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [AWSQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51778) | [AzureQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51737) |
| [AzureQueue.MessageQueueProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55673) | [HowTo: Send a message to an Azure Storage Queue](https://wiki.genexus.com/commwiki/wiki?51781) | [HowTo: Send and receive messages from SQS](https://wiki.genexus.com/commwiki/wiki?51926) |

---
