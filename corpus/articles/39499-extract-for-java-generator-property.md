---
title: "Extract for Java Generator property"
source_id: 39499
source_url: https://wiki.genexus.com/commwiki/wiki?39499
genexus_version: "18"
---

# Extract for Java Generator property

Indicates if the file must be extracted for Java Generator.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Description](#Description)

When this property is enabled (True value), it will display [Java Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39500) for indicating the path where the file will be extracted (by default, the value of [Target Path property](https://wiki.genexus.com/commwiki/wiki?9612,,) followed by "*/web*" subdirectory).

### [Notes](#Notes)

* This property replaces [Extract property](https://wiki.genexus.com/commwiki/wiki?13280) when it is different from "No" value and [Generator property](https://wiki.genexus.com/commwiki/wiki?13280) has "Any" or "Java" value.
* File is copied only if it's newer than the existing one.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Build All.

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,).

### [Scope](#Scope)

**Objects:** File  
**Platforms:** Web(Java)

### [See Also](#See+Also)

* [File object](https://wiki.genexus.com/commwiki/wiki?5852)
* [Java Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39500)


|  |
| --- |
| **Backlinks** |
| [Category:File object](https://wiki.genexus.com/commwiki/wiki?5852) | [Java Generator Extraction Directory property](https://wiki.genexus.com/commwiki/wiki?39500) |

---
