---
title: "Intersect method"
source_id: 59378
source_url: https://wiki.genexus.com/commwiki/wiki?59378
genexus_version: "18"
---

# Intersect method

Returns a Boolean with the result of the intersection of two Geography attributes or variables.

## [Syntax](#Syntax)

*GeographyAttOrVar1*.**Intersect(***GeographyAttOrVar2***)**

**Where:**

*GeographyAttOrVar1*Must be an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) or [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) or derived data types associated with geometry like the [GeoPolygon data type](https://wiki.genexus.com/commwiki/wiki?59361).

*GeographyAttOrVar2*Must be an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) or [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) or derived data types associated with geometry like the [GeoPoint data type](https://wiki.genexus.com/commwiki/wiki?58058).

**Type Returned:**  
Boolean

## [Scope](#Scope)

**Generators:**[Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)  
**Level:** [Attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,), [Variable](https://wiki.genexus.com/commwiki/wiki?7375) ([Geography data type](https://wiki.genexus.com/commwiki/wiki?32408))

## [Description](#Description)

This method allows solving complex algorithms such as "Point in Polygon", by leveraging the implementation of database management systems.

## [Samples](#Samples)

For example, in the code below the Geography variables are initialized with different vector data (points, lines, polygons), in this case from a WKT, and then it is calculated if they intersect.

```
&Point.Fromwkt('POINT(-56.160335101195614 -34.92136488262594)')
&Polygon.Fromwkt('POLYGON((-56.204939 -34.860685, -56.073266 -34.790773 ,  -56.014571 -34.838863, -56.078718 -34.878530, -56.147716 -34.904991, -56.2002342 -34.9062892, -56.204939 -34.860685))')
&Line.Fromwkt("LINESTRING(-56.17584228515625 -34.917466889282515, -56.147518157958984 -34.91662233422328)")

&PointInPolygon = &Polygon.Intersect(&Point)  //&PointInPolygon is a Boolean variable
&LineCrossPolygon = &Polygon.Intersect(&Line) //&LineCrossPolygon is a Boolean variable
```

Similarly, in the code below, the Intersect method is used to solve the "Point in Polygon" case.

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
Neighborhood
{
  NeighborhoodId*
  NeighborhoodName
  NeighborhoodGeography
}
```

The following [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) receives the &GeoPoint variable as a parameter.

The neighborhoods stored in the database are queried performing an optimal search to find where the given point (&GeoPoint variable) is located.

```
Rule:
Parm(&GeoPoint);

Source:
For each Neighborhood
    Where NeighborhoodGeography.Intersect(&GeoPoint)
     &IsIntersected = True
     &PlaceName = NeighborhoodName
     exit
Endfor
```

### [See Also](#See+Also)

[FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900)


|  |
| --- |
| **Backlinks** |
| [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) | [GeoPolygon data type](https://wiki.genexus.com/commwiki/wiki?59361) | [Table of contents:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) |

---
