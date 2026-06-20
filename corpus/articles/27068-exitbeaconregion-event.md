---
title: "ExitBeaconRegion event"
source_id: 27068
source_url: https://wiki.genexus.com/commwiki/wiki?27068
genexus_version: "18"
---

# ExitBeaconRegion event

This event is Invoked when the user exits a monitored beacon region added previously with the [AddBeaconProximityAlert](https://wiki.genexus.com/commwiki/wiki?27054) or [AddBeaconProximityAlerts](https://wiki.genexus.com/commwiki/wiki?27055) Methods.

### [Syntax](#Syntax)

**Event** **LocationAPI.**ExitBeaconRegion**(***&<BeaconRegion>***)**  
*Event\_code*  
**EndEvent**

Where:

*BeaconRegion*  
    An object containing information about the beacon region that was exited. This parameter is based on the [BeaconRegion Data Type](https://wiki.genexus.com/commwiki/wiki?27041,,).

*Event\_code*  
      Code associated with the event.

### 

### [Availability](#Availability)

As from [GeneXus X Evolution 3 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?26959,,).

### [See also](#See+also)

* [Beacons external object](https://wiki.genexus.com/commwiki/wiki?27025)
* [EnterBeaconRegion event](https://wiki.genexus.com/commwiki/wiki?27067)
* [ChangeBeaconsInRange event](https://wiki.genexus.com/commwiki/wiki?27069)


|  |
| --- |
| **Backlinks** |
| [Beacons external object](https://wiki.genexus.com/commwiki/wiki?27025) | [ChangeBeaconsInRange event](https://wiki.genexus.com/commwiki/wiki?27069) |
| [EnterBeaconRegion event](https://wiki.genexus.com/commwiki/wiki?27067) | [HowTo: Using Beacons](https://wiki.genexus.com/commwiki/wiki?27070) |

---
