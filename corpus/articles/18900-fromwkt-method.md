---
title: "FromWkt method"
source_id: 18900
source_url: https://wiki.genexus.com/commwiki/wiki?18900
genexus_version: "18"
---

# FromWkt method

Loads data into an attribute or variable based on the Geography data type (or derived data types associated with geometry like GeoPoint, GeoLine, GeoPolygon) from a representation in WKT format.

### [Syntax](#Syntax)

*AttOrVar*.**FromWkt(***Character***)**

**Where:**

*AttOrVar*    
    Is an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) or [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) (or derived data types associated with geometry like [GeoPoint](https://wiki.genexus.com/commwiki/wiki?58058), [GeoLine](https://wiki.genexus.com/commwiki/wiki?59358), [GeoPolygon](https://wiki.genexus.com/commwiki/wiki?59361)) to which the data will be loaded.

*Character*    
    Is text enclosed in quotation marks that must contain a valid representation of a Point, Line, or Polygon in WKT format. For example,

* To load a Point, *Character* should be: "POINT(Longitude Latitude)"
* To load a Line or Multiline, *Character* should be: "LINESTRING(Longitude1 Latitude1, Longitude2 Latitude2, Longitude3 Latitude3)"
* In the case of a Polygon, *Character* should be: "POLYGON(Longitude1 Latitude1, Longitude2 Latitude2, Longitude3 Latitude3, .....)"

    Longitude, Longitude1, Longitude2, Longitude3 are Longitude Coordinates and Latitude, Latitude1, Latitude2, Latitude3 are Latitude Coordinates.   
      
    For more details about the WKT (Well Known Text) format, refer to: <https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry>

**Type Returned:**  
[Geography](https://wiki.genexus.com/commwiki/wiki?32408) | [GeoPoint](https://wiki.genexus.com/commwiki/wiki?58058) | [GeoLine](https://wiki.genexus.com/commwiki/wiki?59358) | [GeoPolygon](https://wiki.genexus.com/commwiki/wiki?59361)

### [Scope](#Scope)

**Data Types:**  [Geography](https://wiki.genexus.com/commwiki/wiki?32408), [GeoPoint](https://wiki.genexus.com/commwiki/wiki?58058), [GeoLine](https://wiki.genexus.com/commwiki/wiki?59358), [GeoPolygon](https://wiki.genexus.com/commwiki/wiki?59361)    
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### Description

The **FromWkt method** receives a representation in WKT format (Longitude coordinates and Latitude coordinates must always be indicated in that order in the character content) to load attributes or variables based on the Geography data type (or derived data types associated with geometry like GeoPoint, GeoLine, GeoPolygon).

### [Samples](#Samples)

**1)**&Geography is a variable based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408). &Point is a variable based on the [GeoPoint data type](https://wiki.genexus.com/commwiki/wiki?58058). They are being loaded, for example, inside an object Event or an object Source.

```
&Geography.FromWkt("POINT(-56.163740158081055 -34.92478600243492)")
```

or:

```
&Point.FromWkt("POINT(-56.163740158081055 -34.92478600243492)")
```

**2)** AttractionGeography is an [Attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) that is being updated for a certain attraction received as a parameter. The [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) is written inside a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664).

```
Procedure Rule:
Parm(&AttractionId);

Procedure Source:
For each Attraction
      where AttractionId=&AttractionId  
           AttractionGeography.FromWkt("POINT(-56.163740158081055 -34.92478600243492)")  
endfor
```

You can use the same syntax to load and update an attribute based on the [GeoPoint data type](https://wiki.genexus.com/commwiki/wiki?58058).

**3)**&Geography is a variable of [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408). &Line is a variable of [GeoLine data type](https://wiki.genexus.com/commwiki/wiki?59358). They are being loaded, for example, inside an object Event or an object Source:

```
&Geography.FromWkt("LINESTRING(-56.16090774536133 -34.928797162523516, -56.1650276184082 -34.89494244739731)")
```

or:

```
&Line.FromWkt("LINESTRING(-56.16090774536133 -34.928797162523516, -56.1650276184082 -34.89494244739731)")
```

**4)**&Geography is a variable of [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408). &Polygon is a variable of [GeoPolygon data type](https://wiki.genexus.com/commwiki/wiki?59361). They are being loaded, for example, inside an object Event or an object Source:

```
&Geography.FromWkt('POLYGON ((-56.248367 -34.873821, -56.266563 -34.876427, -56.263733 -34.890366, -56.268799 -34.893394, -56.26897 -34.900291, -56.264851 -34.902615, -56.253605 -34.895645, -56.247597 -34.895153, -56.246052 -34.889523, -56.248367 -34.873821, -56.248367 -34.873821))')
```

or:

```
&Polygon.FromWkt('POLYGON ((-56.248367 -34.873821, -56.266563 -34.876427, -56.263733 -34.890366, -56.268799 -34.893394, -56.26897 -34.900291, -56.264851 -34.902615, -56.253605 -34.895645, -56.247597 -34.895153, -56.246052 -34.889523, -56.248367 -34.873821, -56.248367 -34.873821))')
```

### [See Also](#See+Also)

[ToWkt method](https://wiki.genexus.com/commwiki/wiki?59814)


|  |
| --- |
| **Backlinks** |
| [Area method](https://wiki.genexus.com/commwiki/wiki?59377) | [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) | [GeoLine data type](https://wiki.genexus.com/commwiki/wiki?59358) |
| [GeoPoint data type](https://wiki.genexus.com/commwiki/wiki?58058) | [GeoPolygon data type](https://wiki.genexus.com/commwiki/wiki?59361) | [Intersect method](https://wiki.genexus.com/commwiki/wiki?59378) | [KML Geographic data format](https://wiki.genexus.com/commwiki/wiki?59400) |
| [ToWkt method](https://wiki.genexus.com/commwiki/wiki?59814) | [WKT Geographic data format](https://wiki.genexus.com/commwiki/wiki?59398) |

---
