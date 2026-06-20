---
title: "Magazine Viewer Control"
source_id: 17567
source_url: https://wiki.genexus.com/commwiki/wiki?17567
genexus_version: "18"
---

# Magazine Viewer Control

It displays information in Magazine format, which doesn’t mean that only news articles can be included. Basically, it can be used to show any product catalog, recipes, songs, and so on. Even a list of Clients could be shown in this way, as this is only a new way to display a list of data in a certain desired format.

**How to use it**

The Magazine Viewer is a Grid with its **Control Type** property set to Magazine Viewer.

**Properties**

* Show footer: boolean, it hides or displays the footer
* Header Text: it adds a header in the upper section
* **Page Layout**: it allows you to indicate the way in which content will be displayed. The possible values are:
  + **Specific**: the **RowsPerColumn** property is enabled, to indicate the desired number of rows per column (from a Portrait point of view. When the mode is Landscape, although the name of the property says RowsPerColumn you have to read it another way around, as ColumnsPerRow).  
    **RowsPerColumn**: it's a collection of numbers where the length of the collection is the number of columns and each value is the number of rows for the column, thinking in portrait mode.  
    For example:  3 2 means 2 columns, the first one with 3 rows and the second with 2 rows in portrait mode. In landscape, is switching rows per columns, that is, 3 columns in the first row, and 2 columns in the second one.
  + **Random**: the layout is selected at random. The number of items displayed on each page varies depending on the **ItemsPerPage** property.  
    **ItemsPerPage** indicates the number of items to be displayed on one page.

**Example**

In the example below, a change has been made to the control type property of the list in a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) that has the Work With applied. The image shows how the control displays the default data.

`[imagen omitida: wiki id 17523]`


|  |
| --- |
| **Backlinks** |
| [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) | [Category:Control Types](https://wiki.genexus.com/commwiki/wiki?20402) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [PageChanged event](https://wiki.genexus.com/commwiki/wiki?22735) |

---
