---
title: "SetProximityAlerts method"
source_id: 25166
source_url: https://wiki.genexus.com/commwiki/wiki?25166
genexus_version: "18"
---

# SetProximityAlerts method

This method is provided by the [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309). It sets a set of proximity alerts (for each element of the ProximityAlerts SDT parameter) and returns the success status of the operation.

**Type Return**  
Boolean

**Parameters**

|  |  |  |
| --- | --- | --- |
| **Name** | **Type** | **Description** |
| ProximityAlerts | [GeolocationProximityAlert SDT](https://wiki.genexus.com/commwiki/wiki?25185) | Specifies the list of alerts to be set. |

**Note**: The SetProximityAlerts method cannot be used on the server side. If used, the [spc0200](https://wiki.genexus.com/commwiki/wiki?6774) message will be displayed.

### [See Also](#See+Also)

[HowTo: Use Location Proximity Alerts](https://wiki.genexus.com/commwiki/wiki?25194)


|  |
| --- |
| **Backlinks** |
| [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) | [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) | [GeolocationProximityAlert Data Type](https://wiki.genexus.com/commwiki/wiki?25185) |
| [GetProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25188) | [HowTo: Use Location Proximity Alerts](https://wiki.genexus.com/commwiki/wiki?25194) | [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) |

---
