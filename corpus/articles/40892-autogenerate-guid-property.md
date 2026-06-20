---
title: "Autogenerate Guid property"
source_id: 40892
source_url: https://wiki.genexus.com/commwiki/wiki?40892
genexus_version: "18"
---

# Autogenerate Guid property

Automatically generates values for an attribute or variable whose data type is GUID.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

In the example below, the primary keys of the Customer and Invoice Transactions are defined based on the [GUID data type](https://wiki.genexus.com/commwiki/wiki?31772) because several disconnected company branches, as well as the head office, need to always generate unique values for those primary keys.

`[imagen omitida: wiki id 54234]`

Note that the Autogenerate GUID property of both attributes is set to True in order to always obtain a [Global Unique Identifier](https://wiki.genexus.com/commwiki/wiki?21842) automatically when an insertion is performed.

### [See Also](#See+Also)

[Initial value property](https://wiki.genexus.com/commwiki/wiki?11765)


|  |
| --- |
| **Backlinks** |
| [Automatically generated identifiers synching conflicts](https://wiki.genexus.com/commwiki/wiki?23543) | [GUID data type](https://wiki.genexus.com/commwiki/wiki?31772) | [Initial value property](https://wiki.genexus.com/commwiki/wiki?11765) |
| [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) |

---
