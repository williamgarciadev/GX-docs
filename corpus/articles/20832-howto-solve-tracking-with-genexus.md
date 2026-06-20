---
title: "HowTo: Solve Tracking with GeneXus"
source_id: 20832
source_url: https://wiki.genexus.com/commwiki/wiki?20832
genexus_version: "18"
---

# HowTo: Solve Tracking with GeneXus

To create an application that keeps track of a device's position (the GPS must be activated), the following methods are provided by the [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309):

* [StartTracking method](https://wiki.genexus.com/commwiki/wiki?25177): Starts the device tracking.
* [EndTracking method](https://wiki.genexus.com/commwiki/wiki?44309): Ends the device tracking.
* [GetLocationHistory method](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?25180,,): Returns the locations registered by the device.

You can define, for example, a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) with three events (buttons) as follows:

The first button starts the tracking:

```
Event 'StartTracking'
    Composite
        Maps.ClearLocationHistory()
        Maps.StartTracking(60,100,"",0)
        msg("Tracking Started")
    EndComposite
EndEvent
```

The second button stops the tracking:

```
Event 'StopTracking'
    Composite
        Maps.EndTracking()
        msg("Tracking Stoped")
    EndComposite
EndEvent
```

The third button offers to recover the Location History using the [GetLocationHistory method](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?25180,,):

```
Event 'SetPositionsInMap'
    &locationCollection = Maps.GetLocationHistory(&Today)
Endevent
```

The loaded collection (&locationCollection) would be shown in a Grid with its [Control Type property = Maps](https://wiki.genexus.com/commwiki/wiki?15309).

Note that the tracking system can be expensive in terms of battery, so the tracking operations should be started and ended based on the specific needs of the application.

**Note**: In Apple, to do background tracking, it is necessary to include the 'location' value in the [Background Modes property](https://wiki.genexus.com/commwiki/wiki?35408).

### [Tracking - Silent Notifications](#Tracking+-+Silent+Notifications)

Another way to track is through silent notifications. In the methods described above, the control and data registration are done exclusively from the device. The registration of the device's location may be interrupted by it, either because the user does not authorize the activation of the GPS, or the application on the cell phone stops running, etc.

In these cases, it may be useful to offer a tracking mechanism that is centralized from the delivery fleet provider, using notifications. The server sends a silent notification to wake up the device, which should reply with its current location.

You can find more information in: HowTo: Solve Tracking from a Silent Notification in Native Mobile apps.

### [Showcase](#Showcase)

[GeoCity Showcase](https://wiki.genexus.com/commwiki/wiki?49231)**:** In this Knowledge Base, you can find the "MotoDriverApp" Panel that uses Tracking.

### [See Also](#See+Also)

[HowTo: Solve Geofencing with GeneXus](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?53557,,)  
[HowTo: Use GetLocation method from Maps external object](https://wiki.genexus.com/commwiki/wiki?46780)


|  |
| --- |
| **Backlinks** |
| [Background Modes property](https://wiki.genexus.com/commwiki/wiki?35408) | [Geolocation API - Scenarios](https://wiki.genexus.com/commwiki/wiki?21763) | [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) |
| [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) | [Table of contents:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) | [HowTo: Use SD Geolocation Control in Smart Devices](https://wiki.genexus.com/commwiki/wiki?16756) | [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) |
| [StartTracking method](https://wiki.genexus.com/commwiki/wiki?25177) |

---
