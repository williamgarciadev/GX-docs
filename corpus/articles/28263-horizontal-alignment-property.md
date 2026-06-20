---
title: "Horizontal Alignment property"
source_id: 28263
source_url: https://wiki.genexus.com/commwiki/wiki?28263
genexus_version: "18"
---

# Horizontal Alignment property

Horizontal Alignment is a control property for [Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159), whose purpose is to align the control to the left, right or center of the cell where it's contained. In fact, it's a property of the control cell.

### [Values](#Values)

Default, Left, Center, Right.

### [Example](#Example)

Consider a web page header where the logo is sent to the top left corner, and the "welcome user name" text is sent to the top right corner for medium and large screens.

1. Drag a [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961) to the form, which will contain:

* the image of the logo, and
* the [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961) containing the welcome message (named "HeaderTable" here).

Configure its width in percentages for the cell containing the logo. The "HeaderTable" occupies the remaining percentage.

`[imagen omitida: wiki id 27766]`

2. In the "HeaderTable", insert a common [Table control](https://wiki.genexus.com/commwiki/wiki?6001) whose control name is "MessageTable" in this example. The table control has no fixed width and takes all the horizontal space necessary for its content to be displayed without wrapping.

`[imagen omitida: wiki id 27767]`

3. Edit the "MessageTable" properties and configure the Horizontal Alignment property to Right.

`[imagen omitida: wiki id 28264]`

### [Scope](#Scope)

Objects:    [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)  
Controls:    All  
Interfaces:    Web

### [Availability](#Availability)

As from [GeneXus X Evolution 3 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?28251,,).

### [See Also](#See+Also)

[Vertical Alignment property](https://wiki.genexus.com/commwiki/wiki?28650)


|  |
| --- |
| **Backlinks** |
| [Vertical Alignment property](https://wiki.genexus.com/commwiki/wiki?28650) |

---
