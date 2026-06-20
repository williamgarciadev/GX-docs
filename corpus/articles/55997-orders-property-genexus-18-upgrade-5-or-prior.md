---
title: "Orders property (GeneXus 18 upgrade 5 or prior)"
source_id: 55997
source_url: https://wiki.genexus.com/commwiki/wiki?55997
genexus_version: "18"
---

# Orders property (GeneXus 18 upgrade 5 or prior)

Defines several criteria for ordering Grid data.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817)

### [Description](#Description)

This property can be set for a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) included in the Layout of a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

It allows you to define different (simple or compound) orders so that the end user can select any of them at any time.

Each order is identified by a name and composed of a list of attributes (in ascending or descending order).

If more than one order is specified, at runtime the end user will see a combo box with all the order names.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider a [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) containing the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

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

1) Property Name (composed of the PropertyName attribute)  
2) Neighborhood (composed of the NeighborhoodName, PropertyName attributes)

Every "Order node" has a set of properties to be set:

* **Name:** The name given to the order. At runtime, it will be shown in the combo box that offers the possible orders.
* **Break by:** Allows control break. False by default.
* **Enable Alpha Indexer property:** See [Enable Alpha Indexer Property](https://wiki.genexus.com/commwiki/wiki?16583). False by default.

When Break by is set to True, the following properties are enabled:

* **Break by up to:** Indicates, when the order is composed of two or more attributes (for example, Att1, Att2, ..., AttN), the range of attributes for the break. That is, if it is up to Att2, the grouping criteria will be: Att1, Att2. The other attributes (from Att3 to AttN) will be used only for ordering proposes inside each group (and not for the grouping itself).
* **Description attribute:** See [Description attribute](https://wiki.genexus.com/commwiki/wiki?2154).

Every attribute included in an "Order node" has a set of properties to be set:

* **Attribute:** Attribute Name.
* **Description:** See [Description property](https://wiki.genexus.com/commwiki/wiki?7446).
* **Ascending:** True by default.

**Break By node:**Defines multiple control breaks by adding one or more attributes regardless of the order listed.  
This node has one property for indicating the attribute that describes the break:

* **Description Attribute:** See [Description attribute](https://wiki.genexus.com/commwiki/wiki?2154).

Each Attribute node under a **Break By node** will have only one property for changing an attribute in the break by without removing it:

* **Attribute:**Attribute name to which the break criteria will apply.

### [See Also](#See+Also)

[Orders and Filters in Grids of Panels](https://wiki.genexus.com/commwiki/wiki?24805)  
[Order clause](https://wiki.genexus.com/commwiki/wiki?6075) (in For Each, Data Providers and Data Selectors)
