---
title: "Elements Property"
source_id: 19577
source_url: https://wiki.genexus.com/commwiki/wiki?19577
genexus_version: "18"
---

# Elements Property

You can use this property to act programmatically on the chart elements. It contains the name of the variable based on the QueryViewerElements SDT.

### [Values](#Values)

|  |  |
| --- | --- |
| **&Elements** | Name of the variable that will implement the changes’ inherent properties. This is the default value. |

### [QueryViewerElements SDT Structure](#QueryViewerElements+SDT+Structure)

`[imagen omitida: wiki id 47181]`

### [Example](#Example)

For the following example, the following query is taken as a reference.

`[imagen omitida: wiki id 47183]`

The information displayed can often be lengthy when the elements that comprise it are expanded (default setting). This may be easily avoided by collapsing all the elements starting from the first one, or from another element close to the first one. Later on, the user will expand those nodes as needed.

In the image below, the PivotTable is completely expanded.

`[imagen omitida: wiki id 47184]`

The following code shows how to completely collapse all the elements for the *Brand* element.

```
Event Start
    &Element = New()
    &Element.Name = !"CarBrandName"
    &Element.ExpandCollapse.Type = QueryViewerExpandCollapse.CollapseAllValues
    &Elements.Add(&Element)
EndEvent
```

The result would be as follows:

`[imagen omitida: wiki id 47185]`

Besides, if you don't want to display its subtotals, you can add the following to the previous code:

```
    &Element.Format.Subtotals = QueryViewerSubtotals.No
```

and the result would be as shown in the image below.

`[imagen omitida: wiki id 47186]`

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Output type:** | Table, PivotTable, Chart, Card |


|  |
| --- |
| **Backlinks** |
| [Axis and Visible property refactoring](https://wiki.genexus.com/commwiki/wiki?47094) | [Query Object Compatibility](https://wiki.genexus.com/commwiki/wiki?11032) |
| [Category:QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) | [QueryViewer control properties](https://wiki.genexus.com/commwiki/wiki?32920) |

---
