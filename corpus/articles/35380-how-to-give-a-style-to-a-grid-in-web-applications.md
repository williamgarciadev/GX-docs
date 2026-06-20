---
title: "How to give a style to a grid in web applications"
source_id: 35380
source_url: https://wiki.genexus.com/commwiki/wiki?35380
genexus_version: "18"
---

# How to give a style to a grid in web applications

In web applications, there are several properties available for the grid in order to give a style to it.

In [RWD](https://wiki.genexus.com/commwiki/wiki?25157,,), using the [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209) form, the properties are edited using the Theme Editor, and they are grouped under [Theme Classes](https://wiki.genexus.com/commwiki/wiki?6246).

First of all, the Class property of the grid allows setting a Theme Class that groups all the classes for a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817).

In addition, since the grid looks like a table - although it isn't really an HTML table in some cases -, it can be given Theme Classes to style its rows, columns, and headers.

Graphically, the classes available for styling the grid are the following (all of them are grouped under the grid class):

`[imagen omitida: wiki id 35381]`

So, the list of classes would be:

* [gx-grid-row-class property](https://wiki.genexus.com/commwiki/wiki?32772) (Grids, freestyle grids, and tables)
* [Column Class Property](https://wiki.genexus.com/commwiki/wiki?24908) (Grids)
* [gx-grid-header-row-class property](https://wiki.genexus.com/commwiki/wiki?35382) (Grids)
* [gx-grid-column-header-class property](https://wiki.genexus.com/commwiki/wiki?35383) (Grids)
* [gx-table-row-cell-class property](https://wiki.genexus.com/commwiki/wiki?25796) (freestyle grids and tables)

### [Let's see how to...](#Let%27s+see+how+to...)

### [1. Configure all the columns of a grid](#1.+Configure+all+the+columns+of+a+grid)

First, consider that each particular column of a grid can be configured using the *Column Class* property of the grid as shown in the figure:

`[imagen omitida: wiki id 35388]`

In practice, you can configure all the columns of the grid using the [Column Class Property](https://wiki.genexus.com/commwiki/wiki?24908) of the Grid class.

### [2. Configure all the rows of a grid](#2.+Configure+all+the+rows+of+a+grid)

Similar to the [Column Class Property](https://wiki.genexus.com/commwiki/wiki?24908), there is a [gx-grid-row-class property](https://wiki.genexus.com/commwiki/wiki?32772) that allows configuring all the rows of the grid.

### [3. Configure the headers of a grid](#3.+Configure+the+headers+of+a+grid)

The headers of the grid can be configured using the [gx-grid-header-row-class property](https://wiki.genexus.com/commwiki/wiki?35382).

### [4. Configure the settings of a grid's cell at runtime](#4.+Configure+the+settings+of+a+grid%27s+cell+at+runtime)

In general cases, you need to highlight some particular column of the grid, for any particular row; e.g. when the balance is less than zero, you want to display that information highlighted.

In such case, use the Column property at runtime for that specific row, column; i.e. in a loop (which loads the grid data) you assign a Column class for the row and the column which meets certain conditions.

```
Event Grid1.Load
    if authorName = 'Pablo Neruda'
        literaryWorkName.ColumnClass = ThemeClass:GridPreferredColumn
    else
        literaryWorkName.ColumnClass = ThemeClass:GridLWColumn
    endif
Endevent
```

Note that by rule, you have to assign the "default" class to the column when it doesn't meet the conditions; in the example, it is the "GridLWColumn" class.

At runtime, it looks as follows:

`[imagen omitida: wiki id 35385]`

The GridPreferredColumn class is defined in the Theme as follows:

`[imagen omitida: wiki id 35386]`

This is also explained in the [Column Class Property](https://wiki.genexus.com/commwiki/wiki?24908).

In the case of a free style grid, you can use the [gx-table-row-cell-class property](https://wiki.genexus.com/commwiki/wiki?25796) with the same purpose.

### [5. Configure the header's cell of a column grid at runtime](#5.+Configure+the+header%27s+cell+of+a+column+grid+at+runtime)

To set the style of a specific column's header, use the [gx-grid-column-header-class property](https://wiki.genexus.com/commwiki/wiki?35383).
