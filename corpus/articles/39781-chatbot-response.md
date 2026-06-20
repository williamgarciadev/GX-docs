---
title: "Chatbot Response"
source_id: 39781
source_url: https://wiki.genexus.com/commwiki/wiki?39781
genexus_version: "18"
---

# Chatbot Response

Any [Flow of a Conversational instance](https://wiki.genexus.com/commwiki/wiki?38531) has a Response. In the Response node, you can model the behavior after the Flow finishes its execution.

`[imagen omitida: wiki id 39782]`

The Response node can have Response Parameters and/or Messages children nodes.

`[imagen omitida: wiki id 39783]`

### [Response Parameters](#Response+Parameters)

The Response Parameters are automatically added to the structure and are inferred from the **Out** parameters of the [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189).

They are used to be referenced in the [Messages property](https://wiki.genexus.com/commwiki/wiki?39033) of any [Chatbot Message](https://wiki.genexus.com/commwiki/wiki?39875).

If the output of the [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189) is an SDT or a BC (or a collection of any of them), the Response parameters can also be used to auto-generate the Components when the [Action property in Message of Conversational Flow](https://wiki.genexus.com/commwiki/wiki?39492) of the [Chatbot Message](https://wiki.genexus.com/commwiki/wiki?39875) = Component View. That is, when you use the components given at the [Generated Component property](https://wiki.genexus.com/commwiki/wiki?39880) and [Generated Web Component property](https://wiki.genexus.com/commwiki/wiki?39884). You can change the order of the parameters in the list, so as that can be reflected in the form of the Generated SD component or the Generated Web Component.   
The parameters removed from the list, will not be shown in the form.

#### [Examples](#Examples)

I. If the Conversational object is a procedure, the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) is considered. All the Out parameters are automatically added to the list of Response Parameters under the Response node of the Flow.

Consider a Flow where the GetDriverLicenseRenewalInfo procedure is set as its [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189). Its parm rule is as follows:

`[imagen omitida: wiki id 39789]`

So, the &FormalitiesRequirements parameter will be automatically added to the Response Parameters of the Flow:

`[imagen omitida: wiki id 39790]`  
  
The parameters can be of any type, including a [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021).

II. If the Conversational object is a [Data Provider](https://wiki.genexus.com/commwiki/wiki?4417), the Output property of the Data Provider is considered.

`[imagen omitida: wiki id 39787]`

CulturalActivitiesNews, in this case, is a Data Provider whose output is a Business Component.

`[imagen omitida: wiki id 39788]`

So, the Response Parameters include automatically all the attributes / variables which are the output of the Data Provider. In the previous case, all the attributes of the CulturalActivitiesNew BC.

III. If it's a Business Component, only the *Search* Flow includes Response Parameters (all belong to the Transaction structure):

`[imagen omitida: wiki id 39786]`

### [Message](#Message)

The Message node includes the [Condition](https://wiki.genexus.com/commwiki/wiki?39491), and the [Style](https://wiki.genexus.com/commwiki/wiki?39492) to show the message. See [Chatbot Message](https://wiki.genexus.com/commwiki/wiki?39875).

### [Considerations about the order of conditional and non conditional responses](#Considerations+about+the+order+of+conditional+and+non+conditional+responses)

Since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,), if you have conditional and non conditional responses, the non conditional responses have to be defined first, and then the conditional responses. This is for Watson and Dialog Flow.

Previous to [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,), in the case of Watson, you have to define first the conditional responses, and then the non conditional.


|  |
| --- |
| **Backlinks** |
| [Action property in Message of Conversational Flow](https://wiki.genexus.com/commwiki/wiki?39492) | [Chatbot Generator common errors and solutions](https://wiki.genexus.com/commwiki/wiki?42695) | [Chatbot Message](https://wiki.genexus.com/commwiki/wiki?39875) |
| [Chatbot Messages Condition property](https://wiki.genexus.com/commwiki/wiki?39491) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [Conversational Flows Designer](https://wiki.genexus.com/commwiki/wiki?45145) | [Conversational Object property](https://wiki.genexus.com/commwiki/wiki?38189) |
| [Flow of a Conversational instance](https://wiki.genexus.com/commwiki/wiki?38531) | [Generated Component property](https://wiki.genexus.com/commwiki/wiki?39880) | [Generated Web Component property](https://wiki.genexus.com/commwiki/wiki?39884) |
| [KB:HowTo: Create a Scripted Chatbot](https://wiki.genexus.com/commwiki/wiki?45155) | [Messages property](https://wiki.genexus.com/commwiki/wiki?39033) | [Response Name property (Conversational Flows)](https://wiki.genexus.com/commwiki/wiki?46435) |
| [Show Response As property](https://wiki.genexus.com/commwiki/wiki?39494) | [Web Component property](https://wiki.genexus.com/commwiki/wiki?39885) |

---
