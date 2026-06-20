---
title: "On Error Messages property"
source_id: 38958
source_url: https://wiki.genexus.com/commwiki/wiki?38958
genexus_version: "18"
---

# On Error Messages property

Specifies the On Error Messages for this parameter. You can type multiple messages using the ‘;’ delimiter and reference any context parameter using the '&' character.

### [Samples](#Samples)

Here, the "Lighting Claim" [Flow](https://wiki.genexus.com/commwiki/wiki?38531) includes a User input called "UserIdentification", whose purpose is to ask the user to enter his name or identification.

If the information entered by the user isn't valid, the message specified in the On Error Messages property is displayed.

In this case, a [contextual parameter](https://wiki.genexus.com/commwiki/wiki?38942) called &GXUserinput is used to reproduce the user input.

`[imagen omitida: wiki id 38957]`

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [Scope](#Scope)

**Objects:** Conversational Flows

### [See Also](#See+Also)

* [Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520)


|  |
| --- |
| **Backlinks** |
| [Chatbot Flow: Get information about any formality](https://wiki.genexus.com/commwiki/wiki?39072) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [HowTo: Reference context parameters in a conversation](https://wiki.genexus.com/commwiki/wiki?38942) | [Match With Entity property](https://wiki.genexus.com/commwiki/wiki?39295) |

---
