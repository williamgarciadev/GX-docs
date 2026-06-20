---
title: "Conversational Object property"
source_id: 38189
source_url: https://wiki.genexus.com/commwiki/wiki?38189
genexus_version: "18"
---

# Conversational Object property

GeneXus object that will implement the flow’s action. In the case of web objects, it has to be a Web Component.
It's called automatically after the User inputs are entered.
If the Flow Message has a Component view Style, and the SD Component or Web Component property is set, you have to call the Conversational Flows object from the Start Event of the corresponding component.

### [Scope](#Scope)

**Objects:** Conversational Flows

### [Description](#Description)

It is a property of the [Flow of a Conversational instance](https://wiki.genexus.com/commwiki/wiki?38531).

The value of this property should be a GeneXus object (Business Components, Data Providers, Procedures, [Web components](https://wiki.genexus.com/commwiki/wiki?1864) and SD Panels), which will end up resolving the [intent](https://wiki.genexus.com/commwiki/wiki?38949) associated with the Flow.

At the end of the flow necessary to fulfill the intent, all data will be passed on to this object, which may return a response.

**When is the Conversational Object triggered?**

The conversational object can be triggered automatically. It happens when all of these are fulfilled:

1. The intent is recognized
2. All the [Chatbot User Inputs](https://wiki.genexus.com/commwiki/wiki?38959) are entered

There are two different situations in which the conversational object is automatically triggered, which are the following:

1. If there is a [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781) with a [Message](https://wiki.genexus.com/commwiki/wiki?39875) whose [Action](https://wiki.genexus.com/commwiki/wiki?39492) = "Component view", and the Component is auto-generated ([Web Component property](https://wiki.genexus.com/commwiki/wiki?39885) or [SD Component property](https://wiki.genexus.com/commwiki/wiki?39878,,) is empty), the conversational object is called from the auto-generated Component ([Generated Component property](https://wiki.genexus.com/commwiki/wiki?39880) and [Generated Web Component property](https://wiki.genexus.com/commwiki/wiki?39884)).

On the contrary, if the [Action](https://wiki.genexus.com/commwiki/wiki?39492) = "Component view" but you use a custom component ([SD Component property](https://wiki.genexus.com/commwiki/wiki?39878,,) or [Web Component property](https://wiki.genexus.com/commwiki/wiki?39885) is set to a component of your own), you have to call the Conversational object in the ClientStart (Start) event of your component.

2. If there is no [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781), or the [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781) is a Message whose [Action](https://wiki.genexus.com/commwiki/wiki?39492) = "Text message" or "Redirect To", the conversational object is called immediately after the User inputs are entered.

**Notes:**

* You can check the generated object called <ConversationalObject>Bot, where the call to the Component or the call to conversational object is made.
* The value of the Conversational object can be left empty, which means that the Flow doesn't trigger the execution of any GeneXus object.

### [Samples](#Samples)

Consider the following example, where the conversational object associated with the Flow is the "GreenPlaces" procedure:

`[imagen omitida: wiki id 38939]`

The procedure has the following parm rule:

```
parm(in:&UserIdentification, in:&ComplaintDescription, in:&ComplaintAddress,out:&response);
```

Note the [User inputs](https://wiki.genexus.com/commwiki/wiki?38959) declared in the flow which are mapped to each of the parameters received by the "GreenPlaces" procedure.

`[imagen omitida: wiki id 38997]`

The same happens to the &response parameter, which is assigned when the execution of the "GreenPlaces" procedure is complete.

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [See Also](#See+Also)

* [Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520)
* [HowTo: Build a chatbot using GeneXus](https://wiki.genexus.com/commwiki/wiki?37076)


|  |
| --- |
| **Backlinks** |
| [Chatbot Context](https://wiki.genexus.com/commwiki/wiki?39351) | [Chatbot Flow: Complaint about any issue happening on the street](https://wiki.genexus.com/commwiki/wiki?39071) | [Chatbot Flow: Get information about any formality](https://wiki.genexus.com/commwiki/wiki?39072) |
| [Chatbot Flow: Set up an appointment for any administrative formality](https://wiki.genexus.com/commwiki/wiki?39073) | [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781) | [Chatbot User Input](https://wiki.genexus.com/commwiki/wiki?38959) | [Chatbots architecture](https://wiki.genexus.com/commwiki/wiki?38522) |
| [Chatbots Collection property](https://wiki.genexus.com/commwiki/wiki?42650) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [Conversational Flows Designer](https://wiki.genexus.com/commwiki/wiki?45145) | [Conversational Flows Pattern Settings](https://wiki.genexus.com/commwiki/wiki?38532) |
| [KB:eBanking Chatbot sample](https://wiki.genexus.com/commwiki/wiki?54220) | [Generated Component property](https://wiki.genexus.com/commwiki/wiki?39880) | [Generated Web Component property](https://wiki.genexus.com/commwiki/wiki?39884) |
| [KB:HowTo : Create a chatbot with human fallback](https://wiki.genexus.com/commwiki/wiki?46255) | [HowTo: Manage the Context of the conversation through the Chatbot API](https://wiki.genexus.com/commwiki/wiki?41364) | [HowTo: Reference context parameters in a conversation](https://wiki.genexus.com/commwiki/wiki?38942) |
| [HowTo: Send a message to the chatbot from a menu](https://wiki.genexus.com/commwiki/wiki?40912) | [HowTo: Send and receive a message from the Provider](https://wiki.genexus.com/commwiki/wiki?42971) | [Messages property](https://wiki.genexus.com/commwiki/wiki?39033) |
| [Trigger Messages property](https://wiki.genexus.com/commwiki/wiki?39067) | [Trigger the flow of a dialog](https://wiki.genexus.com/commwiki/wiki?39082) | [Web Component property](https://wiki.genexus.com/commwiki/wiki?39885) |

---
