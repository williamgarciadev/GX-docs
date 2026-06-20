---
title: "Generate FOR UPDATE clause property"
source_id: 7952
source_url: https://wiki.genexus.com/commwiki/wiki?7952
genexus_version: "18"
---

# Generate FOR UPDATE clause property

Ensures that procedures that update data with COMMIT close the cursor.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | The SQL sentences that update the data won't be generated with the FOR UPDATE clause. |
| **Use Environment property value** | The SQL sentences will be generated in this object, taking into account the value specified in the corresponding property at Data Store level (this is the default value). |
| **Yes** | The SQL sentences that update the data will always be generated with the FOR UPDATE clause. |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** ORACLE  
**Objects:** Procedure, Transaction  
**Platforms:** Web(.Net, Java)

### [Description](#Description)

When a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) updates many thousands of records, it is usually necessary (and advisable) to include a commit at intervals, so no large spaces are needed for the logs.

In these cases you would use the property with value NO so that the cursor is not closed and the next fetches do not issue an error (the property set to YES causes a COMMIT within a SELECT FOR UPDATE to close the opened cursor).

If the object does not offer a property at the object level it is necessary to set it at the Data Store level. Thus, none of the SELECTS include the FOR UPDATE clause, taking the corresponding risk: in these cases, the SELECT sentence, before performing the UPDATE of a record, is only to read and the record is not locked; therefore, changes made by other users may be lost.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Re-Build All.


|  |
| --- |
| **Backlinks** |
| [DBMS Options for JDBC Technology](https://wiki.genexus.com/commwiki/wiki?9070) |

---
