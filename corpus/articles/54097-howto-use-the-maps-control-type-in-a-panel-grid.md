---
title: "HowTo: Use the Maps Control Type in a Panel Grid"
source_id: 54097
source_url: https://wiki.genexus.com/commwiki/wiki?54097
genexus_version: "18"
---

# HowTo: Use the Maps Control Type in a Panel Grid

To create a map in a [Native Mobile](https://wiki.genexus.com/commwiki/wiki?24799) application, follow the steps below:

**1.** Include a Grid in the [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) where you want to show a map, and set the Grid [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) to **Maps**.

**2.** If the Grid is linked to a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) set in the [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209) (or [Location Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42210)) the attribute/variable/field that contains the location data.

### [Samples](#Samples)

Suppose a [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,) called *Waste Containers* is defined in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

To see the containers' location on a map, with their different icons depending on the type of container, you can create a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) with a Grid and set the following Grid properties:

* Control type property = Maps.
* [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209) = Attribute/Variable of [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) or Geopoint, where the container's location is stored.
* [Pin Image Attribute](https://wiki.genexus.com/commwiki/wiki?42213) = Attribute/Variable of [Image data type](https://wiki.genexus.com/commwiki/wiki?15204), where the icon of each of the containers is stored, depending on its type.

`[imagen omitida: wiki id 54086]`

There is no need for this location attribute/variable/field to be displayed in the Grid layout. What is configured in the grid layout will be displayed upon tapping each point on the map.

`[imagen omitida: wiki id 54111]`


|  |
| --- |
| **Backlinks** |
| [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309) |

---
