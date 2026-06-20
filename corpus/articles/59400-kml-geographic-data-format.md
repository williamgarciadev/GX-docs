---
title: "KML Geographic data format"
source_id: 59400
source_url: https://wiki.genexus.com/commwiki/wiki?59400
genexus_version: "18"
---

# KML Geographic data format

KML (formerly known as Keyhole Markup Language) is a standard XML-based format used to represent vector data.

When developing a Native Mobile application, if you include in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) with its Control Type property set to Maps, you can use the [LoadKmlLayer method](https://wiki.genexus.com/commwiki/wiki?51341) to draw a set of vector data from its representation in KML format.

When developing a Web application, if you include in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) a [Map User Control](https://wiki.genexus.com/commwiki/wiki?5029), you can set the [KML property](https://wiki.genexus.com/commwiki/wiki?42414) to true, and determine the URL where the KML will be loaded from the [KMLURL property](https://wiki.genexus.com/commwiki/wiki?42415).

### [Considerations](#Considerations)

The [LoadKmlLayer method](https://wiki.genexus.com/commwiki/wiki?51341) only allows displaying the content of a KML file.

There is no functionality to initialize a variable based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) from a KML file. To achieve this, you have 2 possible options:

1) Convert the KML file to GeoJSON or WKT and, after that, initialize the attribute or variable of Geography data type using the [FromGeoJSON method](https://wiki.genexus.com/commwiki/wiki?59777) or the [FromWkt method](https://wiki.genexus.com/commwiki/wiki?18900), respectively.  
2) Run through the KML file with the [XMLReader Data Type](https://wiki.genexus.com/commwiki/wiki?6928) and populate a Geography attribute or variable for each coordinate.


|  |
| --- |
| **Backlinks** |
| [Binary Geographic data format](https://wiki.genexus.com/commwiki/wiki?59401) | [Geographic data formats](https://wiki.genexus.com/commwiki/wiki?59397) |
| [Table of contents:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) |

---
