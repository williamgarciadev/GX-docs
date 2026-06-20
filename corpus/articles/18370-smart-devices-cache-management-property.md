---
title: "Smart Devices Cache Management property"
source_id: 18370
source_url: https://wiki.genexus.com/commwiki/wiki?18370
genexus_version: "18"
---

# Smart Devices Cache Management property

Enables/disables query optimization with or without caching.

### [Values](#Values)

|  |  |
| --- | --- |
| **Off** | Disables query optimization. |
| **On** | Enables query optimization using caching. This is the default value. |

### [Scope](#Scope)

**Platforms:** Smart Devices (Android, IOS)  
**Level:** Generator

### [Description](#Description)

As you can read in the main document of Caching implementation for Smart Devices, you can take advantage of caching depending on certain object properties (caching means to use previously navigated data and optimize queries using cached data if it hasn’t changed in the Database).

This is the behavior if the Smart Devices Cache Management Property is set to On.

By setting this property to Off, the data previously navigated is cached, but this cached data is used only if you are working offline. If you are online, the queries are not optimized, which means that data is always requested to the database regardless of whether it has changed or not since the last query.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Build with this Only of the object.

### [See Also](#See+Also)

[Native Mobile caching](https://wiki.genexus.com/commwiki/wiki?18602)  
[Enable Data Caching property](https://wiki.genexus.com/commwiki/wiki?18302)  
[Check For New Data property](https://wiki.genexus.com/commwiki/wiki?18322)  
[Check For New Data After Minutes Elapsed property](https://wiki.genexus.com/commwiki/wiki?18329)


|  |
| --- |
| **Backlinks** |
| [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [Native Mobile caching](https://wiki.genexus.com/commwiki/wiki?18602) | [Server external object](https://wiki.genexus.com/commwiki/wiki?39589) |

---
