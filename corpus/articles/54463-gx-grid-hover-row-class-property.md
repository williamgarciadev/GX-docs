---
title: "gx-grid-hover-row-class property"
source_id: 54463
source_url: https://wiki.genexus.com/commwiki/wiki?54463
genexus_version: "18"
---

# gx-grid-hover-row-class property

Sets the class that is assigned when the row is hovered.

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
     gx-grid-hover-row-class: GridRowHover
}
```

**Where:**

```
.GridRowHover
{
        @include GridRow;
        background-color: black;
        color: white;
}
```

### [See Also](#See+Also)

[DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707)


|  |
| --- |
| **Backlinks** |
| [Hover Row Class property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54477) | [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) |

---
