---
title: "gx-grid-selected-row-class property"
source_id: 54462
source_url: https://wiki.genexus.com/commwiki/wiki?54462
genexus_version: "18"
---

# gx-grid-selected-row-class property

Sets the class for when a selection is made in the row.

### [Scope](#Scope)

**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

You can configure this property in the [Styles](https://wiki.genexus.com/commwiki/wiki?47379) tab of a [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) for the Grid class.

**Notes:**

* This property is valid for the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s.
* Since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853), this property is valid for the [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) in [Panels](https://wiki.genexus.com/commwiki/wiki?24829) (for [Angular](https://wiki.genexus.com/commwiki/wiki?42550) generator).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

This property is defined as follows:

```
.TabularGrid
{
      gx-grid-selected-row-class: GridRowSel
 }
```

**Where:**

```
.GridRowSel
{
       @include GridRow;
        color: yellow;
 }
```

### [See Also](#See+Also)

[DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707)


|  |
| --- |
| **Backlinks** |
| [Selected Row Class property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54476) | [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) |

---
