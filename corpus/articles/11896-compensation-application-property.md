---
title: "Compensation application property"
source_id: 11896
source_url: https://wiki.genexus.com/commwiki/wiki?11896
genexus_version: "18"
---

# Compensation application property

Sets a Procedure to be executed each time a Task workitem is undone.

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)  
**Controls:** [Task](https://wiki.genexus.com/commwiki/wiki?17495), [Subprocess](https://wiki.genexus.com/commwiki/wiki?17268)

### [Description](#Description)

The Procedure object associated to this property must have the following [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862):

```
parm(in:&wfprocessdefinition,in:&wfprocessinstance,in:&wfworkitem);
```

Where the variables are defined as follows:

```
&wfprocessdefinition       - WorkflowProcessDefinition
&wfprocessinstance         - WorkflowProcessInstance
&wfworkitem                - WorkflowWorkitem
```

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.


|  |
| --- |
| **Backlinks** |
| [Adaptability Properties](https://wiki.genexus.com/commwiki/wiki?10957) | [BPD Subprocesses Embedded Properties](https://wiki.genexus.com/commwiki/wiki?17582) | [BPD Subprocesses Reusable Properties](https://wiki.genexus.com/commwiki/wiki?17580) |
| [None Task Properties](https://wiki.genexus.com/commwiki/wiki?17497) | [Reusable Properties](https://wiki.genexus.com/commwiki/wiki?12867) | [Script Task Properties](https://wiki.genexus.com/commwiki/wiki?17498) | [User Task Properties](https://wiki.genexus.com/commwiki/wiki?17499) |

---
