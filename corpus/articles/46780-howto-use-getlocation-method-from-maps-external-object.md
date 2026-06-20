---
title: "HowTo: Use GetLocation method from Maps external object"
source_id: 46780
source_url: https://wiki.genexus.com/commwiki/wiki?46780
genexus_version: "18"
---

# HowTo: Use GetLocation method from Maps external object

The GetLocation method offered by the [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) allows getting the current location.

`[imagen omitida: wiki id 56222]`

### [Parameters](#Parameters)

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Type** | **Description** | **Default** |
| minAccuracy | Numeric (8,0) | Specifies the minimum accuracy required. This accuracy is specified in meters; 0 - ignores the accuracy of the GPS information. | 0 |
| timeout | Numeric (8,0) | Specifies, in seconds, the maximum waiting time to get a location with the desired accuracy. If the device can't get a location in the specified time with the required accuracy, it returns the best location available. 0 means don't wait. | 0 |
| includeHeadingAndSpeed | Boolean | Specifies if it is necessary to include the heading and speed information in the result. | False |
| ignoreErrors | Boolean | Specifies whether the execution of this operation cancels another operation or if this operation's errors are ignored by the application. If an error occurs and the ignore error flag is set to true, an empty value is returned. If an error occurs and the ignore errors flag is set to false, then a msg will prompt the user with the text "Could not get location information". This message can be translated from the language option. | False |

The flag to ignore possible operation errors takes into account the following two errors:

* Location Services are disabled:The message shown is GXM\_LocationServicesAreDisabled.
* The app does not have permission to get the Location Services: The message shown is GXM\_CouldNotGetLocationInformation.

### [Return value](#Return+value)

When you call the GetLocation method, it returns a LocationInfo [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) loaded with the information gathered from the GPS:

`[imagen omitida: wiki id 56223]`

### [Syntax](#Syntax)

&locationInfo = Maps.GetLocation(Numeric, Numeric, Boolean, [Boolean])

### [Samples](#Samples)

#### [Sample #1](#Sample+%231)

```
&locationInfo =  Maps.GetLocation(0,0,false,false)
&texto = &locationInfo.Location.ToString()
```

Sample #2

```
&locationInfo = Maps.GetLocation(10, 60, true, false)
```

Suppose minAccuracy is set to 10 meters, and the resulting accuracy is 500 meters. If the time specified in the timeout parameter has not elapsed, the method will try to get more precise data. However, if the specified time has elapsed and the desired accuracy is not achieved, the method will not provide any location information.

**Notes:**

* In some Android devices, it is necessary to have the Google locator service enabled for this feature to work properly.
* This method is equivalent (and the newest one, which is suggested to be used) to the [GetMyLocation method](https://wiki.genexus.com/commwiki/wiki?25164) of the [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274).

### [Availability](#Availability)

This method has been available since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,).


|  |
| --- |
| **Backlinks** |
| [Maps external object](https://wiki.genexus.com/commwiki/wiki?44309) |

---
