---
title: "Fetching of Remote Values property"
source_id: 48143
source_url: https://wiki.genexus.com/commwiki/wiki?48143
genexus_version: "18"
---

# Fetching of Remote Values property

Indicates how the values are fetched from the server.

### [Values](#Values)

|  |  |
| --- | --- |
| **After Elapsed Time** | While the app is running, and after the Minimum Fetch Interval has elapsed since the last successful fetch, the app will try to fetch the values from the server. |
| **Manual** | The app will not fetch the values automatically; it is up to the developer to add the corresponding code to perform the fetching. |
| **On Application Activation** | (default) The app will try to fetch the remote values every time it launches or returns from a background state, but only if the Minimum Fetch Interval has elapsed since the last successful fetch. |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

Before applying the changes made in the Remote Configuration server, the app needs to fetch them into the device.

This property indicates how and when those values are fetched from the server.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).

### [See Also](#See+Also)

* [Minimum Fetch Interval property](https://wiki.genexus.com/commwiki/wiki?48145)
* [Application of Fetched Values property](https://wiki.genexus.com/commwiki/wiki?48144)
* [RemoteConfig external object](https://wiki.genexus.com/commwiki/wiki?48160)
* [Remote Configuration in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?48101)


|  |
| --- |
| **Backlinks** |
| [Application of Fetched Values property](https://wiki.genexus.com/commwiki/wiki?48144) | [Minimum Fetch Interval property](https://wiki.genexus.com/commwiki/wiki?48145) | [Remote Configuration in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?48101) |
| [Remote Configuration Provider property](https://wiki.genexus.com/commwiki/wiki?48146) |

---
