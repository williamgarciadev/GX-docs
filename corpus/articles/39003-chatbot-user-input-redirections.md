---
title: "Chatbot User Input Redirections"
source_id: 39003
source_url: https://wiki.genexus.com/commwiki/wiki?39003
genexus_version: "18"
---

# Chatbot User Input Redirections

These are redirections stated for the [User Input](https://wiki.genexus.com/commwiki/wiki?38959) of the [Flow of a Conversational instance](https://wiki.genexus.com/commwiki/wiki?38531).

To add a User Input Redirection, right-click on a Variable under the User input node and select Add - > Redirection from the menu.

`[imagen omitida: wiki id 43712]`

The Redirections are executed when the user enters data for the User input parameter. It is executed to the flow indicated under the [Redirect to Flow property](https://wiki.genexus.com/commwiki/wiki?39220) if the [Condition property](https://wiki.genexus.com/commwiki/wiki?43716) evaluates to TRUE.

If none of the User Input Redirection nodes conditions evaluates to TRUE, you can send feedback to the user through the [Chatbot Message](https://wiki.genexus.com/commwiki/wiki?39875) of the Flow.

`[imagen omitida: wiki id 43713]`

The conditions can be expressed using the [reference to a context variable](https://wiki.genexus.com/commwiki/wiki?38942) or the reference to an entity (using the @entity syntax).

### [Availability](#Availability)

Since [GeneXus 16 upgrade 5](https://wiki.genexus.com/commwiki/wiki?43446,,)

### [See also](#See+also)

* [HowTo: Build a chatbot using GeneXus](https://wiki.genexus.com/commwiki/wiki?37076)


|  |
| --- |
| **Backlinks** |
| [Chatbot Entity](https://wiki.genexus.com/commwiki/wiki?39083) | [Chatbot Flow: Get information about any formality](https://wiki.genexus.com/commwiki/wiki?39072) |
| [Chatbot User Input](https://wiki.genexus.com/commwiki/wiki?38959) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [Conversational Flows Editor](https://wiki.genexus.com/commwiki/wiki?45141) |
| [HowTo: Reference context parameters in a conversation](https://wiki.genexus.com/commwiki/wiki?38942) | [Redirect to Flow property](https://wiki.genexus.com/commwiki/wiki?39220) | [Scripted Chatbots](https://wiki.genexus.com/commwiki/wiki?45151) |
| [Trigger the flow of a dialog](https://wiki.genexus.com/commwiki/wiki?39082) | [User Input Redirections Condition property](https://wiki.genexus.com/commwiki/wiki?43716) |

---
