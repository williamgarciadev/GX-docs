---
title: "Auto correction property"
source_id: 21944
source_url: https://wiki.genexus.com/commwiki/wiki?21944
genexus_version: "18"
---

# Auto correction property

Indicates if Character, VarChar or LongVarChar fields will be automatically corrected in edit mode.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** Attribute/Variable (Control Type: Edit)

### [Description](#Description)

Applies to Domains, Attributes, Variables, or [SDT](https://wiki.genexus.com/commwiki/wiki?2427) members whose data type is Character, VarChar, or LongVarchar. The value is inherited when a field is based on a domain or attribute.

**Possible values**

* **False:** Spelling is not checked. It is used for fields that contain alphanumeric codes that are not necessarily words included in a dictionary.
* **True:** Spell checking is automatic and possible errors are indicated. In mobile applications, words are also suggested. This is the default value.

### [See Also](#See+Also)

[Auto capitalization property](https://wiki.genexus.com/commwiki/wiki?21040)


|  |
| --- |
| **Backlinks** |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
