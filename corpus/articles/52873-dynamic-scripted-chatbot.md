---
title: "Dynamic Scripted Chatbot"
source_id: 52873
source_url: https://wiki.genexus.com/commwiki/wiki?52873
genexus_version: "18"
---

# Dynamic Scripted Chatbot

Dynamic [Scripted Chatbots](https://wiki.genexus.com/commwiki/wiki?45151) allow editing their Flows, Trigger Messages, User inputs, etc. at runtime.

The possibility to add/edit Flows, Trigger Messages, User inputs, etc. at runtime provides dynamism.

To configure a Scripted chatbot as Dynamic, you have to set the following properties of the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) instance:

* [NLP Provider property](https://wiki.genexus.com/commwiki/wiki?38931) = None
* [Generate Dynamic Provider property](https://wiki.genexus.com/commwiki/wiki?51753) = True

Take into account that the definition of the Dynamic Scripted Chatbots will be stored in the application database. To this end, the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s will be created:

* ChatbotFlows
* ChatbotInstances
* ChatbotInstancesFlows

These Transactions will be created in the *CommonChatbots* module so that they are available in all the Chatbot development [Environments](https://wiki.genexus.com/commwiki/wiki?7115). In addition, the *hatbotLoadDefaultStructure* [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) will be created to perform the initial loading of the tables associated with these Transactions.

A group of [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s will also be generated to make it easier to edit the Chatbot records. In this way, you will be able to easily and quickly edit the chatbot without having to access the database records and edit them manually. These Web Panels will be distributed as long as the [Generate Dynamic Provider property](https://wiki.genexus.com/commwiki/wiki?51753) is set to True in at least one instance.

The Web Panels mentioned above are as follows:

* PanelChatbotFlows
* PanelChatbotInstances
* PanelChatBotInstancesFlows

To learn how to create a Dynamic Scripted Chatbot, read at: [HowTo: Create a Dynamic Scripted Chatbot](https://wiki.genexus.com/commwiki/wiki?52874)


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [HowTo: Create a Dynamic Scripted Chatbot](https://wiki.genexus.com/commwiki/wiki?52874) | [Scripted Chatbots](https://wiki.genexus.com/commwiki/wiki?45151) |
| [Total Experience with GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51570) |

---
