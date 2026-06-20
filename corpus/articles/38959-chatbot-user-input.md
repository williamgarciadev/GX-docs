---
title: "Chatbot User Input"
source_id: 38959
source_url: https://wiki.genexus.com/commwiki/wiki?38959
genexus_version: "18"
---

# Chatbot User Input

The User Input represents the input parameters of the [Flow of a Conversational instance](https://wiki.genexus.com/commwiki/wiki?38531).

`[imagen omitida: wiki id 38960]`

That is, the different parameters that the [chatbot](https://wiki.genexus.com/commwiki/wiki?38520) will ask the user when it detects the [intent](https://wiki.genexus.com/commwiki/wiki?38949) related to the flow.

The User Inputs are added automatically to the structure and are inferred from the **In** parameters of the [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189).

In the next Flow, the [Conversational Object property](https://wiki.genexus.com/commwiki/wiki?38189) is set to "Lighting2".

`[imagen omitida: wiki id 38967]`

The User Inputs automatically added to the flow match the parameters of the "Lighting2" procedure, which are as follows:

```
parm(in:&UserIdentification, in:&ComplaintDescription, in:&ComplaintAddress,out:&response);
```

If you add a user input (which is not inferred from the Conversational Object), you have to define first the variable on which this user input will be based on.

`[imagen omitida: wiki id 45865]`

### [Important](#Important)

Consider the following if you are adding the User Inputs manually:

* To map the User Input to a parameter of the conversational object, you have to name it equal to the name of the parameter. The order of the definition of the User Inputs is not relevant.
* All the parameters of the conversational object have to be represented as User Inputs.
* You can also add a User Input which doesn't match to any parameter. This could be used as a context data in the conversation. See [HowTo: Reference context parameters in a conversation](https://wiki.genexus.com/commwiki/wiki?38942).

![enlightened](https://wiki.genexus.com/commwiki/static/CKEditor/ckeditor/plugins/smiley/images/lightbulb.png "enlightened")The user inputs can be conditional. See [Chatbot User Input Redirections](https://wiki.genexus.com/commwiki/wiki?39003) for more information on this topic.

### [See also](#See+also)

[HowTo: Build a chatbot using GeneXus](https://wiki.genexus.com/commwiki/wiki?37076)


|  |
| --- |
| **Backlinks** |
| [Ask again property](https://wiki.genexus.com/commwiki/wiki?40215) | [Chatbot Context](https://wiki.genexus.com/commwiki/wiki?39351) | [Chatbot Entity](https://wiki.genexus.com/commwiki/wiki?39083) |
| [Chatbot Flow: Get information about any formality](https://wiki.genexus.com/commwiki/wiki?39072) | [Chatbot User Input Redirections](https://wiki.genexus.com/commwiki/wiki?39003) | [Chatbots Collection property](https://wiki.genexus.com/commwiki/wiki?42650) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [Clean Context Value property](https://wiki.genexus.com/commwiki/wiki?39353) | [Collection property (IsCollection checkbox)](https://wiki.genexus.com/commwiki/wiki?9761) | [Conversational Flows Designer](https://wiki.genexus.com/commwiki/wiki?45145) | [Conversational Flows Editor](https://wiki.genexus.com/commwiki/wiki?45141) |
| [Conversational Object property](https://wiki.genexus.com/commwiki/wiki?38189) | [Entity property](https://wiki.genexus.com/commwiki/wiki?39300) | [Flow of a Conversational instance](https://wiki.genexus.com/commwiki/wiki?38531) |
| [KB:HowTo : Create a chatbot with human fallback](https://wiki.genexus.com/commwiki/wiki?46255) | [HowTo: Manage the Context of the conversation through the Chatbot API](https://wiki.genexus.com/commwiki/wiki?41364) | [Input Not Understood Redirection property](https://wiki.genexus.com/commwiki/wiki?39222) | [Match With Entity property](https://wiki.genexus.com/commwiki/wiki?39295) |
| [Required Condition property](https://wiki.genexus.com/commwiki/wiki?43693) | [Required property](https://wiki.genexus.com/commwiki/wiki?43692) | [Trigger Messages property](https://wiki.genexus.com/commwiki/wiki?39067) |
| [Trigger the flow of a dialog](https://wiki.genexus.com/commwiki/wiki?39082) | [User Input Redirections Condition property](https://wiki.genexus.com/commwiki/wiki?43716) | [Validation Procedure property](https://wiki.genexus.com/commwiki/wiki?42594) |
| [Variable property](https://wiki.genexus.com/commwiki/wiki?45698) | [Web Component property](https://wiki.genexus.com/commwiki/wiki?39885) |

---
