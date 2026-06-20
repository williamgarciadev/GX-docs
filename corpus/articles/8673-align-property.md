---
title: "Align property"
source_id: 8673
source_url: https://wiki.genexus.com/commwiki/wiki?8673
genexus_version: "18"
---

# Align property

Selects the control’s alignment.

### [Syntax](#Syntax)

**control.** Align   

**Where:**  
*control* Is the name of a control inserted in the form.

### [Values](#Values)

|  |  |
| --- | --- |
| **AbsBottom** | It aligns the image's base with the base of the highest item. |
| **AbsMiddle** | It aligns the middle of the image with the environment of the highest element. |
| **Bottom** | It aligns the base of the image with the text's base. |
| **Center** | The table remains centered in the navigator's screen or the cell. In the case of a line or cell, the contents remain centered. |
| **Left** | The table remains on the left of the screen of the navigator or the cell. In the case of a line or cell, the contents remains aligned on the left. |
| **Middle** | It aligns the middle of the image with the line's base. |
| **Right** | The table remains on the right of the screen of the navigator or the cell. In the case of a line or cell, the contents remain aligned on the right. |
| **TextTop** | It aligns the image with the line's highest element. |
| **Top** | It aligns the image with respect to the line's highest element. |

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)  
**Controls:** Embedded Page, FreeStyle Grid, Grid, Image, Table

### [Description](#Description)

In the case of images, the alignment is with respect to the text surrounding it.

In the case of tables, Grids, and Free Style Grids, it indicates the alignment inside the form or the cell that contains it. In the case of a line or a cell, the property indicates the alignment of its contents.

In the case of tables, Grids, and Free Style Grids, it applies at execution time too.

#### Default Values

|  |  |
| --- | --- |
| **Control** | **Default Value** |
| Image | Left |
| Embedded Page | Center |
| Grid, Free Style Grid | Left |
| Tables | Left |
| Tables’s cell | Left |
| Tables’s row | Left |

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.


|  |
| --- |
| **Backlinks** |
| [Free Style Grid Properties](https://wiki.genexus.com/commwiki/wiki?9760) |

---
