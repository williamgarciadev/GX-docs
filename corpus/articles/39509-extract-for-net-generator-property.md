---
title: "Extract for .NET Generator property"
source_id: 39509
source_url: https://wiki.genexus.com/commwiki/wiki?39509
genexus_version: "18"
---

# Extract for .NET Generator property

Indicates if the file must be extracted for the .NET generator.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [File](https://wiki.genexus.com/commwiki/wiki?5852)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

When this property is enabled (True value), it will display [.NET Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39510) for indicating the path where the file will be extracted (by default, the value of [Target Path property](https://wiki.genexus.com/commwiki/wiki?9612,,) followed by "*/web/bin*" subdirectory).

Note: File is copied only if it's newer than the existing one.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,).

### [See Also](#See+Also)

* [File object](https://wiki.genexus.com/commwiki/wiki?5852)
* [.NET Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39510)


|  |
| --- |
| **Backlinks** |
| [.NET Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39510) | [Category:File object](https://wiki.genexus.com/commwiki/wiki?5852) |

---
