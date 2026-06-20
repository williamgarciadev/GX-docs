---
title: "How to change cell width in RWA"
source_id: 26077
source_url: https://wiki.genexus.com/commwiki/wiki?26077
genexus_version: "18"
---

# How to change cell width in RWA

The [Web Abstract Editor](https://wiki.genexus.com/commwiki/wiki?24795) helps the designer to set the width of the cells in percentages for each screen size.

Depending on the width given to a cell for a screen size, a [Bootstrap](http://getbootstrap.com/) class is assigned to that cell at runtime. So at the end, the width of the cells is given by bootstrap classes.

In some cases, you may need to change the width of any of those cells and set a width value different than the values belonging to the range given by Boostrap (8%, 17%, 25%, 33%, 42%, 50%, 58%, 67%, 75%, 83%, 92%, 100%). In general, this won't be necessary, but if it is necessary to declare a width in pixels, the max-width property should be used.

The same happens with the padding values of the Bootstrap classes. By default, its classes have a padding value different than zero, but this can be changed as explained below.

### [Example](#Example)

Consider the following example:

Three items need to be displayed in a single row for medium and large devices (>=992px). In this example, the first cell takes 67%, while the other two take 8% of the width. The following picture shows the [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961) where those items are displayed and the [Responsive Sizes property (X Evolution 3)](https://wiki.genexus.com/commwiki/wiki?25478,,) dialog for this table.

`[imagen omitida: wiki id 26078]`

In particular, the second item of the row (the second cell) takes 8% of the width, plus the padding given by the Boostrap class assigned to it.

The following picture shows the runtime design.

`[imagen omitida: wiki id 26079]`

If you need to change the default settings, you can define a Cell Class and assign it to the cell, as shown in the figure:

`[imagen omitida: wiki id 26081]`

In this case, two classes have been defined in the Theme - ImageCartCell2 and nopadding - which have been associated with the [gx-table-row-cell-class property](https://wiki.genexus.com/commwiki/wiki?25796) of the element.

The definition of each class is as follows:

```
.ImageCartCell2
{
    max-width: 64px;}

.nopadding
{
    padding: 0 !important;}
```

After these settings are made, the resulting design is as shown below:

`[imagen omitida: wiki id 26082]`

### [See Also](#See+Also)

* [Responsive Web Design in GeneXus](https://wiki.genexus.com/commwiki/wiki?25186,,)


|  |
| --- |
| **Backlinks** |
| [Arranging the layout in a RWA](https://wiki.genexus.com/commwiki/wiki?25514) |

---
