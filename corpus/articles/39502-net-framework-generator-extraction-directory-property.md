---
title: ".NET Framework Generator Extraction Directory property"
source_id: 39502
source_url: https://wiki.genexus.com/commwiki/wiki?39502
genexus_version: "18"
---

# .NET Framework Generator Extraction Directory property

Indicates the extraction path of a File object when using the .NET Framework generator.

### [Scope](#Scope)

**Objects:** [File](https://wiki.genexus.com/commwiki/wiki?5852)  
**Generators:** [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)

### [Description](#Description)

This property is visible when [Extract for .NET Framework Generator property](https://wiki.genexus.com/commwiki/wiki?39501) is enabled (True value).

By default, it has an empty value taking as root directory the one indicated on [Target Path property](https://wiki.genexus.com/commwiki/wiki?9612,,) followed by "*/web/bin*" subdirectory.

### [Notes](#Notes)

* This property replaces [Extract to path property](https://wiki.genexus.com/commwiki/wiki?13280) when [Extract property](https://wiki.genexus.com/commwiki/wiki?13280) is different from "No" value and [Generator property](https://wiki.genexus.com/commwiki/wiki?13280) has "Any" or "CSharp" value.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,).

### [See Also](#See+Also)

* [File object](https://wiki.genexus.com/commwiki/wiki?5852)
* [Extract for .NET Framework Generator property](https://wiki.genexus.com/commwiki/wiki?39501)
* [New Environment dialog](https://wiki.genexus.com/commwiki/wiki?24702)
* [GeneXus .NET Framework Generator](https://wiki.genexus.com/commwiki/wiki?2892)


|  |
| --- |
| **Backlinks** |
| [Extract for .NET Framework Generator property](https://wiki.genexus.com/commwiki/wiki?39501) | [Category:File object](https://wiki.genexus.com/commwiki/wiki?5852) |

---
