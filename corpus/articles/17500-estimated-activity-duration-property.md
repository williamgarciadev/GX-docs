---
title: "Estimated activity duration property"
source_id: 17500
source_url: https://wiki.genexus.com/commwiki/wiki?17500
genexus_version: "18"
---

# Estimated activity duration property

Indicates the estimated duration (in minutes) of a Task / Subprocess.

### [Scope](#Scope)

**Controls:** [Task](https://wiki.genexus.com/commwiki/wiki?17495), [Subprocess](https://wiki.genexus.com/commwiki/wiki?17268)

### [Description](#Description)

The default value of this property is zero, but it can be changed to any other value.

### [Sample](#Sample)

Create a [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486) like the one shown below. In the "Reservation" Task, set the Estimated activity duration property to "10":

`[imagen omitida: wiki id 55461]`

After running the BPD, the GXFlow client will be opened. Execute and send the "Reservation" Task. Next, go to the "Statistics" section and click on the [GXflow Task Analysis](https://wiki.genexus.com/commwiki/wiki?18411).

`[imagen omitida: wiki id 55462]`

In Task Analysis, you will be able to see the minimum, maximum, average, and estimated duration of completed task instances.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.


|  |
| --- |
| **Backlinks** |
| [BPD Subprocesses Embedded Properties](https://wiki.genexus.com/commwiki/wiki?17582) | [BPD Subprocesses Reusable Properties](https://wiki.genexus.com/commwiki/wiki?17580) | [None Task Properties](https://wiki.genexus.com/commwiki/wiki?17497) |
| [Script Task Properties](https://wiki.genexus.com/commwiki/wiki?17498) | [User Task Properties](https://wiki.genexus.com/commwiki/wiki?17499) |

---
