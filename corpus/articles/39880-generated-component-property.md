---
title: "Generated Component property"
source_id: 39880
source_url: https://wiki.genexus.com/commwiki/wiki?39880
genexus_version: "18"
---

# Generated Component property

Name of the Component that GeneXus will generate for this Message.

### [Scope](#Scope)

**Objects:** Conversational Flows

### [Description](#Description)

When the [Action property in Message of Conversational Flow](https://wiki.genexus.com/commwiki/wiki?39492) is set to Component view, you can leave the [SD Component property](https://wiki.genexus.com/commwiki/wiki?39878,,) empty, so that the [Chatbot generator](https://wiki.genexus.com/commwiki/wiki?37102) will generate an SD component to be used as the response of this [Flow](https://wiki.genexus.com/commwiki/wiki?38531).

This is a read-only property that determines the name of the auto-generated SD component. The name is <ConversationalObject>ComponentSD.

The Component view is generated based on the Response parameters of the [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781) which are given from the conversational object.

At the moment, the parameters should be:

* An SDT or a BC
* A collection of an SDT or BC.

If you want some parameters not to be included, just remove them from the Response Parameters node.

Note that the ClientStart event of the auto-generated component includes a call to the [Conversational Object](https://wiki.genexus.com/commwiki/wiki?38189).

The generated SD Component should not be changed, as it is generated every time the [Conversational Flows object](https://wiki.genexus.com/commwiki/wiki?37113) is built.

**Temporary Limitation for the out parameters of the conversational object**

To have the SD component generated automatically, remember that having SDTs with substructures as out parameters or SDTs which are a collection is not supported. If you need to return a collection, you have to define as the output parameter a collection of an SDT - not use an SDT which is a collection.

### [See Also](#See+Also)

* [Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520)


|  |
| --- |
| **Backlinks** |
| [Chatbot Message](https://wiki.genexus.com/commwiki/wiki?39875) | [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [Conversational Object property](https://wiki.genexus.com/commwiki/wiki?38189) | [Generate UI property](https://wiki.genexus.com/commwiki/wiki?40680) |

---
