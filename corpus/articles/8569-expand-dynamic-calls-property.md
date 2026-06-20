---
title: "Expand dynamic calls property"
source_id: 8569
source_url: https://wiki.genexus.com/commwiki/wiki?8569
genexus_version: "18"
---

# Expand dynamic calls property

To allow calling GeneXus objects dynamically, i.e., call(&program)

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | No objects are called. This is the default value. |
| **Yes** | Capability to call objects |

### [Description](#Description)

This feature allows *the specifier* to transform a dynamic call (referencing a variable or attribute as first parameter) into a DO CASE, with as many CASEs as programs exist in the KB, with the same number and type of parameters referenced in the CALL.

This feature applies to the Call and Link command. If the name specified is a GeneXus object, it will be called (or linked). Otherwise, the Call or Link is made with the specified name.

The GX CALLs tree is updated, thus allowing to have information regarding who calls whom.

For RPG and Cobol, the parameters type control is by equal (exact) definition. For the rest of generators the criteria is the following:

* Numeric ones must be exactly the same, regardless of having a sign or not.
* Character type parameters (Char, VarChar and LongVarChar) are considered equal, and control is made as corresponding, if the calling parameter length is shorter or equal to the length of the parameter called.
* The objects that the generator cannot generate are excluded from the call expansion.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Re-Build All.

### [Scope](#Scope)

**Objects:** Procedure, Transaction, Web Panel  
**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[Call command](https://wiki.genexus.com/commwiki/wiki?8260)


|  |
| --- |
| **Backlinks** |
| [Call command](https://wiki.genexus.com/commwiki/wiki?8260) | [Modules - Dynamic calls](https://wiki.genexus.com/commwiki/wiki?22585) |

---
