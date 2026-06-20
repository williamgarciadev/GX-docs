---
title: "Database access caching property"
source_id: 8968
source_url: https://wiki.genexus.com/commwiki/wiki?8968
genexus_version: "18"
---

# Database access caching property

Enables or disables the data cache. After configuring the Enable Database Access Caching property, configure the Change Frequency property for each table you want to have cached.
The result set of each table query is stored in a memory cache; while the cache does not expire, it is queried in each read operation without accessing the database.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | Caching is disabled. This is the default value. |
| **Yes** | Caching is enabled. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

The expiration of the cache is configured in the [Time to Time TTL(mins) property](https://wiki.genexus.com/commwiki/wiki?9133) and [Hardly ever TTL(mins) property](https://wiki.genexus.com/commwiki/wiki?9132).

After changing the value of the property, a rebuild all is needed. All the programs which navigate to any table which is affected by this property, will change its source code.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Time to Time TTL(mins) property](https://wiki.genexus.com/commwiki/wiki?9133)  
[Hardly ever TTL(mins) property](https://wiki.genexus.com/commwiki/wiki?9132)  
[Cache storage size property](https://wiki.genexus.com/commwiki/wiki?14436)


|  |
| --- |
| **Backlinks** |
| [Cache storage size property](https://wiki.genexus.com/commwiki/wiki?14436) | [Change frequency property](https://wiki.genexus.com/commwiki/wiki?7156) |
| [Distributed cache in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?28136) | [GAM - Cache Management](https://wiki.genexus.com/commwiki/wiki?58220) | [Hardly ever TTL(mins) property](https://wiki.genexus.com/commwiki/wiki?9132) |
| [Time to Time TTL(mins) property](https://wiki.genexus.com/commwiki/wiki?9133) |

---
