---
title: "Trigger the flow of a dialog"
source_id: 39082
source_url: https://wiki.genexus.com/commwiki/wiki?39082
genexus_version: "18"
---

# Trigger the flow of a dialog

A [Flow](https://wiki.genexus.com/commwiki/wiki?38531) is executed after the [intent](https://wiki.genexus.com/commwiki/wiki?38949) has been detected.

The user enters some keywords or clues which are used by the [AI](https://en.wikipedia.org/wiki/Artificial_intelligence) service to identify what the user wants (the [intent](https://wiki.genexus.com/commwiki/wiki?38949)). Those “clues” are called training phrases/messages, of the intent. In fact, they trigger the dialog that starts when the intent is detected. The should be configured at the [Trigger Messages property](https://wiki.genexus.com/commwiki/wiki?39067) of the Flow.

You have to define the Trigger Messages for each intent (Flow), but you do not need to include all the combinations of the expressions because the underlying Artificial Intelligence collaborates to solve that issue.

For example, a training message for the *"Get Information"* intent could be "*have doubts.*" The following picture shows the way you need to define the intent's Trigger Messages property in the Conversational Flows instance.

`[imagen omitida: wiki id 43868]`

The training message defined in the [Trigger Messages property](https://wiki.genexus.com/commwiki/wiki?39067) can include a reference to an [Entity](https://wiki.genexus.com/commwiki/wiki?39083), so that the [User Inputs](https://wiki.genexus.com/commwiki/wiki?38959) that [match that entity](https://wiki.genexus.com/commwiki/wiki?39295) can be automatically inferred from the query, and won't be prompted to the user.

Only in Watson, if the user's query includes any of the User Inputs (although the training message has no reference to the Entity), the user won't be asked to enter this input. In this case, the User input is recognized if it matches any [entity](https://wiki.genexus.com/commwiki/wiki?39083) value or an entity pattern. Besides, a User input can be inferred from another User Input in Watson.

For example, the Flow "*Green PlacesClaim*" includes the [User Input](https://wiki.genexus.com/commwiki/wiki?38959) "*UserIdentification*" which should match an [entity](https://wiki.genexus.com/commwiki/wiki?39083) defined in the NLP provider.

`[imagen omitida: wiki id 39084]`

If this entity is recognized in what the user has entered, the end user isn't asked to enter this information again (in this case, the "*UserIdentification*"). Note that the user is asked to enter the next User Input; in this case, the "*ComplaintDescription*."

`[imagen omitida: wiki id 40080]`

Continuing with the flow, it can also be triggered when another Flow redirects to it (see [Chatbot User Input Redirections](https://wiki.genexus.com/commwiki/wiki?39003)).  
After the intent of a Flow is detected (or another Flow has redirected to it), the user is asked to enter each of the [User Inputs](https://wiki.genexus.com/commwiki/wiki?38959) of the Flow.

Then, if there is a [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189) set for the Flow, it is executed.

For more information, see [HowTo: Build a chatbot using GeneXus](https://wiki.genexus.com/commwiki/wiki?37076).

### [See Also](#See+Also)

[HowTo: Build a chatbot using GeneXus](https://wiki.genexus.com/commwiki/wiki?37076)  
[Input Not Understood Redirection property](https://wiki.genexus.com/commwiki/wiki?39222)  
[Input Not Understood Messages property](https://wiki.genexus.com/commwiki/wiki?39224)


|  |
| --- |
| **Backlinks** |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |

---
