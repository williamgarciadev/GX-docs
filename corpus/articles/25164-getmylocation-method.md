---
title: "GetMyLocation method"
source_id: 25164
source_url: https://wiki.genexus.com/commwiki/wiki?25164
genexus_version: "18"
---

# GetMyLocation method

**Warning**: This is a method offered by the Geolocation external object. The [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) is newer than the Geolocation external object and it includes the [GetLocation method](https://wiki.genexus.com/commwiki/wiki?44309) that performs the same action as the GetMyLocation method of the Geolocation external object. The use of the Maps external object is highly recommended.

Gets the current location of the Device taking in consideration a new flag to ignore possible errors on the operation. The two errors that are considered are:

* **Location Services are disabled.** The message shown is GXM\_LocationServicesAreDisabled
* **The app does not have permission to get the Location Services.** The message shown is GXM\_CouldNotGetLocationInformation

### [Parameters](#Parameters)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Default** |
| minAccuracy | Numeric (8,0) | Specifies the minimum accuracy required. This accuracy is specified in meters, 0 - ignores the accuracy of the GPS information. | 0 |
| timeout | Numeric (8,0) | Specifies, in seconds, the maximum waiting time to get a location with the desired accuracy. If the device can't get a location in the specified time with the required accuracy it returns the best location available. 0 means don't wait. | 0 |
| includeHeadingAndSpeed | Boolean | Specifies if it is necessary to include the heading and speed information in the result. | False |
| ignoreErrors | Boolean | Specifies where the execution of this operation cancels other operation or this operation error are ignored by the application. If an error occurs and the ignore error flag is set to true an empty value is returned. If an error occurs and the ignore errors flag is set to false then a msg will prompt the user with a text saying "Could not get location information" this message can be translated from the language option. | False |

For example, minAccuracy has a value of 10 meters and the return value has an accuracy of 500 meters, if the time set in the timeout parameter was not reached yet, it will attempt to obtain more precise data. If that time was reached and the desired accuracy was not obtained, the method won't return any location.

### [Return value](#Return+value)

* *GeolocationInfo*
  + Type: [GeolocationInfo SDT](https://wiki.genexus.com/commwiki/wiki?25184) (loaded with the information gathered from the GPS).

### Availability

Available since GeneXus Evolution 2 Upgrade 3.

### [Compatibility](#Compatibility)

Until GeneXus Evolution 2 Upgrade 3 the behavior of the app when an error occurred trying to get the Location Information was different

* **iOS**: If an error occurred getting the Location Information the composite block where the method was would be interrupted.
* **Android**: Would continue the Composite Block that was in it without problems.

From GeneXus Evolution 2 Upgrade 3 the default behavior will be the same and can be changed with the *ignoreErrors* flag on the method.

### See Also

* [How to show My Location](https://wiki.genexus.com/commwiki/wiki?16433).

### [Consideration](#Consideration)

In some Android devices, it is necessary to activate the locator Google service in order to work properly with this feature.


|  |
| --- |
| **Backlinks** |
| [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) | [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) |
| [HowTo: Use GetLocation method from Maps external object](https://wiki.genexus.com/commwiki/wiki?46780) | [Location Always Usage Description property](https://wiki.genexus.com/commwiki/wiki?27084) |

---
