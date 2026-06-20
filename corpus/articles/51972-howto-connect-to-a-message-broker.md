---
title: "HowTo: Connect to a Message Broker"
source_id: 51972
source_url: https://wiki.genexus.com/commwiki/wiki?51972
genexus_version: "18"
---

# HowTo: Connect to a Message Broker

The purpose of this article is to explain the necessary steps to connect to a Message Broker (for sending and receiving messages) with the [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782). For this, you have to use the Connect methods of [MessageBrokerProvider](https://wiki.genexus.com/commwiki/wiki?51784)[External object](https://wiki.genexus.com/commwiki/wiki?5669).

The provider supported for now is [Azure Service Bus](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview).

### [Connecting to Azure Service Bus Queue](#Connecting+to+Azure+Service+Bus+Queue)

The following code is the one used to connect to a Service Bus queue:

```
&receiverOptions = new() // BrokerReceiverOptions, AzureServiceBus
&receiverOptions.Identifier = "ReceiverId"
&senderIdentifier = "SenderId"
&isSessionEnabled = false

&receiverOptions.PrefetchCount = 10

&MessageBroker = AzureServiceBus.MessageBrokerProvider.Connect(&queueName,&queueConnection,&isSessionEnabled,&receiverOptions,&senderIdentifier,&errorMessages,&isOK) //MessageBroker, GeneXusMessagingMessageBroker

//Then process errorMessages
&MessageBroker.Dispose()
```

### [Connecting to Azure Service Bus Topic](#Connecting+to+Azure+Service+Bus+Topic)

The following code is the one used to connect to a Service Bus Topic:

```
&receiverOptions = new() // BrokerReceiverOptions, AzureServiceBus
&receiverOptions.Identifier = "ReceiverId"
&senderIdentifier = "SenderId"
&isSessionEnabled = false

&receiverOptions.PrefetchCount = 10

&MessageBroker = AzureServiceBus.MessageBrokerProvider.Connect(&topicName,&SubscriptionName,&connectionString,&IsSessionEnabled,&receiverOptions,&senderIdentifier,&errorMessages,&isOK)
//MessageBroker, GeneXusMessagingMessageBroker

//Then process errorMessages
&MessageBroker.Dispose()
```

### [Variables defined in the samples](#Variables+defined+in+the+samples)

|  |  |
| --- | --- |
|  |  |
| *&receiverOptions* | [BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943), AzureServiceBus |
| *&MessageBroker* | [MessageBroker](https://wiki.genexus.com/commwiki/wiki?51786), GeneXusMessagingMessageBroker |
| *&errorMessages* | [Messages](https://wiki.genexus.com/commwiki/wiki?40335) |


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) |

---
