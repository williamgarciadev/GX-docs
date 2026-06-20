---
title: "Smart Table control"
source_id: 45577
source_url: https://wiki.genexus.com/commwiki/wiki?45577
genexus_version: "18"
---

# Smart Table control

Over time, web languages have evolved and new standards and practices have emerged that enable HTML modeling in a much more sophisticated and efficient way.

In the case of HTML Tables, there have been transformations that allow modeling scenarios ranging from adjusting the layout based on screen size ([Responsive Tables](https://wiki.genexus.com/commwiki/wiki?24961)) to new ways of writing layouts to organize and display information, such as [Flex Tables](https://wiki.genexus.com/commwiki/wiki?40521) and later **Smart Tables**.

### [Smart Table control](#Smart+Table+control)

Technically, the Smart Table control in HTML is a two-dimensional grid-based layout (rows and columns) that allows you to model elements within a structure in a simpler way.  
The difference with the Flex Table is that, in the case of Flex, it is designed to model elements in a dimension (rows or columns), while in the case of the Smart Table it is possible to define both rows and columns. In short, it is a matrix that allows showing static information in an attractive way.

To add a Smart Table to a Form, drag the "Smart Table" control from the toolbox (`[imagen omitida: wiki id 45578]`) to the desired location:

`[imagen omitida: wiki id 45579]`

Once the control is placed inside the object, its properties are enabled:

`[imagen omitida: wiki id 45581]`

#### Columns Style

Sets the width of each column. An entry will appear for each column that is added to the Smart Table.  
Valid units that may be used are %, px, and dip.

`[imagen omitida: wiki id 45582]`

#### [Rows Style](#Rows+Style)

Sets the height of each row. An entry will appear for each row that is added to the Smart Table.  
Valid units that may be used are %, px, and dip.

`[imagen omitida: wiki id 45583]`

#### [Columns Gap](#Columns+Gap)

Space between columns:

`[imagen omitida: wiki id 45584]`

#### [Rows Gap](#Rows+Gap)

Space between rows:

`[imagen omitida: wiki id 45585]`

#### [Width](#Width)

Total width of the Smart Table (by default it is the sum of all the defined columns).

#### [Height](#Height)

Total height of the Smart Table (by default it is the sum of all the defined rows).

### [Restrictions](#Restrictions)

Because this is an implementation of CSS Grid Layout, Internet Explorer support is [limited](https://caniuse.com/#feat=css-grid).

### [Availability](#Availability)

The Smart Table control is available from [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,).

### [Sample Knowledge Base](#Sample+Knowledge+Base)

See [TravelAgency Knowledge Base](https://wiki.genexus.com/commwiki/wiki?21975)

### [See also](#See+also)

[Table control](https://wiki.genexus.com/commwiki/wiki?6001)  
[Flex control](https://wiki.genexus.com/commwiki/wiki?40521)  
[Responsive Table control](https://wiki.genexus.com/commwiki/wiki?24961)


|  |
| --- |
| **Backlinks** |
| [Columns Gap property](https://wiki.genexus.com/commwiki/wiki?44736) | [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) |
| [Header property](https://wiki.genexus.com/commwiki/wiki?17942) | [Is Slot property](https://wiki.genexus.com/commwiki/wiki?51306) | [Rows Gap property](https://wiki.genexus.com/commwiki/wiki?44737) |

---
