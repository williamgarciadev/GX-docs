---
title: "Android Maps API property"
source_id: 22729
source_url: https://wiki.genexus.com/commwiki/wiki?22729
genexus_version: "18"
---

# Android Maps API property

Indicates the Maps provider to be used in the application.

### [Values](#Values)

|  |  |
| --- | --- |
| **Baidu Maps API** | Baidu, Chinese maps services. |
| **AutoNavi Maps API** | AutoNavi, Chinese maps services. |
| **Google Maps API v2** | Default value. Google Maps services. |
| **Mapbox API** | Mapbox Maps |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

Depending on the property value, different API Keys must be obtained to use its services.

* For **Google** Maps, refer to [Android Google Services API Key property](https://wiki.genexus.com/commwiki/wiki?37267).
* For **Baidu** and **AutoNavi** Maps, refer to [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115).

#### [Note](#Note)

* The value **Google Maps API v1**is deprecated because that version of the API is no longer available. It can only be used if you already have an API Key for it.  
  API v2 compared to API v1:
  + Support for [Pin Image](https://wiki.genexus.com/commwiki/wiki?15309).
  + If [Show My Location](https://wiki.genexus.com/commwiki/wiki?15309) is enabled and the device changes its geolocation, the position of the pin that shows the location will be updated automatically.
  + Hybrid value for [Map Type](https://wiki.genexus.com/commwiki/wiki?15309) is supported.
  + Maps can be rotated.
  + Geolocation picker control allows dragging the selection pin.
* Google map requires [Google Play Services](https://en.wikipedia.org/wiki/Google_Play_Services) installed on the device.
* **Google Maps API**, until [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?33798,,), requires [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115) instead of [Android Google Services API Key property](https://wiki.genexus.com/commwiki/wiki?37267).
* This property can be found in [Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451) until [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?33798,,).  
  As of [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,), it is relocated to [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus X Evolution 2 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?22626,,).

### [See Also](#See+Also)

* [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309)
* [GeoLocation Picker](https://wiki.genexus.com/commwiki/wiki?15969)
* [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115) (for Baidu and AutoNavi, and also Google until [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?33798,,))
* [Android Google Services API Key property](https://wiki.genexus.com/commwiki/wiki?37267) (for Google as of [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,))


|  |
| --- |
| **Backlinks** |
| [Android Google Services API Key property](https://wiki.genexus.com/commwiki/wiki?37267) | [Android Maps API Key property](https://wiki.genexus.com/commwiki/wiki?19115) | [Android specific properties](https://wiki.genexus.com/commwiki/wiki?31449) |
| [HowTo: Maps - Mapbox](https://wiki.genexus.com/commwiki/wiki?48350) | [Mapbox API Private Key property](https://wiki.genexus.com/commwiki/wiki?47972) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
