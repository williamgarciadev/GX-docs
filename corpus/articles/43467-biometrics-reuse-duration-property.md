---
title: "Biometrics Reuse Duration property"
source_id: 43467
source_url: https://wiki.genexus.com/commwiki/wiki?43467
genexus_version: "18"
---

# Biometrics Reuse Duration property

Specifies the number of seconds after which biometric authentication will be required again; if zero, the user's credentials will be asked every time.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This property is available when the [Enable Biometrics property](https://wiki.genexus.com/commwiki/wiki?43466) is set to True.

It represents the validity time (in seconds) that the authentication will have. During this period, the user's session will remain active and the credentials will not be requested again. Once the time indicated in this property has expired, the user will be asked to enter his/her data again.

The time will start counting from the moment the application goes to the background.

If the application is deleted by the operating system, when the application is reopened, the user will be asked to enter his/her data again. In this case, the period of time during which the application was in background mode will not be taken into account.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[Enable Biometrics property](https://wiki.genexus.com/commwiki/wiki?43466)  
[Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214)  
[GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746)  
[KB Platforms](https://wiki.genexus.com/commwiki/wiki?24284)


|  |
| --- |
| **Backlinks** |
| [Enable Biometrics property](https://wiki.genexus.com/commwiki/wiki?43466) |

---
