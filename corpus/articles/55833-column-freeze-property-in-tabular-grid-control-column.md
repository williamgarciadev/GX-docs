---
title: "Column Freeze property in Tabular Grid Control Column"
source_id: 55833
source_url: https://wiki.genexus.com/commwiki/wiki?55833
genexus_version: "18"
---

# Column Freeze property in Tabular Grid Control Column

Indicates whether the column is fixed or not. If fixed, it specifies where it is fixed (at the start or end position).

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | The column is NOT fixed and it moves when scrolling horizontally. This is the default value. |
| **Start** | The column is fixed at the start position (as the first column or after another fixed column that is the first column). |
| **End** | The column is fixed at the end position (as the last column or before another fixed column that is the last column). |

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Controls:** [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449)

### [Description](#Description)

This property allows indicating that a column is fixed in a certain position (Start, End) when scrolling horizontally.

When dragging a fixed column, it can only be moved in the part of other fixed columns in the same zone (Start, End).

In addition, it is not possible to drag a non-fixed column into the fixed columns zone.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240).

### [See Also](#See+Also)

[Column Visible property](https://wiki.genexus.com/commwiki/wiki?55858)  
[Column Hidden property](https://wiki.genexus.com/commwiki/wiki?55816)  
[Column Title Visible property](https://wiki.genexus.com/commwiki/wiki?55860)  
[Column Image property](https://wiki.genexus.com/commwiki/wiki?55829)  
[Column Tooltip property](https://wiki.genexus.com/commwiki/wiki?55830)  
[Column Resizable property](https://wiki.genexus.com/commwiki/wiki?55876)  
[Column Hideable property](https://wiki.genexus.com/commwiki/wiki?55877)


|  |
| --- |
| **Backlinks** |
| [Column Hidden property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55816) | [Column Hideable property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55877) | [Column Image property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55829) |
| [Column Resizable property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55876) | [Column Title Visible property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55860) | [Column Tooltip property in Tabular Grid Control Column](https://wiki.genexus.com/commwiki/wiki?55830) | [Column Visible property in Tabular Grid control Column](https://wiki.genexus.com/commwiki/wiki?55858) |
| [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240) |

---
