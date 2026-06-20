---
title: "AzureServiceBus.MessageBrokerProvider external object (GeneXus 18 Upgrade 5)"
source_id: 55677
source_url: https://wiki.genexus.com/commwiki/wiki?55677
genexus_version: "18"
---

# AzureServiceBus.MessageBrokerProvider external object (GeneXus 18 Upgrade 5)

The *MessageBrokerProvider* external object under the AzureServiceBus module is used to establish a connection to a [Service Bus](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview) (Queue or Topic) using the [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782).

`[imagen omitida: wiki id 51942]`

## [Properties](#Properties)

It doesn't have any.

## [Methods](#Methods)

### [Connect](#Connect)

A static method that allows instantiating a MessageBroker using dynamic data. The method returns a MessageBroker to be used to send and receive messages from the Service Bus.

**Return value** [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786)  
**Parameters** queueName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), connectionString:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), sessionEnabled:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374), receiverOptions: [BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943), senderIdentifier:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), errorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

sessionEnabled : True if it's a [session-enabled](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions) Service Bus queue.  
senderIdentifier: Sets the ID for send operations. This can be used to correlate logs and exceptions.  
[BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943) is considered only for non-session enabled queues.

### [Connect](#Connect)

**Return value** [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786)  
**Parameters** topicName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), subscriptionName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), connectionString:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), sessionEnabled:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374), receiverOptions: [BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943), senderIdentifier:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), errorMessages:[GeneXus.Common.Messages](https://wiki.genexus.com/commwiki/wiki?40335), success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

sessionEnabled : True if it's a [session-enabled](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions) Service Bus queue.  
senderIdentifier: Sets the ID for send operations. This can be used to correlate logs and exceptions.  
[BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943) is considered only for non-session enabled queues.

### [Connect](#Connect)

**Return value** [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786)  
**Parameters** queue:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), connectionString:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), errorMessages:[Messages](https://wiki.genexus.com/commwiki/wiki?40335), success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

### [Connect](#Connect)

**Return value** [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786)  
**Parameters** topicName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), subscriptionName:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), connectionString:[VarChar](https://wiki.genexus.com/commwiki/wiki?6778), errorMessages:[Messages](https://wiki.genexus.com/commwiki/wiki?40335), success:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

## [Events](#Events)

It doesn't have any.

## [Availability](#Availability)

This feature is available since [GeneXus 18 upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081).

## [See Also](#See+Also)

[Azure Service Bus](https://www.serverless360.com/azure-service-bus).
