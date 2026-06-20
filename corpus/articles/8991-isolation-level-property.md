---
title: "Isolation level property"
source_id: 8991
source_url: https://wiki.genexus.com/commwiki/wiki?8991
genexus_version: "18"
---

# Isolation level property

Sets the isolation level of the changes made by the programs.

### [Values](#Values)

|  |  |
| --- | --- |
| **Read Committed** | In this isolation level, the programs do NOT see the changes made by other users until they perform a COMMIT. This is the default value. |
| **Repeatable Read** | In this isolation level, the programs do NOT read Updates made by other users, to all the referenced records, until they make a COMMIT. |
| **Serializable** | In this isolation level, the programs do NOT read Updates, Inserts, or Deletes made by other users, to all the referenced records, until they make a COMMIT. |
| **Read Uncommitted** | In this isolation level, the programs see the changes made by other users even if they haven't performed a COMMIT yet. |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** Iseries, DB2 UDB, INFORMIX, MYSQL, ORACLE, POSTGRESQL, SQLSERVER  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

Setting Isolation level affects read phenomena and concurrency control. Using Read Committed provides higher consistency levels but generates more locks on the database. There is more information about Isolation Level at <https://en.wikipedia.org/wiki/Isolation_(database_systems)> and the documentation of different DBMSes.

Important:

* The property is read-only for Oracle and its value is Read Committed (Oracle Database doesn't use dirty reads, nor does it even allow them)
* The isolation level used for SQLite (Android and iOS programs) is Read Committed.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

Consider a [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) with attributes A, B on which the following [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) are defined:

Procedure1

```
//Enter new values for the attributes and then commit the changes.
new
  A=1
  B=1
endnew

commit

//Enter other new values, but this time do not confirm them.

new
  A=2
  B=2
endnew

//Prints a message on the screen with the values of B. 

for each
   msg(B.ToString()) //In any isolation level 1 and 2 are displayed.
endfor

//Run Procedure2
Procedure2()

//After running Procedure2, it stores the message with the values of B in an internal  
//variable and continues processing (the user will not see the message until the end of the program processing). 
//It then saves the changes made so far.

for each
    msg(B.ToString(), nowait) //In Read Uncommited and Read Commited 11, 2, and 3 are displayed. 
//In Repeatable Read and Serializable 1, 2.
endfor

commit

//Saves the message with the values of B in an internal variable and continues processing.
for each
    msg(B.ToString(), nowait) //In any isolation level except Serializable it shows 11, 2 and 3. 
//In Serializable it shows 1, 2, because it could not do the update or new in Procedure2, 
//it has changes that have not been committed.
endfor
```

Procedure2 has set Execute in new LUW.

```
//Prints on the screen the values of B.
for each 
  msg(B.ToString()) //In Read Uncommited 1 and 2 are shown, in the others only 1.
endfor

//Updates the value of B, as long as A is worth 1.
for each
  where A = 1
  B=11
Endfor

//Add new values to A and B.
new
  A = 3
  B = 3
endnew
```

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[SAC 43993 - Isolation Level Property Support](https://www.genexus.com/developers/websac?,,,43993) contains details related to configuration files, conversion and other related information.


|  |
| --- |
| **Backlinks** |
|
| [Isolation Level behavior property](https://wiki.genexus.com/commwiki/wiki?42091) | [Locking in GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?45652) |

---
