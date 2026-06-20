---
title: "HowTo: Use Horizontal Grid control in Web Panels"
source_id: 30594
source_url: https://wiki.genexus.com/commwiki/wiki?30594
genexus_version: "18"
---

# HowTo: Use Horizontal Grid control in Web Panels

[Horizontal Grid Control](https://wiki.genexus.com/commwiki/wiki?30592) is a way of viewing the elements of a list in a carousel style.

The Horizontal Grid for web applications requires using the [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209) and it should be used for [Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159).

## [How to use the control](#How+to+use+the+control)

Drag a Free Style Grid control to the web form, and set the [Custom Render property](https://wiki.genexus.com/commwiki/wiki?11407) to Horizontal Grid.

`[imagen omitida: wiki id 30595]`

Configure the following properties:

* [Columns property for Free Style Grids in RWD](https://wiki.genexus.com/commwiki/wiki?26600). This property is for any Free Style grid, even those with no horizontal rendering.
* Rows per Page. This property is under the Horizontal grid section of the properties panel of the grid. It allows configuring how many rows will be shown per page depending on the viewport size.  
  Those sizes are the same as the ones considered in the [Responsive Sizes property](https://wiki.genexus.com/commwiki/wiki?29125) dialog.  
  The following figure shows a grid where Columns = 2, and Rows per Page = 2 when the viewport size = small.

`[imagen omitida: wiki id 30601]`

`[imagen omitida: wiki id 30603]`

## [Horizontal Grid properties](#Horizontal+Grid+properties)

|  |  |
| --- | --- |
| **Paged** | Indicates whether the view will display items page-by-page, with each page containing the most ColumnsPerPage\*RowsPerPage items |
| **Show Page Controller** | Specifies whether or not the page controller will be displayed |
| **Page Controller Class** | Class for the page controller |
| **Show Arrows** | Enable Next/Previous arrows |
| **Infinite** | Enable infinite loop sliding (a carousel). |
| **Auto Play** | Auto-play is enabled, or not? |
| **Auto Play Speed** | Speed in milliseconds. |
| **Variable Width** | When Variable Width is enabled, the visible area shows as many slides as possible, according to the width of each slide. Column properties indicate how many slides are scrolled each time a page is changed |
| **Rows per page** | Sets the number of Rows per page for each screen size |
| **CurrentPage** | Gets or sets the current control page (only Runtime property). |

## [Configuring the appearance of the Horizontal Grid](#Configuring+the+appearance+of+the+Horizontal+Grid)

The grid Page Controller Class property allows assigning a Theme Class to configure some style settings for the grid.

The default for Page Controller Class property is GridPageController class, but you can use any of its descendants.

The GridPageController class has the following properties:

|  |  |
| --- | --- |
| [Controller Container Class property](https://wiki.genexus.com/commwiki/wiki?41602,,) | Class used to style the controller's container box (See the image example below). |
| [Indicator Selected Color](https://wiki.genexus.com/commwiki/wiki?47690) | Color of the selected page indicator. |
| [Indicator Unselected Color](https://wiki.genexus.com/commwiki/wiki?47709) | Color of the unselected page indicator. |
| [Indicator Symbol property](https://wiki.genexus.com/commwiki/wiki?41603) | Symbol used for the page indicator. [UTF-8 symbols](http://www.w3schools.com/charsets/ref_utf_symbols.asp) are supported (For example, use \2022 for a dot). |
| [Arrows Color property](https://wiki.genexus.com/commwiki/wiki?41604) | Color of the arrows used to scroll. |
| [Left scrolling arrow symbol property](https://wiki.genexus.com/commwiki/wiki?41605) | Symbol used to scroll to the left. It can be a symbol or its UTF8 representation. |
| [Right scrolling arrow symbol property](https://wiki.genexus.com/commwiki/wiki?41606) | Symbol used to scroll to the right. It can be a symbol or its UTF8 representation. |

`[imagen omitida: wiki id 33019]`

### [Example](#Example)

`[imagen omitida: wiki id 30604]`


|  |
| --- |
| **Backlinks** |
| [Arrows Color property](https://wiki.genexus.com/commwiki/wiki?41604) | [Horizontal Grid Control](https://wiki.genexus.com/commwiki/wiki?30592) |
| [Indicator Symbol property](https://wiki.genexus.com/commwiki/wiki?41603) | [Left scrolling arrow symbol property](https://wiki.genexus.com/commwiki/wiki?41605) | [Right scrolling arrow symbol property](https://wiki.genexus.com/commwiki/wiki?41606) |

---
