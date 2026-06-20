---
title: "Clean Context Value property"
source_id: 39353
source_url: https://wiki.genexus.com/commwiki/wiki?39353
genexus_version: "18"
---

# Clean Context Value property

Clean the value given for this user input when the flow begins.
True -> Clean the context value for this user input when the flow begins, so it will be asked again to the user.
False -> Do not clean the context value for this user input when the flow begins. The value will be remembered / used from the value stored in the context.

### [Description](#Description)

In some cases, it's necessary to clear some [Context](https://wiki.genexus.com/commwiki/wiki?39351) [User Input](https://wiki.genexus.com/commwiki/wiki?38959) values, so the user can be asked to enter them again.

So, we need that the chatbot forgets this information, and doesn't save it in the conversation context.

### [Samples](#Samples)

That's not the case of User Identification; in general, we want the chatbot to remember it. In this case, the Clean Context value property should be set to FALSE.

But consider the example shown in [HowTo: Build a chatbot using GeneXus](https://wiki.genexus.com/commwiki/wiki?37076), where the user can make a claim about different topics (a lighting claim or a problem about a traffic sign). In both cases, the user is asked to enter the address and the description of the problem.

This information should not be saved in the context, so when the user wants to make a new claim he/she is asked again to enter the address and a description of the problem.

`[imagen omitida: wiki id 39352]`

To Apply the changes, just save the instance.

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [Scope](#Scope)

**Objects:** Conversational Flows

### [See Also](#See+Also)

* [Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520)


|  |
| --- |
| **Backlinks** |
| [Chatbot Context](https://wiki.genexus.com/commwiki/wiki?39351) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [Required property](https://wiki.genexus.com/commwiki/wiki?43692) |

---
