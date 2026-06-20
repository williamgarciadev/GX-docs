---
title: "Use decimal arithmetic property"
source_id: 10324
source_url: https://wiki.genexus.com/commwiki/wiki?10324
genexus_version: "18"
---

# Use decimal arithmetic property

Allows the developer to perform floating-point operations with precision.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | Floating point is not applied in the operation. |
| **Yes** | Floating point is applied in the operation. This is the default value. |

### [Samples](#Samples)

Let's suppose you have 72.35 \* 100 in Java. Then the result will be 7234.9999999.

But if in GeneXus you have an N(10) - integer type variable, and you assign the same operation to it, you will not get the expected result:

&integer = 72,35 \* 100  //return 7234

By setting this property to Yes, you will obtain the expected result.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Re-Build All.

### [Scope](#Scope)

**Objects:** Procedure  
**Platforms:** Web(Java)

### [See Also](#See+Also)

[Round function](https://wiki.genexus.com/commwiki/wiki?8486)


|  |
| --- |
| **Backlinks** |
| [Android specific properties](https://wiki.genexus.com/commwiki/wiki?31449) | [Attribute and Variable Data types mapping by Generator](https://wiki.genexus.com/commwiki/wiki?21392) | [iOS Specific properties](https://wiki.genexus.com/commwiki/wiki?31827) |

---
