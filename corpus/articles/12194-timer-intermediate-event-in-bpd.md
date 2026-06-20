---
title: "Timer Intermediate Event in BPD"
source_id: 12194
source_url: https://wiki.genexus.com/commwiki/wiki?12194
genexus_version: "18"
---

# Timer Intermediate Event in BPD

The Timer Intermediate Event adds time-based dependencies to a process. It is either inserted into the sequence flow to create a delay or attached to an activity to create a deadline or "time-out" condition.

### [Symbol](#Symbol)

`[imagen omitida: wiki id 12199]`

### [Description](#Description)

When a token (process instance) arrives at this Event, the clock starts, and the token waits for the specified time-related condition to occur.

### [Timer patterns](#Timer+patterns)

`[imagen omitida: wiki id 53501]`

### [Sample](#Sample)

The diagram below shows how to set periodic notifications. The Timer Intermediate Event attached to the Authorize reservation Customer Care Manager will be activated once a certain time has passed. Next, the flow will continue to the Notify pending authorization script which will send a message to the Manager, notifying him about the pending task.

To implement an infinite loop a Gateway Event and another Timer are necessary, connected as shown in the diagram. This loop must be stopped after the Manager has finished the task; the throwing Signal Event connected to the task manager and the catching Signal Event connected to the Gateway whose flow continues to a None End Event will do this.

Note that to see the Timer Events reflected in your inbox, you must run a program that checks and executes these events. See [Timer Control](https://wiki.genexus.com/commwiki/wiki?43454) for more information.

`[imagen omitida: wiki id 50754]`

### [Properties](#Properties)

* [Timer usage property](https://wiki.genexus.com/commwiki/wiki?18663)
* [Interrupts activity property](https://wiki.genexus.com/commwiki/wiki?16905)
* [Timer definition property](https://wiki.genexus.com/commwiki/wiki?47340)
* [Timer expression type property](https://wiki.genexus.com/commwiki/wiki?47341)
* [Timer date property](https://wiki.genexus.com/commwiki/wiki?47343)
* [Timer duration property](https://wiki.genexus.com/commwiki/wiki?47345)
* [Timer cycle property](https://wiki.genexus.com/commwiki/wiki?47344)
* [Date expression procedure property](https://wiki.genexus.com/commwiki/wiki?47342)

### [See Also](#See+Also)

[Timer Start Event in BPD](https://wiki.genexus.com/commwiki/wiki?43449)  
[Timer Control](https://wiki.genexus.com/commwiki/wiki?43454)  
[How To: Set timers in GXflow](https://wiki.genexus.com/commwiki/wiki?53493,,)


|  |
| --- |
| **Backlinks** |
| [BPD Intermediate Events](https://wiki.genexus.com/commwiki/wiki?17270) | [Conditional Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?12300) | [Error Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?18059) |
| [Event Gateway](https://wiki.genexus.com/commwiki/wiki?17504) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [How the Workflow engine evaluates Timers](https://wiki.genexus.com/commwiki/wiki?49293) |
| [Link Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?18061) | [None Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?12193) | [Signal Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?12196) | [Timer Control](https://wiki.genexus.com/commwiki/wiki?43454) |
| [Timer cycle property](https://wiki.genexus.com/commwiki/wiki?47344) | [Timer date property](https://wiki.genexus.com/commwiki/wiki?47343) | [Timer definition property](https://wiki.genexus.com/commwiki/wiki?47340) | [Timer duration property](https://wiki.genexus.com/commwiki/wiki?47345) |
| [Timer expression type property](https://wiki.genexus.com/commwiki/wiki?47341) | [Timer Start Event in BPD](https://wiki.genexus.com/commwiki/wiki?43449) | [Timer usage property](https://wiki.genexus.com/commwiki/wiki?18663) |

---
