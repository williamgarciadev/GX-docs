---
title: "MessageBroker external object"
source_id: 51786
source_url: https://wiki.genexus.com/commwiki/wiki?51786
genexus_version: "18"
---

# MessageBroker external object

The *MessageBroker* External Object is under the *GeneXusMessagingMessageBroker* module and allows you to send and process messages of a Message Broker using the [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782).

`[imagen omitida: wiki id 51955]`

## [Methods](#Methods+)

### [SendMessage](#SendMessage)

Send a message to a message broker.

**Return value**   boolean  
**Parameters**     Message:[Message](https://wiki.genexus.com/commwiki/wiki?51789), options:Varchar, ErrorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335)

In Azure Service Bus, the options can be left empty.

### [SendMessages](#SendMessages)

Send messages to the message broker.

**Return value**   boolean  
**Parameters**     Message:[Message](https://wiki.genexus.com/commwiki/wiki?51789) (Collection), options:Varchar, ErrorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335)

In Azure Service Bus, the options can be left empty.

### [ReceiveMessages](#ReceiveMessages)

Retrieve messages from a message broker using options.

**Return value**    Message:[Message](https://wiki.genexus.com/commwiki/wiki?51789) (Collection)  
**Parameters**     options:Varchar, ErrorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), success: Boolean

Depending on the Message Broker provider used, the options parameter should be a JSON string formatted using the SDT defined for that purpose in the provider's module.  
In Azure Service Bus, the options parameter has to be a JSON string of [ReceiveMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51952).

### [ReceiveMessage](#ReceiveMessage)

Retrieve a message from a message broker using options.

**Return value**    Message:[Message](https://wiki.genexus.com/commwiki/wiki?51789)   
**Parameters**     options:Varchar, ErrorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), success: Boolean

Depending on the Message Broker provider used, the options parameter should be a JSON string formatted using the SDT defined for that purpose in the provider's module.  
In Azure Service Bus, the options parameter has to be a JSON string of [ReceiveMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51952).

### [ConsumeMessage](#ConsumeMessage)

Consume / settle a message from a message broker using options.

**Return value**    success:Boolean  
**Parameters**     Message:[Message](https://wiki.genexus.com/commwiki/wiki?51789), options:Varchar, ErrorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335)

Depending on the Message Broker provider used, the options parameter should be a JSON string formatted using the SDT defined for that purpose in the provider's module.  
In Azure Service Bus, the options parameter has to be a JSON string of [ConsumeMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51945)

### [ScheduleMessage](#ScheduleMessage)

Schedules a message to appear on Message Broker at a later time.

**Return value**    handleId:Numeric (18)  
**Parameters**     Message:[Message](https://wiki.genexus.com/commwiki/wiki?51789), options:Varchar, ErrorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335)

Depending on the Message Broker provider used, the options parameter should be a JSON string formatted using the SDT defined for that purpose in the provider's module.  
In Azure Service Bus, the options parameter has to be a JSON string of [ScheduleMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51950)

### [CancelSchedule](#CancelSchedule)

Cancels a message that was scheduled.

**Return value**    handleId:Numeric (18)  
**Parameters**     Message:[Message](https://wiki.genexus.com/commwiki/wiki?51789)

In Azure Service Bus, the handleId is the [SequenceNumber](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.servicebus.servicebusreceivedmessage.sequencenumber?view=azure-dotnet-preview#remarks) of the message. See [here](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sequencing) for more information.

### [Dispose](#Dispose)

Dispose all the resources.

### [Availability](#Availability)

This feature is available since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) | [Azure Service Bus: BrokerReceiverOptions SDT](https://wiki.genexus.com/commwiki/wiki?51943) | [Azure Service Bus: ConsumeMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51945) |
| [Azure Service Bus: ReceiveMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51952) | [Azure Service Bus: ScheduleMessageOptions SDT](https://wiki.genexus.com/commwiki/wiki?51950) | [AzureServiceBus.MessageBrokerProvider external object](https://wiki.genexus.com/commwiki/wiki?51784) | [AzureServiceBus.MessageBrokerProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55677) |
| [HowTo: Complete a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51980) | [HowTo: Connect to a Message Broker](https://wiki.genexus.com/commwiki/wiki?51972) | [HowTo: Defer a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51981) | [HowTo: Receive messages from a Message Broker](https://wiki.genexus.com/commwiki/wiki?51977) |
| [HowTo: Receive messages from a session-enabled Message Broker](https://wiki.genexus.com/commwiki/wiki?51984) | [HowTo: Schedule a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51982) | [HowTo: Send messages to a Message Broker](https://wiki.genexus.com/commwiki/wiki?51973) | [Message attributes for Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51791) |

---
