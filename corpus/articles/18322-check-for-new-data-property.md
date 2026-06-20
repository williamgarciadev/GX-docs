---
title: "Check For New Data property"
source_id: 18322
source_url: https://wiki.genexus.com/commwiki/wiki?18322
genexus_version: "18"
---

# Check For New Data property

Indicates whether it uses cached data or asks the server if the data has been changed.

### [Values](#Values)

|  |  |
| --- | --- |
| **After elapsed time** | Ask the server if the data has been changed only after an indicated period of time. |
| **Every time** | Ask the server if the data has been changed every time the query is performed. This is the default value. |

### [Description](#Description)

This property is displayed when [Enable Data Caching property](https://wiki.genexus.com/commwiki/wiki?18302) is set to true.

With ‘Every time’ value, the object asks the Database if the data has been changed since the last request; if not, the cached data is used; otherwise, the query is performed.

‘After elapsed time’ enables a new property called [Check For New Data After Minutes Elapsed property](https://wiki.genexus.com/commwiki/wiki?18329). This value uses the cached data for the time indicated in the new property since the last query.

### [Scope](#Scope)

**Objects:** Panel for Smart Devices, Work With for Smart Devices, Menu for Smart Devices  
**Platforms:** Smart Devices(Android, IOS)

### [See Also](#See+Also)

[Native Mobile caching](https://wiki.genexus.com/commwiki/wiki?18602)  
[Check For New Data After Minutes Elapsed property](https://wiki.genexus.com/commwiki/wiki?18329)  
[Enable Data Caching property](https://wiki.genexus.com/commwiki/wiki?18302)


|  |
| --- |
| **Backlinks** |
| [Check For New Data After Minutes Elapsed property](https://wiki.genexus.com/commwiki/wiki?18329) | [Enable Data Caching property](https://wiki.genexus.com/commwiki/wiki?18302) | [Category:Menu object](https://wiki.genexus.com/commwiki/wiki?16321) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Native Mobile caching](https://wiki.genexus.com/commwiki/wiki?18602) | [Server external object](https://wiki.genexus.com/commwiki/wiki?39589) | [Smart Devices Cache Management property](https://wiki.genexus.com/commwiki/wiki?18370) |

---
