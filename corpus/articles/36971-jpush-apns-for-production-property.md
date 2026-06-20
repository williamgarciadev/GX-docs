---
title: "JPush - APNs for production property"
source_id: 36971
source_url: https://wiki.genexus.com/commwiki/wiki?36971
genexus_version: "18"
---

# JPush - APNs for production property

Indicates whether the APNs Production certificate should be used or not for the iOS application.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

The value of this property indicates if the Production APNs certificate will be used to send Push Notifications to the iOS application. If the value is True, JPush will use the tag *ios-product* to send the notification; otherwise, the tag *ios-dev* is used.

The Default value is False.

For more information, check the Apple Push Notifications service [documentation](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,).

### [See Also](#See+Also)

[Notifications Provider property](https://wiki.genexus.com/commwiki/wiki?33670)  
[JPush - App Key property](https://wiki.genexus.com/commwiki/wiki?36968)  
[JPush - Master Secret property](https://wiki.genexus.com/commwiki/wiki?36969)  
[JPush - Channel property](https://wiki.genexus.com/commwiki/wiki?36970)  
[JPush - NDK ABI Filters property](https://wiki.genexus.com/commwiki/wiki?36972)


|  |
| --- |
| **Backlinks** |
| [JPush - App Key property](https://wiki.genexus.com/commwiki/wiki?36968) | [JPush - Channel property](https://wiki.genexus.com/commwiki/wiki?36970) | [JPush - Master Secret property](https://wiki.genexus.com/commwiki/wiki?36969) |
| [JPush - NDK ABI Filters property](https://wiki.genexus.com/commwiki/wiki?36972) | [Notifications Provider property](https://wiki.genexus.com/commwiki/wiki?33670) |

---
