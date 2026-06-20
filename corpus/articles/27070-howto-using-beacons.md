---
title: "HowTo: Using Beacons"
source_id: 27070
source_url: https://wiki.genexus.com/commwiki/wiki?27070
genexus_version: "18"
---

# HowTo: Using Beacons

### [How to start  monitoring some specific beacon region?](#How+to+start+monitoring+some+specific+beacon+region%3F)

```
Beacons.AddBeaconProximityAlert(proximityAlert)
```

Where  
proximityAlert is a [BeaconProximityAlert SDT](https://wiki.genexus.com/commwiki/wiki?27040). The [AddBeaconProximityAlert method](https://wiki.genexus.com/commwiki/wiki?27054) receives this SDT and add the alert or replace if a region with the same identifier is found.

This can also be done with a collection of [BeaconProximityAlert SDT](https://wiki.genexus.com/commwiki/wiki?27040) and the [AddBeaconProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?27055).


### [I'm inside a Beacon region now what?](#I%27m+inside+a+Beacon+region+now+what%3F)

After you know you are in a Beacon region you can give your users further information (navigation, etc) by determinating the distance between a device and a Beacon.  
For example when people enter to a conference you can give a Welcome information by using the previous API of proximity of a Beacon region, but after this welcome information you know people is in, so you can guide them to navigate the conference by start ranging all the beacons that are inside the conference in different rooms.

In order to start ranging you need to call

```
Beacons.StartRangingBeaconRegion(BeaconRegion)
```

Where  
BeaconRegion is a [BeaconRegion SDT](https://wiki.genexus.com/commwiki/wiki?27041,,) and the [StartRangingBeaconRegion method](https://wiki.genexus.com/commwiki/wiki?27059) starts the delivery of notifications for beacons in the specified region.

---

### [How to know when entering or exiting to a BeaconRegion?](#How+to+know+when+entering+or+exiting+to+a+BeaconRegion%3F)

There are some events on the [Beacons external object](https://wiki.genexus.com/commwiki/wiki?27025) that you can listen to do this.

[EnterBeaconRegion](https://wiki.genexus.com/commwiki/wiki?27067)

```
Event Beacons.EnterBeaconRegion(BeaconRegion)
```

Invoked when the user enters a monitered beacon region

[ExitBeaconRegion](https://wiki.genexus.com/commwiki/wiki?27068)

```
Event Beacons.ExitBeaconRegion(BeaconRegion)
```

Invoked when the user exits a monitored beacon region

[ChangeBeaconsInRange](https://wiki.genexus.com/commwiki/wiki?27069)

```
Event Beacons.ChangeBeaconsInRange(BeaconRegion, Beacons)
```

Invoked when a new set of beacons' states are available in the specified region.

The first two events are fired for proximityAlerts being added previously, the third one, is called periodicaly with beacons states updates for regions started ranging previously.

---

### [Let your device be a Beacon](#Let+your+device+be+a+Beacon)

As explained in [What is a Beacon?](https://wiki.genexus.com/commwiki/wiki?27071,,) any device with at least Bluetooth 4.0 is potencially a Beacon.

GeneXus provides a method in Beacons to allow your device (if allowed) became ranging as a Beacon.

```
Beacons.StartAsBeacon(BeaconInfo)
```

BeaconInfo is based on the [BeaconInfo Data Type](https://wiki.genexus.com/commwiki/wiki?27039) and contains the beacon information to advertise.

In order to stop advertising the current device as a beacon use

```
Beacons.StopAsBeacon()
```

---

### [Additional Functions](#Additional+Functions)

```
Beacons.GetBeaconProximityAlerts()
```

Retrieve a collection for the beacon regions that are currently being monitored. [See more](https://wiki.genexus.com/commwiki/wiki?27056)

```
Beacons.RemoveBeaconProximityAlert(proximityAlertRegionId)
```

Remove the region being monitored by identifier. [See more](https://wiki.genexus.com/commwiki/wiki?27057)

```
Beacons.ClearBeaconProximityAlerts()
```

Removes all the beacon regions being monitored. [See more](https://wiki.genexus.com/commwiki/wiki?27058)

```
Beacons.GetBeaconRegionState(regionId)
```

Retrieve the cached state of the specified beacon region. [See more](https://wiki.genexus.com/commwiki/wiki?27065)

```
Beacons.StopRagingBeaconRegion(regionId)
```

Stops the delivery of notifications for the specified beacon region. [See more](https://wiki.genexus.com/commwiki/wiki?27061)

```
Beacons.GetRangedBeaconRegions()
```

Retrieve a collection for the beacon regions thar are currently providing ranging. [See more](https://wiki.genexus.com/commwiki/wiki?27060)

```
Beacons.GetBeaconsInRange(regionId)
```

Retrieve a collection for the beacons (sorted by proximity) currently in range for the given region. Empty regionId means all regions. [See more](https://wiki.genexus.com/commwiki/wiki?27062)

---

### [See also](#See+also)

[Beacons external object](https://wiki.genexus.com/commwiki/wiki?27025)

---

|  |
| --- |
| **Backlinks** |
| [Beacons external object](https://wiki.genexus.com/commwiki/wiki?27025) |

---
