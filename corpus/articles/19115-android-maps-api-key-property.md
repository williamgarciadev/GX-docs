---
title: "Android Maps API Key property"
source_id: 19115
source_url: https://wiki.genexus.com/commwiki/wiki?19115
genexus_version: "18"
---

# Android Maps API Key property

Indicates the API key to use Maps services.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))

### [Description](#Description)

This property must be set when using [Maps Control](https://wiki.genexus.com/commwiki/wiki?15309) or [SD Geolocation Picker Control](https://wiki.genexus.com/commwiki/wiki?15969).

#### [Value](#Value)

An alphanumeric key that can be obtained from [Baidu Maps](http://lbsyun.baidu.com/apiconsole/key) or [AutoNavi's Gaode Maps](http://lbs.amap.com/dev/key) depending on the value of [Android Maps API property](https://wiki.genexus.com/commwiki/wiki?22729).

#### [Notes](#Notes)

* When modifying the value of this property, make sure to update the related [Application Signing section](https://wiki.genexus.com/commwiki/wiki?23328) (Key Store File, Alias, and passwords).
* As of [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,), this property applies only when [Android Maps API](https://wiki.genexus.com/commwiki/wiki?22729) is ***Baidu Maps API*** or ***AutoNavi Maps API***.
* Until [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?33798,,), this property also applies to ***Google Maps API v2***and you must refer to [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055) in order to fill this property*.*Higher upgrades must use [Android Google Services API Key property](https://wiki.genexus.com/commwiki/wiki?37267).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [See Also](#See+Also)

* [Android Maps API property](https://wiki.genexus.com/commwiki/wiki?22729)
* [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817)
* [Baidu - Get API Key](http://lbsyun.baidu.com/index.php?title=androidsdk/guide/key)
* [AutoNavi - Get API Key](https://lbs.amap.com/api/android-location-sdk/guide/create-project/get-key)


|  |
| --- |
| **Backlinks** |
| [Android Google Services API Key property](https://wiki.genexus.com/commwiki/wiki?37267) | [Android Maps API property](https://wiki.genexus.com/commwiki/wiki?22729) | [Android specific properties](https://wiki.genexus.com/commwiki/wiki?31449) |
| [Geography data type](https://wiki.genexus.com/commwiki/wiki?32408) | [HowTo: Configure Google Places API in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?30810) | [HowTo: Get an API Key from Google](https://wiki.genexus.com/commwiki/wiki?19055) |
| [HowTo: Maps - Mapbox](https://wiki.genexus.com/commwiki/wiki?48350) | [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
