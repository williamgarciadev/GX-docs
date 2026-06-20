---
title: "Asynchronous messaging APIs"
source_id: 51735
source_url: https://wiki.genexus.com/commwiki/wiki?51735
genexus_version: "18"
---

# Asynchronous messaging APIs

One of the characteristics of modern applications (scalable, distributable, and robust applications) is the ability to communicate and control changes through asynchronous messages.

To achieve an asynchronous model, the solution is to use messaging services for communication between components and decoupling each one of them.

GeneXus meets this need through different APIs that provide access to solutions from different Message Queue providers.


* [Queue API](https://wiki.genexus.com/commwiki/wiki?51771)
  + Samples
    - [HowTo: Connect to a Queue](https://wiki.genexus.com/commwiki/wiki?51761)
    - [HowTo: Send a message to an Azure Storage Queue](https://wiki.genexus.com/commwiki/wiki?51781)
    - [HowTo: Send and receive messages from SQS](https://wiki.genexus.com/commwiki/wiki?51926)
  + External Objects & components
    - Azure Queue
      * [MessageQueueProvider](https://wiki.genexus.com/commwiki/wiki?51737)
    - Amazon SQS
      * [MessageQueueProvider](https://wiki.genexus.com/commwiki/wiki?51778)
      * [AWS SQS configuration requirements](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59001,,)
    - [MessageQueue](https://wiki.genexus.com/commwiki/wiki?51736)
      * SDTs
        + [Message](https://wiki.genexus.com/commwiki/wiki?51738)
        + [MessageOptions](https://wiki.genexus.com/commwiki/wiki?51743)
        + [MessageProperty](https://wiki.genexus.com/commwiki/wiki?51798)
        + [MessageResult](https://wiki.genexus.com/commwiki/wiki?51740)
    - [Queue API domains](https://wiki.genexus.com/commwiki/wiki?51928)
* [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782)
  + Samples (Azure Service Bus)
    - [Connect to a Message Broker](https://wiki.genexus.com/commwiki/wiki?51972)
    - [Send messages to a Message Broker](https://wiki.genexus.com/commwiki/wiki?51973)
    - [Receive messages from a Message Broker](https://wiki.genexus.com/commwiki/wiki?51977)
    - [Receive messages from a session enabled Message Broker](https://wiki.genexus.com/commwiki/wiki?51984)
    - [Schedule a message](https://wiki.genexus.com/commwiki/wiki?51982)
    - [Settling messages from a Message Broker](https://wiki.genexus.com/commwiki/wiki?51978)
      * [Completing a message](https://wiki.genexus.com/commwiki/wiki?51980)
      * [Deferring a message](https://wiki.genexus.com/commwiki/wiki?51981)
  + External Objects & components
    - Azure Service Bus
      * [MessageBrokerProvider](https://wiki.genexus.com/commwiki/wiki?51784)
      * [Message attributes for Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51791)
      * SDTs
        + [BrokerReceiverOptions](https://wiki.genexus.com/commwiki/wiki?51943)
          - Method options
            * [ConsumeMessageOptions](https://wiki.genexus.com/commwiki/wiki?51945)
            * [ScheduleMessageOptions](https://wiki.genexus.com/commwiki/wiki?51950)
            * [ReceiveMessageOptions](https://wiki.genexus.com/commwiki/wiki?51952)
    - [MessageBroker](https://wiki.genexus.com/commwiki/wiki?51786)
      * SDTs
        + [Message](https://wiki.genexus.com/commwiki/wiki?51789)
        + [MessageProperty](https://wiki.genexus.com/commwiki/wiki?51969)
* [Event Messaging API](https://wiki.genexus.com/commwiki/wiki?55334)
  + Samples
    - [Send Event using CloudEvents Schema](https://wiki.genexus.com/commwiki/wiki?55400)
    - [Send Events using EventGrid Schema](https://wiki.genexus.com/commwiki/wiki?55401)
  + [Azure Event Grid](https://wiki.genexus.com/commwiki/wiki?55354)
    - [Infrastructure setup](https://wiki.genexus.com/commwiki/wiki?55346)
  + External Objects & components
    - Azure Event Grid
      * [EventGridRouterProvider](https://wiki.genexus.com/commwiki/wiki?55341)
        + SDTs
          - [EventGridSchema](https://wiki.genexus.com/commwiki/wiki?55344)
    - [Event Router](https://wiki.genexus.com/commwiki/wiki?55337)
      * SDTs
        + [CloudEvent](https://wiki.genexus.com/commwiki/wiki?55339)

---
