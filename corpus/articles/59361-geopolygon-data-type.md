---
title: "GeoPolygon data type"
source_id: 59361
source_url: https://wiki.genexus.com/commwiki/wiki?59361
genexus_version: "18"
---

# GeoPolygon data type

The GeoPolygon data type is derived from the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408). This means it has a similar functionality to the Geography data type but is specific to represent the Geometry areas.

### [Scope](#Scope)

**DBMSs:** SQL Server, Oracle, MySQL, SAP Hana, PostgreSQL  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

To initialize an attribute or variable based on the GeoPolygon data type you must use the [FromGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59777) or [FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900).

### [Sample](#Sample)

```
&GeoPolygon.FromGeoJson('{ "type": "Polygon", "coordinates": ... }')
```

&GeoPolygon is a [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the GeoPolygon data type. It can also be an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) based on the same data type.

### [Properties](#Properties)

| **Property** | **Type** | **Description** |
| --- | --- | --- |
| Srid | int | Spatial Reference System Identifier (SRID), identifies the reference system for the represented Geographic object. See <https://en.wikipedia.org/wiki/SRID> |

### [Methods](#Methods)

Although the following methods specifically apply to the GeoPolygon data type, all the methods that apply to the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) can also be applied to the GeoPolygon data type:

| **Method** | **Type Returned** | **Description** |
| --- | --- | --- |
| [FromWkt(Character)](https://wiki.genexus.com/commwiki/wiki?18900) | GeoPolygon | The format of the Character parameter should be: 'POLYGON(Longitude1 Latitude1, Longitude2 Latitude2, Longitude3 Latitude3, .....)' |
| [Intersect(GeoPolygon)](https://wiki.genexus.com/commwiki/wiki?59378) | Boolean |  |
| ToGeography(GeoPolygon) | Geography | Converts the GeoPolygon to Geography type. |

**Note**: [FromString](https://wiki.genexus.com/commwiki/wiki?12694) and [ToString](https://wiki.genexus.com/commwiki/wiki?7090) methods for Geography data types are enabled only for compatibility reasons. Use [FromWkt](https://wiki.genexus.com/commwiki/wiki?18900) and [ToWkt](https://wiki.genexus.com/commwiki/wiki?59814) instead.


|  |
| --- |
| **Backlinks** |
| [Area method](https://wiki.genexus.com/commwiki/wiki?59377) | [FromGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59777) | [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) |
| [FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900) | [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) | [GeoJSON Geographic data format](https://wiki.genexus.com/commwiki/wiki?59399) | [Table of contents:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) |
| [GeoSuite - Geography Data Type in UI](https://wiki.genexus.com/commwiki/wiki?52973) | [HowTo: Group and Visualize Geographic Data Logically](https://wiki.genexus.com/commwiki/wiki?48253) | [Intersect method](https://wiki.genexus.com/commwiki/wiki?59378) | [ToGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59810) |
| [ToWkt method](https://wiki.genexus.com/commwiki/wiki?59814) | [WKT Geographic data format](https://wiki.genexus.com/commwiki/wiki?59398) |

---
