---
title: "Reassign when loop property"
source_id: 11885
source_url: https://wiki.genexus.com/commwiki/wiki?11885
genexus_version: "18"
---

# Reassign when loop property

When a task is executed several times (because of a loop), it makes it possible to always assign the task to the person working on it.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Controls:** [Task](https://wiki.genexus.com/commwiki/wiki?17495)

### [Description](#Description)

To reassign the task, the loop must resemble the example below:

`[imagen omitida: wiki id 55757]`

In this case, each time the flow returns to task 'A', it will be reassigned to the same user who executed it the first time.

Tasks with this property set to true will not be reassigned when the loop is triggered by the [Loop Type property](https://wiki.genexus.com/commwiki/wiki?11898).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.


|  |
| --- |
| **Backlinks** |
| [Automatic Assignment Conditions Properties Group](https://wiki.genexus.com/commwiki/wiki?10972) | [User Task Properties](https://wiki.genexus.com/commwiki/wiki?17499) |

---
