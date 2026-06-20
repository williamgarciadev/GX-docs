---
title: "How the Workflow engine evaluates Timers"
source_id: 49293
source_url: https://wiki.genexus.com/commwiki/wiki?49293
genexus_version: "18"
---

# How the Workflow engine evaluates Timers

[Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486)s allow defining Timers.

You can use the [Timer Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?12194) as an intermediate event in your Business Process Diagram, and attached to a task to represent a deadline to execute the task, for example.

If the Timer is associated with a task, the timestamp is assigned to the work item corresponding to the timer. If the [Timer usage property](https://wiki.genexus.com/commwiki/wiki?18663) is specified in the timer as Deadline, the same timestamp is also assigned to the work item corresponding to the task (only for maintaining compatibility with the statistics).

Then to evaluate when the timestamp of the Timer is reached, the [Timer Control](https://wiki.genexus.com/commwiki/wiki?43454) has to be executed.

**Note:** Deadlines set in GeneXus 9.0 or older define a deadline directly for the tasks, which translates into a timestamp in the corresponding work items.  
  
The [Deadline Checker](https://wiki.genexus.com/commwiki/wiki?23379) is the program responsible for evaluating Deadlines, controlling when the timestamp expires. Tasks eventually have successors with deadline-type edges which are triggered when they expire.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |

---
