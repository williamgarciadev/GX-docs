---
title: "gx-grid-column-header-class property"
source_id: 35383
source_url: https://wiki.genexus.com/commwiki/wiki?35383
genexus_version: "18"
---

# gx-grid-column-header-class property

Sets a class to style the header of a grid column.

### [Scope](#Scope)

**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

The value of this property is a class that has the desired Style for the grid column's header.

### [Samples](#Samples)

Suppose that you set the ColumnClass property of any column of the grid at runtime, as shown in the following code:

```
Event grid1.Load
    if AuthorName = 'Pablo Neruda'
        LiteraryWorkName.ColumnClass = StyleClass:GridPreferredColumn
    else
        LiteraryWorkName.ColumnClass = StyleClass:GridLWColumn
    endif
Endevent
```

Besides highlighting that pair (row, column), you may also need to highlight the column's header.

That's where the gx-grid-column-header-class property comes into play.

In the [Styles](https://wiki.genexus.com/commwiki/wiki?47379) section of your [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375), define:

```
.GridPreferredColumn
{    
gx-grid-column-header-class:GridPreferredColumnHead;
}

 .GridPreferredColumnHead
{
background-color: black; 
}
```

The Grid's column header will take the value of the background-color property defined in the GridPreferredColumnHead class.

### [See Also](#See+Also)

[gx-grid-row-class property](https://wiki.genexus.com/commwiki/wiki?32772)  
[gx-grid-header-row-class property](https://wiki.genexus.com/commwiki/wiki?35382)  
[Column Class property in Grid and Tabular Grid](https://wiki.genexus.com/commwiki/wiki?24908)  
[DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707)
