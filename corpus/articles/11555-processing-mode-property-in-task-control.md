---
title: "Processing mode property in Task control"
source_id: 11555
source_url: https://wiki.genexus.com/commwiki/wiki?11555
genexus_version: "18"
---

# Processing mode property in Task control

Allows the Task to run (or not to run) in a parallel execution thread.

### [Values](#Values)

|  |  |
| --- | --- |
| **Synchronous** | The application associated with the task is executed in the same thread as the workflow engine, and the latter waits for it to be completed in order to continue processing. This is the default value. |
| **Asynchronous** | The application associated with the task is executed in an independent thread and the workflow engine doesn't wait for it to be completed. The application is responsible for notifying the workflow engine through the Complete method when this task processing is completed. |

### [Scope](#Scope)

**Controls:** [Task](https://wiki.genexus.com/commwiki/wiki?17495)

### [Description](#Description)

This property is offered when the [Task control](https://wiki.genexus.com/commwiki/wiki?17495) has [Type property](https://wiki.genexus.com/commwiki/wiki?11464) = Script.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Processing mode property in BPD Subprocesses](https://wiki.genexus.com/commwiki/wiki?12869)


|  |
| --- |
| **Backlinks** |
| [Processing mode property in BPD Subprocesses](https://wiki.genexus.com/commwiki/wiki?12869) | [Script Task Properties](https://wiki.genexus.com/commwiki/wiki?17498) |

---
