---
title: "Queue API MessageOptions SDT"
source_id: 51743
source_url: https://wiki.genexus.com/commwiki/wiki?51743
genexus_version: "18"
---

# Queue API MessageOptions SDT

The *MessageOptions*[Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) is defined under the GeneXusMessagingQueue.SimpleQueue module and allows you to make general settings when using the [Queue API](https://wiki.genexus.com/commwiki/wiki?51771).

`[imagen omitida: wiki id 51775]`

Depending on the method and the provider, the meaning of the property may vary.  
  

**Warning**: The recommendation for using any of these properties is to check the documentation of the corresponding provider.

|  |  |  |
| --- | --- | --- |
|  | **Azure Storage Queue** | **AWS SQS** |
| **MaxNumberOfMessages** | *Receive messages method:*  A nonzero integer value that specifies the number of messages to retrieve from the queue, up to a maximum of 32. See [this](https://learn.microsoft.com/en-us/dotnet/api/azure.storage.queues.queueclient.receivemessages?view=azure-dotnet) reference. | *Receive messages method:*  The maximum number of messages to return. Amazon SQS never returns more messages than this value (however, fewer messages might be returned). Valid values: 1 to 10. Default: 1. See [this](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) reference. |
| **WaitTimeout** | ---- | *Receive method:*  In the documentation of SQS is called WaitTimeSeconds  The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. If a message is available, the call returns sooner than `WaitTimeSeconds`. If no messages are available and the wait time expires, the call returns successfully with an empty list of messages. See [this](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) reference.  See also [this](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html#sqs-long-polling) doc. |
| **VisibilityTimeout** | *Send method:*  The visibility timeout specifies how long the message should be invisible to Dequeue and Peek operations.  *Receive method:*  Specifies the new visibility timeout value, in seconds, relative to server time. The default value is 30 seconds. | *Receive method:*  The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved.  Follow [this link](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html) |
| **TimeToLive** | *Send method:*  Specifies the time-to-live interval for the message, in seconds. See more information [here](https://learn.microsoft.com/en-us/rest/api/storageservices/put-message). | ---- |
| **DelaySeconds** | ---- | *Send method:*  The length of time, in seconds, for which to delay a specific message. For more information see [here](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html). |
| **ReceiveRequestAttemptId** | ---- | *Receive method:* This parameter applies only to FIFO (first-in-first-out) queues.  The token used for deduplication of Receive message calls. See [this](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) reference. |

The following do not correspond to any property of the provider's.

|  |  |  |
| --- | --- | --- |
|  | **Azure Storage Queue** | **AWS SQS** |
| **ReceiveMessageAttributes** |  | *Receive method:* Return the message attributes of the message retrieved. |
| **DeleteConsumedMessages** | *Receive method:*  Delete the message after being received, thus, removing it from the queue. |  |

### [Availability](#Availability)

This feature is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Queue API MessageQueue external object](https://wiki.genexus.com/commwiki/wiki?51736) |

---
