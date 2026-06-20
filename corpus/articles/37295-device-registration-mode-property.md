---
title: "Device Registration Mode property"
source_id: 37295
source_url: https://wiki.genexus.com/commwiki/wiki?37295
genexus_version: "18"
---

# Device Registration Mode property

Indicates how the notifications permission is handled.

### [Values](#Values)

|  |  |
| --- | --- |
| **Automatic** | The permission is launched when the app starts running. |
| **Manual** | The permission will be requested when it is programmed with the corresponding External Object Permission for each platform. |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

This property is shown when the [Enable Notifications property](https://wiki.genexus.com/commwiki/wiki?49799) is set to True.

The Manual value is recommended when you need more control over the application permission requests. For example, in an application with authentication, you want to run the permission request when you are sure that the user is logged in the application.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[HowTo: Configure Push Notifications in Apple Applications](https://wiki.genexus.com/commwiki/wiki?17451)  
[HowTo: Configure Push Notifications in Android Applications](https://wiki.genexus.com/commwiki/wiki?18147)


|  |
| --- |
| **Backlinks** |
| [HowTo: Configure Push Notifications in Apple Applications](https://wiki.genexus.com/commwiki/wiki?17451) | [iOS Device Registration Mode property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54518) | [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687) |

---
