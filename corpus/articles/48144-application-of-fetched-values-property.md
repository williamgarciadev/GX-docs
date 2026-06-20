---
title: "Application of Fetched Values property"
source_id: 48144
source_url: https://wiki.genexus.com/commwiki/wiki?48144
genexus_version: "18"
---

# Application of Fetched Values property

Indicates when the fetched values should be applied.

### [Values](#Values)

|  |  |
| --- | --- |
| **Immediately** | The fetched values are applied immediately after the fetch finishes. The next read of these values will return the newly fetched value. |
| **Manual** | Values are not applied automatically; the developer is responsible for applying them. |
| **On Application Launch** | (default) The app will apply the fetched values, if any, when the application is launched. If Fetching of Remote Values is set to On Application Activation, the values are applied before fetching new values, meaning that the fetched values are applied the next time the application is launched. |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

After the values are fetched from the Remote Configuration server, they need to be applied locally.

This property controls how and when those changes are applied.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).

### [See Also](#See+Also)

* [Fetching of Remote Values property](https://wiki.genexus.com/commwiki/wiki?48143)
* [RemoteConfig external object](https://wiki.genexus.com/commwiki/wiki?48160)
* [Remote Configuration in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?48101)


|  |
| --- |
| **Backlinks** |
| [Fetching of Remote Values property](https://wiki.genexus.com/commwiki/wiki?48143) | [Remote Configuration in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?48101) | [Remote Configuration Provider property](https://wiki.genexus.com/commwiki/wiki?48146) |

---
