---
title: "HowTo: Build a chatbot using GeneXus"
source_id: 37076
source_url: https://wiki.genexus.com/commwiki/wiki?37076
genexus_version: "18"
---

# HowTo: Build a chatbot using GeneXus

The [Citizen Service Chatbot sample](https://wiki.genexus.com/commwiki/wiki?40937) contains an application (Web and Mobile) that offers information to residents and provides them with services related to the administrative formalities that can be carried out in the city they live in.

Instead of providing a solution where the user is presented with a menu with options for the user to choose from, in this solution the user tells directly what he or she needs in a conversational fashion.

How is this solution implemented using the [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102)?

### [Planning the chatbot system](#Planning+the+chatbot+system)

Planning the chatbot system requires outlining the dialog. The dialog may have several [Flows](https://wiki.genexus.com/commwiki/wiki?38531).

First, you have to plan the range of user questions and requests that will be within the scope of the system to answer. In this sense, you have to think of the verbs that will be used or requests that will be made by the user, and what you want the bot to respond automatically. These are called [intents](https://wiki.genexus.com/commwiki/wiki?38949).

The next step is outlining the different dialog Flows of the example.


|  |
| --- |
| **Backlinks** |
| [Chatbot Entity](https://wiki.genexus.com/commwiki/wiki?39083) | [Chatbot Intent](https://wiki.genexus.com/commwiki/wiki?38949) |
| [Chatbot User Input](https://wiki.genexus.com/commwiki/wiki?38959) | [Chatbot User Input Redirections](https://wiki.genexus.com/commwiki/wiki?39003) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [KB:Citizen Service Chatbot sample](https://wiki.genexus.com/commwiki/wiki?40937) |
| [Clean Context Value property](https://wiki.genexus.com/commwiki/wiki?39353) | [Category:Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) | [Conversational Object property](https://wiki.genexus.com/commwiki/wiki?38189) | [KB:eBanking Chatbot sample](https://wiki.genexus.com/commwiki/wiki?54220) |
| [Flow of a Conversational instance](https://wiki.genexus.com/commwiki/wiki?38531) | [Generate Dynamic Provider property](https://wiki.genexus.com/commwiki/wiki?51753) | [HowTo: Create a chatbot using a Dashboard](https://wiki.genexus.com/commwiki/wiki?46416) | [HowTo: Initialize entity values in the AI provider](https://wiki.genexus.com/commwiki/wiki?39302) |
| [HowTo: Integrate queries in a chatbot](https://wiki.genexus.com/commwiki/wiki?46415) | [HowTo: Reference context parameters in a conversation](https://wiki.genexus.com/commwiki/wiki?38942) | [HowTo: Send a message to the chatbot from a menu](https://wiki.genexus.com/commwiki/wiki?40912) |
| [Messages property](https://wiki.genexus.com/commwiki/wiki?39033) | [Trigger Messages property](https://wiki.genexus.com/commwiki/wiki?39067) | [Trigger the flow of a dialog](https://wiki.genexus.com/commwiki/wiki?39082) |

---
