---
title: "Auto-register Anonymous User property"
source_id: 19912
source_url: https://wiki.genexus.com/commwiki/wiki?19912
genexus_version: "18"
---

# Auto-register Anonymous User property

Sets whether the application opens a dialogue to log in or register or automatically creates a user based on information from the device.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))

### [Description](#Description)

The **Auto-register Anonymous User**property is available when GAM is enabled ([Enable Integrated Security property](https://wiki.genexus.com/commwiki/wiki?14706) = True) for [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s, [Menu object](https://wiki.genexus.com/commwiki/wiki?16321)s and [Work With object](https://wiki.genexus.com/commwiki/wiki?15974)s with their [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) = True.

The available values for this property are as follows:

* **False:**This is the default value. When a user not registered in the application tries to access the first object that has the Integrated Security Level property = Authentication or Authorization, the dialogue to log in or register will be shown.
* **True:**Instead of requesting login or registration, the application automatically creates a user based on information from the device.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[GAM - Auto-register anonymous users](https://wiki.genexus.com/commwiki/wiki?19395)  
[GAM - Auto-register anonymous users - How it works](https://wiki.genexus.com/commwiki/wiki?19909)  
[GAM - Auto-register anonymous user - Panel usage example](https://wiki.genexus.com/commwiki/wiki?19911)


|  |
| --- |
| **Backlinks** |
| [Auto-Registration in SD: What to do when a certain action requires the user to log in](https://wiki.genexus.com/commwiki/wiki?19835) | [GAM - Auto-register anonymous user - Panel usage example](https://wiki.genexus.com/commwiki/wiki?19911) |
| [GAM - Auto-register anonymous users](https://wiki.genexus.com/commwiki/wiki?19395) | [GAM - Auto-register anonymous users - How it works](https://wiki.genexus.com/commwiki/wiki?19909) | [HowTo: Develop Secure REST Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?15918) |

---
