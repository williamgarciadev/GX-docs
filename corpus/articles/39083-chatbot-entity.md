---
title: "Chatbot Entity"
source_id: 39083
source_url: https://wiki.genexus.com/commwiki/wiki?39083
genexus_version: "18"
---

# Chatbot Entity

When the user's input is received, the [AI](https://en.wikipedia.org/wiki/Artificial_intelligence) service identifies both the [intents](https://wiki.genexus.com/commwiki/wiki?38949) and entities.

For example, an **intent** can be “*Get information.*” The **entities**, in this case, would be the topic you need information about. See the example shown in [HowTo: Build a chatbot using GeneXus](https://wiki.genexus.com/commwiki/wiki?37076):

* @Activities information
* @Administrative process information

So, the dialog will be defined in such a way that intents and entities are combined to help the [AI](https://en.wikipedia.org/wiki/Artificial_intelligence) service choose the correct response. In addition, an entity definition includes a set of entity *values* that can be used to trigger different responses.

For example, @Activities information entity may have the values:

* Art
* Culture
* Nature

Besides, each entity value can have multiple *synonyms*that define different ways in which the same value might be specified in user input.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Art** | Design | Painting | Music | Dance | Theatre |
| **Culture** | History | Literature | museum |  |  |
| **Nature** | Sports | Outdoors | Beach | Park | square |

The entity is created automatically upon some information that is configured in the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113):

* When the entity is referenced using the @ prefix. For example, in the [Trigger Messages property](https://wiki.genexus.com/commwiki/wiki?39067) or in [Chatbot User Input Redirections](https://wiki.genexus.com/commwiki/wiki?39003).
* When a [User Input](https://wiki.genexus.com/commwiki/wiki?38959) has [Match With Entity property](https://wiki.genexus.com/commwiki/wiki?39295) set.

To add values to the entities, see [HowTo: Initialize entity values in the AI provider](https://wiki.genexus.com/commwiki/wiki?39302).


|  |
| --- |
| **Backlinks** |
| [Chatbot Flow: Get information about any formality](https://wiki.genexus.com/commwiki/wiki?39072) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [KB:Chatbots workshop](https://wiki.genexus.com/commwiki/wiki?44641) |
| [Configuring Google Dialogflow for the Chatbot Generator](https://wiki.genexus.com/commwiki/wiki?39749) | [Entity property](https://wiki.genexus.com/commwiki/wiki?39300) | [HowTo: Initialize entity values in the AI provider](https://wiki.genexus.com/commwiki/wiki?39302) |
| [Match With Entity property](https://wiki.genexus.com/commwiki/wiki?39295) | [Trigger Messages property](https://wiki.genexus.com/commwiki/wiki?39067) | [Trigger the flow of a dialog](https://wiki.genexus.com/commwiki/wiki?39082) | [User Input Redirections Condition property](https://wiki.genexus.com/commwiki/wiki?43716) |
|

---
