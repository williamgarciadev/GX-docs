---
title: "Minimum Fetch Interval property"
source_id: 48145
source_url: https://wiki.genexus.com/commwiki/wiki?48145
genexus_version: "18"
---

# Minimum Fetch Interval property

Indicates the minimum time that must pass after a successful fetch to perform a new automatic fetch (that is, when Fetching of Remote Values != Manual).

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This property's values are expressed in minutes; the default value is 1,440 (24 hours).

Setting a low value in this property will (potentially) make the app perform several unnecessary requests to the Remote Configuration server because configuration values will not have changed between calls.

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
