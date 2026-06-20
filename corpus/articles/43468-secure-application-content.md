---
title: "Secure Application Content"
source_id: 43468
source_url: https://wiki.genexus.com/commwiki/wiki?43468
genexus_version: "18"
---

# Secure Application Content

Blurs the application screen (iOS) or shows a blank screen (Android) in the OS application switcher when the app goes to background. In Android, it also prevents the user from capturing application screenshots when the application is running.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This application provides an extra level of security in your application, preventing the exposure of sensitive application data. The effect of this property varies depending on the platform:

In iOS:

When this property is enabled, the application will be blurred in the application switcher on the device.

In Android:

First, it doesn't allow taking screenshots of the application. Also, the application will not be listed in the application switcher.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

|  |  |
| --- | --- |
| **iOS** | **Android** |
|  |  |

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [See Also](#See+Also)

[Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214)

[GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746)

[Enable Biometrics property](https://wiki.genexus.com/commwiki/wiki?43466)


|  |
| --- |
| **Backlinks** |
| [Enable Biometrics property](https://wiki.genexus.com/commwiki/wiki?43466) |

---
