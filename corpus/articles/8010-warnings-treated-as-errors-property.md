---
title: "Warnings treated as errors property"
source_id: 8010
source_url: https://wiki.genexus.com/commwiki/wiki?8010
genexus_version: "18"
---

# Warnings treated as errors property

Specifies a list of warning and/or information codes to consider as errors at specification time.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

In this property, you can include a list of codes that correspond to [SPC](https://wiki.genexus.com/commwiki/wiki?5933) and/or [NFO](https://wiki.genexus.com/commwiki/wiki?45847) messages so that they are considered as if they were errors, and thus displayed at specification time as errors.

The list must be separated by spaces or commas, as shown below:  
  
            Spc0038 nfo0003

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [See Also](#See+Also)

[SRC Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?38589)  
[Information Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?45847)  
[Disabled warnings property](https://wiki.genexus.com/commwiki/wiki?8009)


|  |
| --- |
| **Backlinks** |
| [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953) | [Toc:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) | [Disabled warnings property](https://wiki.genexus.com/commwiki/wiki?8009) |
| [Macroservices and Miniservices systems](https://wiki.genexus.com/commwiki/wiki?55518) | [Microservices systems](https://wiki.genexus.com/commwiki/wiki?55526) |
| [Scenario of backward compatible reorganizations](https://wiki.genexus.com/commwiki/wiki?48715) |

---
