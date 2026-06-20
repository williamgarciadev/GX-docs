---
title: "Vertical Alignment property"
source_id: 28650
source_url: https://wiki.genexus.com/commwiki/wiki?28650
genexus_version: "18"
---

# Vertical Alignment property

Vertical Alignment is a control property for [Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159), whose purpose is to align the control to the top, middle or bottom of the cell where it's contained. In fact, it's a property of the control cell.

### [Values](#Values)

Default, Top, Middle, Bottom

By default, the height of a responsive cell is the same as the height of the cell contents. The only way to vertically align the contents of a cell (to the top, middle or bottom), is to give it a fixed height greater than the height of the contents.

Also, not all the columns of the same responsive row have the same height. The height is given by the contents of the cell, as mentioned before.

### [Example](#Example)

Consider the following example where the attribute "ArticleCode" is going to be vertically aligned to the middle of the cell.

`[imagen omitida: wiki id 28651]`

To get the desired results, the cell is assigned to a class where the height is given a fixed value:

`[imagen omitida: wiki id 28652]`

Another possibility is to assign a fixed height to the row, using the *Row Height property* (available as since GeneXus 15).

`[imagen omitida: wiki id 32381]`

### [Availability](#Availability)

As from GeneXus X Evolution 3 upgrade 4.

### [See Also](#See+Also)

[Horizontal Alignment property](https://wiki.genexus.com/commwiki/wiki?28263)


|  |
| --- |
| **Backlinks** |
| [Horizontal Alignment property](https://wiki.genexus.com/commwiki/wiki?28263) |

---
