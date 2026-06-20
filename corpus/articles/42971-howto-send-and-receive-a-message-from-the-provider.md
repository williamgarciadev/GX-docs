---
title: "HowTo: Send and receive a message from the Provider"
source_id: 42971
source_url: https://wiki.genexus.com/commwiki/wiki?42971
genexus_version: "18"
---

# HowTo: Send and receive a message from the Provider

The Message API allows sending and receiving a message from the Provider (keeping track of the context, and triggering the execution of the flow).  
In addition, there's a method that allows analyzing the expression and getting the response of the Provider for that expression.

These are methods of the [Chatbot Module](https://wiki.genexus.com/commwiki/wiki?37102).

### [Analyzing a message](#Analyzing+a+message)

To evaluate an expression in the Provider, the *Chatbot.Message.Analyze* method is used.

Its signature is as follows:

```
parm(in:&Instance, in:&UserMessage, inout:&AnalyzeResponse, out:&Messages)
```

**Where:**

*&Instance*  
      Is the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) name

*&UserMessage*  
      Is varchar(256) and represents the user's message.

*&AnalyzeResponse*  
      Is an [SDT](https://wiki.genexus.com/commwiki/wiki?2427), which represents the Provider's response.  
      Note that this is an inout parameter. It means that it can receive a previous response (which includes the conversation [context](https://wiki.genexus.com/commwiki/wiki?39351)), in order to be evaluated by the Provider along with the user's message. For more information, see below in this document.

*&Messages*  
      Is an out parameter of Messages data type where you can get the errors thrown by the Provider.

### [Sample](#Sample)

```
&Instance = !"Citizen"
&UserMessage = !"Hello"
Chatbot.Message.Analyze(&Instance, &UserMessage, &AnalyzeResponse, &Messages)
&BotResponse  = &AnalyzeResponse.GXOutputCollection.toJson() (2)
&Intent       = &AnalyzeResponse.Intents.Item(1).Intent
&Confidence   = &AnalyzeResponse.Intents.Item(1).Confidence
```

### [Sending a message and triggering the execution of the flow](#Sending+a+message+and+triggering+the+execution+of+the+flow)

The purpose of this method is to analyze the expression (the user's message) and, additionally, execute the business logic defined for that [Flow](https://wiki.genexus.com/commwiki/wiki?38531). That is, do the [redirections](https://wiki.genexus.com/commwiki/wiki?39220)(1) defined for the flow, execute the [user input validations](https://wiki.genexus.com/commwiki/wiki?42594), and the [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189).

Its signature is as follows:

```
parm(in:&Instance, in:&UserMessage, in:&Image, inout:&AnalyzeResponse, out:&Messages)
```

**Where:**

*&Instance*  
      Is the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113)'s name

*&UserMessage*  
      Is varchar(256) and represents the user's message

*&Image*  
      Is of Image data type

*&AnalyzeResponse*  
      Is an SDT, which represents the Provider's response.

*&Messages*  
      Is an out parameter of Messages data type where you can get the errors thrown by the Provider.

#### [Samples](#Samples)

1. The PanelChatWeb and PanelChatSD objects, which are [resources](https://wiki.genexus.com/commwiki/wiki?37102) of the Chatbot Generator, are examples that call (indirectly) the *Chatbot.Message.SendMessage* method. They invoke the CommonChatbots.SendMessage Procedure, which calls the *Chatbot.Message.SendMessage*.

2. Another interesting use of this API is to build a test case of your chatbot. You can program, in batch mode, the dialog to the Provider and check the responses. The [Chatbot Context](https://wiki.genexus.com/commwiki/wiki?39351) will be kept on track as the &AnalyzeResponse parameter which contains the context (among other information) is inout.

```
&Instance = !"Citizen"

&UserMessage = !"Hi"
do "ProcessMessageSend"
&UserMessage = !"I'd like to make a complaint"
do "ProcessMessageSend"
&UserMessage = !"About traffic"
do "ProcessMessageSend"
&UserMessage = !"There's a car parked in front of a garage"
do "ProcessMessageSend"

Sub "ProcessMessageSend"  
    msg(format(!"User: %1",&UserMessage), status)
   Chatbot.Message.SendMessage(&Instance,&UserMessage,&Image,&AnalyzeResponse,&Messages)
    msg(format(!"Bot: %1", &AnalyzeResponse.GXOutput), status)
   
    if &Messages.Count > 0
        msg(format(!"%1 (%2)",&Messages.Item(1).Description,&Messages.Item(1).Id), status)
    endif
EndSub
```

The output of running this test procedure would be as follows:

**User**: *Hi*  
**Bot**:   Hello! I'm your Citizen Assistant!  
**User**: *I'd like to make a complaint*  
**Bot**:   What's the topic of your complaint? It can be about Lighting, Traffic, or Green Spaces  
**User**: *About traffic*  
**Bot**: Please describe the problem   
**User**: *There's a car parked in front of a garage*  
**Bot**: Thanks for your feedback. Your claim is 655.

### [Analyze Response structure](#Analyze+Response+structure)

`[imagen omitida: wiki id 43205]`

**Context:** Substructure that contains the definition of the standard parameters for the context.  
**Custom Context**: Key-Value collection, which represents the specific parameters of the model of your chatbot.  
**GXOutput:** Represents the last of the response messages.  
**Intents:** Collection containing the detected intent and its confidence.  
**GXOutputCollection:** The collection of response messages from the chatbot for your query.

**Notes:**

**(1)** Depending on the case, if the redirections are server side, it is necessary to use the SendMessage method (case of DialogFlow); if the redirections are provider side (case of Watson), the Analyze method can be used to execute the redirections.

**(2)** GXOutputCollection is useful when it comes with multiple answers. GXOutput has the last message, but in the case of redirection, for example, the bot has two answers and GXOutputCollection has both.

### [Availability](#Availability)

Since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,)


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [HowTo: Send a message to the chatbot from a menu](https://wiki.genexus.com/commwiki/wiki?40912) |

---
