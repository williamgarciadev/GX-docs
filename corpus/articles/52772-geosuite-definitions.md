---
title: "GeoSuite - Definitions"
source_id: 52772
source_url: https://wiki.genexus.com/commwiki/wiki?52772
genexus_version: "18"
---

# GeoSuite - Definitions

Geolocation refers not only to obtaining the geographic position of an object but also to the position itself and its geographic coordinates in the real world. This position can be obtained in several ways, including by GPS data or a "tracking" system, by the IP of a terminal, or by other alternative means.

Geographic location may vary in accuracy depending on the data source.

GeneXus expects the location coordinates in latitude and longitude format (WGS84 geographic coordinate system). To store this data, it uses the functionalities offered by the DBMS where the data can be not only Geographic points but also polygons (areas) and lines (roads). The name of this data type is [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408).

The data can also be stored in string format for those DBMSs that do not support geographic data. In GeneXus, the string format to store geographic data is called [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644).

There is a set of functions and operations on this data. Many of them, which do not have a UI, are available in the [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309).


|  |
| --- |
| **Backlinks** |
| [Toc:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) |

---
