---
title: "Initialize not referenced attributes property"
source_id: 7946
source_url: https://wiki.genexus.com/commwiki/wiki?7946
genexus_version: "18"
---

# Initialize not referenced attributes property

When new records are added to a database either by transactions or by a procedure’s NEW group, attributes not referenced are stored in the database with null values (case the attribute supports Nulls). In its navigation diagram, GeneXus indicates the list of attributes that will be inserted; those that do not appear in the list remain with null values.
This property avoids the situation described above. Upon activating it, the generators automatically initialize all attributes that were not referenced (in a transaction structure or a NEW group) with their corresponding Empty Value.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | No action is taken. |
| **Use Environment property value** |
| **Yes** | The generators automatically initialize all attributes that were not referenced. |

### [Description](#Description)

#### [Notes:](#Notes%3A)

* Long Varchar attributes are not initialized by this property, meaning that if a value is not assigned, it will remain as null. This exception is meant to reduce the space used by these types of attributes.
* If the value of this property changes, then you will need to force the generation of the program.
* The property at object level has priority over the one specified at Environment level.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Re-Build All.

### [Scope](#Scope)

**Objects:** Procedure, Transaction  
**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[Handling Nulls with GeneXus](https://wiki.genexus.com/commwiki/wiki?15691,,)  
[Generate null for nullvalue() property](https://wiki.genexus.com/commwiki/wiki?8986)  
[Nullable property - Attribute](https://wiki.genexus.com/commwiki/wiki?7642)  
[Empty value for each DBMS/Data type](https://wiki.genexus.com/commwiki/wiki?22488,,)


|  |
| --- |
| **Backlinks** |
| [Android specific properties](https://wiki.genexus.com/commwiki/wiki?31449) | [Copy table groups property](https://wiki.genexus.com/commwiki/wiki?7973) | [Generate null for nullvalue() property](https://wiki.genexus.com/commwiki/wiki?8986) |
| [iOS Specific properties](https://wiki.genexus.com/commwiki/wiki?31827) |

---
