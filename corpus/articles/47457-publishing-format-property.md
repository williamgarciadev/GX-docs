---
title: "Publishing Format property"
source_id: 47457
source_url: https://wiki.genexus.com/commwiki/wiki?47457
genexus_version: "18"
---

# Publishing Format property

Indicates whether the output file is generated as .aab or .apk.

### [Values](#Values)

|  |
| --- |
| **Android App Bundle (.aab)** |
| **Legacy (.apk)** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

It specifies the extension of the Android application installation file: .apk or .aab.  
  
By default, an installation file with .apk (Android Application Package) extension is generated.

**Alert**: In November 2020, it was announced that applications uploaded to Google Play Store must have the format .aab (Android App Bundle). This new format allows reducing the size required for installing an application, and it will be absolutely necessary to publish applications as from August 2021. For more information, read: [New Android App Bundle and target API level requirements in 2021](https://android-developers.googleblog.com/2020/11/new-android-app-bundle-and-target-api.html)

Notice the property is available when the [Compilation Mode property](https://wiki.genexus.com/commwiki/wiki?35447) is set to *Distribution*

.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 2](https://wiki.genexus.com/commwiki/wiki?47418,,).

### [See Also](#See+Also)

[Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449)
