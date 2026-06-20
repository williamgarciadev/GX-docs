---
title: "HowTo: Use Location Proximity Alerts"
source_id: 25194
source_url: https://wiki.genexus.com/commwiki/wiki?25194
genexus_version: "18"
---

# HowTo: Use Location Proximity Alerts

The purpose of this article is to explain the necessary steps to use Location Proximity Alerts to [solve Geofencing with GeneXus](https://wiki.genexus.com/commwiki/wiki?53557,,).

The following methods are used to create an application to alert the user when moving within or beyond a defined distance from a geolocation.

### [Steps to set a new Alert](#Steps+to+set+a+new+Alert)

New alerts are created on the device. To do this, follow two steps:

**1.** Create an [action](https://wiki.genexus.com/commwiki/wiki?20623) (user-defined event executed on the client-side) in the [Main object](https://wiki.genexus.com/commwiki/wiki?17817).  
This event will be executed when the alert is triggered. For example:

```
Event 'ProxAlertNotification'
    // event code
EndEvent
```

**2.** Use the [SetProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25166), and set up the following data:

* Name
* Description
* Geolocation
* Radius
* Expiration Time
* Action Name

The information must be loaded in a [GeolocationProximityAlert SDT](https://wiki.genexus.com/commwiki/wiki?25185) -*&alert*-, and added to a collection of the same type -*&alerts*- so that the method can receive it.

```
&alert.ActionName = 'ProxAlertNotification' 
&alert.Name = 'Test' 
&alert.ExpirationTime = #2015-12-31# 
&alert.GeoLocation = '-35,-56' 
&alert.Radius = 1000 
&alerts.Add(&alert) 

&boolean = Maps.SetProximityAlerts(&alerts)
```

This will trigger an alert that will execute the event 'ProxAlertNotification' when the user moves within or beyond 1000m from the geolocation '-35,-56'.

### [Get the information of the current alert](#Get+the+information+of+the+current+alert)

Executing an event when the alert is triggered is optional. But if you do it, you must know which alert executed the event, in order to do something with that information.  
This method must be used in the event executed by the alert to get the information on it.

```
&alert = Maps.GetCurrentProximityAlert()
```

### [Get the list of active alerts in the device](#Get+the+list+of+active+alerts+in+the+device)

To get the list of active alerts on the device, you should use the [GetProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25188).

```
&alerts = Maps.GetProximityAlerts()
```

### [Clear the Proximity Alerts set on the device](#Clear+the+Proximity+Alerts+set+on+the+device)

In order to delete all the alerts set on a device, you must execute the [ClearProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25190) as follows:

```
Maps.ClearProximityAlerts()
```

### [Considerations](#Considerations)

* In order to use this feature on
  [Apple](https://wiki.genexus.com/commwiki/wiki?14917) devices, set the [*Location Always usage description*](https://wiki.genexus.com/commwiki/wiki?32755).
* In order to use this feature on
  [Android](https://wiki.genexus.com/commwiki/wiki?14453) devices, enable *Use Proximity Alert property* at [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817). The purpose of this property is to indicate that alerts must be recovered after a device reboot.

### [Sample](#Sample)

You can download the sample here: [Geolocation Proximity Alerts Sample](https://wiki.genexus.com/commwiki/wiki?36985,,).

### [See Also](#See+Also)

[Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274)  
[SetProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25166)  
[GetCurrentProximityAlert method](https://wiki.genexus.com/commwiki/wiki?25189)  
[GetProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25188)  
[ClearProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25190)  
[GeolocationProximityAlert Data Type](https://wiki.genexus.com/commwiki/wiki?25185)


|  |
| --- |
| **Backlinks** |
| [ClearProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25190) | [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) |
| [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) | [GeolocationProximityAlert Data Type](https://wiki.genexus.com/commwiki/wiki?25185) | [GetCurrentProximityAlert method](https://wiki.genexus.com/commwiki/wiki?25189) | [GetProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25188) |
| [Location Always Usage Description property](https://wiki.genexus.com/commwiki/wiki?27084) | [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |
| [SetProximityAlerts method](https://wiki.genexus.com/commwiki/wiki?25166) |

---
