---
title: "User Input Redirections Condition property"
source_id: 43716
source_url: https://wiki.genexus.com/commwiki/wiki?43716
genexus_version: "18"
---

# User Input Redirections Condition property

Condition to evaluate in order to do a redirection.

### [Scope](#Scope)

**Objects:** [Conversational Flows Instance](https://wiki.genexus.com/commwiki/wiki?37113)

### [Description](#Description)

This property is availble for the [Chatbot User Input Redirections](https://wiki.genexus.com/commwiki/wiki?39003) nodes. The condition must evaluate to TRUE in order to the redirection to be executed. The flow to be redirected is determined by the [Redirect to Flow property](https://wiki.genexus.com/commwiki/wiki?39220).

The condition should be an expression based on a [context](https://wiki.genexus.com/commwiki/wiki?39351) variable.   
You have to use the same casing as the variable defined as [User Input](https://wiki.genexus.com/commwiki/wiki?38959) in the instance.

Note:

**Only for Watson**, you could also use code to be directly evaluated by the Provider, for example:

* @entity

In this case, you specify that the input has to match any value (or a synonymous) of the [entity](https://wiki.genexus.com/commwiki/wiki?39083).

* @entity:(value)

In this case, you specify that the input has to match a specific value of the entity (or a synonymous). Consider the casing for the values. For example, if the value is "Debt Refinancing", the condition can be: @AdmProcessType:(Debt Refinancing)  
The final user, can enter "debt refinancing". But at the property level, you have to refer to it with the correct casing according  to what has been originally defined in the provider. This syntax is valid only for Watson.  
  
Nevertheless, the recommendation is to use GeneXus code, so the chatbot model is portable to any provider.

### [Samples](#Samples)

In the following example, the "AdmProcessInformationType" User input has the [Match With Entity property](https://wiki.genexus.com/commwiki/wiki?39295) set to an [entity](https://wiki.genexus.com/commwiki/wiki?39083) of the model.`[imagen omitida: wiki id 43714]`

Then, it adds four conditions, and they all depend on some entity value. In this case, it's the "Driver License Renewal" value.

`[imagen omitida: wiki id 43715]`

If none of the conditions matched, the user would receive the response message.

**Notes:**

1. It's important to respect the case sensitivity of the value defined in the Provider. In this case it's "Driver License Renewal" with these uppercase letters.

2. The user can enter the same value of the Entity, or any synonymous of it ("Driver Licen**c**e Renewal"). However, the [Chatbot User Input](https://wiki.genexus.com/commwiki/wiki?38959) variable will take the Value of the entity instead ("Driver Licen**s**e Renewal").

When this property evaluates to TRUE; the flow indicated in the [Redirect to Flow property](https://wiki.genexus.com/commwiki/wiki?39220) is executed.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 5](https://wiki.genexus.com/commwiki/wiki?43446,,).


|  |
| --- |
| **Backlinks** |
| [Chatbot Flow: Get information about any formality](https://wiki.genexus.com/commwiki/wiki?39072) | [Chatbot User Input Redirections](https://wiki.genexus.com/commwiki/wiki?39003) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [Redirect to Flow property](https://wiki.genexus.com/commwiki/wiki?39220) |

---
