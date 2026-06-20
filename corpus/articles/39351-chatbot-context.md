---
title: "Chatbot Context"
source_id: 39351
source_url: https://wiki.genexus.com/commwiki/wiki?39351
genexus_version: "18"
---

# Chatbot Context

As in any human conversation, where two or more people talk, there is a context known to all participants. They know what they are talking about, and the information they have already exchanged. This is crucial for good communication.

The same happens with a [Chatbot](https://wiki.genexus.com/commwiki/wiki?38520).

In many cases, the information that the user exchanges with the chatbot should be stored in a space called "context" so that the chatbot doesn't need to ask for the same information again, repeatedly.

So, the context is the state information for the conversation.

In the [conversation process](https://wiki.genexus.com/commwiki/wiki?38522), the context is always included in each (JSON) response.

### [What are the predefined context parameters (variables) in the conversation?](#What+are+the+predefined+context+parameters+%28variables%29+in+the+conversation%3F)

The following are predefined context parameters added to the conversation:

1. **&GXUserInput** is a standard variable used to reproduce the user input. It keeps the last user input, and can also be used as a parameter of a Conversational Object of any Flow (it hasn't to be the same Flow where the user was prompted to enter that user input).
2. The [input parameters](https://wiki.genexus.com/commwiki/wiki?38959) of each of the [Flows](https://wiki.genexus.com/commwiki/wiki?38531). For example, in a chatbot where the following Flows have been defined, some context parameters will be: &UserIdentification, &ComplaintDescription, &ComplaintAddress, &informationType.  
     
   `[imagen omitida: wiki id 38960]`  
     
   In this case, the context can be cleared, using the [Clean Context Value property](https://wiki.genexus.com/commwiki/wiki?39353) of the [User inputs](https://wiki.genexus.com/commwiki/wiki?38959).
3. The output parameters of the [conversational object](https://wiki.genexus.com/commwiki/wiki?38189) of the flow.

### [Custom context information](#Custom+context+information)

Custom context information can be defined and queried, using the [Context API](https://wiki.genexus.com/commwiki/wiki?41364)

### [See Also](#See+Also)

[HowTo: Reference context parameters in a conversation](https://wiki.genexus.com/commwiki/wiki?38942)  
[HowTo: Manage the Context of the conversation through the Chatbot API](https://wiki.genexus.com/commwiki/wiki?41364)


|  |
| --- |
| **Backlinks** |
| [Chatbot Flow: Get information about any formality](https://wiki.genexus.com/commwiki/wiki?39072) | [Chatbot Messages Condition property](https://wiki.genexus.com/commwiki/wiki?39491) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [KB:Chatbots workshop](https://wiki.genexus.com/commwiki/wiki?44641) | [Clean Context Value property](https://wiki.genexus.com/commwiki/wiki?39353) | [KB:HowTo : Create a chatbot with human fallback](https://wiki.genexus.com/commwiki/wiki?46255) | [HowTo: Get the User ID when using chatbots and WhatsApp channel](https://wiki.genexus.com/commwiki/wiki?45850) |
| [HowTo: Manage the Context of the conversation through the Chatbot API](https://wiki.genexus.com/commwiki/wiki?41364) | [HowTo: Reference context parameters in a conversation](https://wiki.genexus.com/commwiki/wiki?38942) | [HowTo: Send and receive a message from the Provider](https://wiki.genexus.com/commwiki/wiki?42971) | [Messages property](https://wiki.genexus.com/commwiki/wiki?39033) |
| [Required Condition property](https://wiki.genexus.com/commwiki/wiki?43693) | [Required property](https://wiki.genexus.com/commwiki/wiki?43692) | [User Input Redirections Condition property](https://wiki.genexus.com/commwiki/wiki?43716) | [Validation Procedure property](https://wiki.genexus.com/commwiki/wiki?42594) |

---
