---
title: "Event Gateway"
source_id: 17504
source_url: https://wiki.genexus.com/commwiki/wiki?17504
genexus_version: "18"
---

# Event Gateway

Event-Based Exclusive Gateways represent an alternative branching point where the decision is based on two or more Events that might occur, rather than data-oriented conditions (as in an [Exclusive-Gateway](https://wiki.genexus.com/commwiki/wiki?11641,,)).

### [Symbol](#Symbol)

`[imagen omitida: wiki id 12462]`

### [Description](#Description)

As with the other gateways, the Event-Based Exclusive Gateway allows you to control when a process *diverges* or *converges*.

The Event Gateway is unique in BPMN in that its normal behavior is actually determined by a combination of flow objects. The gateway by itself is not sufficient to accomplish the exclusive splitting of the flow. It uses a combination of Intermediate Events to create the behavior. These Events, which must be of the *catch* variety, are the first objects connected by the Gateway's outgoing Sequence flows (as details the example below). The valid catch Intermediate Events are: *Timer*, *Conditional*, *Signal*.

Since all the Intermediate Events are *catch* Events, the process will wait until one of the Events is triggered. The Intermediate Events that are part of the Gateway configuration become involved in a race condition. Whichever one finishes first (fires) will win the race and take control of the Process; the other events are discarded.

The merging behavior of the Event Gateway is exactly the same as the merging behavior of the [Exclusive Gateway](https://wiki.genexus.com/commwiki/wiki?11641,,).

### [**Properties**](#Properties)

|  |
| --- |
| [Name](https://wiki.genexus.com/commwiki/wiki?6985) |
| [Type](https://wiki.genexus.com/commwiki/wiki?17496) |
| [Visible in history](https://wiki.genexus.com/commwiki/wiki?11472) |

### [Example](#Example)

In the following example, the Event Gateway receives the process flow which will wait for the triggering of a signal (to execute *DisplayFlightReservations*) or will wait for a *Timer* to end the Process.

`[imagen omitida: wiki id 12469]`

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)

### [See Also](#See+Also)

[Exclusive Gateway](https://wiki.genexus.com/commwiki/wiki?17505)  
[Parallel Gateway](https://wiki.genexus.com/commwiki/wiki?17507)  
[Inclusive Gateway](https://wiki.genexus.com/commwiki/wiki?17506)  
[Timer Intermediate Event](https://wiki.genexus.com/commwiki/wiki?12194)  
[Conditional Intermediate Event](https://wiki.genexus.com/commwiki/wiki?12300)  
[Signal Intermediate Event](https://wiki.genexus.com/commwiki/wiki?12196)


|  |
| --- |
| **Backlinks** |
| [Category:BPD Gateways](https://wiki.genexus.com/commwiki/wiki?17496) | [Exclusive Gateway](https://wiki.genexus.com/commwiki/wiki?17505) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |
| [Inclusive Gateway](https://wiki.genexus.com/commwiki/wiki?17506) | [Parallel Gateway](https://wiki.genexus.com/commwiki/wiki?17507) |

---
