---
title: "HowTo: Defer a message in Azure Service Bus"
source_id: 51981
source_url: https://wiki.genexus.com/commwiki/wiki?51981
genexus_version: "18"
---

# HowTo: Defer a message in Azure Service Bus

This article contains an example that shows how to consume (defer) a message in Azure Service Bus Queue.

### [Steps](#Steps)

The code consists of the following:

**1.** Connect to the Azure Service Bus using the [AzureServiceBus.MessageBrokerProvider external object](https://wiki.genexus.com/commwiki/wiki?51784).  
**2.** The [Connect method](https://wiki.genexus.com/commwiki/wiki?51784) returns a [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786) that should be used to receive the messages.  
**3.** The message has to be received prior to consuming it.  
The [ReceiveMessage method](https://wiki.genexus.com/commwiki/wiki?51786) returns a [Message](https://wiki.genexus.com/commwiki/wiki?51789) and a variable of [GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335) to process the errors.  
**4.** The [ConsumeMessage method](https://wiki.genexus.com/commwiki/wiki?51786) consumes the message received in step 3, also passing the [ConsumeMessageOptions](https://wiki.genexus.com/commwiki/wiki?51945) parameter depending on what you want to do with the message (complete, abandon, defer, etc).

Consider that:

* The receive mode option has to be Peek Lock. See Settling receive operations in Azure Service Bus.
* When a message is received in [PeekLock](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.servicebus.servicebusreceivemode?view=azure-dotnet#azure-messaging-servicebus-servicebusreceivemode-peeklock) mode, the message is locked in the server for this receiver instance for the duration specified in the Queue/Subscription creation (LockDuration).

### [Connecting to Azure Service Bus Queue](#Connecting+to+Azure+Service+Bus+Queue)

The following code is the one used to connect to an Azure Service Bus Queue:

```
brokerReceiverOptions = new()
&brokerReceiverOptions.ReceiveMode = ReceiveModeOptions.PeekLock
&brokerReceiverOptions.PrefetchCount = 10

&MessageBroker = AzureServiceBus.MessageBrokerProvider.Connect(&queueName,&queueConnection,&isSessionEnabled,&brokerReceiverOptions,&senderIdentifier,&errorMessages,&isOK)
```

### [Receiving a message from the Service Bus Queue](#Receiving+a+message+from+the+Service+Bus+Queue)

The following code is the one used for receiving messages from the Azure Service Bus Queue:

```
receiveMessageOptions.MaxWaitTime = 10
&receivedMessage = &MessageBroker.ReceiveMessage(&receiveMessageOptions.ToJson(),&errorMessages,&isOK)
if not &isOK
   for &errorMessage in &errorMessages
      msg(format(!"%1 (%2)",&errorMessage.Description, &errorMessage.Id), status)
   endfor
endif
```

### [Defer the message](#Defer+the+message)

To defer the message, use:

```
If &isOK
  &ConsumeMessaOptions = new()
  &ConsumeMessaOptions.ConsumeMode = ConsumeModeOptions.Defer
  &success =  &MessageBroker.ConsumeMessage(&receivedMessage,&ConsumeMessaOptions.ToJson(),&errorMessages)
endif

//retrieve sequenceNumber to be able to receive the message again
For &MessageProperty in &receivedMessage.MessageAttributes
    if (&MessageProperty.PropertyKey = !"SequenceNumber")
        &sequenceNumber = &MessageProperty.PropertyValue.ToNumeric()
        exit
    endif
endfor
```

### [Receiving the deferred message](#Receiving+the+deferred+message)

To receive the deferred message, use:

```
&receiveMessageOptions = new()
&receiveMessageOptions.ReceiveDeferredSequenceNumbers.Add(&sequenceNumber)

&receivedMessage = &MessageBroker.ReceiveMessage(&receiveMessageOptions.ToJson(),&errorMessages,&success)

if not &isOK
    for &errorMessage in &errorMessages
        msg(format(!"%1 (%2)",&errorMessage.Description, &errorMessage.Id), status)
    endfor
endif
&MessageBroker.Dispose()
```

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
| [Table of contents:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Azure Service Bus: ReceiveMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51952) | [HowTo: Settle messages from a Message Broker](https://wiki.genexus.com/commwiki/wiki?51978) |

---
