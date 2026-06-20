---
title: "AzureQueue.MessageQueueProvider external object (GeneXus 18 Upgrade 5)"
source_id: 55673
source_url: https://wiki.genexus.com/commwiki/wiki?55673
genexus_version: "18"
---

# AzureQueue.MessageQueueProvider external object (GeneXus 18 Upgrade 5)

The *MessageQueueProvider* is an external object of the[Queue API](https://wiki.genexus.com/commwiki/wiki?51771) located under AzureQueue module.

It allows establishing a connection to an [Azure Storage Queue](https://docs.microsoft.com/en-us/azure/storage/queues/storage-queues-introduction), passing its credentials (queueName and queueURL).

To send or receive messages from Azure Queue, first you have to establish a connection using the method of this external object. It returns a [MessageQueue](https://wiki.genexus.com/commwiki/wiki?51736), which must be used to process the queue (produce and consume messages).

This guarantees that only the Azure Queue dependencies are downloaded to your machine and taken to the deployment.

`[imagen omitida: wiki id 51777]`

## [Properties](#Properties)

It doesn't have any.

## [Methods](#Methods)

### [Connect](#Connect)

Static method that allows instantiating a Queue from dynamic data.

**Return value**  [MessageQueue](https://wiki.genexus.com/commwiki/wiki?51736)  
**Parameters**   queueName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), queueURL:VarChar, errorMessages:[Messages](https://wiki.genexus.com/commwiki/wiki?40335), success: [Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

To connect to the queue without hard coding the credentials and use Environment variables see [here](https://wiki.genexus.com/commwiki/wiki?51928).

## [Events](#Events)

It doesn't have any.

### [Availability](#Availability)

This feature is available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).
