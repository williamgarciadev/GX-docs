---
title: "Scripted Chatbots"
source_id: 45151
source_url: https://wiki.genexus.com/commwiki/wiki?45151
genexus_version: "18"
---

# Scripted Chatbots

A scripted chatbot is a "command-based" chat.

Scripted chatbots can be defined in scenarios where they can understand predefined commands.

In general, chatbots are associated with [AI](https://en.wikipedia.org/wiki/Artificial_intelligence) and [NLP](https://en.wikipedia.org/wiki/Natural_language_processing). But in fact, there are two main ways in which a chatbot can do its job:

* With machine learning.
* Without machine learning.

Chatbots that use machine learning can be trained to "understand" the user [Intent](https://wiki.genexus.com/commwiki/wiki?38949)s when they are expected to decipher natural speech and all its possible variations depending on the culture and localization.

On the other hand, in some scenarios where the conversation tends to be more "command-oriented," you do not need to add the complexity of an NLP solution. In these cases where scripted conversations are enough, and where the chatbot’s output is predetermined you don't need to use AI through an NLP provider.

The following image shows a scripted chatbot at runtime:

`[imagen omitida: wiki id 50331]`

### [How to create a scripted Chatbot in GeneXus](#How+to+create+a+scripted+Chatbot+in+GeneXus)

Just configure the [NLP Provider property](https://wiki.genexus.com/commwiki/wiki?38931) to the value None. The other considerations to create a chatbot are the same as for any Chatbot that may use NLP, taking into account that all the information of the chatbot (such as Trigger Messages and Context) isn't stored in an NLP Provider but managed by the [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102).

`[imagen omitida: wiki id 45153]`

Consider that:

* Each flow represents a question of the user.
* The Trigger Messages, unlike what happens with a machine-intelligent chatbot, are considered exactly as they are defined. You can define more than one Trigger Message for each Flow.
* Each conversation can follow a number of defined paths (entering through different flows). This is solved, as usual, using [Chatbot User Input Redirections](https://wiki.genexus.com/commwiki/wiki?39003) or Message redirections. As the user enters an input, that information is saved, so the state of the conversation is persisted.
* In the Response, only one text [Message](https://wiki.genexus.com/commwiki/wiki?39033) is considered (the first one), as there is no NLP to decide randomly what to answer.

After any change to the model, you can do "Generate Chatbot" and build.

You can download the sample here: [HowTo: Create a Scripted Chatbot](https://wiki.genexus.com/commwiki/wiki?45155).

### [Summary](#Summary)

Machine-intelligent chatbots can understand user intents the way people phrase them (with all the different variations they may have, such as culture, localization, or jargon).

Scripted chatbots are useful for those scenarios where it's enough to understand a set of predefined commands.

### [Availability](#Availability)

Since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,).

### [See Also](#See+Also)

[Scripted Chatbots : Generated objects](https://wiki.genexus.com/commwiki/wiki?45538,,)  
[Multi-Tenant Scripted Chatbots](https://wiki.genexus.com/commwiki/wiki?45526,,)  
[Dynamic Scripted Chatbot](https://wiki.genexus.com/commwiki/wiki?52873)

**Notes:**

Until [GeneXus 17 upgrade 2](https://wiki.genexus.com/commwiki/wiki?47418,,) there were the following restrictions:

* The input and output parameters of conversational objects must be strings (Varchar, LongVarchar, etc).
* Support to answer with components has not been implemented yet.
* Conversational objects can be procedures only.

Since [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/wiki?47659,,) the same Conversational Objects are generated as for NLP.


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [Custom Chatbot Definition property](https://wiki.genexus.com/commwiki/wiki?45528) | [Dynamic Scripted Chatbot](https://wiki.genexus.com/commwiki/wiki?52873) |
| [KB:eBanking Chatbot sample](https://wiki.genexus.com/commwiki/wiki?54220) | [KB:HowTo: Create a Scripted Chatbot](https://wiki.genexus.com/commwiki/wiki?45155) | [HowTo: Integrate Chatbots using WhatsApp](https://wiki.genexus.com/commwiki/wiki?44346) |
| [NLP Provider property](https://wiki.genexus.com/commwiki/wiki?38931) |

---
