---
title: "gx-grid-header-row-class property (GeneXus 18 Upgrade 2 or prior)"
source_id: 54491
source_url: https://wiki.genexus.com/commwiki/wiki?54491
genexus_version: "18"
---

# gx-grid-header-row-class property (GeneXus 18 Upgrade 2 or prior)

Sets the class to style the grid's header.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

It allows setting a style for the header row of the grid.

At the same time, it must be assigned to any [Design System Class](https://wiki.genexus.com/commwiki/wiki?49309) that is below the node of the "GridRow" predefined class.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Once you have associated the Grid with the "GridLiteraryWork" class, you need to configure the *Header Class* property of the class with any class (GridRow or one of its descendants). In the example, the class is "GridHeadLWRow".

Next, configure the class according to how you want the grid's header row to look.

The Grid will look as follows:

`[imagen omitida: wiki id 35399]`

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See Also](#See+Also)

[Design System Object](https://wiki.genexus.com/commwiki/wiki?47375)
