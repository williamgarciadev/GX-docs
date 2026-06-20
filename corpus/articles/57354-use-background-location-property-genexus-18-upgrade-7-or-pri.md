---
title: "Use Background Location property (GeneXus 18 Upgrade 7 or prior)"
source_id: 57354
source_url: https://wiki.genexus.com/commwiki/wiki?57354
genexus_version: "18"
---

# Use Background Location property (GeneXus 18 Upgrade 7 or prior)

Indicates whether Background Location is used in an application (to include the necessary permission: ACCESS\_BACKGROUND\_LOCATION).

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

Allows setting whether the application requires permissions to access location in the background.

When this property is set to True, the ACCESS\_BACKGROUND\_LOCATION permission is added to the Android Application Manifest.

When the application targets Android 10 (API level 29) or higher, and requires the use of this permission, make sure that it is really necessary since in most cases applications need locations when the user interacts with the app.  
If it is necessary, follow Google's recommendations on the use of this permission: [Requesting access to location in the background](https://support.google.com/googleplay/android-developer/answer/9799150?hl=en). Otherwise, you could receive a message stating "Prominent Disclosure Not Found" when trying to have an application approved.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [See Also](#See+Also)

[Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274)
