---
title: "BackColor property"
source_id: 8688
source_url: https://wiki.genexus.com/commwiki/wiki?8688
genexus_version: "18"
---

# BackColor property

Determines the background color of a control. A numeric value representing an RGB color value must be assigned.

### [Syntax](#Syntax)

**control.** BackColor = Expression   

**Where:**  
*Control*  
   Is the name of a control inserted in the form.  
  
*Expression*  
   Represents an RGB color that is going to be applied to the control  
  
**Default Value** = ‘White’

### [Scope](#Scope)

**Objects:** Transaction, Web Panel  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** Attribute/Variable, ErrorViewer, Grid

### [Description](#Description)

The Background property has preference over this property. For example, if a background is indicated, the backcolor will have no effect.

The `[imagen omitida: wiki id 8689]`button must be pressed to select a color. This property only applies when BackColorStyle property has the Uniform value.  
  
**Design Time:** Applies to Edits, Error Viewer, Forms, Free Style Grids, Grids, Grid’s Columns, Tables, Table Cells, Table Rows Controls.

### [Samples](#Samples)

The following should be added to make the backcolor of an edit control green:

```
EditCtrl.Backcolor = RGB(0,255,0)
```

### [See Also](#See+Also)

[BackColorStyle property](https://wiki.genexus.com/commwiki/wiki?8692)  
[ForeColor property](https://wiki.genexus.com/commwiki/wiki?8693)


|  |
| --- |
| **Backlinks** |
| [Attribute/Variable control properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8133) | [BackColorStyle property](https://wiki.genexus.com/commwiki/wiki?8692) | [Check Box properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8738) |
| [Color rule](https://wiki.genexus.com/commwiki/wiki?8348) | [Dynamic Combo Box and Dynamic List Box Properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8740) | [ForeColor property](https://wiki.genexus.com/commwiki/wiki?8693) | [Form Control](https://wiki.genexus.com/commwiki/wiki?14619) |
| [Text Block properties](https://wiki.genexus.com/commwiki/wiki?9908) |

---
