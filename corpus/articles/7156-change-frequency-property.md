---
title: "Change frequency property"
source_id: 7156
source_url: https://wiki.genexus.com/commwiki/wiki?7156
genexus_version: "18"
---

# Change frequency property

Table property that indicates how often the table data changes. Its value is used to control database access caching when the Database Access Caching property is enabled.

### [Values](#Values)

|  |  |
| --- | --- |
| **0. Pretty Often** | Use this value for objects that should not be cached. This is the default value. |
| **1. Time to Time** | The cache is refreshed when the time period specified by the "Time to Time" property has elapsed. |
| **2. Hardly Ever** | The cache is refreshed when the time period specified by the "Hardly ever" property has elapsed. |
| **3. Almost Never** | This value should be used for objects that, once read, should never be removed from the cache. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This is a Table property.

Select the desired Table in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) to configure its **Change frequency property**.

`[imagen omitida: wiki id 58369]`

**Notes:**

* Cached database accesses may be flushed from memory with the [Cache storage size property](https://wiki.genexus.com/commwiki/wiki?14436).
* After changing the value of the **Change frequency property**, a rebuild all is needed. In fact, only the programs that navigate to the cached table will change their source code.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Time to Time TTL(mins) property](https://wiki.genexus.com/commwiki/wiki?9133)  
[Hardly ever TTL(mins) property](https://wiki.genexus.com/commwiki/wiki?9132)


|  |
| --- |
| **Backlinks** |
| [Database access caching property](https://wiki.genexus.com/commwiki/wiki?8968) | [GAM - Cache Management](https://wiki.genexus.com/commwiki/wiki?58220) |
|

---
