---
title: "Use Huawei Analytics property"
source_id: 47541
source_url: https://wiki.genexus.com/commwiki/wiki?47541
genexus_version: "18"
---

# Use Huawei Analytics property

Specifies if this application uses Analytics when generating for the Huawei platform.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

Defines if the generated application will use the Huawei-specific Analytics platform called [Analytics Kit](https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/android-config-agc-0000001050163815).

When this property is enabled, remember to follow [these steps](https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/android-config-agc-0000001050163815) to enable it.

Then, the [Huawei Services File property](https://wiki.genexus.com/commwiki/wiki?47545) is enabled to add the associated configuration. Note that you need to upload the *agconnect-services.json* configuration file to the Knowledge Base and keep it up to date.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 2](https://wiki.genexus.com/commwiki/wiki?47418,,).

### [See Also](#See+Also)

* [Analytics Provider property](https://wiki.genexus.com/commwiki/wiki?41575)
* [Huawei Services File property](https://wiki.genexus.com/commwiki/wiki?47545)


|  |
| --- |
| **Backlinks** |
| [Generate Huawei property](https://wiki.genexus.com/commwiki/wiki?47485) | [GeneXus support for Huawei Mobile Services Platform](https://wiki.genexus.com/commwiki/wiki?47484) |

---
