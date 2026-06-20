---
title: "Column Class property in Grid (GeneXus 18 Upgrade 3 or prior)"
source_id: 55106
source_url: https://wiki.genexus.com/commwiki/wiki?55106
genexus_version: "18"
---

# Column Class property in Grid (GeneXus 18 Upgrade 3 or prior)

Sets the Cascading Style Sheet Class for the grid column.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** Grid

### [Description](#Description)

The Standard [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) has the **Column** **Class property** for each of its columns. The property is also available for the Grid class in the [Theme](https://wiki.genexus.com/commwiki/wiki?6420).

The following figure shows how to display this property, for each grid's column:

`[imagen omitida: wiki id 35393]`

Consider that the Column Class property is for setting the column class, whereas the Class Property is for setting the class of the control inside the cell (which can be an attribute, a variable, or an image).

In the image above, the *Class* Property is set to the Attribute class, while the *Column Class* property is set to "GridColumn" class. This class  - the "GridColumn" class- is predefined and it is located under the Classes node of the [Theme](https://wiki.genexus.com/commwiki/wiki?6420), as shown in the figure below:

`[imagen omitida: wiki id 35394]`

Although the *Column Clas*s property is left with an empty value in new grids, the user can configure it with GridColumn class or any other child node of it, which should be previously created by the user.

The Column Class property can also be set as a runtime property. See the example below.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [Samples](#Samples)

#### [Example: setting the "Column Class" property for a grid's column](#Example%3A+setting+the+%22Column+Class%22+property+for+a+grid%27s+column)

Consider a scenario where you need to set the background color of the "Price" column to red, for each row of the "Products" grid, which has a price greater than 50.  
In this case, the load code of the grid could be as follows:

```
Event grid1.Load
    for each product
        &productid = productId
        &productdesc = productDesc
        &productprice = productPrice
        if &productprice >50
            &productprice.ColumnClass = "RedColumn"
        else
            &productprice.ColumnClass = "GridColumn"
        endif
    grid1.Load()
    endfor
endevent
```

In this example, the "RedColumn" class should be defined as a child node of the GridColumn predefined class.

The Column Class property is very useful in the case of developing a [Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159). See [How to design a Responsive Web Application: Hiding a column in a grid](https://wiki.genexus.com/commwiki/wiki?25495).

### [See Also](#See+Also)

[Row Class property](https://wiki.genexus.com/commwiki/wiki?53415,,)  
[Cell Class property](https://wiki.genexus.com/commwiki/wiki?53511,,)
