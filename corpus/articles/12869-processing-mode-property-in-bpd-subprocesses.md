---
title: "Processing mode property in BPD Subprocesses"
source_id: 12869
source_url: https://wiki.genexus.com/commwiki/wiki?12869
genexus_version: "18"
---

# Processing mode property in BPD Subprocesses

Allows choosing the process type. Sub-processes can be Chained or Nested.

### [Values](#Values)

|  |  |
| --- | --- |
| **Chained** | The sub-processes modality assumes that a process instance causes the creation and execution of an instance of another process (the sub-process). Once the sub-process execution has started, the instance of the original process may finish or continue with its own execution, reducing interest in the sub-process created. |
| **Nested** | The nested sub-processes modality allows an instance of a process (child) to be completely encapsulated as a unique task within another process (parent). The parent process waits for the termination of the child process before continuing with its own execution. Therefore, there is a hierarchical relationship between the two processes. The hierarchical relationship may be extended through different levels, making up a group of nested sub-processes. |

### [Scope](#Scope)

**Controls:** [Subprocess](https://wiki.genexus.com/commwiki/wiki?17268)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Processing mode property in Task control](https://wiki.genexus.com/commwiki/wiki?11555)


|  |
| --- |
| **Backlinks** |
| [BPD Subprocesses Reusable Properties](https://wiki.genexus.com/commwiki/wiki?17580) | [Processing mode property in Task control](https://wiki.genexus.com/commwiki/wiki?11555) | [Reusable Properties](https://wiki.genexus.com/commwiki/wiki?12867) |

---
