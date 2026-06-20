---
title: "Message attributes for Azure Service Bus"
source_id: 51791
source_url: https://wiki.genexus.com/commwiki/wiki?51791
genexus_version: "18"
---

# Message attributes for Azure Service Bus

With the [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782), you can send messages to Azure Service Bus.

Message attributes are represented as a collection of a [MessageProperty SDT](https://wiki.genexus.com/commwiki/wiki?51969) that is a collection (property / value), as shown below.

`[imagen omitida: wiki id 51792]`

To send a message, use the [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786) after having connected to Azure Service Bus with the [AzureServiceBus.MessageBrokerProvider external object](https://wiki.genexus.com/commwiki/wiki?51784).  
The message to send is set up using the [Message SDT](https://wiki.genexus.com/commwiki/wiki?51789), where you can optionally specify custom and broker message attributes.

The same happens with the received messages, which arrive with a set of broker and custom properties that are loaded in the MessageAttributes item of the Message SDT.

The message properties supported by Azure Service Bus are listed [here](https://docs.microsoft.com/en-us/dotnet/api/azure.messaging.servicebus.servicebusmessage?view=azure-dotnet#properties).

### [Sample](#Sample)

```
&Message = new() //Message, GeneXusMessagingMessageBroker
&Message.MessageId = !"123456"
&Message.MessageBody = !"test1 send one message"

//Custom Properties

&MessageProperty = new() //MessageProperty, GeneXusMessagingMessageBroker
&MessageProperty.PropertyKey = !"key1"
&MessageProperty.PropertyValue = !"Value1"
&Message.MessageAttributes.Add(&MessageProperty)

&MessageProperty = new() 
&MessageProperty.PropertyKey = !"key2"
&MessageProperty.PropertyValue = !"Value2"
&Message.MessageAttributes.Add(&MessageProperty)

//Broker Properties 

&MessageProperty = new()
&MessageProperty.PropertyKey = !"subject"
&MessageProperty.PropertyValue = !"TestSubject"
&Message.MessageAttributes.Add(&MessageProperty)

&MessageProperty = new()
&MessageProperty.PropertyKey = !"sessionid"
&MessageProperty.PropertyValue = !"sessionIdTest"
&Message.MessageAttributes.Add(&MessageProperty)

&success = &MessageBroker.SendMessage(&Message,&errorMessages) //MessageBroker, GeneXusMessagingMessageBroker
```

Checking the message sent using the Service Bus Explorer:

`[imagen omitida: wiki id 51793]`

### [Availability](#Availability)

This feature is available since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Azure Service Bus: ConsumeMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51945) | [Message Broker API: Message SDT](https://wiki.genexus.com/commwiki/wiki?51789) |
| [Message Broker API: MessageProperty SDT](https://wiki.genexus.com/commwiki/wiki?51969) |

---
