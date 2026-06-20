---
title: "Copy table groups property"
source_id: 7973
source_url: https://wiki.genexus.com/commwiki/wiki?7973
genexus_version: "18"
---

# Copy table groups property

Controls the optimization when the copy tables pattern is detected.

### [Values](#Values)

|  |  |
| --- | --- |
| **Always** | All detected patterns for copying are optimized even though there exists a unique index defined in GeneXus. |
| **If no unique index** | All detected patterns whose New group’s base table do not include the definition of a unique index (primary key or candidate) in GeneXus are optimized. This is the default value. |
| **Never** | Patterns for copying are never detected. |
| **Use Environment property value** |

### [Description](#Description)

The idea is to detect what table information is being copied to another table and generate an INSERT w/SUBSELECT to avoid traffic. Reorganization programs could make frequent use of this command.

The programming pattern that needs to be detected is:

```
For Each
   [where Condition]
   [defined by Att1, Att2, …]
    New|XNew
       &Var|Attribute=Attribute1
        ...   ...   ...

    EndNew|EndXNew
EndFor
```

#### [Conditions:](#+Conditions%3A+)

* Both tables (for each’s and new’s base table) need to be on the same DBMS. Optimizations, for example, between local and remote tables are not possible.
* This behavior depends on the **Initialize not reference attribute** property.  
    - When set to **Yes**, all base table attributes should be referenced in order to do a subselect.  
    - When set to **No**, fields should allow nulls.
* The fields that originate assignments must be stored in the base table corresponding to the superior for each group. On the other hand, assigned target fields must be stored in the New|XNew group’s base table.
* The New|XNew group cannot include **When Duplicate**. This means that duplicates need to be managed or the possibility of defining a condition to accept duplicate keys is defined.
* The DBMS must support the INSERT w/SUBSELECT command. There are some that support it but there are restrictions. For example, ORACLE supports the command if references to Long Varchar attributes (TEXT in ORACLE) are not made.
* The length of target fields must be greater than or equal to their source fields in order to avoid value overflows. DBMSs generally abort the entire process being executed; GeneXus tolerates them by truncating or generating an internal overflow that does not abort.

#### [Notes:](#Notes%3A)

* When **Always value** is specified, the generated programs **can cancel** when executed as they try to add a record with a duplicate key.
* Important: When **Never value** is specified, it affects the performance of **reorganization** programs as it inhibits their optimization.

This property also exists at an **object level**. The property at a model level applies to the entire model, unlike object properties that only apply to the specific object in which they are specified. Also, the property at an object level has priority over the ones specified at the environment level.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Re-Build All.

### [Scope](#Scope)

**Objects:** Procedure  
**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[Initialize not referenced attributes property](https://wiki.genexus.com/commwiki/wiki?7946)
