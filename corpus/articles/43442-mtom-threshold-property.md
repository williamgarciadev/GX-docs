---
title: "MTOM Threshold property"
source_id: 43442
source_url: https://wiki.genexus.com/commwiki/wiki?43442
genexus_version: "18"
---

# MTOM Threshold property

Indicates the size in bytes starting from which files will be sent using MTOM.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)  
**Platforms:** Web (Java)

### [Description](#Description)

Important: This property will be available only if you have set the [Use Native Soap property](https://wiki.genexus.com/commwiki/wiki?13446) and the [Enable MTOM property](https://wiki.genexus.com/commwiki/wiki?43441) to True.

It allows you to set the [MTOM](https://en.wikipedia.org/wiki/Message_Transmission_Optimization_Mechanism) threshold to specify when the xs:binary64 data is sent inline or as an attachment.

By default, the MTOM threshold is 0 bytes, which means all xs:binary64 data is sent as an attachment. If a message is greater than or equal to the value of this property, the xs:binary64 data will be sent as an attachment. Otherwise, the content will be sent inline as part of the SOAP message body.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Build with this Only of the object.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 5](https://wiki.genexus.com/commwiki/wiki?43446,,).


|  |
| --- |
| **Backlinks** |
| [Enable MTOM property](https://wiki.genexus.com/commwiki/wiki?43441) |

---
