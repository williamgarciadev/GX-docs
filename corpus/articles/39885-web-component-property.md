---
title: "Web Component property"
source_id: 39885
source_url: https://wiki.genexus.com/commwiki/wiki?39885
genexus_version: "18"
---

# Web Component property

Web component that shows the response. If the property value is empty, a default Web component will be generated, considering the response parameters of the flow. Its name is given in the Generated Web component property. If the property value is not empty, and it is assigned to any custom Web component, you have to call the Conversational Object in the Start event of your Web component.

### [Description](#Description)

Allows determining the Web component that will be used to show the response, when the [Action property in Message of Conversational Flow](https://wiki.genexus.com/commwiki/wiki?39492) is set to Component View.

The property value can be left empty, which means that the component will be generated automatically, based on the Response Parameters of the [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781) node. The [Generated Web Component property](https://wiki.genexus.com/commwiki/wiki?39884) determines the name of the auto-generated component. This component should not be changed, as it is generated every time the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) is generated or built.

On the other hand, if you need to customize the Web component shown at response time, you can create your own and configure the Web component property with that value.

The Component must meet the following requirements:

1. The parm rule has to include, as in parameters, the [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189)'s in parameters.
2. Call the [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189) in the Start Event.

So, the Web component is like an intermediary object which receives the Input parameters, calls the Conversational object, and displays the results.

### [Samples](#Samples)

Consider the following example where the [Conversational Object property](https://wiki.genexus.com/commwiki/wiki?38189) of the [Flow](https://wiki.genexus.com/commwiki/wiki?38531) is a Data Provider.

`[imagen omitida: wiki id 39882]`

In the [Chatbot Message](https://wiki.genexus.com/commwiki/wiki?39875) node, the [Action property in Message of Conversational Flow](https://wiki.genexus.com/commwiki/wiki?39492) is set to "Component view", and the Web Component property is set to "CulturalActivitiesNewsComponentCustom" which is the web component that will be shown after the user enters all the [user inputs](https://wiki.genexus.com/commwiki/wiki?38959).

`[imagen omitida: wiki id 39883]`

"CulturalActivitiesNewsComponentCustom" contains the following in the Start Event, which is a call to the [Conversation Object](https://wiki.genexus.com/commwiki/wiki?38189) of the Flow.

```
Event Start
    &CulturalActivitiesNew = CulturalActivitiesNews(&CulturalActivitiesCategory)
Endevent
```

Note that the &CulturalActivitiesCategory parameter should be received by the Web Component, and it's the [User input](https://wiki.genexus.com/commwiki/wiki?38959) (received by the CulturalActivitiesNews Data Provider).

So, the parm rule of "CulturalActivitiesNewsComponentCustom" is as follows:

```
parm(in:&CulturalActivitiesCategory);
```

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [Scope](#Scope)

**Objects:** Conversational Flows

### [See Also](#See+Also)

* [Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520)
* [SD Component property](https://wiki.genexus.com/commwiki/wiki?39878,,)


|  |
| --- |
| **Backlinks** |
| [Chatbot Flow: Get information about any formality](https://wiki.genexus.com/commwiki/wiki?39072) | [Chatbot Message](https://wiki.genexus.com/commwiki/wiki?39875) | [Chatbots Collection property](https://wiki.genexus.com/commwiki/wiki?42650) |
| [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) | [Conversational Object property](https://wiki.genexus.com/commwiki/wiki?38189) | [Generated Web Component property](https://wiki.genexus.com/commwiki/wiki?39884) |

---
