---
title: "Geolocation domain"
source_id: 14644
source_url: https://wiki.genexus.com/commwiki/wiki?14644
genexus_version: "18"
---

# Geolocation domain

**Deprecated**: Since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853) . Replaced by [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408).

The Geolocation domain is a [Semantic Domain](https://wiki.genexus.com/commwiki/wiki?17227) that allows managing geographic information in terms of latitude and longitude.

A variable or attribute based on this domain accepts latitude/longitude coordinates as character input.

### [Sample](#Sample)

&varGeolocation = "-36.123 , -57.235"

**Where:**

&varGeolocation is defined as shown below:

`[imagen omitida: wiki id 42932]`

In View mode, when the selector displayed is selected with a tap, it allows you to jump to a map indicating the location given by the coordinates with a pin.

#### [Sample in View Mode                                     Sample after tapping](#Sample+in+View+Mode+Sample+after+tapping)

#### 

### [Considerations](#Considerations)

* Android: In order to show the map in View Mode on Android (compiled) application, you must have an API Key from Google. See [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055).  
  In order to work properly, you need to enable the following API services for the created Key:
  + Maps Javascript API
  + Maps static API
  + Geocoding API
  + Geolocation API
* iOS: Not requiered when using [KBN](https://wiki.genexus.com/commwiki/wiki?14974).

### [Troubleshooting](#Troubleshooting)

The following errors may appear:

```
The Google Maps Platform server rejected your request. The provided API key is expired
The Google Maps Platform server rejected your request. This API project is not authorized to use this API
```

Make sure you enable the previous services from the Google console and double check the API key is valid.


|  |
| --- |
| **Backlinks** |
| [Center property](https://wiki.genexus.com/commwiki/wiki?42220) | [Custom Center Attribute property](https://wiki.genexus.com/commwiki/wiki?42221) | [Custom Center Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42222) |
| [Category:Domains with Special Semantics](https://wiki.genexus.com/commwiki/wiki?14610) | [FromJson method](https://wiki.genexus.com/commwiki/wiki?37809) | [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) | [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) |
| [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) | [GeoSuite - Definitions](https://wiki.genexus.com/commwiki/wiki?52772) | [HowTo: Configure Google Places API in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?30810) |
| [HowTo: Get a Google Maps API Key for Apple](https://wiki.genexus.com/commwiki/wiki?39319) | [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055) | [HowTo: Use SD Geolocation Control in Smart Devices](https://wiki.genexus.com/commwiki/wiki?16756) | [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209) |
| [Location Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42210) | [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309) | [Maps Control Type Properties](https://wiki.genexus.com/commwiki/wiki?54092) | [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) |
| [Semantic Domains](https://wiki.genexus.com/commwiki/wiki?17227) |

---
