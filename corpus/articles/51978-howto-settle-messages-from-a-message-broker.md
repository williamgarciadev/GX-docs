---
title: "HowTo: Settle messages from a Message Broker"
source_id: 51978
source_url: https://wiki.genexus.com/commwiki/wiki?51978
genexus_version: "18"
---

# HowTo: Settle messages from a Message Broker

With the [Message Broker API](https://wiki.genexus.com/commwiki/wiki?51782), you can send, receive, and consume messages from a Message Broker.

After receiving a message, the consumer decides what to do with the message. If the processing was successful, the decision can be to delete the message from the queue. Otherwise, depending on other factors, the decision could be that the message has to go into the dead letter queue, defer the processing, etc.

Check [this](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-transfers-locks-settlement#settling-receive-operations) documentation about message settlement.

* [HowTo: Complete a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51980)
* [HowTo: Defer a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51981)

### [See Also](#See+Also)

[Message settlement with peek lock mode](https://medium.com/event-driven-utopia/azure-service-bus-essentials-message-settlement-with-peek-lock-mode-cc2e5917e92b)


|  |
| --- |
| **Backlinks** |
| [Toc:Asynchronous messaging APIs](https://wiki.genexus.com/commwiki/wiki?51735) |

---
