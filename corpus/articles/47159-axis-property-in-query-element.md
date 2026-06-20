---
title: "Axis property in Query Element"
source_id: 47159
source_url: https://wiki.genexus.com/commwiki/wiki?47159
genexus_version: "18"
---

# Axis property in Query Element

Sets where the query element will be presented (specific to the Pivot Table).

### [Values](#Values)

|  |  |
| --- | --- |
| **Columns** | It’s the one that has the column headers, and in particular, are present in the Pivot table view. It’s ideal for creating a data matrix or showing trends over time. Any column can be dragged to the filters area and vice versa. |
| **Pages** | This area is located above the control and contains an optional group of one or more drop-down controls, similar to combo boxes. |
| **Rows** | It shows the field’s unique values on the left side. Typically, this area has at least one field even though it may have none. The data types included here are those that group and categorize. |

### [Scope](#Scope)

**Objects:** [Query](https://wiki.genexus.com/commwiki/wiki?9026)

### [Description](#Description)

An Axis can be set as:

* Rows
* Columns
* Pages

The property is only valid when the Output is a PivotTable; it does not apply to the case of Table, Card, or Chart.

### [Rows](#Rows)

It shows the field’s unique values on the left side. Typically, this area has at least one field even though it may have none. The data types included here are those that group and categorize, such as products, names, places, etc. and they can be of any type.

### [Columns](#Columns)

It’s the one that has the column headers, and in particular, are present in the Pivot table view. It’s ideal for creating a data matrix or showing trends over time. Any column can be dragged to the filters area and vice versa.

### [Pages](#Pages)

This area is located above the control and contains an optional group of one or more drop-down controls, similar to combo boxes. Usually, the types of fields included here are those to be isolated from the rest to obtain a different view of the entire table.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Samples](#Samples)

`[imagen omitida: wiki id 47172]`

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Build with this Only of the object.

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,).

### [See Also](#See+Also)

[Type property in Query Element](https://wiki.genexus.com/commwiki/wiki?47137)  
[Visible property in Query Element](https://wiki.genexus.com/commwiki/wiki?47140)


|  |
| --- |
| **Backlinks** |
| [Axis and Visible property refactoring](https://wiki.genexus.com/commwiki/wiki?47094) | [Type property in Query Element](https://wiki.genexus.com/commwiki/wiki?47137) |

---
