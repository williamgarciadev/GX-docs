---
title: "Cache Provider property"
source_id: 31147
source_url: https://wiki.genexus.com/commwiki/wiki?31147
genexus_version: "18"
---

# Cache Provider property

Determines the provider used for distributed caching.

### [Values](#Values)

|  |  |
| --- | --- |
| **In Process** | The cache is stored on the server, and no distribution mechanism is implemented for data caching. |
| **Memcached** | The cache is managed using Memcached, which is a distributed memory object caching system. |
| **Redis** | The cache is managed using Redis, which is an in-memory data structure store. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

The **Cache Provider** **property** default value is 'In Process'. This means that a Local cache (per virtual directory) is used. In other words, the cache is independent per virtual directory. If the cache is recycled in a virtual directory (or webapps) the other virtual directories will not be affected.

In a distributed environment, the Local cache of the application server is useless. In this case, you need a distributed memory object caching system.

The **Cache Provider** **property** allows determining the provider used for [Distributed cache in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?28136).

#### [**Considerations**](#Considerations)

* [GeneXus Java Generator](https://wiki.genexus.com/commwiki/wiki?12258) supports it since [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?42129,,).
* [GeneXus .NET Generator](https://wiki.genexus.com/commwiki/wiki?38604) supports Redis value since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?45275,,).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute [Build any object](https://wiki.genexus.com/commwiki/wiki?17719) with the purpose of generating the \*.config files.

### [See Also](#See+Also)

[Cache Location property](https://wiki.genexus.com/commwiki/wiki?31331)  
[Cache Username property](https://wiki.genexus.com/commwiki/wiki?31332)  
[Cache Password property](https://wiki.genexus.com/commwiki/wiki?31333)


|  |
| --- |
| **Backlinks** |
| [Cache API](https://wiki.genexus.com/commwiki/wiki?32105) | [Cache Location property](https://wiki.genexus.com/commwiki/wiki?31331) | [Cache Password property](https://wiki.genexus.com/commwiki/wiki?31333) |
| [Cache Username property](https://wiki.genexus.com/commwiki/wiki?31332) | [CacheTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?21863) | [Distributed cache in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?28136) | [Extension Library concept for Extending GeneXus for Native Mobile](https://wiki.genexus.com/commwiki/wiki?33545) |
| [GAM - Cache Management](https://wiki.genexus.com/commwiki/wiki?58220) |

---
