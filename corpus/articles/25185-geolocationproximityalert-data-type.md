---
title: "GeolocationProximityAlert Data Type"
source_id: 25185
source_url: https://wiki.genexus.com/commwiki/wiki?25185
genexus_version: "18"
---

# GeolocationProximityAlert Data Type

This [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) is needed to set up [Proximity Alerts](https://wiki.genexus.com/commwiki/wiki?25166) for Native Mobile applications. 

#### [Fields](#Fields)

|  |  |  |
| --- | --- | --- |
| **Name** | **Type** | **Description** |
| Name | Character(50) | Specifies the Name of the Alert. |
| Description | Character(50) | Description of the Alert. |
| GeoLocation | Geolocation | Center of the region which will fire the Alert. |
| Radius | Numeric(4.0) | A user moves within or beyond a set distance from a location. |
| ExpirationTime | DateTime | Date and time for the alert to expire. The Alert will not be fired after this. |
| ActionName (optional) | Character(50) | Action to execute if the Alert is fired.  If specified, the specified action is raised and the [GetCurrentProximityAlert](https://wiki.genexus.com/commwiki/wiki?25189) can be used in the event associated with the action.  If no action is specified a message with the Description of the alert is the default behavior. |

**Note**: Each 'Name' of the collection must be unique. If there's any repeated value, the application will take the last one inserted.

### [See Also](#See+Also)

[HowTo: Use Location Proximity Alerts](https://wiki.genexus.com/commwiki/wiki?25194)


|  |
| --- |
| **Backlinks** |
| [ClearProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25190) | [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) | [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) |
| [GetCurrentProximityAlert method](https://wiki.genexus.com/commwiki/wiki?25189) | [GetProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25188) | [HowTo: Use Location Proximity Alerts](https://wiki.genexus.com/commwiki/wiki?25194) | [SetProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25166) |

---
