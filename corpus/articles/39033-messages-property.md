---
title: "Messages property"
source_id: 39033
source_url: https://wiki.genexus.com/commwiki/wiki?39033
genexus_version: "18"
---

# Messages property

Specifies the response messages for this flow. You can type multiple messages using the ‘;’ delimiter, and reference any context parameter using the '&' character.

### [Scope](#Scope)

**Objects:** [Conversational Flows Instance](https://wiki.genexus.com/commwiki/wiki?37113)

### [Description](#Description)

Through the Messages property of a [Message node](https://wiki.genexus.com/commwiki/wiki?39875) - under the [Response](https://wiki.genexus.com/commwiki/wiki?39781) of a [Flow of a Conversational instance](https://wiki.genexus.com/commwiki/wiki?38531), you can specify a text response to the end user, after the Flow finishes its execution.

If you specify more than one text message at the Messages property, the provider sends any of them in a ramdom way. However, if the response is a redirection (i.e: [Action property](https://wiki.genexus.com/commwiki/wiki?39029,,) is set to "Redirect To", the first message is the one to be sent to the user always).

In order to specify [context](https://wiki.genexus.com/commwiki/wiki?39351) parameters into the Messages, see [HowTo: Reference context parameters in a conversation](https://wiki.genexus.com/commwiki/wiki?38942).

### [Samples](#Samples)

In the next example, the Greetings [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) has a Message node under the Response, which Messages property includes a text message greeting the end user.

The &Greeting variable is returned by the [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189) of the Flow.

`[imagen omitida: wiki id 39779]`

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [See Also](#See+Also)

* [HowTo: Build a chatbot using GeneXus](https://wiki.genexus.com/commwiki/wiki?37076)
* [Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520)


|  |
| --- |
| **Backlinks** |
| [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [HowTo: Reference context parameters in a conversation](https://wiki.genexus.com/commwiki/wiki?38942) | [Scripted Chatbots](https://wiki.genexus.com/commwiki/wiki?45151) | [Starting the conversation with the chatbot](https://wiki.genexus.com/commwiki/wiki?39076) | [Trigger Messages property](https://wiki.genexus.com/commwiki/wiki?39067) |

---
