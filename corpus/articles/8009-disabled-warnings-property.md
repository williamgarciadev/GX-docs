---
title: "Disabled warnings property"
source_id: 8009
source_url: https://wiki.genexus.com/commwiki/wiki?8009
genexus_version: "18"
---

# Disabled warnings property

Specifies a list of warning and/or information codes to be ignored at specification time for each object.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

You can complete this property with a list of codes that correspond to [SPC](https://wiki.genexus.com/commwiki/wiki?5933) and/or [NFO](https://wiki.genexus.com/commwiki/wiki?45847) messages to avoid displaying them at specification time.

The list must be separated by spaces or commas, as shown below:  
  
            Spc0005 Spc0038

This property applies at both Object and Generator levels. When the object and the Generator contain matching values, the Object values are applied first. In the absence of object values, all values included in the Generator property are applied.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [See Also](#See+Also)

[SRC Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?38589)  
[Information Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?45847)  
[Warnings treated as errors property](https://wiki.genexus.com/commwiki/wiki?8010)


|  |
| --- |
| **Backlinks** |
| [Check type errors property](https://wiki.genexus.com/commwiki/wiki?8953) | [Toc:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) |
| [Warnings treated as errors property](https://wiki.genexus.com/commwiki/wiki?8010) |

---
