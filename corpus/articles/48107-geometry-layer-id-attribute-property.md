---
title: "Geometry Layer Id Attribute property"
source_id: 48107
source_url: https://wiki.genexus.com/commwiki/wiki?48107
genexus_version: "18"
---

# Geometry Layer Id Attribute property

Sets the attribute or variable containing the geometry layer identifier for the geometry being drawn.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309))

### [Description](#Description)

You have to complete this property of the [Panel](https://wiki.genexus.com/commwiki/wiki?24829) [Grid](https://wiki.genexus.com/commwiki/wiki?24817) whose Control Type property = Maps with the attribute or variable that determines the logical [Geometry Layer](https://wiki.genexus.com/commwiki/wiki?48253). In other words, this attribute/variable is the one that categorizes and builds the logical group.

For example, consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
UrbanArea
{
 UrbanAreaId* - Numeric
 UrbanAreaGeo - Geography
 UrbanAreaGeoLayerID - Character (it may be Numeric)
}
```

The UrbanAreaGeoLayerID attribute stores values like "BusWay", "BikeWay" and "Avenue". This attribute can be assigned to the **Geometry Layer Id Attribute** property in order to build logical [Geometry Layers](https://wiki.genexus.com/commwiki/wiki?48253).

Then, the [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209) has to be set with the UrbanAreaGeo attribute.

### [See Also](#See+Also)

[HowTo: Group and Visualize Geographic Data Logically](https://wiki.genexus.com/commwiki/wiki?48253)


|  |
| --- |
| **Backlinks** |
| [Geometry Layer Id Field Specifier property](https://wiki.genexus.com/commwiki/wiki?48108) | [HowTo: Group and Visualize Geographic Data Logically](https://wiki.genexus.com/commwiki/wiki?48253) |

---
