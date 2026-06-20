---
title: "HowTo: Get the User ID when using chatbots and WhatsApp channel"
source_id: 45850
source_url: https://wiki.genexus.com/commwiki/wiki?45850
genexus_version: "18"
---

# HowTo: Get the User ID when using chatbots and WhatsApp channel

When the [chatbot is exposed through WhatsApp](https://wiki.genexus.com/commwiki/wiki?44346), the user's ID (who receives the message) is retrieved in the [webhook](https://wiki.genexus.com/commwiki/wiki?44346). Due to the architecture (the webhook is a service - a procedure with [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) = HTTP), that information has to be persisted in a place where it can be retrieved afterwards from any other piece of code.

Therefore, the information is persisted in the [context](https://wiki.genexus.com/commwiki/wiki?39351) so that it can be used elsewhere.

### [Where in the code is the User ID persisted?](#Where+in+the+code+is+the+User+ID+persisted%3F)

The User ID is saved in the context in a procedure called *SendMessageFromChannel* which is called by the WhatsappWebhook object.

If the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) has the [Enable WhatsApp property](https://wiki.genexus.com/commwiki/wiki?45163) set to TRUE, and the WhatsApp partner data is also configured (i.e.: [Twilio Token property](https://wiki.genexus.com/commwiki/wiki?45166)), the WhatsappWebhook is automatically generated.  
In this webhook, the *SendMessageFromChannel* procedure is called (located in the CommonChatbots module) and it is in charge of saving the message, calling the chatbot, and saving the response.

`[imagen omitida: wiki id 45856]`

There, in the *SendMessageFromChannel* procedure, the User ID is retrieved using the *GetUserIdByDevice* procedure. It receives the user message recipient as a parameter, and returns a User GUID which is saved in the context for that user:

`[imagen omitida: wiki id 45857]`

### [How to use that information](#How+to+use+that+information)

Although it is saved in the AnalyzeResponse object, to retrieve it from any other piece of code, it has to be done using a variable of Context type where Context is an SDT under a module with the name <InstanceName>Chatbot. For example, if the Instance name is "Citizen," the Context SDT is under CitizenChatbot module.

You can use the Context where it is instantiated. For example, a procedure where the context can be instantiated (because it is automatically received as a parameter) is the [Validation Procedure](https://wiki.genexus.com/commwiki/wiki?42594) of any user input.

The following can be used to get the user's GUID:

```
&UserIdContext = &Context.Context.GXUserId
```

### [Availability](#Availability)

Since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |

---
