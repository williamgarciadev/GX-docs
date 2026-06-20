---
title: "GXtest UI Commands - Drag and Drop"
source_id: 47574
source_url: https://wiki.genexus.com/commwiki/wiki?47574
genexus_version: "18"
---

# GXtest UI Commands - Drag and Drop

This command is useful for dragging and dropping a **source** control inside a **target** control.

`[imagen omitida: wiki id 47609]`

`[imagen omitida: wiki id 47610]`

Parameters

* SourceControl: control name of the control to be dragged.
* SourceRow: row number if source control is inside a grid or table; if it is not, set it to -1.
* TargetControl: control name where to drop the source control.
* TargetRow: row number if target control is inside a grid or table; if it is not, set it to -1.

Example:

```
&driver.DragAndDrop("ControlX", "ControlY")

&driver.DragAndDrop("ControlX", 2, "ControlY", -1)

&driver.DragAndDrop("ControlX", -1, "ControlY", 1) 

&driver.DragAndDrop("ControlX", 2, "ControlY", 4)
```

### [Availability](#Availability)

This command is available since [GeneXus 17 upgrade 2](https://wiki.genexus.com/commwiki/wiki?47418,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
