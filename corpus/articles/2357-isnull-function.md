---
title: "IsNull function"
source_id: 2357
source_url: https://wiki.genexus.com/commwiki/wiki?2357
genexus_version: "18"
---

# IsNull function

Determines if an attribute's value is DBMS NULL.

### [Syntax](#Syntax)

**IsNull(**Attribute**)**

**Where:**  
  
*Attribute*  
    Is the attribute that will be evaluated.

**Type Returned:**  
Boolean Value

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

In some cases it is necessary to determine if an attribute's value matches the DBMS NULL. This value is different from the nullvalue (obtained, for example, by using the [Nullvalue](https://wiki.genexus.com/commwiki/wiki?8226) (Attribute) function), determined by GeneXus according to the data/DBMS type.   
  
The NULL value of an attribute could have been generated, for example, if the attribute has not been instanced in a New command (with the “Initialize not referenced attributes” preference set to “No”). It may also be necessary to distinguish it from other values when external tables are accessed.   
When the function is used by including it in Where or Condition commands that are optimized (which means the condition is solved in the server), it will be translated as...**Attribute IS NULL** in the SQL statement.

**Notes**:

* This function can only be used within For Each and Condition commands of Grids that have a base table.
* For local DBMSs (Access and DBFs) the IsNull() function behaves in the same way as the Null() function.

### [Samples](#Samples)

#### Sample 1

```
For each
    Where IsNull(CustomerName)
       ...   ...
       ...   ...
EndFor
```

This [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) navigates through all the Customer records that have the CustomerName attribute with a DBMS NULL value.

#### Sample 2

```
For each
    If IsNull(CustomerName)
       ...
    EndIf
    ...
    ...
EndFor
```

Even though both samples return the same results, the first one is more efficient, as the condition is solved in the server whereas the second one is solved in the client.

### [See Also](#See+Also)

[Null function](https://wiki.genexus.com/commwiki/wiki?8421)  
[Nullvalue function](https://wiki.genexus.com/commwiki/wiki?8226)


|  |
| --- |
| **Backlinks** |
| [Cosmos DB nulls handling](https://wiki.genexus.com/commwiki/wiki?53633) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [IsEmpty method](https://wiki.genexus.com/commwiki/wiki?9645) | [IsNull method](https://wiki.genexus.com/commwiki/wiki?12735) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |
| [Null function](https://wiki.genexus.com/commwiki/wiki?8421) | [Nullvalue function](https://wiki.genexus.com/commwiki/wiki?8226) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [SetEmpty method](https://wiki.genexus.com/commwiki/wiki?9646) |
| [SetNull method](https://wiki.genexus.com/commwiki/wiki?12730) |

---
