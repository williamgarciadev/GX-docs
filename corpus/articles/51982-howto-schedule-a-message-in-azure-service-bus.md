---
title: "HowTo: Schedule a message in Azure Service Bus"
source_id: 51982
source_url: https://wiki.genexus.com/commwiki/wiki?51982
genexus_version: "18"
---

# HowTo: Schedule a message in Azure Service Bus

This article contains an example that shows how to schedule a message in Azure Service Bus.

### [Steps](#Steps)

The code consists of the following:

**1.** Connect to the Azure Service Bus using the [AzureServiceBus.MessageBrokerProvider external object](https://wiki.genexus.com/commwiki/wiki?51784).  
**2.** The [Connect method](https://wiki.genexus.com/commwiki/wiki?51784) returns a [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786) that should be used to schedule the message.

**3.** Use the [ScheduleMessage](https://wiki.genexus.com/commwiki/wiki?51786) method, passing to it [ScheduleMessageOptions](https://wiki.genexus.com/commwiki/wiki?51950). The method returns the message [SequenceNumber](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.servicebus.servicebusreceivedmessage.sequencenumber?view=azure-dotnet-preview#remarks), to be able to cancel it later.

### [Connecting to Azure Service Bus Queue](#Connecting+to+Azure+Service+Bus+Queue)

The following code is the one used to connect to an Azure Service Bus Queue:

```
&MessageBroker = AzureServiceBus.MessageBrokerProvider.Connect(&queueName,&queueConnection,&errorMessages,&isOK)
```

### [Send a message to be scheduled](#Send+a+message+to+be+scheduled)

The following code is the one used for sending a message to be scheduled:

```
&Message = new()
&Message.MessageId = GUID.NewGuid().ToString()
&Message.MessageBody = !"message body"

&MessageProperty = new()
&MessageProperty.PropertyKey = !"propKey1"
&MessageProperty.PropertyValue = !"propValue1"
&Message.MessageAttributes.Add(&MessageProperty)

&MessageProperty = new()
&MessageProperty.PropertyKey = !"propKey2"
&MessageProperty.PropertyValue = !"propValue2"
&Message.MessageAttributes.Add(&MessageProperty)

//Broker Properties 

&MessageProperty = new()
&MessageProperty.PropertyKey = !"subject"
&MessageProperty.PropertyValue = !"Subject of message"
&Message.MessageAttributes.Add(&MessageProperty)

//SEND

&datetime = Datetime.Now() 
&ScheduleMessageOptions.ScheduledEnqueueTime = &datetime.AddMinutes(60)

&sequenceNumber = &MessageBroker.ScheduleMessage(&Message,&ScheduleMessageOptions.ToJson(),&errorMessages)

if &sequenceNumber = 0
    for &errorMessage in &errorMessages
        msg(format(!"%1 (%2)",&errorMessage.Description, &errorMessage.Id), status)
    endfor
else 
    msg(!"sequenceNumber scheduled:" + &sequenceNumber, status)
endif
```

### [Canceling the schedule](#Canceling+the+schedule)

To cancel the schedule, use:

```
&isOK= &MessageBroker.CancelSchedule(&sequenceNumber,&errorMessages)
//Process &errorMessages 
&MessageBroker.Dispose()
```

### [Variables defined in the samples](#Variables+defined+in+the+samples)

|  |  |
| --- | --- |
|  |  |
| *&MessageBroker* | [MessageBroker](https://wiki.genexus.com/commwiki/wiki?51786), GeneXusMessagingMessageBroker |
| *&ScheduleMessageOptions* | [ScheduleMessageOptions](https://wiki.genexus.com/commwiki/wiki?51950) |
| *&Message* | [Message](https://wiki.genexus.com/commwiki/wiki?51789) |
| *&MessageProperty* | [MessageProperty](https://wiki.genexus.com/commwiki/wiki?51969) |
| *&sequenceNumber* | Numeric(18) |

###


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) |

---
