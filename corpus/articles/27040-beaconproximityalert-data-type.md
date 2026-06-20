---
title: "BeaconProximityAlert Data Type"
source_id: 27040
source_url: https://wiki.genexus.com/commwiki/wiki?27040
genexus_version: "18"
---

# BeaconProximityAlert Data Type

This SDT is defined in order to specify a Beacon Proximity Alert.

### [Fields](#Fields)

|  |  |  |
| --- | --- | --- |
| **Name** | **Type** | **Description** |
| BeaconRegion | [BeaconRegion](https://wiki.genexus.com/commwiki/wiki?27041,,) | Identifies the [Beacon](https://wiki.genexus.com/commwiki/wiki?27025) which will execute the alert. |
| NotifyOnEntry | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) | Alert will be executed when the user enters the region. |
| NotifyOnExit | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) | Alert will be executed when the user exits the region. |

**NOTE:**In order for the Beacon Proximity Alerts to work you need to have configured the property [Location Always Usage Description](https://wiki.genexus.com/commwiki/wiki?27084)


|  |
| --- |
| **Backlinks** |
| [AddBeaconProximityAlert method](https://wiki.genexus.com/commwiki/wiki?27054) | [AddBeaconProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?27055) |
| [Beacons external object](https://wiki.genexus.com/commwiki/wiki?27025) | [GetBeaconProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?27056) | [HowTo: Using Beacons](https://wiki.genexus.com/commwiki/wiki?27070) | [Location Always Usage Description property](https://wiki.genexus.com/commwiki/wiki?27084) |
|

---
