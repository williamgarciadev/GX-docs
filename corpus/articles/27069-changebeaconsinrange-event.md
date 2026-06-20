---
title: "ChangeBeaconsInRange event"
source_id: 27069
source_url: https://wiki.genexus.com/commwiki/wiki?27069
genexus_version: "18"
---

# ChangeBeaconsInRange event

This event is Invoked when a new set of beacons' states are available in the specified region. Is called periodicaly with beacons states updates for regions started ranging previously with the [StartRangingBeaconRegion method](https://wiki.genexus.com/commwiki/wiki?27059).

### [Syntax](#Syntax)

**Event** **LocationAPI.**ChangeBeaconsInRange(*&<BeaconRegion>,&<Beacons>***)**  
*Event\_code*  
**EndEvent**

Where:

*BeaconRegion*  
    The region object containing the parameters that were used to locate the beacons. This parameter is based on the [BeaconRegion Data Type](https://wiki.genexus.com/commwiki/wiki?27041,,).

Beacons  
     The beacons currently in range, sorted by proximity. If beacons is empty, it may be assumed no beacons that match the specified region are nearby. Similarly if a specific beacon no longer appears in beacons, it may be assumed the beacon is no longer received by the device.

*Event\_code*  
      Code associated with the event. 

### 

### [Availability](#Availability)

As from [GeneXus X Evolution 3 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?26959,,).

### [See also](#See+also)

* [EnterBeaconRegion event](https://wiki.genexus.com/commwiki/wiki?27067)
* [ExitBeaconRegion event](https://wiki.genexus.com/commwiki/wiki?27068)


|  |
| --- |
| **Backlinks** |
| [Beacons external object](https://wiki.genexus.com/commwiki/wiki?27025) | [EnterBeaconRegion event](https://wiki.genexus.com/commwiki/wiki?27067) | [ExitBeaconRegion event](https://wiki.genexus.com/commwiki/wiki?27068) |
| [HowTo: Using Beacons](https://wiki.genexus.com/commwiki/wiki?27070) |

---
