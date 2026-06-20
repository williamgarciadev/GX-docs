---
title: "Required property"
source_id: 43692
source_url: https://wiki.genexus.com/commwiki/wiki?43692
genexus_version: "18"
---

# Required property

Indicates if User Input is required.
Always -> The parameter is required if its value is empty.
Never -> The parameter is not required.
Condition -> The parameter is required if the 'Required condition' is true.

### [Description](#Description)

This property is in the [Chatbot User Input](https://wiki.genexus.com/commwiki/wiki?38959) and allows establishing if the user input will be required to be entered or not.

Its possible values are:

Always     -> Means that the user input is required if its value is empty.  
If the [Clean Context Value property](https://wiki.genexus.com/commwiki/wiki?39353) is FALSE, and the value is in the [context](https://wiki.genexus.com/commwiki/wiki?39351), the user won't be asked to enter another value.

Never       -> The user input is not required.  
  
Condition -> The user input is required if the [Required Condition property](https://wiki.genexus.com/commwiki/wiki?43693) is true. Only for Watson.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 5](https://wiki.genexus.com/commwiki/wiki?43446,,).

### [Scope](#Scope)

**Objects:** [Conversational Flows Instance](https://wiki.genexus.com/commwiki/wiki?37113)


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [Required Condition property](https://wiki.genexus.com/commwiki/wiki?43693) |

---
