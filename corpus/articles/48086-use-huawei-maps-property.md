---
title: "Use Huawei Maps property"
source_id: 48086
source_url: https://wiki.genexus.com/commwiki/wiki?48086
genexus_version: "18"
---

# Use Huawei Maps property

Specifies if this application uses Huawei Maps provider (Map Kit) when generating for the Huawei platform.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

Defines if the generated application will use the Huawei-specific Maps provider platform called [Map Kit](https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/android-sdk-brief-introduction-0000001061991343).

When this property is enabled, remember to follow [these steps](https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/android-sdk-config-agc-0000001061560289) to enable it on the Huawei console and set the correct information.

You need to set the [Huawei Services API Key property](https://wiki.genexus.com/commwiki/wiki?48087) to a valid value and download and assign the [Huawei Services File property](https://wiki.genexus.com/commwiki/wiki?47545) with the *agconnect-services.json* configuration file.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).

### [See Also](#See+Also)

* [Huawei Services API Key property](https://wiki.genexus.com/commwiki/wiki?48087)
* [Huawei Services File property](https://wiki.genexus.com/commwiki/wiki?47545)


|  |
| --- |
| **Backlinks** |
| [Generate Huawei property](https://wiki.genexus.com/commwiki/wiki?47485) | [GeneXus support for Huawei Mobile Services Platform](https://wiki.genexus.com/commwiki/wiki?47484) |
| [Huawei Services API Key property](https://wiki.genexus.com/commwiki/wiki?48087) |

---
