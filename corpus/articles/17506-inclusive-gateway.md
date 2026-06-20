---
title: "Inclusive Gateway"
source_id: 17506
source_url: https://wiki.genexus.com/commwiki/wiki?17506
genexus_version: "18"
---

# Inclusive Gateway

#### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?11423,,)

#### [Symbol](#Symbol)

`[imagen omitida: wiki id 12466]`

#### [Purpose](#Purpose)

This type of Gateway supports situations in which more than one decision may be possible. When a signal reaches this Gateway, a complete evaluation is performed including all the conditions considered in the control. Each condition evaluated as true will result in a signal towards that exit flow. There will always have to be at least one true condition.

#### [Description](#Description)

In divergence, the behavior is similar to the Exclusive Gateway in the sense that it allows for the creation of multiple alternative pathways based on conditions imposed on those pathways. The difference lies in that more than one path can be chosen, that is, all those whose corresponding conditions evaluate to true. In this case, the use of "default" paths is recommended in order to prevent the process from getting stuck in any situation.

Convergence works similarly to a Parallel Gateway convergence in the sense that it synchronizes the paths arriving to the Gateway. Unlike Parallel, it only synchronizes those paths that actually reach the Gateway, which are not necessarily all the paths that reach the Gateway in the diagram; this could be specific to each process instance.

**Properties**

|  |
| --- |
| [Name](https://wiki.genexus.com/commwiki/wiki?6985) |
| [Type](https://wiki.genexus.com/commwiki/wiki?17496) |
| [Condition Procedure](https://wiki.genexus.com/commwiki/wiki?17510,,) |
| [Visible in history](https://wiki.genexus.com/commwiki/wiki?11472) |

#### [Examples](#Examples)

In this example of divergence, the Compile Documents process moves its flow to an Inclusive Gateway that branches in three possible parallel conditions. They are evaluated if they are true. In the instance example, if Complement A and Complement B are true, the flow keeps moving forward through their corresponding exit paths. If only Complement C were true, the flow would move only from that condition.

`[imagen omitida: wiki id 12471]`

#### [See Also](#See+Also)

[HowTo: Define conditions or events that determine the path(s) to follow in a BPD](https://wiki.genexus.com/commwiki/wiki?13757)

[Event Gateway](https://wiki.genexus.com/commwiki/wiki?17504)  
[Parallel Gateway](https://wiki.genexus.com/commwiki/wiki?17507)  
[Exclusive Gateway](https://wiki.genexus.com/commwiki/wiki?17505)


|  |
| --- |
| **Backlinks** |
| [Category:BPD Gateways](https://wiki.genexus.com/commwiki/wiki?17496) | [Condition Procedure](https://wiki.genexus.com/commwiki/wiki?13266) |
| [Event Gateway](https://wiki.genexus.com/commwiki/wiki?17504) | [Exclusive Gateway](https://wiki.genexus.com/commwiki/wiki?17505) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |
| [Parallel Gateway](https://wiki.genexus.com/commwiki/wiki?17507) |

---
