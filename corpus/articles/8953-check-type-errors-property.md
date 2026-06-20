---
title: "Check type errors property"
source_id: 8953
source_url: https://wiki.genexus.com/commwiki/wiki?8953
genexus_version: "18"
---

# Check type errors property

Uses type controls to check whether expressions, conditions, formulas, and rules are valid.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | If you select NO for Check Type errors, the error message will be shown as a warning during specification, which will allow the program generation to continue. |
| **Yes** | When an expression is not valid (i.e.: type mismatch, property not available for some control/platform, etc.), the object navigation will show an error message. This is the default value. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

You can define whether you want to display Error or Warning messages when Type control is carried out.

The following table shows the messages that can be shown as warning when the property is set to "No".

|  |  |
| --- | --- |
| [spc0001](https://wiki.genexus.com/commwiki/wiki?6431) | Control/object %1 not found/defined. Is it on the form? |
| [spc0006](https://wiki.genexus.com/commwiki/wiki?6431) | %1 objects do not have the ‘%2’ method. |
| [spc0009](https://wiki.genexus.com/commwiki/wiki?6431) | Type mismatch in %1: %2. |
| [spc0010](https://wiki.genexus.com/commwiki/wiki?6431) | Type mismatch in assignment: %1 = %2 (%3=%4). |
| [spc0011](https://wiki.genexus.com/commwiki/wiki?6431) | Type mismatch in rule %1. |
| [spc0017](https://wiki.genexus.com/commwiki/wiki?6431) | Expression %1 does not return a value. |
| [spc0018](https://wiki.genexus.com/commwiki/wiki?6431) | Property %1 is read only. It cannot be assigned. |
| [spc0050](https://wiki.genexus.com/commwiki/wiki?6432) | Inferred subtype %1, cannot be assigned. |
| [spc0075](https://wiki.genexus.com/commwiki/wiki?6432) | Operand %1 does not match the data type of %2 in the IN comparison. |
| [spc0076](https://wiki.genexus.com/commwiki/wiki?6432) | %1 must be a collection to be used as the right operand in an IN comparison. |
| [spc0077](https://wiki.genexus.com/commwiki/wiki?6432) | %1’s data type (%2) is not supported in an IN comparison. |
| [spc0100](https://wiki.genexus.com/commwiki/wiki?6433) | Item description in dynamic combo box %1 has an unsupported data type %2. |
| [spc0101](https://wiki.genexus.com/commwiki/wiki?6433) | Item value %1 does not match control %2 data type. |
| [spc0109](https://wiki.genexus.com/commwiki/wiki?6433) | %1 is (part of) a candidate key. It must be referenced in the transaction’s structure. |
| [spc0112](https://wiki.genexus.com/commwiki/wiki?6433) | Item value %1 for control %2 must be Character or VarChar. |

#### [**Note:**Cobol and RPG generators do not allow to show spc0001 as "warning".](#Note%3A+Cobol+and+RPG+generators+do+not+allow+to+show+spc0001+as+%22warning%22.)

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [See Also](#See+Also)

[Standard Functions property at Knowledge Base level](https://wiki.genexus.com/commwiki/wiki?7403)  
[Warnings treated as errors property](https://wiki.genexus.com/commwiki/wiki?8010)  
[Disabled warnings property](https://wiki.genexus.com/commwiki/wiki?8009)


|  |
| --- |
| **Backlinks** |
| [Specification Codes from spc0000 to spc0049](https://wiki.genexus.com/commwiki/wiki?6431) | [Specification Codes from spc0050 to spc0099](https://wiki.genexus.com/commwiki/wiki?6432) | [Specification Codes from spc0100 to spc0149](https://wiki.genexus.com/commwiki/wiki?6433) |
| [Standard Functions property at Knowledge Base level](https://wiki.genexus.com/commwiki/wiki?7403) |

---
