---
title: "HowTo: Send messages to a Message Broker"
source_id: 51973
source_url: https://wiki.genexus.com/commwiki/wiki?51973
genexus_version: "18"
---

# HowTo: Send messages to a Message Broker

This article contains an example that shows how to send messages to a Message Broker with the [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782), using Azure Service Bus (Topic).

### [Steps](#Steps)

The process consists of the following:

**1.** Connect to the Azure Service Bus using the [AzureServiceBus.MessageBrokerProvider external object](https://wiki.genexus.com/commwiki/wiki?51784).  
**2.** The [Connect method](https://wiki.genexus.com/commwiki/wiki?51784) returns a [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786) that should be used to send the messages.  
**3.** The [SendMessages method](https://wiki.genexus.com/commwiki/wiki?51786) returns a boolean result depending on the success of the execution and a variable of [GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335) to process the errors.

### [Connecting to Azure Service Bus Topic](#Connecting+to+Azure+Service+Bus+Topic+)

The following code is the one used to connect to an Azure Service Bus Topic:

```
&brokerReceiverOptions = new() // BrokerReceiverOptions, AzureServiceBus
&brokerReceiverOptions .ReceiveMode = ReceiveModeOptions.ReceiveAndDelete

&MessageBroker = AzureServiceBus.MessageBrokerProvider.Connect(&topicName,&SubscriptionName,&connectionString,&IsSessionEnabled,&brokerReceiverOptions ,&senderIdentifier,&errorMessages,&success) 

if not &success
    msg(!"Connection failed", status)
    for &errorMessage in &errorMessages
        msg(format(!"%1 (%2)",&errorMessage.Description, &errorMessage.Id), status)
    endfor
endif
```

### [Sending a batch of messages](#Sending+a+batch+of+messages)

The following code is the one used for sending a batch of messages:

```
&Message = new() 
&Message.MessageId = GUID.NewGuid().ToString().Trim()
&Message.MessageBody = !"message body"

&MessageProperty = new()
&MessageProperty.PropertyKey = !"key1"
&MessageProperty.PropertyValue = !"Value1"
&Message.MessageAttributes.Add(&MessageProperty)

&MessageProperty = new()
&MessageProperty.PropertyKey = !"key2"
&MessageProperty.PropertyValue = !"Value2"
&Message.MessageAttributes.Add(&MessageProperty)

&Messages.Add(&message)

---------

//Send//
&success =  &MessageBroker.SendMessages(&Messages,"",&errorMessages)

//Process &errorMessages 
&MessageBroker.Dispose()
```

### [Variables defined in the samples](#Variables+defined+in+the+samples)

|  |  |
| --- | --- |
|  |  |
| *&brokerReceiverOptions* | [BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943), AzureServiceBus |
| *&MessageBroker* | [MessageBroker](https://wiki.genexus.com/commwiki/wiki?51786), GeneXusMessagingMessageBroker |
| *&MessageProperty* | [MessageProperty](https://wiki.genexus.com/commwiki/wiki?51969), GeneXusMessagingMessageBroker |


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) |

---
