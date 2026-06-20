---
title: "GeoPoint data type"
source_id: 58058
source_url: https://wiki.genexus.com/commwiki/wiki?58058
genexus_version: "18"
---

# GeoPoint data type

The GeoPoint data type is derived from the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408). This means it has a similar functionality to the Geography data type but is specific to represent the Geometry Point.

### [Scope](#Scope)

**DBMSs:** SQL Server, Oracle, MySQL, SAP Hana, PostgreSQL  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

To initialize an attribute or variable based on the GeoPoint data type you must use the New constructor as follows:

Att|Variable = **GeoPoint.New**(Latitude Number, Longitude Number)

**Where:**

*Att*| *Variable*  
    Is an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) or [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the GeoPoint data type.

*Latitude Number*    
    Is a Latitude Coordinate.

*Longitude Number* Is a Longitude Coordinate.

### [Sample](#Sample)

```
&OfficeLocation = GeoPoint.New(-34.8910275746741, -56.18720064473088)
```

### [Properties](#Properties)

Specific properties that apply to the GeoPoint data type are as follows:

|  |  |  |
| --- | --- | --- |
| **Property** | **Type** | **Description** |
| Srid | int | Spatial Reference System Identifier (SRID), identifies the reference system for the represented Geographic object. See <https://en.wikipedia.org/wiki/SRID>. |
| Longitude | int(12,8) | Value of the Longitude (horizontal) coordinate for the point. |
| Latitude | int(12.8) | Value of the Latitude (vertical) coordinate for the point. |

### [Methods](#Methods)

Although the following methods specifically apply to the GeoPoint data type, all the methods that apply to the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) can also be applied to the GeoPoint data type:

|  |  |  |
| --- | --- | --- |
| **Method** | **Type Returned** | **Description** |
| [FromWKT(Character)](https://wiki.genexus.com/commwiki/wiki?18900) | GeoPoint | The format of the Character parameter should be: 'POINT(LongitudeNumber LatitudeNumber)' |
| [FromString(Character)](https://wiki.genexus.com/commwiki/wiki?12694) | GeoPoint | Analogous to the [FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900). In addition to using the FromWkt method (that receives a Wkt format as an input parameter), the FromString method can be applied to a GeoPoint data type (receiving a string based on the [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644) as an input parameter). **This is only available for Android.  Sample:** &GeoPointVariable.FromString("-34.92478600243492, -56.163740158081055") |
| [FromGeoJson (Character)](https://wiki.genexus.com/commwiki/wiki?59777) | GeoPoint | The format of the Character parameter should be: '{"type":"Point","coordinates":[LongitudeNumber, LatitudeNumber]}' |
| ToGeography(GeoPoint) | Geography | Converts the Point to a Geography type. |

**Note**: There is also a static version of these methods.


|  |
| --- |
| **Backlinks** |
| [FromGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59777) | [FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900) | [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) |
| [GeoJSON Geographic data format](https://wiki.genexus.com/commwiki/wiki?59399) | [Table of contents:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) | [GeoSuite - Geography Data Type in UI](https://wiki.genexus.com/commwiki/wiki?52973) | [HowTo: Draw animations between locations on a Map](https://wiki.genexus.com/commwiki/wiki?59366) |
| [HowTo: Group and Visualize Geographic Data Logically](https://wiki.genexus.com/commwiki/wiki?48253) | [HowTo: Select a Location on a Map](https://wiki.genexus.com/commwiki/wiki?59365) | [HowTo: Solve Geocoding with GeneXus](https://wiki.genexus.com/commwiki/wiki?53464) |
| [Intersect method](https://wiki.genexus.com/commwiki/wiki?59378) | [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309) | [SetMapCenter method](https://wiki.genexus.com/commwiki/wiki?59362) | [ToGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59810) |
| [ToWkt method](https://wiki.genexus.com/commwiki/wiki?59814) | [WKT Geographic data format](https://wiki.genexus.com/commwiki/wiki?59398) |

---
