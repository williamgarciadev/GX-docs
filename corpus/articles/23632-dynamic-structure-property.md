---
title: "Dynamic structure property"
source_id: 23632
source_url: https://wiki.genexus.com/commwiki/wiki?23632
genexus_version: "18"
---

# Dynamic structure property

Indicates whether the SDT (Structured Data Type) structure is dynamic.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021)

### [Description](#Description)

Default value: False.

This property is used with the [Infer Structure property](https://wiki.genexus.com/commwiki/wiki?23628). When set as True in the SDT, all changes made to the [Data Provider's](https://wiki.genexus.com/commwiki/wiki?5270) structure (with this SDT set in its Output property) will be applied to it (inferred).

**Note:** If the SDT structure is changed by the user, this property will automatically be set to False, thus disabling the inference mechanism.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at runtime.

### [See Also](#See+Also)

[Infer Structure property](https://wiki.genexus.com/commwiki/wiki?23628)


|  |
| --- |
| **Backlinks** |
| [HowTo: Use the Infer Structure property of a Data Provider](https://wiki.genexus.com/commwiki/wiki?23651) |

---
