---
title: "Enable Data Caching property"
source_id: 18302
source_url: https://wiki.genexus.com/commwiki/wiki?18302
genexus_version: "18"
---

# Enable Data Caching property

Specifies whether the object will use data caching or not.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** Panel for Smart Devices, Work With for Smart Devices

### [Description](#Description)

If the property is set to false, the smart device caching for this object is disabled. This means that every time a requirement for this object is made, the Database query is performed regardless of whether any table involved in the query has been changed or not. False value does not optimize the device resource and if you are working offline this object does not show data.

Default value: True.

When the property is set to True, the [Check For New Data property](https://wiki.genexus.com/commwiki/wiki?18322) is displayed.

### [See Also](#See+Also)

[Native Mobile caching](https://wiki.genexus.com/commwiki/wiki?18602)  
[Check For New Data property](https://wiki.genexus.com/commwiki/wiki?18322)


|  |
| --- |
| **Backlinks** |
| [Check For New Data After Minutes Elapsed property](https://wiki.genexus.com/commwiki/wiki?18329) | [Check For New Data property](https://wiki.genexus.com/commwiki/wiki?18322) |
| [Hardening of GeneXus Systems and Deployments with GAM](https://wiki.genexus.com/commwiki/wiki?47237) | [Category:Menu object](https://wiki.genexus.com/commwiki/wiki?16321) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Native Mobile caching](https://wiki.genexus.com/commwiki/wiki?18602) |
| [Server external object](https://wiki.genexus.com/commwiki/wiki?39589) | [Smart Devices Cache Management property](https://wiki.genexus.com/commwiki/wiki?18370) |

---
