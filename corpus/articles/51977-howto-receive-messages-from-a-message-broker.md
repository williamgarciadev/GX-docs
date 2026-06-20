---
title: "HowTo: Receive messages from a Message Broker"
source_id: 51977
source_url: https://wiki.genexus.com/commwiki/wiki?51977
genexus_version: "18"
---

# HowTo: Receive messages from a Message Broker

With the [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782), you can send and receive messages from a Message Broker. This article contains an example that shows how to receive messages from Azure Service Bus Queue.

### [Steps](#Steps)

The process consists of the following:

**1.** Connect to the Azure Service Bus using the [AzureServiceBus.MessageBrokerProvider external object](https://wiki.genexus.com/commwiki/wiki?51784).  
**2.** The [Connect method](https://wiki.genexus.com/commwiki/wiki?51784) returns a [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786) that should be used to receive the messages.  
**3.** The [ReceiveMessages method](https://wiki.genexus.com/commwiki/wiki?51786) returns a collection of [Message](https://wiki.genexus.com/commwiki/wiki?51789)s and a variable of [GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335) to process the errors.

### [Connecting to Azure Service Bus Queue](#Connecting+to+Azure+Service+Bus+Queue)

The following code is the one used to connect to an Azure Service Bus Queue:

```
&brokerReceiverOptions = new()
&brokerReceiverOptions.PrefetchCount = 10

&MessageBroker = AzureServiceBus.MessageBrokerProvider.Connect(&queueName,&queueConnection,&isSessionEnabled,&brokerReceiverOptions,&senderIdentifier,&errorMessages,&isOK)

if not &isOK
    for &errorMessage in &errorMessages
        msg(format(!"%1 (%2)",&errorMessage.Description, &errorMessage.Id), status)
    endfor
endif
```

### [Receiving messages from the Service Bus Queue](#Receiving+messages+from+the+Service+Bus+Queue)

The following code is the one used for receiving messages from the Azure Service Bus Queue:

```
&receiveMessageOptions.MaxMessages = 100
&receiveMessageOptions.MaxWaitTime = 10
&MessageCollection = &MessageBroker.ReceiveMessages(&receiveMessageOptions.ToJson(), &errorMessages,&success)
//Process &errorMessages
&MessageBroker.Dispose()
```

### [Variables defined in the example](#Variables+defined+in+the+example)

|  |  |
| --- | --- |
|  |  |
| *&brokerReceiverOptions* | [BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943), AzureServiceBus |
| *&MessageBroker* | [MessageBroker](https://wiki.genexus.com/commwiki/wiki?51786), GeneXusMessagingMessageBroker |
| *&receiveMessageOptions* | [ReceiveMessageOptions](https://wiki.genexus.com/commwiki/wiki?51952), AzureServiceBus |
| *&MessageCollection* | [Message](https://wiki.genexus.com/commwiki/wiki?51789) (Collection), GeneXusMessagingMessageBroker |


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) |

---
