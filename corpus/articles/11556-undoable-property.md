---
title: "Undoable property"
source_id: 11556
source_url: https://wiki.genexus.com/commwiki/wiki?11556
genexus_version: "18"
---

# Undoable property

Allows process administrator users to undo the execution of Tasks workitems from GXflow Client.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Controls:** [Task](https://wiki.genexus.com/commwiki/wiki?17495)

### [Description](#Description)

You can go back to a Task, only if all the successor Tasks are active. Those successor Tasks will be aborted, and the undone Task will be set to active.

### [Samples](#Samples)

As shown in the image, select the Task B in the Business Process Diagram. Set the Undoable property to True.

`[imagen omitida: wiki id 55722]`

Execute Task A. Then, execute the Task B and wait to execute Task C.

Go to the GXFlow backend and click on the Process Manager section > Task. Then select the Task B (undoable Task) on the MORE ACTIONS dynamic combo, then click 'Undo' option.


|  |
| --- |
| **Backlinks** |
| [Adaptability Properties](https://wiki.genexus.com/commwiki/wiki?10957) | [Script Task Properties](https://wiki.genexus.com/commwiki/wiki?17498) | [User Task Properties](https://wiki.genexus.com/commwiki/wiki?17499) |

---
