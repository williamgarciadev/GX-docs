---
title: "Trigger Messages property"
source_id: 39067
source_url: https://wiki.genexus.com/commwiki/wiki?39067
genexus_version: "18"
---

# Trigger Messages property

Specifies the trigger messages for this flow. You can type multiple messages using the ‘;’ delimiter.

### [Scope](#Scope)

**Objects:** Conversational Flows

### [Description](#Description)

Trigger Messages of the [Flow](https://wiki.genexus.com/commwiki/wiki?38531) help train the [AI](https://en.wikipedia.org/wiki/Artificial_intelligence) engine to recognize the [intents](https://wiki.genexus.com/commwiki/wiki?38949) in the user's query.

Trigger messages can include a reference to an [entity](https://wiki.genexus.com/commwiki/wiki?39083), which is represented as &EntityName.  
It can also include a reference to a system entity, such as

* &datetime
* &date
* &Numeric

This has two purposes:

* Better recognize the intent,
* Automatically infer from the user's query some [User input](https://wiki.genexus.com/commwiki/wiki?38959) values, and avoid prompting for them.

See the examples below.

### [Samples](#Samples)

I. The "*Greetings*" Flow of a conversational instance can be defined as follows.

The Trigger messages are the following:

`[imagen omitida: wiki id 39074]`

When the intent is detected, the Flow is executed as it has been modeled.  
In this example, a [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189) is executed: "*GreetingsProcedure.*" It returns a &Greeting depending on the time of day:

```
parm(out:&Greeting);
```

```
&datetime = now()
if &datetime.Hour() >= 12
    &Greeting =!"Good afternoon!"
else
    &Greeting = !"Good morning"
endif
```

In order to display the greeting to the end user, the [Messages property](https://wiki.genexus.com/commwiki/wiki?39033) uses the &Greeting [contextual parameter](https://wiki.genexus.com/commwiki/wiki?38942).

`[imagen omitida: wiki id 39075]`

II. Using entity references in the Trigger Messages.

Suppose that you have the following Flow, where the intent is to ask for free tickets for an activity or to visit a place in the city.

`[imagen omitida: wiki id 41350]`

One Trigger Message is the following: "I need &numeric tickets for a guided visit to &ActivityName:{Solis Theater}"

&numeric refers to the "PromotionalTicketsQty" [User Input](https://wiki.genexus.com/commwiki/wiki?38959) which is of numeric data type:

`[imagen omitida: wiki id 41351]`

&ActivityName refers to the "ActivityName" User Input, which has [Match With Entity property](https://wiki.genexus.com/commwiki/wiki?39295) = TRUE, and [Entity property](https://wiki.genexus.com/commwiki/wiki?39300) = ActivityName.

`[imagen omitida: wiki id 41352]`

So when the user says: "I want 3 tickets for a guided visit to Solis Theater," the "PromotionalTicketsQty" value is automatically inferred as well as the "ActivityName," without the need to prompt him for this information.

### [See Also](#See+Also)

* [HowTo: Build a chatbot using GeneXus](https://wiki.genexus.com/commwiki/wiki?37076)


|  |
| --- |
| **Backlinks** |
| [Chatbot Entity](https://wiki.genexus.com/commwiki/wiki?39083) | [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102) | [Chatbot Intent](https://wiki.genexus.com/commwiki/wiki?38949) |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [Conversational Flows Designer](https://wiki.genexus.com/commwiki/wiki?45145) | [KB:HowTo: Create a Scripted Chatbot](https://wiki.genexus.com/commwiki/wiki?45155) |
| [HowTo: Manage training examples using the Chatbot Generator API](https://wiki.genexus.com/commwiki/wiki?41314) | [HowTo: Send a message to the chatbot from a menu](https://wiki.genexus.com/commwiki/wiki?40912) | [Match With Entity property](https://wiki.genexus.com/commwiki/wiki?39295) | [Merge Triggers property](https://wiki.genexus.com/commwiki/wiki?46434) |
| [Starting the conversation with the chatbot](https://wiki.genexus.com/commwiki/wiki?39076) | [Trigger the flow of a dialog](https://wiki.genexus.com/commwiki/wiki?39082) |

---
