---
title: "Match With Entity property"
source_id: 39295
source_url: https://wiki.genexus.com/commwiki/wiki?39295
genexus_version: "18"
---

# Match With Entity property

If true, the provider maps this parameter with an entity value.

### [Scope](#Scope)

**Objects:** [Conversational Flows Instance](https://wiki.genexus.com/commwiki/wiki?37113)

### [Description](#Description)

Through this property, the [User Input](https://wiki.genexus.com/commwiki/wiki?38959) can be matched with an [entity](https://wiki.genexus.com/commwiki/wiki?39083). The entity has to be specified in the [Entity property](https://wiki.genexus.com/commwiki/wiki?39300).

This guarantees that the user input will be validated against an entity value by the provider.

If you want to match with more than one entity value, the variable associated with the User input must have the Collection property set to TRUE. See [Variable collection property behavior for User inputs](https://wiki.genexus.com/commwiki/wiki?46144,,) for more information.

**Important**

When a User Input has Match With Entity property = TRUE, the entity value can also be obtained from the user's initial query (which triggers the flow), if the [Trigger Messages property](https://wiki.genexus.com/commwiki/wiki?39067) includes a training phrase that references the [Entity](https://wiki.genexus.com/commwiki/wiki?39083). See the example below.

### [Samples](#Samples)

I.

In the following example, UserIdentification is a [User Input](https://wiki.genexus.com/commwiki/wiki?38959) which has the Match With entity property configured. The Entity property determines the name of the entity that will be matched. In this case, it's called "*UserIdentification*."  
  
When the end user is asked to enter the user ID, the input has to match any value of the "UserIdentification" entity defined in the [AI](https://en.wikipedia.org/wiki/Artificial_intelligence) provider.

`[imagen omitida: wiki id 39294]`

If the user fails to enter a valid value, the message specified in the [On Error Messages property](https://wiki.genexus.com/commwiki/wiki?38958) is displayed.

II. **Obtaining the Entity value from the user's initial query**

In this example, one [Trigger Message](https://wiki.genexus.com/commwiki/wiki?39067) of the "Get Activities Information" Flow is as follows:

*"information about @Activities"*

Where *@Activities* is a reference to the *Activities* Entity defined in the NLP Provider. At the same time, the Flow is as follows:

`[imagen omitida: wiki id 41357]`

Note that the User Input (which prompts the user for the type of activity he's interested in), [matches the Entity](https://wiki.genexus.com/commwiki/wiki?39295) *Activities*.

So, if the user's initial query is "I need information about artistic activities," he won't be asked to enter the User Input because he has already included that information in his query (as "artistic" is a valid value for "Activities" entity).

At runtime:

`[imagen omitida: wiki id 41359]`

`[imagen omitida: wiki id 41360]`

### [See Also](#See+Also)

* [Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520)


|  |
| --- |
| **Backlinks** |
| [Chatbot Entity](https://wiki.genexus.com/commwiki/wiki?39083) | [Chatbot Flow: Get information about any formality](https://wiki.genexus.com/commwiki/wiki?39072) | [Chatbot Flow: Set up an appointment for any administrative formality](https://wiki.genexus.com/commwiki/wiki?39073) |
| [Chatbots Collection property](https://wiki.genexus.com/commwiki/wiki?42650) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [Entity property](https://wiki.genexus.com/commwiki/wiki?39300) |
| [Match With Entity property](https://wiki.genexus.com/commwiki/wiki?39295) | [Trigger Messages property](https://wiki.genexus.com/commwiki/wiki?39067) | [Trigger the flow of a dialog](https://wiki.genexus.com/commwiki/wiki?39082) | [User Input Redirections Condition property](https://wiki.genexus.com/commwiki/wiki?43716) |
| [Validation Procedure property](https://wiki.genexus.com/commwiki/wiki?42594) |

---
