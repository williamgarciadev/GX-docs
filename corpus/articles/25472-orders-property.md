---
title: "Orders property"
source_id: 25472
source_url: https://wiki.genexus.com/commwiki/wiki?25472
genexus_version: "18"
---

# Orders property

Defines several criteria for ordering Grid / Tabular Grid data.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449)

### [Description](#Description)

This property can be set for Grids and Tabular Grids (in this last case, only for Angular) included in [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s.

It allows you to define different (simple or compound) orders so that the end user can select any of them at any time.

Each order is identified by a name and composed of a list of attributes (in ascending or descending order).

If more than one order is specified, at runtime the end user will see a combo box with all the order names.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) containing the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,)s:

```
Neighborhood
{ 
   NeighborhoodId*
   NeighborhoodName
}

Property
{
   PropertyId*
   PropertyName
   PropertyPhoto
   PropertyAddress
   NeighborhoodId
   NeighborhoodName
}
```

Suppose you include a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) in the Layout of a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) as shown below.

`[imagen omitida: wiki id 36839]`

Two orders have been defined for the **Orders property** of the Grid:

1) Property Name, composed of the PropertyName attribute.  
2) Neighborhood, composed of the NeighborhoodName, PropertyName attributes.

Each "Order" node (in the above example there are two "Order" nodes) has a set of properties to configure:

* **Name:** The name given to the order. At runtime, it will be shown in the combo box that offers the possible orders.
* **Break by:** Allows control break. False by default.
* **Enable Alpha Indexer property:** See [Enable Alpha Indexer Property](https://wiki.genexus.com/commwiki/wiki?16583). False by default.

When the **Break by** property is set to True, the following properties are enabled:

* **Break by up to:** Indicates, when the order is composed of two or more attributes (for example, Att1, Att2, ..., AttN), the range of attributes for the break. That is, if it is up to Att2, the grouping criteria will be: Att1, Att2. The other attributes (from Att3 to AttN) will be used only for ordering purposes inside each group and not for the grouping itself.
* **Description attribute:** See [Description attribute](https://wiki.genexus.com/commwiki/wiki?2154).

Additionally, aesthetic customization of the grouped rows can be achieved by setting the 'gx-group-separator-class' property in the Design System Object (DSO).

In turn, for each attribute in the list that makes up the order, there are three properties to be set:

* **Attribute:** Attribute Name.
* **Description:** See [Description property](https://wiki.genexus.com/commwiki/wiki?7446).
* **Ascending:** True by default.

Continuing with the example, suppose that for the first order, you leave the default property values and for the second order, you set the properties as follows:  
  
`[imagen omitida: wiki id 59298]`

This means that although the second order is composed of two attributes (NeighborhoodName, PropertyName), a break is desired but only by the NeighborhoodName attribute (to show the properties grouped by NeighborhoodName). As the order is composed of the pair (NeighborhoodName, PropertyName), for each NeighborhoodName the properties will be displayed ordered by PropertyName.

At runtime, when the second order is selected, the result will be as follows:

`[imagen omitida: wiki id 59299]`

On the other hand, when the first order is selected (by PropertyName and with no break), the result will be as follows:

`[imagen omitida: wiki id 59300]`

**"Break By" node**

Suppose you do not want to define orders but to define a break. This node allows you to indicate the attributes for which you want to make the break.

The "Break By" node provides a short way to define a break. However, if you define an order with its **Break by** property set to True, the break will be performed considering what you indicate in the **Break by up to**property associated with the order.

### [See Also](#See+Also)

[Orders and Filters in Grids of Panels](https://wiki.genexus.com/commwiki/wiki?24805)  
[Order clause](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?6075,,) (in For Each, Data Providers and Data Selectors)


|  |
| --- |
| **Backlinks** |
| [Orders and Filters in Grids of Panels](https://wiki.genexus.com/commwiki/wiki?24805) | [Orders property (GeneXus 18 upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55997) | [Search property](https://wiki.genexus.com/commwiki/wiki?36833) |

---
