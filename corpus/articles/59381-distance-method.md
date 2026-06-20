---
title: "Distance method"
source_id: 59381
source_url: https://wiki.genexus.com/commwiki/wiki?59381
genexus_version: "18"
---

# Distance method

Returns the distance, in meters, between two Geography attributes or variables.

## [Syntax](#Syntax)

*GeographyAttOrVar1*.**Distance(***GeographyAttOrVar2***)**

**Where:**

*GeographyAttOrVar1*Must be an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) or [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408).

*GeographyAttOrVar2*Must be an [attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,) or [variable](https://wiki.genexus.com/commwiki/wiki?7375) based on the [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408).

**Type Returned:**  
Numeric

## [Scope](#Scope)

**Generators:**[Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)  
**Level:** [Attribute](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?7240,,), [Variable](https://wiki.genexus.com/commwiki/wiki?7375) ([Geography data type](https://wiki.genexus.com/commwiki/wiki?32408))

## [Description](#Description)

The distance between two points is calculated, but the method accepts geographies and assumes centers or equidistance in the case of calculating it based on GeoLines or GeoPolygon.

## [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,):

```
Place
{
  PlaceId*
  PlaceName
  PlaceGeo
}
```

and the following [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021):

`[imagen omitida: wiki id 59774]`

In this example of 'Places NearBy', the places that are within 1km of the center of the Map are loaded in the &NearPlaces variable (based on the NearPlaces SDT). To do so, the following [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) was defined:

```
Rule:
Parm(&Center);

Variables:
&Center: Geography
&Radius: Numeric(4)
&NearPlaces: NearPlaces (SDT)
&Place: NearPlaces.NearPlacesItem

Source:
&Radius = 1000
For each Place
    where PlaceGeo.Distance(&Center) <= &Radius
     &Place = new()
     &Place.PlaceName = PlaceName
     &Place.PlaceDistance = PlaceGeo.Distance(&Center)/1000  // distance in Kilometers 
     &NearPlaces.Add(&Place)
endfor
```


|  |
| --- |
| **Backlinks** |
| [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) | [Table of contents:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) |

---
