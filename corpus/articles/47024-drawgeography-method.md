---
title: "DrawGeography method"
source_id: 47024
source_url: https://wiki.genexus.com/commwiki/wiki?47024
genexus_version: "18"
---

# DrawGeography method

Draws geography in a Grid whose Control Type property = Maps (included in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)).

### [Syntax](#Syntax)

**&**GUID = GridControlName**.DrawGeography**(Geography)  
  
**Where:**

*GridControlName*  
   Grid control name whose Control Type property is set to Maps.

*Geography*  
   Attribute or variable based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408).

**Type Returned:**  
Varchar (GUID to identify the geography drawn).

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Controls:** | [Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309)) |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

### [Sample](#Sample)

```
&Geography.FromString("LINESTRING(-56.082774 -34.884341, -56.074583 -34.881745)")
&GeographyId = MapGrid.DrawGeography(&Geography)
```

### [Considerations](#Considerations)

This only applies to events on the client, such as user events, excepts for the ClientStart event.

To draw on the server, use the [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209).  
The refresh event clears the geometries drawn by this method.

### [Availability](#Availability)

This method is available since [GeneXus 17](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46066,,).

### [See Also](#See+Also)

[DrawGeoLine Method](https://wiki.genexus.com/commwiki/wiki?47026)


|  |
| --- |
| **Backlinks** |
| [Clear method in Grids with Control Type = Maps](https://wiki.genexus.com/commwiki/wiki?46862) | [DrawGeoLine method](https://wiki.genexus.com/commwiki/wiki?47026) | [GeneXus deprecated functions, methods, and rules](https://wiki.genexus.com/commwiki/wiki?6620) |
| [HowTo: Group and Visualize Geographic Data Logically](https://wiki.genexus.com/commwiki/wiki?48253) | [HowTo: Maps - Mapbox](https://wiki.genexus.com/commwiki/wiki?48350) | [LoadKmlLayer method](https://wiki.genexus.com/commwiki/wiki?51341) |
| [Maps Control Type Methods](https://wiki.genexus.com/commwiki/wiki?54095) |

---
