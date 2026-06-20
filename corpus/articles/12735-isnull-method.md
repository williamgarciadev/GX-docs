---
title: "IsNull method"
source_id: 12735
source_url: https://wiki.genexus.com/commwiki/wiki?12735
genexus_version: "18"
---

# IsNull method

Determines if an attribute's value is DBMS NULL.

### [Syntax](#Syntax)

*Attribute***.****IsNull()**

**Where:**  
*Attribute*  
   Is the attribute that will be evaluated.

**Type Returned:**  
Boolean

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

In some cases, it is necessary to determine if an attribute's value matches the DBMS NULL. This value is different from the nullvalue (obtained, for example, using the [Nullvalue](https://wiki.genexus.com/commwiki/wiki?8226) (Attribute) function), determined by GeneXus according to the data/DBMS type.   
  
The NULL value of an attribute could have been generated, for example, if the attribute has not been instanced in a New command (with the “Initialize not referenced attributes” preference set to “No”). It may also be necessary to distinguish it from other values when external tables are accessed.   
When the method is used by including it in Where or Condition commands that are optimized (which means the condition is solved in the server), it will be translated as...**Attribute IS NULL** in the SQL statement.  
  
**Notes:**

* This method can only be used within For Each and Condition commands of Grids that have a base table.
* For local DBMSs (Access and DBFs) the IsNull() method behaves in the same way as the Null() function.

### [Samples](#Samples)

#### [Sample 1](#Sample+1)

```
For each
    Where CustomerName.IsNull()
       ...   ...
       ...   ...
EndFor
```

This [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) navigates through all the Customer records that have the CustomerName attribute with a DBMS NULL value.

#### [Sample 2](#Sample+2)

```
For each
    If CustomerName.IsNull()
       ...
    EndIf
    ...
    ...
EndFor
```

Even though both samples return the same results, the first one is more efficient, as the condition is solved in the server whereas the second one is solved in the client.

### [See Also](#See+Also)

[IsNull function](https://wiki.genexus.com/commwiki/wiki?2357)  
[Null function](https://wiki.genexus.com/commwiki/wiki?8421)  
[Nullvalue function](https://wiki.genexus.com/commwiki/wiki?8226)


|  |
| --- |
| **Backlinks** |
| [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |

---
