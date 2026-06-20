---
title: "Is ad-hoc property"
source_id: 11875
source_url: https://wiki.genexus.com/commwiki/wiki?11875
genexus_version: "18"
---

# Is ad-hoc property

Indicates whether the task is ad-hoc.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486)  
**Controls:** [Task](https://wiki.genexus.com/commwiki/wiki?17495)

### [Description](#Description)

If the task is ad-hoc, when a task workitem is completed from the GXflow Client, a dialog will be shown allowing the user to choose the task through which the process will continue, and to select the users responsible for each of those tasks. In this dialog, the user will also be able to indicate whether the process is finished, by executing the "End" task. Please note that an ad-hoc task does not necessarily require a connection through paths towards successor tasks.

Also, use this property for processes. When a process Is ad-hoc, all its interactive tasks will be Ad-Hoc too, regardless of what is assigned in their “Is Ad-Hoc” preference. This can be configured in the process diagram properties by selecting the “Is ad-hoc” property.

### [Values](#Values)

|  |  |
| --- | --- |
| **Default** | False. |
| **True** | The task is ad-hoc. In this case, the Multiple Choice, Custom Ad-Hoc Application and Custom Assign Application properties are enabled. |
| **False** | The task is not ad-hoc. |

### [See Also](#See+Also)

[Multiple Choice Property](https://wiki.genexus.com/commwiki/wiki?12576,,)  
[Custom ad-hoc application property](https://wiki.genexus.com/commwiki/wiki?12577)  
[Custom Assign Application Property](https://wiki.genexus.com/commwiki/wiki?12578)  
[Selectable for ad-hoc Property](https://wiki.genexus.com/commwiki/wiki?11475)


|  |
| --- |
| **Backlinks** |
| [Adaptability Properties](https://wiki.genexus.com/commwiki/wiki?10957) | [Business Process Diagram Properties](https://wiki.genexus.com/commwiki/wiki?20896) | [Custom ad-hoc application property](https://wiki.genexus.com/commwiki/wiki?12577) |
| [User Task Properties](https://wiki.genexus.com/commwiki/wiki?17499) |

---
