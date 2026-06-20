---
title: "Date expression procedure property"
source_id: 47342
source_url: https://wiki.genexus.com/commwiki/wiki?47342
genexus_version: "18"
---

# Date expression procedure property

A procedure that returns the date and time of the next execution.

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)

### [Description](#Description)

Visible if Timer Expression Type is set to 'Procedure'.

Allows setting a procedure that returns the date and time ([DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370)) in which the event will be triggered next.

If [Timer definition property](https://wiki.genexus.com/commwiki/wiki?47340) is set to 'Date' or 'Duration', this procedure is called just once; if [Timer definition property](https://wiki.genexus.com/commwiki/wiki?47340) is set to Cycle, the procedure is called again after a timer is triggered. If it returns a past date and time, the timer event will not be triggered again in that process instance (unless the control flow returns to the timer).

The associated procedure must have the following parm rule:

```
parm( in:&WorkflowProcessDefinition, in:&WorkflowProcessInstance, in:&WorkflowWorkitem, out:&DateTime)
```

Where:

*&WorkflowProcessDefinition* is a [WorkflowProcessDefinition Data Type](https://wiki.genexus.com/commwiki/wiki?17239) variable

*&WorkflowProcessInstance* is a [WorkflowProcessInstance Data Type](https://wiki.genexus.com/commwiki/wiki?17771)  variable

*&WorkflowWorkitem* is a [WorkflowWorkitem Data Type](https://wiki.genexus.com/commwiki/wiki?11731) variable

*&DateTime*[DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370) variable.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Build All.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,).


|  |
| --- |
| **Backlinks** |
| [Timer Intermediate Event in BPD](https://wiki.genexus.com/commwiki/wiki?12194) | [Timer Start Event in BPD](https://wiki.genexus.com/commwiki/wiki?43449) |

---
