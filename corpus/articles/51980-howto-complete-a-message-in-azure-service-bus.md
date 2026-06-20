---
title: "HowTo: Complete a message in Azure Service Bus"
source_id: 51980
source_url: https://wiki.genexus.com/commwiki/wiki?51980
genexus_version: "18"
---

# HowTo: Complete a message in Azure Service Bus

This article contains an example that shows how to consume (complete) a message from Azure Service Bus Queue.

### [Steps](#Steps)

The code consists of the following:

**1.** Connect to the Azure Service Bus using the [AzureServiceBus.MessageBrokerProvider external object](https://wiki.genexus.com/commwiki/wiki?51784).  
**2.** The [Connect method](https://wiki.genexus.com/commwiki/wiki?51784) returns a [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786) that should be used to receive the messages.  
**3.** The message has to be received prior to consuming it.  
The [ReceiveMessage method](https://wiki.genexus.com/commwiki/wiki?51786) returns a [Message](https://wiki.genexus.com/commwiki/wiki?51789) and a variable of [GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335) to process the errors.  
**4.** The [ConsumeMessage method](https://wiki.genexus.com/commwiki/wiki?51786) consumes the message received in step 3, also passing the [ConsumeMessageOptions](https://wiki.genexus.com/commwiki/wiki?51945) parameter depending on what you want to do with the message (complete, abandon, defer, etc).

Consider that:

* The receive mode option has to be Peek Lock. See Settling receive operations in Azure Service Bus.
* When a message is received in [PeekLock](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.servicebus.servicebusreceivemode?view=azure-dotnet#azure-messaging-servicebus-servicebusreceivemode-peeklock) mode, the message is locked in the server for this receiver instance for the duration specified in the Queue/Subscription creation (LockDuration).

### [Connecting to Azure Service Bus Queue](#Connecting+to+Azure+Service+Bus+Queue)

The following code is the one used to connect to an Azure Service Bus Queue:

```
&brokerReceiverOptions = new()
&brokerReceiverOptions.ReceiveMode = ReceiveModeOptions.PeekLock
&brokerReceiverOptions.PrefetchCount = 10

&MessageBroker = AzureServiceBus.MessageBrokerProvider.Connect(&queueName,&queueConnection,&isSessionEnabled,&brokerReceiverOptions,&senderIdentifier,&errorMessages,&isOK)
```

### [Receive a message from the Service Bus Queue](#Receive+a+message+from+the+Service+Bus+Queue)

The following code is the one used for receiving messages from the Azure Service Bus Queue:

```
&receiveMessageOptions.MaxWaitTime = 10
&receivedMessage = &MessageBroker.ReceiveMessage(&receiveMessageOptions.ToJson(),&errorMessages,&isOK)
if not &isOK
   for &errorMessage in &errorMessages
      msg(format(!"%1 (%2)",&errorMessage.Description, &errorMessage.Id), status)
   endfor
endif
```

### [Complete the message](#Complete+the+message)

To complete the message, use:

```
If &isOK
   &ConsumeMessageOptions = new()
   &ConsumeMessageOptions.ConsumeMode = ConsumeModeOptions.Complete

   &success =  &MessageBroker.ConsumeMessage(&receivedMessage,&ConsumeMessageOptions.ToJson(),&errorMessages)

   if &success
     msg(!"Message completed successfully",status)
   else
     for &errorMessage in &errorMessages
        msg(format(!"%1 (%2)",&errorMessage.Description, &errorMessage.Id), status)
     endfor
    endif
endif
&MessageBroker.Dispose()
```

### [Manage errors](#Manage+errors)

It may happen that the message cannot be consumed, for example, due to a MessageLockLost exception.

```
&ConsumeMessaOptions = new()
&ConsumeMessaOptions.ConsumeMode = ConsumeModeOptions.Complete

&success =  &MessageBroker.ConsumeMessage(&receivedMessage,&ConsumeMessaOptions.ToJson(),&errorMessages)

if not &success

  if &errorMessages.Item(1).Id = !"MessageLockLost"
    //Here receive the message again
  endif
endif
```

The ErrorMessage Id contains the Reason of the exception, which is given by the provider. See [ServiceBus failure reason list](https://azuresdkdocs.blob.core.windows.net/$web/dotnet/Azure.Messaging.ServiceBus/7.11.0/api/Azure.Messaging.ServiceBus/Azure.Messaging.ServiceBus.ServiceBusFailureReason.html).

### [Variables defined in the samples](#Variables+defined+in+the+samples)

| **Name** | **Type** |
| --- | --- |
| *&MessageBroker* | [MessageBroker](https://wiki.genexus.com/commwiki/wiki?51786), GeneXusMessagingMessageBroker |
| *&receiveMessageOptions* | [ReceiveMessageOptions](https://wiki.genexus.com/commwiki/wiki?51952), AzureServiceBus |
| *&receivedMessage* | [Message](https://wiki.genexus.com/commwiki/wiki?51789) |
| *&ConsumeMessageOptions* | [ConsumeMessageOptions](https://wiki.genexus.com/commwiki/wiki?51945) |
| *&brokerReceiverOptions* | [BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943), AzureServiceBus |

### [See Also](#See+Also)

[Message settlement with peek lock mode](https://medium.com/event-driven-utopia/azure-service-bus-essentials-message-settlement-with-peek-lock-mode-cc2e5917e92b)


|  |
| --- |
| **Backlinks** |
| [Table of contents:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [HowTo: Settle messages from a Message Broker](https://wiki.genexus.com/commwiki/wiki?51978) |

---
