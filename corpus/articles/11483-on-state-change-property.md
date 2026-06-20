---
title: "On state change property"
source_id: 11483
source_url: https://wiki.genexus.com/commwiki/wiki?11483
genexus_version: "18"
---

# On state change property

Executes a Procedure if the state of a process or Task instance changes.

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)  
**Controls:** [Subprocess](https://wiki.genexus.com/commwiki/wiki?17268), [Task](https://wiki.genexus.com/commwiki/wiki?17495)   
**Level:** [Version](https://wiki.genexus.com/commwiki/wiki?7860)

### [Description](#Description)

The [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) has the following [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862):

```
parm(in:&wfevent);
```

**Where**  
    *&wfevent* has the [WorkflowStateChangeEvent Data Type](https://wiki.genexus.com/commwiki/wiki?10276) associated with it.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[HowTo: Work With Event Handlers](https://wiki.genexus.com/commwiki/wiki?11558)


|  |
| --- |
| **Backlinks** |
| [BPD Subprocesses Embedded Properties](https://wiki.genexus.com/commwiki/wiki?17582) | [BPD Subprocesses Reusable Properties](https://wiki.genexus.com/commwiki/wiki?17580) | [Business Process Diagram Properties](https://wiki.genexus.com/commwiki/wiki?20896) |
| [None Task Properties](https://wiki.genexus.com/commwiki/wiki?17497) | [Reusable Properties](https://wiki.genexus.com/commwiki/wiki?12867) | [Script Task Properties](https://wiki.genexus.com/commwiki/wiki?17498) | [User Task Properties](https://wiki.genexus.com/commwiki/wiki?17499) |

---
