---
title: "Synchronize Chatbot menu option"
source_id: 40243
source_url: https://wiki.genexus.com/commwiki/wiki?40243
genexus_version: "18"
---

# Synchronize Chatbot menu option

When you save the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113), the dialog is synchronized to the [AI](https://en.wikipedia.org/wiki/Artificial_intelligence) Provider. That is, a JSON object is created including the necessary changes, and it's sent to the Provider to update the conversational model.

Addittionally, (when [Merge Triggers property](https://wiki.genexus.com/commwiki/wiki?46434) = TRUE), the data in the Provider (the training messages), are merged with the trigger messages of the instance, so the instance is kept up to date in relation to the Provider's information.

Note that there is a [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) which allows forcing the synchronization although the instance hasn't got pending changes to save.

`[imagen omitida: wiki id 40244]`

When you synchronize (as well as when you save the instance), the GXCF\_Chatbots.config (it was called GXCF\_<Conversational Flows instance name>Chatbot.config prior to GeneXus 16 upgrade 7) file is updated (which contains the necessary information to connect to the AI Provider).

### [See also](#See+also)

[Force Chatbot Generation menu option](https://wiki.genexus.com/commwiki/wiki?40241)


|  |
| --- |
| **Backlinks** |
| [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102) | [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [Force Chatbot Generation menu option](https://wiki.genexus.com/commwiki/wiki?40241) | [Synchronize Chatbot menu option](https://wiki.genexus.com/commwiki/wiki?40243) |

---
