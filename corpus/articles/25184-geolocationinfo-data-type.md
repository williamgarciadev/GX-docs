---
title: "GeolocationInfo Data Type"
source_id: 25184
source_url: https://wiki.genexus.com/commwiki/wiki?25184
genexus_version: "18"
---

# GeolocationInfo Data Type

This SDT is defined in order to get information from the GPS in a format that can be manageable by a GeneXus User.

### [Fields](#Fields)

|  |  |  |
| --- | --- | --- |
| **Name** | **Type** | **Description** |
| Location | Geolocation | A Location defined in Geolocation Domain. |
| Description | Character(50) | Information context in relation to the location.  For iOS no value is returned, for Android, it returns the name of the provider that was used to get the location, for example when using the GPS "LocationInfo (GPS)" is returned. |
| Time | DateTime | Time Stamp of the Location returned. |
| Precision | Numeric(8,2) | Precision of the how the location has been gathered (in meters). |
| RestrictedAccuracy | Boolean | Indicates if the Location was obtained using reduced location accuracy (available from [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,)) |
| Heading | Numeric(6,2) | Direction were it was heading the device. If this field cannot be calculated a -1 is returned instead. |
| Speed | Numeric(8,2) | Speed at which the device is moving. If this field cannot be calculated a -1 is returned instead. |

The GeoLocationInfo is used to transport georeferenced information from the device to the App.


|  |
| --- |
| **Backlinks** |
| [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) | [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) | [GetMyLocation method](https://wiki.genexus.com/commwiki/wiki?25164) |
|

---
