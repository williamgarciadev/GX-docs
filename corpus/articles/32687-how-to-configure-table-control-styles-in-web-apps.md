---
title: "How to configure Table control styles in web apps"
source_id: 32687
source_url: https://wiki.genexus.com/commwiki/wiki?32687
genexus_version: "18"
---

# How to configure Table control styles in web apps

The [Table control](https://wiki.genexus.com/commwiki/wiki?6001) and [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961) Rows settings (Even Rows, Odd Rows, First Row, Last Row), as well as Cell properties, can be easily configured using the Theme.

The **TableRow** and the **TableCell** Theme classes are introduced for that purpose.

### [How to configure the Row settings of a table](#How+to+configure+the+Row+settings+of+a+table)

This can be done using the following Table Theme Class properties under the "Table Rows" section:

* [gx-grid-row-class property](https://wiki.genexus.com/commwiki/wiki?32772)
* Even Row Class
* Odd Row Class
* First Row Class
* Last Row Class

Any of these properties can be associated with a **TableRow** class (or a descendant of it) where you can configure the Rows style as you want.

`[imagen omitida: wiki id 32689]`

In order to set the cell style of a row, use the Cell Class property of the TableRow Class. There you can assign the **TableCell** property (or one of its descendants).

`[imagen omitida: wiki id 32690]`

### [Note](#Note)

The Row Class property is also available at the control level, so you can also configure a TableRow class for that row in the table itself.  
The same happens for the [gx-table-row-cell-class property](https://wiki.genexus.com/commwiki/wiki?25796), which can be configured in the control.
