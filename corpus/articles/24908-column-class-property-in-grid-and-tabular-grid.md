---
title: "Column Class property in Grid and Tabular Grid"
source_id: 24908
source_url: https://wiki.genexus.com/commwiki/wiki?24908
genexus_version: "18"
---

# Column Class property in Grid and Tabular Grid

Sets the class that styles a column of a Grid included in a Web Panel or a column of a Tabular Grid included in a Panel.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

For each column of a Grid included in a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) or a [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449) included in a [Panel](https://wiki.genexus.com/commwiki/wiki?24829), you can set the **Column Class property** (with the name of a class) to give a style to it.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [Samples](#Samples)

The following image shows a Web Panel that contains a Grid in its Web Layout. For each column of the Grid, the **Column Class property** can be set.

`[imagen omitida: wiki id 55771]`

As you can see, for the second column of the Grid (ProductDesc attribute), the Column Class property is set to GridColumn. GridColumn is the name of a predefined class included in every [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420).

Suppose that for the GridColumn class of the [Web Theme you are using](https://wiki.genexus.com/commwiki/wiki?8145) you set the Background Color property, as shown below:

`[imagen omitida: wiki id 55779]`

At runtime, the second column (ProductDesc attribute) of the Web Panel Grid will be shown as follows:

`[imagen omitida: wiki id 55780]`

The **Column Class property** can also be set at runtime. For example, look at the following [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916); in this case, it contains a Grid with variables.

`[imagen omitida: wiki id 55772]`

To add the same style as the example above to the second column, you can define the following code:

```
Event Start
      &ProductDesc.ColumnClass = "GridColumn"
endevent
```

In addition, when setting the **ColumnClass property** at runtime, you can set it for a column, line by line.

Suppose you need to set the column showing ProductPrice with a red background color for the rows of the Grid whose price is higher than 500.

The following code solves this requirement:

```
Event Grid1.Load
    For each Product
        &ProductId = ProductId
        &ProductDesc = ProductDesc
        &ProductPrice = ProductPrice
        if &ProductPrice >500
            &ProductPrice.ColumnClass = "RedColumn"
        else
            &ProductPrice.ColumnClass = "GridColumn"
        endif
        grid1.Load()
    endfor
endevent
```

Consider that the "RedColumn" class must be defined as a child node of the GridColumn predefined class.

At runtime, you will see:

`[imagen omitida: wiki id 55781]`

#### [Setting the Column Class property to a class of a Design System object](#Setting+the+Column+Class+property+to+a+class+of+a+Design+System+object)

The **Column Class property** can also be set to a class of a [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375).

To do so, follow the steps below.

Suppose your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is named "BillingSystem", and therefore a predefined Design System object is created with the same name.

Look at the Style tab of your "BillingSystem" Design System object:

```
styles BillingSystem {
@import GeneXusUnanimo.UnanimoWeb;
}
```

You only have to define there, a class (named for example "GridProductColumn") and set its "background-color" property as follows:

```
styles BillingSystem {
@import GeneXusUnanimo.UnanimoWeb;
    .GridProductColumn 
    {
      background-color: #0F0;
    }
}
```

Finally, for the second column (ProductDesc) of the Grid included in your Web Panel, set its **Column Class property** to GridProductColumn class:

`[imagen omitida: wiki id 55786]`

At runtime, the second column (ProductDesc attribute) of the Web Panel Grid will be shown as follows:

`[imagen omitida: wiki id 55780]`

The **Column Class property** is very useful for developing [Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159). See [How to design a Responsive Web Application: Hiding a column in a grid](https://wiki.genexus.com/commwiki/wiki?25495).

### [See Also](#See+Also)

[gx-grid-column-class property](https://wiki.genexus.com/commwiki/wiki?54459)  
[Class property](https://wiki.genexus.com/commwiki/wiki?8741)


|  |
| --- |
| **Backlinks** |
| [Column Class property in Grid (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55106) | [gx-grid-column-header-class property](https://wiki.genexus.com/commwiki/wiki?35383) | [gx-grid-column-hidden property](https://wiki.genexus.com/commwiki/wiki?56456) |
| [gx-grid-column-size property](https://wiki.genexus.com/commwiki/wiki?56550) | [How to design a Responsive Web Application: Hiding a column in a grid](https://wiki.genexus.com/commwiki/wiki?25495) | [KB:OnlineShop (Shopping cart sample)](https://wiki.genexus.com/commwiki/wiki?27158) |

---
