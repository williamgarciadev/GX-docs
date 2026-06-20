---
title: "HowTo: Reference context parameters in a conversation"
source_id: 38942
source_url: https://wiki.genexus.com/commwiki/wiki?38942
genexus_version: "18"
---

# HowTo: Reference context parameters in a conversation

When designing a chatbot [Flow](https://wiki.genexus.com/commwiki/wiki?38531), it may be necessary to reference some [context](https://wiki.genexus.com/commwiki/wiki?39351) parameters.

You can reference the context parameters using the '&' character.

The context parameters can be used at any level of the Flow: [On Error Messages property](https://wiki.genexus.com/commwiki/wiki?38958), [Message conditions](https://wiki.genexus.com/commwiki/wiki?39491), [User Input conditions](https://wiki.genexus.com/commwiki/wiki?39003), [Messages](https://wiki.genexus.com/commwiki/wiki?39033), and Ask Messages property.

![enlightened](https://wiki.genexus.com/commwiki/static/CKEditor/ckeditor/plugins/smiley/images/lightbulb.png "enlightened") **&GXUserInput** is a standard variable used to reproduce the user input.

### [Sample](#Sample)

In this example, you'll see how to reference the context output of a procedure executed to fulfill the [Chatbot Intent](https://wiki.genexus.com/commwiki/wiki?38949) of a Flow.

The context parameter will be used in the [Messages](https://wiki.genexus.com/commwiki/wiki?39033) returned after the execution of the flow.

Consider the following example, where a Flow is defined, whose related intent is to get debt refinancing information in a chatbot for assistance to citizens.  
The [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189) associated with the Flow is the "DebtRefinancingInfo" procedure.

`[imagen omitida: wiki id 38945]`

The "DebtRefinancingInfo" code is as follows. Note that it returns a variable called &FormalitiesRequirements:

```
parm(out:&FormalitiesRequirements);

for each FormalitiesDetails
    where FormalitiesReason = FormalitiesReason.DebtRefinancing
    &FormalitiesRequirements = FormalitiesRequirements
endfor
```

To return the complete output of the DebtRefinancingInfo procedure to the user, the Message Response defined in the Flow has the Messages Property set to &FormalitiesRequirements.

`[imagen omitida: wiki id 38946]`

At runtime:

`[imagen omitida: wiki id 40084]`

### [See Also](#See+Also)

[HowTo: Build a chatbot using GeneXus](https://wiki.genexus.com/commwiki/wiki?37076)


|  |
| --- |
| **Backlinks** |
| [Chatbot Context](https://wiki.genexus.com/commwiki/wiki?39351) | [Chatbot User Input](https://wiki.genexus.com/commwiki/wiki?38959) | [Chatbot User Input Redirections](https://wiki.genexus.com/commwiki/wiki?39003) |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [Input Not Understood Messages property](https://wiki.genexus.com/commwiki/wiki?39224) | [Messages property](https://wiki.genexus.com/commwiki/wiki?39033) |
| [On Error Messages property](https://wiki.genexus.com/commwiki/wiki?38958) | [Trigger Messages property](https://wiki.genexus.com/commwiki/wiki?39067) |

---
