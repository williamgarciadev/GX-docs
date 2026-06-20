---
title: "Default Values property"
source_id: 48142
source_url: https://wiki.genexus.com/commwiki/wiki?48142
genexus_version: "18"
---

# Default Values property

Provides default values for remote configuration parameters.

### [Scope](#Scope)

**Objects:** [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974), [Menu](https://wiki.genexus.com/commwiki/wiki?16321) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

The values configured in this property are used by the [RemoteConfig external object](https://wiki.genexus.com/commwiki/wiki?48160) as default values.

That is, if any of the getter methods are called before fetching the values from the remote configuration provider, or if the value is not set in the remote configuration provider, the value configured in this property is returned.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).

### [See Also](#See+Also)

* [RemoteConfig external object](https://wiki.genexus.com/commwiki/wiki?48160)
* [Remote Configuration in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?48101)


|  |
| --- |
| **Backlinks** |
| [Remote Configuration in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?48101) |

---
