---
title: "Messages structured data type"
source_id: 40335
source_url: https://wiki.genexus.com/commwiki/wiki?40335
genexus_version: "18"
---

# Messages structured data type

This [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) is automatically provided by GeneXus when a new [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is created. It contains a collection of messages, each of them with an identifier, a type, and a description. This collection is meant to allow access to the messages issued during the execution.

### [Members](#Members)

* **Message**: Collection

  + **Id**: Character(128)  
    A message identifier.
  + **Error**: MessageType  
    An error type.
  + **Description**: Character(256)  
    A description of the message.

### [Considerations](#Considerations)

* As a best-practice, you can use this [SDT](https://wiki.genexus.com/commwiki/wiki?2427) for triggering and handling errors, even for debugging.
* For the GeneXus standard messages, the "Id" is ever in English, no matter the model configured language.
* Procedures with a &Messages out parm rule called from Smart Device object will behave automatically as follows:  
  - If the &Messages have an item with Type filed of MessageType.Error, it will display a msg() (or alert).  
  - If the &Messages have an item with Type field of Message.Warning or Message.Info, it will display a msg(,nowait) (or toast message).

### [MessageType domain](#MessageType+domain)

Enumerated domain with the following values:

|  |  |
| --- | --- |
| **Error** | An error message. |
| **Warning** | A warning message. |
| **Info** | An informational message. |
| **Debug** | A debug message. |

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | Web (Java,.NET,.NET Framework), Native Mobile (Android,iOS) |

### [Availability](#Availability)

This Structured Data Type is available as of [GeneXus X Evolution 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?9256,,).

* It is part of [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) as of [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?28265,,).

### [See Also](#See+Also)

[Business Component GetMessages method](https://wiki.genexus.com/commwiki/wiki?23475)  
[Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687)


|  |
| --- |
| **Backlinks** |
| [AWSQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51778) | [AzureEventGrid.EventGridRouterProvider external object](https://wiki.genexus.com/commwiki/wiki?55341) | [AzureQueue.MessageQueueProvider external object](https://wiki.genexus.com/commwiki/wiki?51737) |
| [AzureQueue.MessageQueueProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55673) | [AzureServiceBus.MessageBrokerProvider external object](https://wiki.genexus.com/commwiki/wiki?51784) | [AzureServiceBus.MessageBrokerProvider external object (GeneXus 18 Upgrade 5)](https://wiki.genexus.com/commwiki/wiki?55677) | [Business Component GetMessages method](https://wiki.genexus.com/commwiki/wiki?23475) |
| [Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279) | [EventRouter external object](https://wiki.genexus.com/commwiki/wiki?55337) | [GeneXus Cognitive API - Analyze procedure](https://wiki.genexus.com/commwiki/wiki?41041) |
| [GeneXus Cognitive API - Check procedure](https://wiki.genexus.com/commwiki/wiki?44242) | [GeneXus Cognitive API - Classify procedure](https://wiki.genexus.com/commwiki/wiki?40171) | [GeneXus Cognitive API - Delete procedure](https://wiki.genexus.com/commwiki/wiki?44243) | [GeneXus Cognitive API - Deploy procedure](https://wiki.genexus.com/commwiki/wiki?44247) |
| [GeneXus Cognitive API - DetectFaces procedure](https://wiki.genexus.com/commwiki/wiki?40177) | [GeneXus Cognitive API - DetectLanguage procedure](https://wiki.genexus.com/commwiki/wiki?40181) | [GeneXus Cognitive API - DetectObjects procedure](https://wiki.genexus.com/commwiki/wiki?40178) | [GeneXus Cognitive API - DetectScene procedure](https://wiki.genexus.com/commwiki/wiki?40179) |
| [GeneXus Cognitive API - Error handling and codes](https://wiki.genexus.com/commwiki/wiki?40188) | [GeneXus Cognitive API - Evaluate procedure](https://wiki.genexus.com/commwiki/wiki?44244) | [GeneXus Cognitive API - ExtractEntities procedure](https://wiki.genexus.com/commwiki/wiki?40182) | [GeneXus Cognitive API - KeyPhrases procedure](https://wiki.genexus.com/commwiki/wiki?40183) |
| [GeneXus Cognitive API - OCR procedure](https://wiki.genexus.com/commwiki/wiki?40180) | [GeneXus Cognitive API - Predict procedure](https://wiki.genexus.com/commwiki/wiki?44245) | [GeneXus Cognitive API - Process procedure](https://wiki.genexus.com/commwiki/wiki?41042) | [GeneXus Cognitive API - SentimentAnalysis procedure](https://wiki.genexus.com/commwiki/wiki?40184) |
| [GeneXus Cognitive API - Train procedure](https://wiki.genexus.com/commwiki/wiki?44246) | [GeneXus Cognitive API - Translate procedure](https://wiki.genexus.com/commwiki/wiki?40185) | [HowTo: Complete a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51980) | [HowTo: Connect to a Message Broker](https://wiki.genexus.com/commwiki/wiki?51972) |
| [HowTo: Defer a message in Azure Service Bus](https://wiki.genexus.com/commwiki/wiki?51981) | [HowTo: Receive messages from a Message Broker](https://wiki.genexus.com/commwiki/wiki?51977) | [HowTo: Send messages to a Message Broker](https://wiki.genexus.com/commwiki/wiki?51973) | [MessageBroker external object](https://wiki.genexus.com/commwiki/wiki?51786) |
| [Queue API MessageQueue external object](https://wiki.genexus.com/commwiki/wiki?51736) | [SpeechToText procedure](https://wiki.genexus.com/commwiki/wiki?40169) | [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087) | [TextToSpeech procedure](https://wiki.genexus.com/commwiki/wiki?40170) |

---
