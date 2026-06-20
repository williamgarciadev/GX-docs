---
title: "StartTracking method"
source_id: 25177
source_url: https://wiki.genexus.com/commwiki/wiki?25177
genexus_version: "18"
---

# StartTracking method

This method is provided by the [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309). It triggers the GPS to start tracking the device's location. The updated location will be changed for every *ChangesInterval* and also if the device moves a certain *distance*.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | TrackingParameters SDT |

### [TrackingParameters SDT members](#TrackingParameters+SDT+members)

* **ChangesInterval:** Numeric (8.0)

Specifies the minimum time in seconds between change updates. 0 means ignore this parameter.

* **Distance:** Numeric (8.0)

Specifies the minimum distance between change updates. 0 means any distance.

* **Action:** Character (20)

Specifies the name of the action that the app will automatically call to process the latest updates of the Tracking methods.

This action must be defined in the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770):

* In case of a Main [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), the action should be defined as an event.
* In case of a Main [Menu object](https://wiki.genexus.com/commwiki/wiki?16321), it should be defined as an Item or Notification (Notifications area). For more information, refer to the Samples section.

**Important:** The called action must be an event that does not contain any UI interaction.

* **ActionTimeInterval:** Numeric (8.0)

Specifies the minimum time that must elapse before the action is executed again. The value entered in this parameter must be greater than ChangesInterval; otherwise, this parameter will be ignored. This time interval is restarted when the Action is executed, and is not affected when the geolocation changes.

* **Accuracy:** Numeric (8.0)

Measurement in meters per second of the device's movement.

* **UseForegroundService:** Boolean

Only for the Android Platform. You need to enable this option to use this method on Android Devices with an operating system greater than or equal to Android 8.

### [Consideration](#Consideration)

#### [As the **StartTracking method** is also supported by the [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274), it also accepts scalar parameters as follows:](#As+the+StartTracking+method+is+also+supported+by+the+com.gxwiki.wiki%3F31274%2CGeolocation%2Bexternal%2Bobject+Geolocation+external+object%2C+it+also+accepts+scalar+parameters+as+follows%3A)

* changeInterval:[Numeric(8.0)](https://wiki.genexus.com/commwiki/wiki?6793)
* distance:[Numeric(8.0)](https://wiki.genexus.com/commwiki/wiki?6793)
* action:[Character(20)](https://wiki.genexus.com/commwiki/wiki?6777)
* actionTimeInterval:[Numeric(8.0)](https://wiki.genexus.com/commwiki/wiki?6793)
* [accuracy:[Numeric(8.0)](https://wiki.genexus.com/commwiki/wiki?6793) ]

### [Samples](#Samples)

You can define, for example, an event (associated with a button) in a Main [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) as follows:

```
Event 'StartTracking'
    Composite
        Maps.ClearLocationHistory()
        Maps.StartTracking(60,100,"",0)
        msg("Tracking Started")
    EndComposite
EndEvent
```

When defining an Action, you can program an event (associated with a button) as follows:

**Main Panel1:**

```
Event 'CallsTrackingPanel'
   Composite
     TrackingPanel()
     msg("Call Tracking Panel")
   EndComposite 
EndEvent

Event 'PositionChange'
   Composite
     &LocationInfo = GeneXus.Common.Maps.GetLocationHistory(&Today)
     SaveTime(...) //SaveTime is a Procedure that stores tracking information in the database
   EndComposite 
EndEvent
```

The **T****rackingPanel** [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) should invoke the StartTracking method, for example, in an event associated with a button:

```
​​​Event 'Tracking'
Composite
     &TrackingParameters.Action ="PositionChange"
     &TrackingParameters.UseForegroundService =True
     Maps.ClearLocationHistory()
     Maps.StartTracking(&TrackingParameters)
     msg("Tracking Started")
EndComposite
EndEvent
```

### [Availability](#Availability)

The parameters Action and ActionTimeInterval are available for:

* Android since [GeneXus X Evolution 3 Upgrade 2](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?26959,,).
* [Apple](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?23122,,) since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?20247,,).

UseForegroundService is available for Android since [GeneXus 16 upgrade 5](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?43446,,).

**Warning**: The [Use Background Location property](https://wiki.genexus.com/commwiki/wiki?47527) is mandatory since Android 10.

### [See Also](#See+Also)

[HowTo: Solve Tracking with GeneXus](https://wiki.genexus.com/commwiki/wiki?20832)  
[Location When In Use Usage Description property](https://wiki.genexus.com/commwiki/wiki?27085)


|  |
| --- |
| **Backlinks** |
| [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) | [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) | [HowTo: Solve Tracking with GeneXus](https://wiki.genexus.com/commwiki/wiki?20832) |
| [Location Always Usage Description property](https://wiki.genexus.com/commwiki/wiki?27084) | [Location When In Use Usage Description property](https://wiki.genexus.com/commwiki/wiki?27085) | [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) |

---
