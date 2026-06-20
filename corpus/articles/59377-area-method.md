---
title: "Area method"
source_id: 59377
source_url: https://wiki.genexus.com/commwiki/wiki?59377
genexus_version: "18"
---

# Area method

Returns the area of a given GeoPolygon attribute or variable.

## [Syntax](#Syntax)

*GeoPolygonAttOrVar*.**Area()**

**Where:**

*GeoPolygonAttOrVar*  
   Must be an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) or [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the [GeoPolygon data type](https://wiki.genexus.com/commwiki/wiki?59361).

**Type Returned:**
Numeric

## [Scope](#Scope)

**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)  
**Level:** [Attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,), [Variable](https://wiki.genexus.com/commwiki/wiki?7375) ([GeoPolygon data type](https://wiki.genexus.com/commwiki/wiki?59361))

## [Description](#Description)

Returns the area of a polygon in square meters (m2).  
The calculation is solved in the language of the current [environment](https://wiki.genexus.com/commwiki/wiki?7115) or in the database management system (DBMS), for example, by invoking it from the Where clause of a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744).

## [Samples](#Samples)

```
&zonePlace.FromWkt('POLYGON((-122.358 47.653 , -122.348 47.649, -122.348 47.658, -122.358 47.658, -122.358 47.653))') 
&areavalue = &zonePlace.Area()
```

The &zonePlace variable (based on the [GeoPolygon data type](https://wiki.genexus.com/commwiki/wiki?59361)) is initialized with a polygon, from a WKT (or a GeoJSON).

When applying the **Area method** to the &zonePlace variable, its numerical value in square meters is returned (and assigned to the &areavalue Numeric variable).

## [See Also](#See+Also)

[FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) |

---
