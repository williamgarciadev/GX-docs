---
title: "Generate null for nullvalue() property"
source_id: 8986
source_url: https://wiki.genexus.com/commwiki/wiki?8986
genexus_version: "18"
---

# Generate null for nullvalue() property

Used to store attributes with null values in the database using function NullValue() (or SetNull method). Even if using this property, the function NullValue() will return the database null value that corresponds to that attribute, It cannot be used to compare with attributes that have null values.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | If we have the assignment Att = NullValue(Att) in the transaction rules or as a command (in any object where it is possible to use it), Att will be assigned the corresponding value returned by NullValue(). This value will be: blank spaces, zeroes, null date, etc., depending on Att data type. This is the default value. |
| **Use Environment property value** |
| **Yes** | The behavior in this case is similar to the previous case (value=No), only that the Att is internally marked" so that when an insertion or update is performed the attribute is stored as null. |

### [Description](#Description)

If an attribute is assigned a NullValue() and then any other value (not null), a value different than null will be stored in the database. Example:

```
Att = NullValue(Att)
If &X = 1
   Att = 5
EndIf
```

In the case that &X's value is 1, Att's value will be 5 (not null), and when &X value is different than 1 Att's value will be null in the database.

"Transitive" assignments are not valid.

### [Samples](#Samples)

```
Att = NullValue(Att)
Attx = Att 
```

Attx's value will not be null. It will be assigned Att's value, but it will not be marked as null As a   consequence of this, if an attribute or variable which has been assigned a null value is passed as  parameter between programs, and the received value is assigned to an attribute, only the received value is assigned and not the "property" of being null.

Attributes that are stored as null cannot be used as filters because they are not equal or different to any other value. For example, comparing with the date ‘ / / ‘ in a condition will not filter the records with null dates.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Re-Build All.

### [Scope](#Scope)

**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[Initialize not referenced attributes property](https://wiki.genexus.com/commwiki/wiki?7946)  
[Nullvalue function](https://wiki.genexus.com/commwiki/wiki?8226)  
[SetNull method](https://wiki.genexus.com/commwiki/wiki?12730)


|  |
| --- |
| **Backlinks** |
| [Declare referential integrity property](https://wiki.genexus.com/commwiki/wiki?9093) | [Initialize not referenced attributes property](https://wiki.genexus.com/commwiki/wiki?7946) | [Nullvalue function](https://wiki.genexus.com/commwiki/wiki?8226) |
| [SetNull method](https://wiki.genexus.com/commwiki/wiki?12730) |

---
