---
title: "Auto Grow in Grids for Native Mobile Applications"
source_id: 22697
source_url: https://wiki.genexus.com/commwiki/wiki?22697
genexus_version: "18"
---

# Auto Grow in Grids for Native Mobile Applications

Grids in Native Mobile Applications support the [Auto Grow property](https://wiki.genexus.com/commwiki/wiki?20204). Its purpose is to enable scrolling of the whole screen and not only the grid when the grid has more rows to show than the display can show.

Take a look at the Light CRM default screen:

`[imagen omitida: wiki id 22700]`

What if you want the text block "The Companies listed are the following" to scroll too when scrolling the [Grid](https://wiki.genexus.com/commwiki/wiki?24817)?

Using Auto Grow Property the Grid can be configured so that when a Grid grows the scroll moves the whole screen instead of just scrolling the grid.

`[imagen omitida: wiki id 22704]`

### [Considerations](#Considerations)

* The Cells of the Grid must be of fixed height. No element inside de Grid should have Auto Grow enabled.
* The Grid can't have the search option available.
* A grid with *A**uto Grow* can't have paging. This is because as the scroll is not going to be on the grid the next page of records is never retrieved from the server.
* The grids in a table with *A**uto Grow*enabled must have the *A**uto Grow* property set too. Grids with the scroll in a panel with scroll (nested scrolls) do not work due to Android limitations.

### [Sample](#Sample)

You can see this example working on the [LightCRM (X Evolution 2)](https://wiki.genexus.com/commwiki/wiki?21779,,) sample.

### [Note](#Note)

* In case that [Rows property](https://wiki.genexus.com/commwiki/wiki?2452)=N (a numeric value) and Autogrow=False, the Grid control will not make pagination, it will load only N rows instead.

### [Availability](#Availability)

This options is available as of [GeneXus X Evolution 2 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?22626,,).


|  |
| --- |
| **Backlinks** |
| [Auto Grow property](https://wiki.genexus.com/commwiki/wiki?20204) | [Enable Header Row Pattern property](https://wiki.genexus.com/commwiki/wiki?29843) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
