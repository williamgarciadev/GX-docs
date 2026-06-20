---
title: "On warning property"
source_id: 11478
source_url: https://wiki.genexus.com/commwiki/wiki?11478
genexus_version: "18"
---

# On warning property

Executes Procedures after a warning is shown.

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)  
**Controls:** [Task](https://wiki.genexus.com/commwiki/wiki?17495), [Subprocess](https://wiki.genexus.com/commwiki/wiki?17268)   
**Level:** [Version](https://wiki.genexus.com/commwiki/wiki?7860)

### [Description](#Description)

Procedures have the following [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862):

```
parm(in:&wfevent);
```

**Where:**  
    &wfevent has the [WorkflowEvent Data Type](https://wiki.genexus.com/commwiki/wiki?10275) associated with it.

It fires an event when a Task's timer expires and the [Timer usage property](https://wiki.genexus.com/commwiki/wiki?18663) is set to "Warning".

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
