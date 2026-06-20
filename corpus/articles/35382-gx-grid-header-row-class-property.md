---
title: "gx-grid-header-row-class property"
source_id: 35382
source_url: https://wiki.genexus.com/commwiki/wiki?35382
genexus_version: "18"
---

# gx-grid-header-row-class property

Sets the class to style the header.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

It allows setting a style for the header row of the grid.

At the same time, it must be assigned to any [Design System Class](https://wiki.genexus.com/commwiki/wiki?49309) that is below the node of the "GridRow" predefined class.

**Notes:**

* This property is valid for the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s.
* Since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853), this property is valid for the [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) in [Panels](https://wiki.genexus.com/commwiki/wiki?24829) (for [Angular](https://wiki.genexus.com/commwiki/wiki?42550) generator).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Once you have associated the Grid with the "GridLiteraryWork" class, you need to configure the *Header Class* property of the class with any class (GridRow or one of its descendants). In the example, the class is "GridHeadLWRow".

Next, configure the class according to how you want the grid's header row to look.

The Grid will look as follows:

`[imagen omitida: wiki id 35399]`

### [See Also](#See+Also)

[Design System Object](https://wiki.genexus.com/commwiki/wiki?47375)  
[DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707)


|  |
| --- |
| **Backlinks** |
| [gx-grid-column-header-class property](https://wiki.genexus.com/commwiki/wiki?35383) | [gx-grid-header-row-class property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54491) | [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) |

---
