---
title: "HowTo: Solve Geocoding with GeneXus"
source_id: 53464
source_url: https://wiki.genexus.com/commwiki/wiki?53464
genexus_version: "18"
---

# HowTo: Solve Geocoding with GeneXus

Geocoding is the process of transforming a description of a location (such as a pair of coordinates, an address, or the name of a place) into a location on the Earth's surface.

To geocode an address or to reverse geocode a coordinate ([GeoPoint](https://wiki.genexus.com/commwiki/wiki?58058)), the following methods are available in the [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309):

1. [GeocodeAddress method](https://wiki.genexus.com/commwiki/wiki?44309)
2. [ReverseGeocode method](https://wiki.genexus.com/commwiki/wiki?44309)

### [Samples](#Samples)

#### 1. Using the GeocodeAddress method (Maps external object)

```
&Locations = Maps.GeocodeAddress("Peatonal Sarandi, Montevideo, Uruguay")  //&Locations: collection variable of GeoPoint type
for &GeoPoint in &Locations                                                //GeoPoint: variable of GeoPoint type
   &Latitude =  &GeoPoint.Latitude
   &longitude = &GeoPoint.Longitude
   //do something with the &Latitude and &longitude variables
endfor
```

#### 2. Using the ReverseGecode method (Maps external object)

```
&GeoPoint = GeoPoint.New(-34.8910275746741, -56.18720064473088)            //GeoPoint: variable of GeoPoint type
&CollectionChar = Maps.ReverseGeocode(&GeoPoint)  
For &Char in &CollectionChar
   &PlaceName = &Char
   //do something with the &PlaceName variable
EndFor
```

In this sample, the &GeoPoint variable (based on the [GeoPoint data type](https://wiki.genexus.com/commwiki/wiki?58058)) is loaded with the coordinates of a mall in Montevideo. After that, the ReverseGecode method is used to load the &CollectionChar variable with a list of place names that correspond to the &GeoPoint coordinates. Finally, the collection is scanned to use each place name.

**Note**: The [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) (deprecated) offers similar methods based on the Geolocation domain (deprecated too). Their names are GetLocation and GetAddress.


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) |

---
