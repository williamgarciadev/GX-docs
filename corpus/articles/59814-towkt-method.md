---
title: "ToWkt method"
source_id: 59814
source_url: https://wiki.genexus.com/commwiki/wiki?59814
genexus_version: "18"
---

# ToWkt method

Returns the WKT representation of a Geography, GeoPoint, GeoLine, or GeoPolygon data type.

### [Syntax](#Syntax)

*AttOrVar*.**ToWkt(****)**

**Where:**

*AttOrVar*    
    Is an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) or [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) (or derived data types associated with geometry like [GeoPoint](https://wiki.genexus.com/commwiki/wiki?58058), [GeoLine](https://wiki.genexus.com/commwiki/wiki?59358), [GeoPolygon](https://wiki.genexus.com/commwiki/wiki?59361)) containing the data to be converted to a WKT representation.

**Type Returned:**  
Character  
    Is a valid representation of a Point, Line, or Polygon in WKT format.

### [Scope](#Scope)

**Data Types:**  [Geography](https://wiki.genexus.com/commwiki/wiki?32408), [GeoPoint](https://wiki.genexus.com/commwiki/wiki?58058), [GeoLine](https://wiki.genexus.com/commwiki/wiki?59358), [GeoPolygon](https://wiki.genexus.com/commwiki/wiki?59361)    
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### Description

The **ToWkt method** can be applied to an attribute or variable based on the Geography data type (or derived data types associated with geometry like GeoPoint, GeoLine, or GeoPolygon) and returns the corresponding representation in WKT format.

### [Samples](#Samples)

```
&WKTChar=&Geography.ToWkt()

&WKTChar=&GeoPoint.ToWkt()

&WKTChar=&GeoLine.ToWkt()

&WKTChar=&GeoPolygon.ToWkt()
```

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
Place
{
  PlaceId* 
  PlaceName --> Character data type
  PlaceGeo --> Geography data type
}
```

The following code can be defined, for example, in a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293):

```
Rules:
Parm(&PlaceId);

Source:
For each Place 
    where PlaceId = &PlaceId
       &WKTChar = PlaceGeo.ToWkt()  //&WKTChar is based on the Character data type
       //do something with &WKTChar
endfor
```

Suppose that &PlaceId = 10. When executing the [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) and filtering the record where PlaceId = 10, the stored PlaceName is 'Cristo Redentor, Rio de Janeiro, Brazil,' and when applying the **ToWkt() method** to the PlaceGeo attribute, the &WKTChar variable will be loaded as follows:

```
"POINT(-43.2105 -22.9519)"
```

### [See Also](#See+Also)

[FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900)


|  |
| --- |
| **Backlinks** |
| [FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900) | [GeoPolygon data type](https://wiki.genexus.com/commwiki/wiki?59361) | [WKT Geographic data format](https://wiki.genexus.com/commwiki/wiki?59398) |

---
