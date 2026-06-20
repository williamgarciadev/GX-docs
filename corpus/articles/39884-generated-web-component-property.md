---
title: "Generated Web Component property"
source_id: 39884
source_url: https://wiki.genexus.com/commwiki/wiki?39884
genexus_version: "18"
---

# Generated Web Component property

Name of the Web Component that GeneXus will generate for this Message.

### [Description](#Description)

When the [Action property in Message of Conversational Flow](https://wiki.genexus.com/commwiki/wiki?39492) is set to Component view, you can leave the [Web Component property](https://wiki.genexus.com/commwiki/wiki?39885) empty, so that the [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102) will generate a Web component to be used as the response of this [Flow](https://wiki.genexus.com/commwiki/wiki?38531).

This is a read-only property which determines the name of the auto-generated Web component. The name is <[ConversationalObject](https://wiki.genexus.com/commwiki/wiki?38189)>Component.

The Component view is generated based on the Response parameters of the [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781), which are given from the Conversational object.

At the moment, the parameters should be:

* an SDT or a BC
* a collection of an SDT or BC

If you want some parameters not to be included, just remove them from the Response parameters node.

Note that the Start event of the auto-generated component includes a call to the [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189).

The Web-generated web component should not be changed, as it is generated every time the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) is built.

**Temporary Limitation for the out parameters of the conversational object**

To have the Web component generated automatically, consider that It's not supported to have SDTs with substructures as out parameters, or SDTs which are a collection. If you need to return a collection, you have to define as the output parameter a collection of an SDT - not use an SDT which is a collection.

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [Scope](#Scope)

**Objects:** Conversational Flows


|  |
| --- |
| **Backlinks** |
| [Chatbot Message](https://wiki.genexus.com/commwiki/wiki?39875) | [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [Conversational Object property](https://wiki.genexus.com/commwiki/wiki?38189) | [Generate Web UI property](https://wiki.genexus.com/commwiki/wiki?40211) | [Web Component property](https://wiki.genexus.com/commwiki/wiki?39885) |

---
