---
title: "Timer definition property"
source_id: 47340
source_url: https://wiki.genexus.com/commwiki/wiki?47340
genexus_version: "18"
---

# Timer definition property

Specifies the type of time expression used to determine when the timer event is triggered.

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)

### [Description](#Description)

Possible values:

* Compatible: Enables handling timers the way older GeneXus versions allowed it. More information at [Timer Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?43461,,). This value is deprecated and maintained for compatibility reasons.
* Date: Process instance is delayed until a fixed date and time. When attached to an Activity, the event is triggered at a fixed date and time.
* Duration: Process instance or Activity is delayed for a specific time-lapse (duration). When attached to an Activity, the event is triggered after a specific time-lapse (duration). This is the default value (as of [GeneXus 16 upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,)).
* Cycle: Process instances are triggered periodically. When attached to an Activity, the event is triggered periodically.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Build All.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,).

### [See Also](#See+Also)

[Timer Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?12194)

[Timer Start Event in BPD](https://wiki.genexus.com/commwiki/wiki?43449)


|  |
| --- |
| **Backlinks** |
| [Date expression procedure property](https://wiki.genexus.com/commwiki/wiki?47342) | [Timer cycle property](https://wiki.genexus.com/commwiki/wiki?47344) | [Timer date property](https://wiki.genexus.com/commwiki/wiki?47343) |
| [Timer duration property](https://wiki.genexus.com/commwiki/wiki?47345) | [Timer Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?12194) | [Timer Start Event in BPD](https://wiki.genexus.com/commwiki/wiki?43449) |

---
