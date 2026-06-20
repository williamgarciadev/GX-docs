---
title: "Column Size property in Tabular Grid Control Column"
source_id: 55506
source_url: https://wiki.genexus.com/commwiki/wiki?55506
genexus_version: "18"
---

# Column Size property in Tabular Grid Control Column

Configures the size of a column included in a Tabular Grid.

### [Values](#Values)

|  |  |
| --- | --- |
| **Minimum content** | Indicates that the size of the column will be determined based on the minimum required content. In other words, the column will automatically adjust its width to accommodate the smallest amount of content within it. |
| **Maximum content** | Indicates that the size of the column will be determined based on the maximum content it contains. The column will expand its width to accommodate the widest content within it. |
| **Autoexpand** | The column will automatically expand or shrink its size based on the available space in the layout or container. It allows the column to dynamically adjust its width to fill the available space while considering the content within it. |
| **Fraction** | The available space is distributed proportionally. |
| **From ColumnClass** | The column size is determined by the class indicated in the Column Class property of the column. |

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Controls:** [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449)

### [Description](#Description)

The **Column Size property** is available when you are positioned in a column of a [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) included in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

**1)** If a Tabular Grid contains three columns and all of them have their **Column Size property** set to "Fraction", each column size will be 33% of the total.

**2)** Consider a Tabular Grid whose size is 500 px and contains three columns. If the first column size is 100 px and the other two columns have their **Column Size property** set to "Fraction", then 500 px - 100 px = 400 px. Therefore, 400 px are to be split between two columns (each column size would be 200 px).

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).


|  |
| --- |
| **Backlinks** |
| [gx-grid-column-size property](https://wiki.genexus.com/commwiki/wiki?56550) |

---
