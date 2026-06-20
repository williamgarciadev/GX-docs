---
title: "HowTo: Receive messages from a session-enabled Message Broker"
source_id: 51984
source_url: https://wiki.genexus.com/commwiki/wiki?51984
genexus_version: "18"
---

# HowTo: Receive messages from a session-enabled Message Broker

With the [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782), you can send and receive messages from a Message Broker, in particular, [session-enabled](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions).

This article contains an example that shows how to receive messages from a session-enabled Azure Service Bus.

The Session ID has to be set for the Receive operation, as a session receiver is defined to be used until the session lock expires.

Consider that it is mandatory for session-enabled queues or topics to set the Session ID for each message you send. Otherwise, you get an exception from Azure Service Bus. The Session ID for each message is set as a [MessageProperty](https://wiki.genexus.com/commwiki/wiki?51969).

### [Receiving a message](#Receiving+a+message)

The following code is the one used to receive a message:

```
&BrokerReceiverOptions = new()
&BrokerReceiverOptions.ReceiveMode = ReceiveModeOptions.ReceiveAndDelete
&BrokerReceiverOptions.SessionId = &SessionId

&receiveMessageOptions = new()
&receiveMessageOptions.MaxMessages = 3
&receiveMessageOptions.MaxWaitTime = 3
&receiveMessageOptions.BrokerReceiverOptions = &BrokerReceiverOptions

&MessageCollection = &MessageBroker.ReceiveMessages(&BrokerReceiverOptions.ToJson(), &errorMessages,&success)
```

### [Sending a message with a Session ID](#Sending+a+message+with+a+Session+ID)

The following code is the one used for sending a message with a Session ID:

```
&Message = new()
&Message.MessageId = GUID.NewGuid().ToString()
&Message.MessageBody = !"message body"

//Broker Properties 

&MessageProperty = new()
&MessageProperty.PropertyKey = !"SessionId"
&MessageProperty.PropertyValue = &SessionId.Trim()
&Message.MessageAttributes.Add(&MessageProperty)

//SEND

&success = &MessageBroker.SendMessage(&Message,"",&errorMessages)

if not &success
    for &errorMessage in &errorMessages
        msg(format(!"%1 (%2)",&errorMessage.Description, &errorMessage.Id), status)
    endfor
endif

&MessageBroker.Dispose()
```

### [Variables defined in the example](#Variables+defined+in+the+example)

|  |  |
| --- | --- |
|  |  |
| *&brokerReceiverOptions* | [BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943), AzureServiceBus |
| *&MessageBroker* | [MessageBroker](https://wiki.genexus.com/commwiki/wiki?51786), GeneXusMessagingMessageBroker |
| *&receiveMessageOptions* | [ReceiveMessageOptions](https://wiki.genexus.com/commwiki/wiki?51952), AzureServiceBus |
| *&Message* | [Message](https://wiki.genexus.com/commwiki/wiki?51789), GeneXusMessagingMessageBroker |
| *&MessageCollection* | [Message](https://wiki.genexus.com/commwiki/wiki?51789) (Collection), GeneXusMessagingMessageBroker |
| *&MessageProperty* | [MessageProperty](https://wiki.genexus.com/commwiki/wiki?51969), GeneXusMessagingMessageBroker |

**Note**: When the session is held by a client, the client holds an exclusive lock on all messages with that session's session ID in the queue or subscription.

For the generated code, for Peek Lock operations, the lock is released when the lock expires (Message Lock duration defined for the queue or topic).  
For Receive and Delete operations, the lock is released when the operation finishes.

### [See Also](#See+Also)

[Session-features](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions#session-features)


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) |

---
