---
title: "Standard Functions property at Object level"
source_id: 8013
source_url: https://wiki.genexus.com/commwiki/wiki?8013
genexus_version: "18"
---

# Standard Functions property at Object level

Enables using specific functions that are not explicitly supported by GeneXus or by certain generators.

### [Values](#Values)

|  |  |
| --- | --- |
| **Allow non-standard functions** | Functions not supported by GeneXus can be used. |
| **Use Environment property value** | The configured value for the "Standard Functions" property at Environment level is inherited. |
| **Only standard functions** | Only the standard functions supported by GeneXus can be used. This is the default value. |

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This property is useful when you want to use specific functions that are not explicitly supported by GeneXus or in any generator. The check will be made when the object is saved.

All functions supported by GeneXus become standard functions, even if they are only available for some generators.

Note that this property is available at the following levels:

* Knowledge Base
* Environment
* Generator
* Object

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [See Also](#See+Also)

[Standard and non standard functions](https://wiki.genexus.com/commwiki/wiki?8565)  
[Standard Functions property at Knowledge Base level](https://wiki.genexus.com/commwiki/wiki?7403)


|  |
| --- |
| **Backlinks** |
| [Standard and non standard functions](https://wiki.genexus.com/commwiki/wiki?8565) |
| [Standard Functions property at Knowledge Base level](https://wiki.genexus.com/commwiki/wiki?7403) |

---
