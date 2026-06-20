---
title: "GetCurrentProximityAlert method"
source_id: 25189
source_url: https://wiki.genexus.com/commwiki/wiki?25189
genexus_version: "18"
---

# GetCurrentProximityAlert method

Gets the information related to the [ProximityAlert](https://wiki.genexus.com/commwiki/wiki?25185) which triggered the action.

**Type Returned:**  
GeolocationProximityAlerts  
    Collection of [GeolocationProximityAlert SDT](https://wiki.genexus.com/commwiki/wiki?25185).

### [Description](#Description)

If a Proximity Alert has an action defined, an event is executed when the alert is triggered. In that event, some of the information used to set that alert could be needed. 

This method only works when called from an action triggered by a [ProximityAlert](https://wiki.genexus.com/commwiki/wiki?25185), returning an SDT with the information of the alert which triggered the event.

### [See Also](#See+Also)

[HowTo: Use Location Proximity Alerts](https://wiki.genexus.com/commwiki/wiki?25194)


|  |
| --- |
| **Backlinks** |
| [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) | [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) | [GeolocationProximityAlert Data Type](https://wiki.genexus.com/commwiki/wiki?25185) |
| [HowTo: Use Location Proximity Alerts](https://wiki.genexus.com/commwiki/wiki?25194) |

---
