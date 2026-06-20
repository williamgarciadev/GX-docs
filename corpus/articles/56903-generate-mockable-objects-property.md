---
title: "Generate Mockable Objects property"
source_id: 56903
source_url: https://wiki.genexus.com/commwiki/wiki?56903
genexus_version: "18"
---

# Generate Mockable Objects property

Indicates whether to generate GeneXus source-level code to allow mock testing on objects.

### [Values](#Values)

|  |
| --- |
| **No** |
| **Yes** |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Environment](https://wiki.genexus.com/commwiki/wiki?7115)

### [Description](#Description)

This property is useful for implementing a mocking system that allows associating mock objects at runtime for [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) and [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270).

The functionality enabled by this property is described in detail in [Object Mock Testing](https://wiki.genexus.com/commwiki/wiki?55859).

**Note:** It is recommended to avoid enabling Mock objects in production environments to preserve the stability and security of the system.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242).

### [See Also](#See+Also)

[Generate Code Coverage information property](https://wiki.genexus.com/commwiki/wiki?44910)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) | [Object Mock Testing](https://wiki.genexus.com/commwiki/wiki?55859) |

---
