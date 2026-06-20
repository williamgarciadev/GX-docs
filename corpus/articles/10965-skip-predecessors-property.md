---
title: "Skip predecessors property"
source_id: 10965
source_url: https://wiki.genexus.com/commwiki/wiki?10965
genexus_version: "18"
---

# Skip predecessors property

Completes automatically all predecessors Tasks.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Controls:** [Task](https://wiki.genexus.com/commwiki/wiki?17495)

### [Description](#Description)

The default value for this property is True.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

`[imagen omitida: wiki id 55601]`

Activities A and B are executed.

Activity B is completed, but activity A is not completed.

Ending activity B gives rise to initialization of activity C.

This property allows eliminating activity A, since it will not contribute to the creation of activity C.


|  |
| --- |
| **Backlinks** |
| [Script Task Properties](https://wiki.genexus.com/commwiki/wiki?17498) | [User Task Properties](https://wiki.genexus.com/commwiki/wiki?17499) |

---
