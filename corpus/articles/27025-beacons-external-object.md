---
title: "Beacons external object"
source_id: 27025
source_url: https://wiki.genexus.com/commwiki/wiki?27025
genexus_version: "18"
---

# Beacons external object

Beacons are devices that support Bluetooth low energy and allow bi-directional communications with them. So, with beacons, you can take advantage of this new way of communication and solve new scenarios of Geofencing with accuracy and enable to solve several in-door localization problems.

|  |  |
| --- | --- |
|  |  |

**Note**: See [Beacons Scenarios](https://wiki.genexus.com/commwiki/wiki?27026,,) to see why Beacons become important in many localization scenarios.

## [Properties](#Properties)

### [RangingAvailable property](#RangingAvailable+property)

Determines whether the device supports ranging. If False, all attempts to range beacons will fail.

### [BeaconProximityAlertsAvailable property](#BeaconProximityAlertsAvailable+property)

Determines whether the device supports beacon proximity alerts. If False, all attempts to set proximity alerts will fail.

### [ServiceEnabled property](#ServiceEnabled+property)

Determines whether the user has location services enabled. If False, and you proceed to call other Beacons, the user will be prompted with the warning or fail depending on the current authorization status.

### [AuthorizationStatus property](#AuthorizationStatus+property)

Returns the current authorization status. It is based on APIAuthorizationStatus domain.

## [Methods](#Methods)

### [AddBeaconProximityAlert method](#AddBeaconProximityAlert+method)

Start monitoring the specified beacon region.  
Details in [AddBeaconProximityAlert method](https://wiki.genexus.com/commwiki/wiki?27054).

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | proximityAlert:BeaconProximityAlert |
|  |  |

### [AddBeaconProximityAlerts method](#AddBeaconProximityAlerts+method)

Start monitoring the specified beacon regions (multiple beacons).  
Details in [AddBeaconProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?27055).

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | proximityAlerts:Collection( BeaconProximityAlert ) |
|  |  |

### [GetBeaconProximityAlerts method](#GetBeaconProximityAlerts+method)

Retrieve a collection for the beacon regions that are currently being monitored.  
Details in [GetBeaconProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?27056)

|  |  |
| --- | --- |
| **Return value** | Collection( BeaconProximityAlert ) |
| **Parameters** | None |
|  |  |

### [RemoveBeaconProximityAlert method](#RemoveBeaconProximityAlert+method)

Removes the beacon region being monitored.  
Details in [RemoveBeaconProximityAlert method](https://wiki.genexus.com/commwiki/wiki?27057).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | proximityAlertRegionId:[VarChar(256)](https://wiki.genexus.com/commwiki/wiki?6778) |
|  |  |

### [ClearBeaconProximityAlerts method](#ClearBeaconProximityAlerts+method)

Removes all the beacon regions being monitored.  
Details in [ClearBeaconProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?27058).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |
|  |  |

### [GetBeaconRegionState method](#GetBeaconRegionState+method)

Retrieve the cached state of the specified region.  
Details in [GetBeaconRegionState method](https://wiki.genexus.com/commwiki/wiki?27065).

|  |  |
| --- | --- |
| **Return value** | RegionState |
| **Parameters** | regionId:[VarChar(256)](https://wiki.genexus.com/commwiki/wiki?6778) |
|  |  |

### [StartRangingBeaconRegion method](#StartRangingBeaconRegion+method)

Starts the delivery of notifications for beacons in the specified region.  
Details in [StartRangingBeaconRegion method](https://wiki.genexus.com/commwiki/wiki?27059)

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | beaconRegion:BeaconRegion |
|  |  |

### [GetRangedBeaconRegions method](#GetRangedBeaconRegions+method)

Retrieve a collection for the beacon regions that are currently providing ranging.  
Details in [GetRangedBeaconRegions method](https://wiki.genexus.com/commwiki/wiki?27060).

|  |  |
| --- | --- |
| **Return value** | Collection( BeaconRegion ) |
| **Parameters** | None |
|  |  |

### [StopRangingBeaconRegion method](#StopRangingBeaconRegion+method)

Stops the delivery of notifications for the specified beacon region.  
Details in [StopRangingBeaconRegion method](https://wiki.genexus.com/commwiki/wiki?27061).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | regionId:[VarChar(256)](https://wiki.genexus.com/commwiki/wiki?6778) |
|  |  |

### [GetBeaconsInRange method](#GetBeaconsInRange+method)

Retrieve a collection for the beacons (sorted by proximity) currently in range for the given region.  
Details in [GetBeaconsInRange method](https://wiki.genexus.com/commwiki/wiki?27062).

|  |  |
| --- | --- |
| **Return value** | Collection( BeaconState ) |
| **Parameters** | regionId:[VarChar(256)](https://wiki.genexus.com/commwiki/wiki?6778) |
|  |  |

### [StartAsBeacon method](#StartAsBeacon+method)

Advertises the current device as a beacon.  
Details in [StartAsBeacon method](https://wiki.genexus.com/commwiki/wiki?27063).

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | beaconInfo:BeaconInfo |
|  |  |

### [StopAsBeacon method](#StopAsBeacon+method)

Stops advertising the current device as a beacon.  
Details in [StopAsBeacon method](https://wiki.genexus.com/commwiki/wiki?27064).

|  |  |
| --- | --- |
| **Return value** | [Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Parameters** | None |
|  |  |

## [Events](#Events)

### [EnterBeaconRegion event](#EnterBeaconRegion+event)

Invoked when the user enters a monitored beacon region.  
Details in [EnterBeaconRegion event](https://wiki.genexus.com/commwiki/wiki?27067).

|  |  |
| --- | --- |
| **Input** | beaconRegion:BeaconRegion |
| **Ouytput** | None |
|  |  |

### [ExitBeaconRegion event](#ExitBeaconRegion+event)

Invoked when the user exits a monitored beacon region.  
Details in [ExitBeaconRegion event](https://wiki.genexus.com/commwiki/wiki?27068).

|  |  |
| --- | --- |
| **Input** | beaconRegion:BeaconRegion |
| **Ouytput** | None |
|  |  |

### [ChangeBeaconsInRange event](#ChangeBeaconsInRange+event)

Invoked when a new set of beacons' states are available in the specified region.  
Details in [ChangeBeaconsInRange event](https://wiki.genexus.com/commwiki/wiki?27069).

|  |  |
| --- | --- |
| **Input** | beaconRegion:BeaconRegion, beacons:Collection( BeaconState ) |
| **Ouytput** | None |
|  |  |

## [Domains](#Domains)

### [APIAuthorizationStatus domain](#APIAuthorizationStatus+domain)

Detailed description in [APIAuthorizationStatus domain](https://wiki.genexus.com/commwiki/wiki?39656).

## [Structured Data Types](#Structured+Data+Types)

### [BeaconInfo](#BeaconInfo)

Detailed description in [BeaconInfo Data Type](https://wiki.genexus.com/commwiki/wiki?27039).

### [BeaconProximityAlert](#BeaconProximityAlert)

Detailed description in [BeaconProximityAlert Data Type](https://wiki.genexus.com/commwiki/wiki?27040)

### [BeaconRegion](#BeaconRegion)

Detailed description in [BeaconRegion Data Type](https://wiki.genexus.com/commwiki/wiki?27041,,)

### [BeaconState](#BeaconState)

Detailed description in [BeaconState Data Type](https://wiki.genexus.com/commwiki/wiki?27042,,)

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | Smart Devices (iOS, Android) |

## [Availability](#Availability)

This external object is available for iOS since [GeneXus X Evolution 3 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?26959,,) and for Android since GeneXus 16 Upgrade 11.

## [See Also](#See+Also)

* [What is a Beacon?](https://wiki.genexus.com/commwiki/wiki?27071,,)
* [Beacon Requirements](https://wiki.genexus.com/commwiki/wiki?33730,,)
* [HowTo: Using Beacons](https://wiki.genexus.com/commwiki/wiki?27070)


|  |
| --- |
| **Backlinks** |
| [AddBeaconProximityAlert method](https://wiki.genexus.com/commwiki/wiki?27054) | [AddBeaconProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?27055) | [BeaconInfo Data Type](https://wiki.genexus.com/commwiki/wiki?27039) |
| [BeaconProximityAlert Data Type](https://wiki.genexus.com/commwiki/wiki?27040) | [ClearBeaconProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?27058) |
| [EnterBeaconRegion event](https://wiki.genexus.com/commwiki/wiki?27067) | [ExitBeaconRegion event](https://wiki.genexus.com/commwiki/wiki?27068) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) |
| [GetBeaconProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?27056) | [GetBeaconRegionState method](https://wiki.genexus.com/commwiki/wiki?27065) | [GetBeaconsInRange method](https://wiki.genexus.com/commwiki/wiki?27062) |
| [GetRangedBeaconRegions method](https://wiki.genexus.com/commwiki/wiki?27060) | [HowTo: Using Beacons](https://wiki.genexus.com/commwiki/wiki?27070) | [RemoveBeaconProximityAlert method](https://wiki.genexus.com/commwiki/wiki?27057) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) |
| [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) | [StartAsBeacon method](https://wiki.genexus.com/commwiki/wiki?27063) | [StartRangingBeaconRegion method](https://wiki.genexus.com/commwiki/wiki?27059) | [StopAsBeacon method](https://wiki.genexus.com/commwiki/wiki?27064) |
| [StopRangingBeaconRegion method](https://wiki.genexus.com/commwiki/wiki?27061) |

---
