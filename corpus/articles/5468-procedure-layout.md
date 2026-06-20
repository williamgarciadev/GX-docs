---
title: "Procedure Layout"
source_id: 5468
source_url: https://wiki.genexus.com/commwiki/wiki?5468
genexus_version: "18"
---

# Procedure Layout

If you need to generate a visual output in a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), you have to access to the Procedure **Layout** section in order to define the data to be listed and the output format.

`[imagen omitida: wiki id 5469]`

By default, the **Layout** section contains a first [printblock](https://wiki.genexus.com/commwiki/wiki?1958)(named: printBlock1), which is empty and ready to be used. Inside it, you can include whatever you want to show.

Suppose you have to define a procedure in order to list all the airlines a Travel Agency works with.

Since the procedure **Layout** is composed by one or several printblocks (that do not necessarily have to respond to the same order as required for the output), each printblock must have one single name to be referenced from the [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) (by using the [Print command](https://wiki.genexus.com/commwiki/wiki?5479)).

In the example, the first printblock will contain a logo, a title, the current day and hour, the page number, labels with titles and a line. So, insert those controls inside the printblock and rename it as "Pb\_Header" (by modifying the printblock **Name** property).

`[imagen omitida: wiki id 5470]`

Observe the elements that were added to the "Pb\_Header" printblock. Most of the actions were achieved through [drag&drop](https://wiki.genexus.com/commwiki/wiki?5060) from the available Toolbox for this section:

`[imagen omitida: wiki id 31553]`

and by setting the controls properties.

In particular to insert the logo, the **Image** icon has to be dragged from the Toolbox to the printblock and a dialog is opened offering you some possibilities, such as import the image from a file.

The system variables such as &Date, &Time and &Page, can be inserted by selecting: **Insert > Variable...** from the Menubar or by dragging and dropping the **Attribute/Variable** control from the Toolbox.

### [Inserting Printblocks](#Inserting+Printblocks)

Inserting printblocks is very simple. To do so, you have to right-click on a specific printblock and select from the context menu the **Insert Printblock** option. This action will insert a new printblock below it.

`[imagen omitida: wiki id 31555]`

Look at the following figure. The second printblock has been inserted in the Layout section and the AirlineId and AirlineName attributes have been added to it.

`[imagen omitida: wiki id 5474]`

To change a printblock'sposition, the context menu offers the **Move Up** and **Move Down** options.

### [Aligning and Resizing Controls](#Aligning+and+Resizing+Controls)

To align several controls at once (or to make them the same size), select them by holding down the Ctrl (or Shift) key and clicking on the desired controls. The last one (which will have its selection nodes highlighted in bold) will be the reference control for the action. Then, you only have to right-click and select from the context menu the option you are needing.

`[imagen omitida: wiki id 5667]`

### [Inserting a variable based on an SDT](#Inserting+a+variable+based+on+an+SDT)

You can also insert in any printblock a variable that is based on a [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021). The options to insert it in the printblock are the same as for any variable. A dialog will be opened so that you can select which members you want to include in the printblock. One control for each member will be inserted and their **FieldSpecifier** property (which is mandatory) is for setting the collection position to be shown.

### [Invoking the Printblocks](#Invoking+the+Printblocks)

Remember the procedure logic is written in the [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) and from there, the Printblocks defined in the **Procedure Layout** must be invoked using the [Print command](https://wiki.genexus.com/commwiki/wiki?5479):

`[imagen omitida: wiki id 31577]`

Note that:

* The [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) is used as in any procedure to navigate in this case the Airline table and one of the printblocks is referenced inside it in order to print the scanned data.
* The other printblock is referenced inside the [Header command](https://wiki.genexus.com/commwiki/wiki?7994) in order to be printed at the top of each page.

### Layout Properties

You may access another set of [properties](https://wiki.genexus.com/commwiki/wiki?16180,,) (such as paper height, width, orientation, and so on) by clicking on the arrow in the upper left-hand corner of the layout window:

`[imagen omitida: wiki id 8574]`

### Note

In most cases, procedures with **Layout** are defined in order to print PDF outputs. Therefore, the following simple [requirements](https://wiki.genexus.com/commwiki/wiki?13531) must be set for the object.

### See Also

[Printing Commands Summary](https://wiki.genexus.com/commwiki/wiki?5526)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Lists and For Each command to query the database](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/lists-and-for-each-command-to-query-the-database-6104762)


|  |
| --- |
| **Backlinks** |
| [Alignment property](https://wiki.genexus.com/commwiki/wiki?28993) | [Border Style property for Rectangle controls](https://wiki.genexus.com/commwiki/wiki?29323) | [Corner Radius property](https://wiki.genexus.com/commwiki/wiki?29321) |
| [Customizable Layout property](https://wiki.genexus.com/commwiki/wiki?24473) | [End user customizable reports](https://wiki.genexus.com/commwiki/wiki?18909) | [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) | [Form and layout comparer](https://wiki.genexus.com/commwiki/wiki?22712) |
| [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Output variable](https://wiki.genexus.com/commwiki/wiki?8101) | [PDF Reports](https://wiki.genexus.com/commwiki/wiki?13531) | [PDF Reports (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54937) |
| [PDF Reports (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55935) | [Print If Detail Command](https://wiki.genexus.com/commwiki/wiki?5467) | [Printblock control](https://wiki.genexus.com/commwiki/wiki?1958) | [Category:Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) |
| [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) | [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |
| [Category:Static reports](https://wiki.genexus.com/commwiki/wiki?5489) | [View Layout Option](https://wiki.genexus.com/commwiki/wiki?9984) |

---
