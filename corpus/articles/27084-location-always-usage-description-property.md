---
title: "Location Always Usage Description property"
source_id: 27084
source_url: https://wiki.genexus.com/commwiki/wiki?27084
genexus_version: "18"
---

# Location Always Usage Description property

Specifies the reason for your app to access the user's location information at all times. Used up to iOS 10; in iOS 11, Always And When In Use usage description is used instead.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This property is offered under the [Purpose Strings properties group](https://wiki.genexus.com/commwiki/wiki?32755) available for Main Smart Device objects under the Apple group.

When an API that involves user privacy is used in an iOS device, as of iOS 8.0 developers must ask the user for permission. For this reason, they must define the message that will be displayed to users in a dialog box that will prompt them for permission, describing the reason(s) why the application is going to use the content.

In particular, when using the [Geolocation Proximity Alerts](https://wiki.genexus.com/commwiki/wiki?25194) or [BeaconProximityAlert Data Type](https://wiki.genexus.com/commwiki/wiki?27040), this is the property where you have to enter the reason(s) why the application will access the user's location all the time (always). This description is also needed if you use [GetMyLocation method](https://wiki.genexus.com/commwiki/wiki?25164) or [StartTracking method](https://wiki.genexus.com/commwiki/wiki?25177) methods when the application is running in the background, for example in an action executed by a notification.

#### [Notes](#Notes)

* A warning message like this will be displayed if the developer uses location services but this property is not set.  
  warning: In iOS 8.0 or later, a value for one of these properties is required when you use location services. ('Location Always Usage Description' of <Menu|Panel> for Smart Devices instance '%')  
  The iOS version may vary depending on which XCode version is used with support as of iOS 8.0.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [See Also](#See+Also)

* [Location When In Use Usage Description property](https://wiki.genexus.com/commwiki/wiki?27085)
* [Purpose Strings properties group](https://wiki.genexus.com/commwiki/wiki?32755)


|  |
| --- |
| **Backlinks** |
| [BeaconProximityAlert Data Type](https://wiki.genexus.com/commwiki/wiki?27040) | [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) |
| [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) | [Location When In Use Usage Description property](https://wiki.genexus.com/commwiki/wiki?27085) | [Purpose Strings properties group](https://wiki.genexus.com/commwiki/wiki?32755) |

---
