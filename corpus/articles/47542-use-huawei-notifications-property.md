---
title: "Use Huawei Notifications property"
source_id: 47542
source_url: https://wiki.genexus.com/commwiki/wiki?47542
genexus_version: "18"
---

# Use Huawei Notifications property

Specifies if this application uses Notifications when generating for the Huawei platform; this will include special settings in the OneSignal setup.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

Defines if the generated application will use the Huawei-specific Notifications platform called [Push Kit](https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/service-introduction-0000001050040060).

When this property is enabled, remember to follow [these steps](https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/android-config-agc-0000001050170137) to enable it and set the correct information.

You need to set the [Notifications Provider property](https://wiki.genexus.com/commwiki/wiki?33670) to *OneSignal* and complete steps #3 and #4 from the [OneSignal Huawei SDK Setup Guide for Android Studio](https://documentation.onesignal.com/docs/huawei-sdk-setup). For Production environments (using the [Compilation Mode property](https://wiki.genexus.com/commwiki/wiki?35447) in Distribution), make sure to download and use the certificate file provided by Huawei (step #4) as it details a specific SHA256 fingerprint otherwise the following error may appear at runtime:

```
com.huawei.hms.common.ApiException: 6003: certificate fingerprint error
at com.huawei.hms.aaid.constant.ErrorEnum.toApiException(ErrorEnum.java:1)
at com.huawei.hms.opendevice.l.a(GetTokenTask.java:26)
```

Then, the [Huawei Services File property](https://wiki.genexus.com/commwiki/wiki?47545) is enabled to add the associated configuration. Note that you need to upload the *agconnect-services.json* configuration file to the Knowledge Base and keep it up to date.

When using the [Notifications Provider property](https://wiki.genexus.com/commwiki/wiki?33670) with *Jpush,* set this property to false and complete the JPush configuration for the Huawei platform.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 2](https://wiki.genexus.com/commwiki/wiki?47418,,).

### [See Also](#See+Also)

[Main Platform property](https://wiki.genexus.com/commwiki/wiki?18657)  
[Huawei Services File property](https://wiki.genexus.com/commwiki/wiki?47545)


|  |
| --- |
| **Backlinks** |
| [Generate Huawei property](https://wiki.genexus.com/commwiki/wiki?47485) | [GeneXus support for Huawei Mobile Services Platform](https://wiki.genexus.com/commwiki/wiki?47484) |

---
