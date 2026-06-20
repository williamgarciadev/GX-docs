---
title: "Height property"
source_id: 8792
source_url: https://wiki.genexus.com/commwiki/wiki?8792
genexus_version: "18"
---

# Height property

Determines the height of a control. A numeric value must be assigned.

### [Syntax](#Syntax)

**control.** Height = Expression   

**Where:**  
*Control*  
    Is the name of a control inserted in the form  
  
*Expression*  
    Is a numeric that represents the control’s height.  
    Tables, table cells and embedded pages: if we enter a number, the height will be expressed in pixels. If we enter a number followed by a ‘%’ the height will be expressed in relation to the control container height.  
     In Edit control Height is given in rows. In runtime this value is included as a row attribute of the textarea.

### [Description](#Description)

**Design Time****:** Applies to Bitmap type Variables, Embedded Pages, Images, Tables, Table’s Cells.  
**Execution Time****:** Applies to Button, Check Box, Combo Box, Dynamic Combo Box, Dynamic List Box, Edit, Frame, Free Style Grids, Grids, List Box, Radio Button, Tables, Text.

### [Samples](#Samples)

Photo.Height = 200 (photo is a bitmap control)  
The bitmap control’s height will be 200 pixels.  
Edit control Height = 2row is created as <textarea row=2 ....>

### [Scope](#Scope)

**Objects:** Transaction, Web Panel  
**Platforms:** Web(.Net, Java)  
**Controls:** Embedded Page, FreeStyle Grid, Grid, Image, Table

### [See Also](#See+Also)

[Width property of Animation SD Class](https://wiki.genexus.com/commwiki/wiki?8793,,)


|  |
| --- |
| **Backlinks** |
| [Align Items property](https://wiki.genexus.com/commwiki/wiki?36111) | [Attribute/Variable control properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8133) | [Auto Resize property in QueryViewer control](https://wiki.genexus.com/commwiki/wiki?19597) |
| [Fixed Grid header with vertical scroll](https://wiki.genexus.com/commwiki/wiki?36036) | [Free Style Grid Properties](https://wiki.genexus.com/commwiki/wiki?9760) | [HeightUnit property](https://wiki.genexus.com/commwiki/wiki?8794) | [Justify Content property](https://wiki.genexus.com/commwiki/wiki?36108) |
| [Max number of lines control property](https://wiki.genexus.com/commwiki/wiki?30795) | [QueryViewer control properties](https://wiki.genexus.com/commwiki/wiki?32920) | [Width property](https://wiki.genexus.com/commwiki/wiki?38374) |

---
