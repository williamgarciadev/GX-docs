---
title: "Enable MTOM property"
source_id: 43441
source_url: https://wiki.genexus.com/commwiki/wiki?43441
genexus_version: "18"
---

# Enable MTOM property

Enables the MTOM (blob data is sent as an attachment; otherwise, it is sent inline as part of the SOAP message body).

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)  
**Platforms:** Web (Java)

### [Description](#Description)

Important: This property will be available only if you have set the [Use Native Soap property](https://wiki.genexus.com/commwiki/wiki?13446) to True.

This property enables the [MTOM](https://en.wikipedia.org/wiki/Message_Transmission_Optimization_Mechanism) (sends blob data as an attachment; otherwise, it is sent inline as part of the SOAP message body).

After setting this property to True, the [MTOM Threshold property](https://wiki.genexus.com/commwiki/wiki?43442) will be offered for the same object.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build a main object.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 5](https://wiki.genexus.com/commwiki/wiki?43446,,).


|  |
| --- |
| **Backlinks** |
| [MTOM Threshold property](https://wiki.genexus.com/commwiki/wiki?43442) |

---
