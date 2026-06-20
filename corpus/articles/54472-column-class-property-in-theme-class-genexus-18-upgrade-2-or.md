---
title: "Column Class property in Theme Class (GeneXus 18 Upgrade 2 or prior)"
source_id: 54472
source_url: https://wiki.genexus.com/commwiki/wiki?54472
genexus_version: "18"
---

# Column Class property in Theme Class (GeneXus 18 Upgrade 2 or prior)

Sets the class to style all the grid columns.

### [Scope](#Scope)

**Level:** [Theme Class](https://wiki.genexus.com/commwiki/wiki?6246)

### [Description](#Description)

The **Column Class property** is available for the Grid Class (as well as for all child classes of the Grid class) of every [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420).

`[imagen omitida: wiki id 55794]`

The **Column Class property** must be configured with the GridColumn class or with a child class of the GridColumn class.

By setting the properties of the GridColumn class and/or their child classes, you define different styles to be applied to all the columns of a grid.

Finally, each Grid has its own Class property that by default is configured with the Grid class of the Web Theme you are using. You can keep this value or change it for a child class of the Grid class to style each Grid as you wish.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Suppose you define a [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420) and [make the configuration to use it](https://wiki.genexus.com/commwiki/wiki?8145).

Below the Grid class, you define a child class named "GridProduct".

`[imagen omitida: wiki id 55799]`

Its **Column Class property** must be configured with the GridColumn class or with a child class of the GridColumn class. So, you define a child class of the GridColumn class named "GridColumnProduct" and assign it to the **Column Class property**as explained before​​​​​​.

For the "GridColumnProduct" class, for example, you set its Background Color property to a specific color:

`[imagen omitida: wiki id 55804]`

Finally, to add style to all the grid columns of a Web Panel, you set the Class property of the Grid to **GridProduct**class.

`[imagen omitida: wiki id 55798]`

When you run the Web Panel, its entire Grid is shown as follows:

`[imagen omitida: wiki id 55805]`
