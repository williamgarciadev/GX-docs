---
title: "Java Generator Extraction Directory property"
source_id: 39500
source_url: https://wiki.genexus.com/commwiki/wiki?39500
genexus_version: "18"
---

# Java Generator Extraction Directory property

Indicates the extraction path of a File object when using the Java Generator.

### [Scope](#Scope)

**Objects:** File  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This property is visible when [Extract for Java Generator property](https://wiki.genexus.com/commwiki/wiki?39499) is enabled (True value). By default, it has an empty value taking as root directory the one indicated on [Target Path property](https://wiki.genexus.com/commwiki/wiki?9612,,) followed by "*/web*" subdirectory.

**Note**: This property replaces [Extract to path property](https://wiki.genexus.com/commwiki/wiki?13280) when [Extract property](https://wiki.genexus.com/commwiki/wiki?13280) is different from "No" value and [Generator property](https://wiki.genexus.com/commwiki/wiki?13280) has "Any" or "Java" value.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,).

### [See Also](#See+Also)

[File object](https://wiki.genexus.com/commwiki/wiki?5852)  
[Extract for .NET Framework Generator property](https://wiki.genexus.com/commwiki/wiki?39501)  
[New Environment dialog](https://wiki.genexus.com/commwiki/wiki?24702)


|  |
| --- |
| **Backlinks** |
| [Extract for Java Generator property](https://wiki.genexus.com/commwiki/wiki?39499) | [Category:File object](https://wiki.genexus.com/commwiki/wiki?5852) | [Tips for deploying an application that references External Objects](https://wiki.genexus.com/commwiki/wiki?50961) |
| [Tips for deploying an application that references External Objects (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57576) |

---
