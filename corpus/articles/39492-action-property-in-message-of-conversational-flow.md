---
title: "Action property in Message of Conversational Flow"
source_id: 39492
source_url: https://wiki.genexus.com/commwiki/wiki?39492
genexus_version: "18"
---

# Action property in Message of Conversational Flow

Defines the behavior to show the message.

### [Values](#Values)

|  |  |
| --- | --- |
| **component view** | Shows the response as a component view. |
| **redirect to** | Redirects to another flow. |
| **text message** | Shows the response as a text message. |

### [Scope](#Scope)

**Objects:** Conversational Flows

### [Description](#Description)

The Action property determines the behavior of the response of the [Flow of a Conversational instance](https://wiki.genexus.com/commwiki/wiki?38531).

The [Chatbot Message](https://wiki.genexus.com/commwiki/wiki?39875) (child of the [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781) node) can be a component (Web or Mobile) or a text message. In other cases, the message is shown and afterwards, another flow is automatically executed after having finished this one.

`[imagen omitida: wiki id 42132]`

**Note:** When the Action property is set to Component View, the [Show Response As property](https://wiki.genexus.com/commwiki/wiki?39494) is offered.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [See Also](#See+Also)

[Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520)


|  |
| --- |
| **Backlinks** |
| [Chatbot Message](https://wiki.genexus.com/commwiki/wiki?39875) | [Chatbot Response](https://wiki.genexus.com/commwiki/wiki?39781) | [Toc:Chatbots in GeneXus](https://wiki.genexus.com/commwiki/wiki?38520) |
| [Conversational Object property](https://wiki.genexus.com/commwiki/wiki?38189) | [Generated Component property](https://wiki.genexus.com/commwiki/wiki?39880) | [Generated Web Component property](https://wiki.genexus.com/commwiki/wiki?39884) |
| [Show Response As property](https://wiki.genexus.com/commwiki/wiki?39494) | [Web Component property](https://wiki.genexus.com/commwiki/wiki?39885) |

---
