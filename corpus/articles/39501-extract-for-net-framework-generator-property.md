---
title: "Extract for .NET Framework Generator property"
source_id: 39501
source_url: https://wiki.genexus.com/commwiki/wiki?39501
genexus_version: "18"
---

# Extract for .NET Framework Generator property

Indicates if the file must be extracted for the .NET Framework generator.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [File](https://wiki.genexus.com/commwiki/wiki?5852)  
**Generators:** [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892)

### [Description](#Description)

When this property is enabled (True value), it will display [.NET Framework Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39502) for indicating the path where the file will be extracted (by default, the value of [Target Path property](https://wiki.genexus.com/commwiki/wiki?9612,,) followed by "*/web/bin*" subdirectory).

### [Notes](#Notes)

* This property replaces [Extract property](https://wiki.genexus.com/commwiki/wiki?13280) when it is different from "No" value and [Generator property](https://wiki.genexus.com/commwiki/wiki?13280) has "Any" or "CSharp" value.
* File is copied only if it's newer than the existing one.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,).

### [See Also](#See+Also)

* [File object](https://wiki.genexus.com/commwiki/wiki?5852)
* [.NET Framework Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39502)


|  |
| --- |
| **Backlinks** |
| [.NET Framework Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39502) | [Category:File object](https://wiki.genexus.com/commwiki/wiki?5852) | [Java Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39500) |

---
