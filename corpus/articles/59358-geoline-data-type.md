---
title: "GeoLine data type"
source_id: 59358
source_url: https://wiki.genexus.com/commwiki/wiki?59358
genexus_version: "18"
---

# GeoLine data type

The GeoLine data type is derived from the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408). This means it has a similar functionality to the Geography data type but is specific to represent the Geometry Line.

### [Scope](#Scope)

**DBMSs:** SQL Server, Oracle, MySQL, SAP Hana, PostgreSQL  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

To initialize an attribute or variable based on the GeoLine data type you must use the [FromGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59777) or the [FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900).

### [Sample](#Sample)

```
&GeoLine.FromGeoJson('{ "type": "LineString", "coordinates":  [ -56.18528366088867, -34.90571271703311 ,  -56.17850303649902, -34.90641660705113 ,  -56.15318298339844, -34.9140182347531 ,  -56.14863395690918, -34.91521472314688  ] }')
```

&GeoLine is a [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the GeoLine data type. It can also be an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) based on the same data type.

### [Properties](#Properties)

| **Property** | **Type** | **Description** |
| --- | --- | --- |
| Srid | int | Spatial Reference System Identifier (SRID), identifies the reference system for the represented Geographic object. See <https://en.wikipedia.org/wiki/SRID> |

### [Methods](#Methods)

Although the following method specifically apply to the GeoLine data type, all the methods that apply to the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) can also be applied to the GeoLine data type, except Distance.

| **Method** | **Type Returned** | **Description** |
| --- | --- | --- |
| ToGeography(GeoLine) | Geography | Converts the GeoLine to Geography type. |


|  |
| --- |
| **Backlinks** |
| [FromGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59777) | [FromString method](https://wiki.genexus.com/commwiki/wiki?12694) | [FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900) |
| [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) | [GeoJSON Geographic data format](https://wiki.genexus.com/commwiki/wiki?59399) | [Table of contents:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) | [GeoSuite - Geography Data Type in UI](https://wiki.genexus.com/commwiki/wiki?52973) |
| [HowTo: Group and Visualize Geographic Data Logically](https://wiki.genexus.com/commwiki/wiki?48253) | [ToGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59810) | [ToWkt method](https://wiki.genexus.com/commwiki/wiki?59814) | [WKT Geographic data format](https://wiki.genexus.com/commwiki/wiki?59398) |

---
