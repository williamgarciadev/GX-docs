---
title: "PickLocation Method"
source_id: 36729
source_url: https://wiki.genexus.com/commwiki/wiki?36729
genexus_version: "18"
---

# PickLocation Method

Opens the Geolocation Picker to pick a location.

#### [Parameters](#Parameters)

|  |  |  |
| --- | --- | --- |
| **Name** | **Type** | **Description** |
| GeolocationPickerParms | [GeolocationPickerParameters Data Type](https://wiki.genexus.com/commwiki/wiki?39587,,) | It initializes the map shown to the user |

#### [Return value](#Return+value)

* *Location:*  
  type: Geolocation  
  The location selected by the user

### [Notes](#Notes)

* In Android, the only parameter value taken into account is the InitialLocation

### [Code samples](#Code+samples)

```
Event "Select"
   composite
     &CarGeolocation = CarGeolocationGet() // Gets position of the Car from the Database or Session
     If &CarGeolocation.IsEmpty()
        &CarGeolocation = Geolocation.GetMyLocation(0,0,false) //Initialize with My Location if Empty.
     endif
     &GeolocationPickerParms.InitialLocation = &CarGeolocation
     &CarGeolocation = Geolocation.PickLocation( &GeolocationPickerParms)
     CarGeolocationSet(&CarGeolocation)
     refresh
   endcomposite
EndEvent
```


|  |
| --- |
| **Backlinks** |
| [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) | [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) |
| [HowTo: Get a Google Maps API Key for Apple](https://wiki.genexus.com/commwiki/wiki?39319) | [Layers in Maps](https://wiki.genexus.com/commwiki/wiki?40763) |

---
