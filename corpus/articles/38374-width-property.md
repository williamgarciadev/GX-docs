---
title: "Width property"
source_id: 38374
source_url: https://wiki.genexus.com/commwiki/wiki?38374
genexus_version: "18"
---

# Width property

Determines the width of a control. A numeric value must be assigned.

### [Syntax](#Syntax)

**control.** Width = Expression   

**Where:**  
*Control*

    Is the name of a control inserted in the form  
  
*Expression*

    In images and bitmap type variables the value of the inserted control is proposed by default, but it can be modified to change its size. It indicates the control width in pixels.  
    In tables, cells, grids, grids columns describes the width desired for the tables. This can be specified in pixels (nnn) or as a percentage of the window width (nnn%). The browser has a complex heuristic that is applied to the tables and their cells to present a table in the best possible manner. When we fix this property we replace this heuristic and focus the effort on putting the desired width according to what was specified.   
    In the tables, when we specify the values as percentages, these percentages are relative to the window or to the cell where the window is located.  
    We must take into account that, when we assign a value to this property in a table, we are indicating the minimum desired value; i.e.: if there is a larger control within the table, we will assign the required size to include this control. Thus, the size will be larger than the specified one.   
    In Edit control width is given in chr. In runtime this value is included as a cols attribute of the textarea.

### [Description](#Description)

This property allows establishing the control width. It will be enabled only when the AutoResize property has the ‘False’ value.  
  
**Design Time****:** Applies to bitmap type variables, embedded pages, images, tables, table cells.  
  
**Execution Time****:** Applies to buttons, frames, grids, free style grids, texts, radio buttons, check boxes, dynamic combo boxes, combo boxes, edits, list boxes, dynamic list boxes and tables.

### [Samples](#Samples)

* photo.Width = 200 (photo is a bitmap control). The bitmap control’s width will be 200 pixels.
* If we want a table to occupy the whole window width, we put width=100% in the table property. The same happens if we have a table within another one and we want the inside table to occupy the whole width of the outside table cell.
* If we want a table column to occupy the minimum size of 200 pixels, we put width=200 in one of the column's cells.
* If we have a table with 2 columns and we want the first one to occupy 80% and the second 20% regarding the table, we put the property width=80% for a cell of the first column. This will be enough, since the 20% of the second one will be deducted.
* Edit control Width = 120chr is created as <textarea cols="120"....>

### [Scope](#Scope)

**Objects:** Transaction, Web Panel  
**Platforms:** Web(.Net, Java)  
**Controls:** Embedded Page, FreeStyle Grid, Grid, Image, Table

### [See Also](#See+Also)

[Height property](https://wiki.genexus.com/commwiki/wiki?8792)  
[Auto Resize property](https://wiki.genexus.com/commwiki/wiki?8687)


|  |
| --- |
| **Backlinks** |
| [Align Items property](https://wiki.genexus.com/commwiki/wiki?36111) | [Attribute/Variable control properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8133) | [Auto Resize property in QueryViewer control](https://wiki.genexus.com/commwiki/wiki?19597) |
| [Free Style Grid Properties](https://wiki.genexus.com/commwiki/wiki?9760) | [Justify Content property](https://wiki.genexus.com/commwiki/wiki?36108) | [QueryViewer control properties](https://wiki.genexus.com/commwiki/wiki?32920) | [WidthUnit property](https://wiki.genexus.com/commwiki/wiki?8795) |

---
