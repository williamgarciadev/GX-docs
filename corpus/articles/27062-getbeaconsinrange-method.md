---
title: "GetBeaconsInRange method"
source_id: 27062
source_url: https://wiki.genexus.com/commwiki/wiki?27062
genexus_version: "18"
---

# GetBeaconsInRange method

Retrieve a collection for the beacons (sorted by proximity) currently in range for the given region.

### [Parameters](#Parameters)

|  |  |  |
| --- | --- | --- |
| **Name** | **Type** | **Description** |
| regionId | VarChar(256) | The beacon region's identifier to retrieve becons in range. Empty means all regions. |

### [Return Value](#Return+Value)

* BeaconState
  + Type: [BeaconState SDT Collection](https://wiki.genexus.com/commwiki/wiki?27042,,)
  + Returns the beacons that are currently in range for the given region.

### [See Also](#See+Also)

[Beacons external object](https://wiki.genexus.com/commwiki/wiki?27025)  
[GetBeaconRegionState method](https://wiki.genexus.com/commwiki/wiki?27065)  
[StartRangingBeaconRegion method](https://wiki.genexus.com/commwiki/wiki?27059)  
[GetRangedBeaconRegions method](https://wiki.genexus.com/commwiki/wiki?27060)  
[StopRangingBeaconRegion method](https://wiki.genexus.com/commwiki/wiki?27061)


|  |
| --- |
| **Backlinks** |
| [Beacons external object](https://wiki.genexus.com/commwiki/wiki?27025) | [GetBeaconRegionState method](https://wiki.genexus.com/commwiki/wiki?27065) | [GetRangedBeaconRegions method](https://wiki.genexus.com/commwiki/wiki?27060) |
| [HowTo: Using Beacons](https://wiki.genexus.com/commwiki/wiki?27070) | [StartRangingBeaconRegion method](https://wiki.genexus.com/commwiki/wiki?27059) | [StopRangingBeaconRegion method](https://wiki.genexus.com/commwiki/wiki?27061) |

---
