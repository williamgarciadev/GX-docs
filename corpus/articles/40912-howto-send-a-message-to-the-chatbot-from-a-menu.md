---
title: "HowTo: Send a message to the chatbot from a menu"
source_id: 40912
source_url: https://wiki.genexus.com/commwiki/wiki?40912
genexus_version: "18"
---

# HowTo: Send a message to the chatbot from a menu

This document explains how to send a message to the [Chatbot](https://wiki.genexus.com/commwiki/wiki?38520) from any user event (such as a menu item).

Its purpose is to show the user a Web or SD panel where he/she is presented with many options to choose from, and after selecting any of them, the Chatbot is notified so it can answer according to the inquiry made by the user.

### [Sample](#Sample)

Consider that when the user or the Chatbot greets, the first action of the Chatbot is to tell the user what he can talk about; take a look at the figure below:

`[imagen omitida: wiki id 40913]`

Note that the user selects an action from an action list, and the Chatbot repeats the user's intention, so it's clear what the [intent](https://wiki.genexus.com/commwiki/wiki?38949) to be processed is: "*Make an inquiry*."

Afterwards, the Chatbot answers the user after the message has been processed by the [NLP](https://en.wikipedia.org/wiki/Natural_language_processing) provider.

### [How to implement it](#How+to+implement+it)

#### [Defining the Flows of the conversation](#Defining+the+Flows+of+the+conversation)

In this example, the "Greetings" [Flow](https://wiki.genexus.com/commwiki/wiki?38531) looks as follows:

`[imagen omitida: wiki id 40914]`

Note that the [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189) set for the Flow is the "Greetings" object, which in this case is a Web Panel (it could be an SD Panel).

Depending on the selection made by the user, one of the following Flows show be triggered:

* Make a Claim Flow
* Get Information Flow
* Set a date and time Flow

So, the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) looks like the following picture:

`[imagen omitida: wiki id 40916]`

To trigger any of these Flows, a valid message has to be sent to the NLP Provider, so the intent is correctly identified.

Look at the [Trigger Messages property](https://wiki.genexus.com/commwiki/wiki?39067) of each Flow, to know which messages should be used to trigger the intent.

The "Greetings" Web panel form is as follows:

`[imagen omitida: wiki id 40915]`

#### [Defining the UI objects of the Flow](#Defining+the+UI+objects+of+the+Flow)

The code of the Conversational Object panel ("Greetings Web Panel") is as shown below:

```
Event Start
    GreetingsProcedure(&greeting)
    GreetingLbl.Caption = format(!"%1 I'm here to assist you. This is what I can help you with. Let's start!",&greeting)
Endevent

Event 'Get Information' //On click event for "Make an inquiry" button.
    GlobalEvents.BotEvent(!"Make an inquiry")
Endevent

Event 'Schedule an activity' //On click event for "Set a date and time" button
    GlobalEvents.BotEvent(!"Set a date and time")
Endevent

Event 'Do a claim' //On click event for "Do a claim" button
    GlobalEvents.BotEvent(!"Do a claim")
Endevent
```

First, in the "Start Event," a procedure that takes part of the greeting message is called, depending on the time of the day.

Then, each button has an associated event, which notifies the Chatbot that there is a new message. The message that you will use to trigger the Flow has to be a valid [Trigger Message](https://wiki.genexus.com/commwiki/wiki?39067) for that Flow, as previously explained.

When the event is executed, the Chatbot services are triggered, and a response is sent to the user as if the user had entered his query typing the message in the message box of the Chatbot.

This is because you are using the [Global Events](https://wiki.genexus.com/commwiki/wiki?31164) functionality.

#### [How does this work behind the scenes?](#How+does+this+work+behind+the+scenes%3F)

The *GlobalEvents.BotEvent* event is defined in the objects "PanelChatWeb" and "PanelChatSD" [generated](https://wiki.genexus.com/commwiki/wiki?37102). As in the example, you are using these objects, the corresponding *GlobalEvents.BotEvent* is triggered, which receives the message, and sends it to the NLP provider.

```
Event GlobalEvents.BotEvent(&Send)
    Do 'SendMessage'
Endevent

Sub 'SendMessage' //Send Message
    &WebClient = &WebNotification.ClientId
    &NotificationInfo = new()
    &PreviousContext = GetChatMeta(&UserId, &Instance)    
    NewMessage(&UserId, ChatbotMessageTypes.User, &Send, "", &PreviousContext, "", &WebClient, &Instance)
    GridSent.Refresh()    
    CommonChatbots.SendMessage.Submit("", &Instance, ChatbotPlatform.Web, &Send, "", &PreviousContext, &WebClient)
    Do 'NotifyOtherClients'
    &Send.SetEmpty()
endsub
```

The CommonChatbots.SendMessage procedure calls the [SendMessage](https://wiki.genexus.com/commwiki/wiki?42971) method.

**Note**: You don't have to program these events, because they are already defined in the objects PanelChatWeb and PanelChatSD generated.

### [Download the sample](#Download+the+sample)

Take a look at the complete example in [HowTo: Build a chatbot using GeneXus](https://wiki.genexus.com/commwiki/wiki?37076). The solution is in the CitizenSDAdv and CitizenAdv instances of the example.


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |

---
