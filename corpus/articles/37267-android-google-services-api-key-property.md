---
title: "Android Google Services API Key property"
source_id: 37267
source_url: https://wiki.genexus.com/commwiki/wiki?37267
genexus_version: "18"
---

# Android Google Services API Key property

Indicates the API key to use Google services.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

This property must be set in order to include [maps](https://wiki.genexus.com/commwiki/wiki?15309), use the [geolocation picker](https://wiki.genexus.com/commwiki/wiki?15969) or embed [YouTube videos](https://wiki.genexus.com/commwiki/wiki?21923) in the application, all of them through [Google services](https://en.wikipedia.org/wiki/Google_Play_Services).

#### [Values](#Values)

A key of 39 alphanumeric characters long, obtained as explained in [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055).

### [Notes](#Notes)

* The device requires [Google Play Services](https://en.wikipedia.org/wiki/Google_Play_Services) installed.
* For maps, the [Android Maps API property](https://wiki.genexus.com/commwiki/wiki?22729) must be set to **Google Maps API v2**. The API Key must have a billing account enabled; otherwise, the grid will not be displayed as a map. More information [here](https://support.google.com/googleapi/answer/6158867?hl=en).
* When changing this property value, make sure to update the related [Application Signing section](https://wiki.genexus.com/commwiki/wiki?23328) (Key Store File, Alias, and passwords).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [See Also](#See+Also)

* [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115)
* [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055)
* [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309)
* [GeoLocation Picker](https://wiki.genexus.com/commwiki/wiki?15969)
* [HowTo: Embedding YouTube videos in an Android application](https://wiki.genexus.com/commwiki/wiki?21923)


|  |
| --- |
| **Backlinks** |
| [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115) | [Android Maps API property](https://wiki.genexus.com/commwiki/wiki?22729) | [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309) |
| [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) | [KB:Showcase - GeoCity](https://wiki.genexus.com/commwiki/wiki?49231) |

---
