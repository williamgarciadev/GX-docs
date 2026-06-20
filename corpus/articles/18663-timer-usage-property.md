---
title: "Timer usage property"
source_id: 18663
source_url: https://wiki.genexus.com/commwiki/wiki?18663
genexus_version: "18"
---

# Timer usage property

Indicates if the timer will be used as a deadline or a warning.

### [Values](#Values)

|  |  |
| --- | --- |
| **None** | It does not have a specific use. |
| **Deadline** | In this case, you can set the property Interrupts Activity. |
| **Warning** | In this case, you cannot set the property Interrupts Activity. |

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)

### [Description](#Description)

Available for timer events that are attached to Activities.

After the deadline or warning event occurs, the modeled routes will be followed.

If the value Deadline is selected, the [Interrupts activity property](https://wiki.genexus.com/commwiki/wiki?16905) is enabled and you can set if the task will be interrupted or not after the deadline is reached.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Build All.

### [Availability](#Availability)

This property is available since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?27605,,).

### [See Also](#See+Also)

[Timer Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?12194)


|  |
| --- |
| **Backlinks** |
| [How the Workflow engine evaluates Timers](https://wiki.genexus.com/commwiki/wiki?49293) | [On warning property](https://wiki.genexus.com/commwiki/wiki?11478) | [Timer Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?12194) |

---
