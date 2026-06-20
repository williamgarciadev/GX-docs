---
title: "Registration Handler property"
source_id: 22981
source_url: https://wiki.genexus.com/commwiki/wiki?22981
genexus_version: "18"
---

# Registration Handler property

Specifies which procedure will be executed to register the device information needed to send messages (Push Notifications) to the device.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

The [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) set on this property must be generated as a web service. It will be executed from the Smart Device at application startup (which has Enable Notification property enabled).

GeneXus, by default, creates a procedure called **NotificationsRegistrationHandler** in *GeneXus/SD/Notifications* directory under the *Root Module* in your Knowledge Base that has:

* [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) = True
* [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) = Online

You can create another with your own business logic for registering the devices in your system.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [See Also](#See+Also)

[HowTo: Use a Device's Registration Service for Push Notifications](https://wiki.genexus.com/commwiki/wiki?18149)  
[Push Notifications in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19945)


|  |
| --- |
| **Backlinks** |
| [HowTo: Use a Device's Registration Service for Push Notifications](https://wiki.genexus.com/commwiki/wiki?18149) |

---
