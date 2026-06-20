---
title: "Cache Username property"
source_id: 31332
source_url: https://wiki.genexus.com/commwiki/wiki?31332
genexus_version: "18"
---

# Cache Username property

Indicates the username used to connect to the Cache system in a distributed caching environment.

### [Scope](#Scope)

**Level:** Generator

### [Description](#Description)

In a [distributed caching](https://wiki.genexus.com/commwiki/wiki?28136) environment, when configuring the [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147) to 'Memcached', the **Cache Username property** will be available to enter the username to connect to the Cache system.

It's required if the server supports SASL (e.g., Memcached SASL Authentication protocol).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [See Also](#See+Also)

[Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147)  
[Cache Location property](https://wiki.genexus.com/commwiki/wiki?31331)


|  |
| --- |
| **Backlinks** |
| [Cache Location property](https://wiki.genexus.com/commwiki/wiki?31331) | [Cache Password property](https://wiki.genexus.com/commwiki/wiki?31333) | [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147) |
| [Distributed cache in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?28136) |

---
