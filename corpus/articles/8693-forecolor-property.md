---
title: "ForeColor property"
source_id: 8693
source_url: https://wiki.genexus.com/commwiki/wiki?8693
genexus_version: "18"
---

# ForeColor property

Sets the foreground color of a control. A numeric value representing an RGB color value must be assigned.

### [Syntax](#Syntax)

**control.** ForeColor = value   

**Where:**  
*value*  
    Represents an RGB color.

*Control*  
    Is the name of a control inserted in the form.

### [Scope](#Scope)

**Objects:** Transaction, Web Panel  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** ErrorViewer, Attribute/Variable, Grid

### [Description](#Description)

**Design Time:** Applies to check boxes, combo/dynamic combo, edits, error viewer, list/dynamic list box, radio buttons and grid columns.

**Execution Time:**Applies to check boxes, combo/dynamic combo, edits, list/dynamic list box, radio buttons and grid columns.

### [Samples](#Samples)

The following should be added to make the forecolor of an edit control blue:

```
EditCtrl.Forecolor = RGB(0,0,255)
```

### [See Also](#See+Also)

[BackColor property](https://wiki.genexus.com/commwiki/wiki?8688)


|  |
| --- |
| **Backlinks** |
| [Attribute/Variable control properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8133) | [BackColor property](https://wiki.genexus.com/commwiki/wiki?8688) | [Check Box properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8738) |
| [Color rule](https://wiki.genexus.com/commwiki/wiki?8348) | [Dynamic Combo Box and Dynamic List Box Properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8740) | [Maps in QueryViewer](https://wiki.genexus.com/commwiki/wiki?48199) | [Text Block properties](https://wiki.genexus.com/commwiki/wiki?9908) |
|

---
