---
title: "FontStrikethru property"
source_id: 8779
source_url: https://wiki.genexus.com/commwiki/wiki?8779
genexus_version: "18"
---

# FontStrikethru property

Determines the font style in the control with a StriktThru line in it.

### [Syntax](#Syntax)

**control.** FontStrikethru = value   

**Where:**  
*control*  
    Is the name of a control inserted in the form.

#### [Values](#Values)

|  |  |
| --- | --- |
| **0 (False)** | Turns off the formatting in that style |
| **1 (True)** | Turns on the formatting in that style |

### [Description](#Description)

If FontStrikeThru's value is 1, the FontUnderline's value is ignored.

Applies to: Check Boxes, Combo Boxes, Dynamic Combo Boxes, Dynamic List Boxes, Edits, Grid’s Columns, List Boxes, Radio Buttons.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at run-time.

### [Samples](#Samples)

```
txctl.FontStrikethru = 1
```

Where txctl is the name of a text control.

### [Scope](#Scope)

**Objects:** Transaction, Web Panel  
**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[FontItalic property](https://wiki.genexus.com/commwiki/wiki?8776)  
[FontName property](https://wiki.genexus.com/commwiki/wiki?8777)  
[FontBold property](https://wiki.genexus.com/commwiki/wiki?8775)  
[FontSize property](https://wiki.genexus.com/commwiki/wiki?8778)  
[FontUnderline property](https://wiki.genexus.com/commwiki/wiki?8780)


|  |
| --- |
| **Backlinks** |
| [Font property](https://wiki.genexus.com/commwiki/wiki?8774) | [FontBold property](https://wiki.genexus.com/commwiki/wiki?8775) | [FontItalic property](https://wiki.genexus.com/commwiki/wiki?8776) |
| [FontName property](https://wiki.genexus.com/commwiki/wiki?8777) | [FontSize property](https://wiki.genexus.com/commwiki/wiki?8778) | [FontUnderline property](https://wiki.genexus.com/commwiki/wiki?8780) |

---
