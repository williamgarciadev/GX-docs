---
title: "IsEmpty method"
source_id: 9645
source_url: https://wiki.genexus.com/commwiki/wiki?9645
genexus_version: "18"
---

# IsEmpty method

Returns True if the value of a given attribute or variable is empty.

### [Syntax](#Syntax)

*Attribute* | *&Variable***.IsEmpty(****)**

**Type Returned:**  
Boolean

### [Scope](#Scope)

**Data Types:** [Audio](https://wiki.genexus.com/commwiki/wiki?16529), [Blob](https://wiki.genexus.com/commwiki/wiki?6704), [BlobFile](https://wiki.genexus.com/commwiki/wiki?40420), [Boolean](https://wiki.genexus.com/commwiki/wiki?4374), 
[Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371), [Date](https://wiki.genexus.com/commwiki/wiki?7373), [DateTime](https://wiki.genexus.com/commwiki/wiki?7370), 
[Geography](https://wiki.genexus.com/commwiki/wiki?32408), GeoLine, GeoPoint, GeoPolygon, [GUID](https://wiki.genexus.com/commwiki/wiki?31772), [Image](https://wiki.genexus.com/commwiki/wiki?15204), [Numeric](https://wiki.genexus.com/commwiki/wiki?6793), [Video](https://wiki.genexus.com/commwiki/wiki?16608)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG,  Cobol, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

Using the method with attributes will depend on whether the condition is evaluated on the **Server** (DBMS) or on the **Client** (Application Server). On the **Client's side**, if an attribute is null (or empty), this method returns true (in most situations, GeneXus handles nulls for attributes as expected). On the **Server's side**, only if the attribute is empty (not null), the IsEmpty method returns true.

Trailing blanks are ignored.

### [Empty Value for each DBMS/Data Type](#Empty+Value+for+each+DBMS%2FData+Type)

The following table shows the corresponding empty value for each data type and DBMS.

| **DBMS** | **Numeric** | **Date** | **Datetime** | **Character (n)** | **Varchar** | **Long Varchar** | **Blob** | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **SQL Server** | 0 | 1753-01-01 00:00:00.000 | 1753-01-01 00:00:00.000 | n blanks | <empty string> | <empty string> | <empty file> |
| **Oracle** | 0 | 0001-01-01 00:00:00 | 0001-01-01 00:00:00 | n blanks | 1 blank | 1 blank | <empty file> |
| **DB2 UDB** | 0 | 0001-01-01 | 0001-01-01 00:00:00.000 | n blanks | <empty string> | <empty string> | <empty file> |
| **DB2 iSeries** | 0 | "00000000" or 0001-01-01(\*) | 0001-01-01-00.00.00 | n blanks | <empty string> | <empty string> | <empty file> |
| **MySQL** | 0 | 1000-01-01 | 1000-01-01 00:00:00 | <empty string> | <empty string> | <empty string> | <empty file> |
| **PostgreSQL** | 0 | 0001-01-01 | 0001-01-01 00:00:00 | n blanks | <empty string> | <empty string> | <empty file> |
| **Informix** | 0 | 0001-01-01 | 0001-01-01 00:00:00 | n blanks | <empty string> | <empty string> | <empty file> | |

### [Samples](#Samples)

**Example 1: Server's side evaluation**

In this case, the condition is evaluated on the Server's side, so only empty values are retrieved.

```
For each
    Where attribute.IsEmpty() // server side execution
          ...  // Only Empty attributes will be considered
EndFor
```

**Note**: Some *Where* conditions could be resolved on the Client's side.  This could happen when the navigation group (For Each, Data Provider, Grid) includes in their **Where/Condition** clause a [function or method that can not be evaluated by the DBMS](https://wiki.genexus.com/commwiki/wiki?11572). In this case, a warning icon `[imagen omitida: wiki id 21326]` will be shown for that condition in the navigation list. Passing the mouse over it displays: "Constraint evaluated in the client. This may lead to poor performance"

**Example 2:  Client's Side evaluation**

This code is evaluated on the Client's side. Both null and empty values are retrieved.

```
For Each
    If attribute.IsEmpty() // client side execution
       ...   // Empty and Null attributes will be considered
    EndIf
EndFor
```

### [See Also](#See+Also)

[Nullvalue function](https://wiki.genexus.com/commwiki/wiki?8226)  
[IsNull function](https://wiki.genexus.com/commwiki/wiki?2357)  
[Null function](https://wiki.genexus.com/commwiki/wiki?8421)


|  |
| --- |
| **Backlinks** |
| [Boolean data type](https://wiki.genexus.com/commwiki/wiki?4374) | [ControlValueChanging event](https://wiki.genexus.com/commwiki/wiki?35768) | [Cosmos DB nulls handling](https://wiki.genexus.com/commwiki/wiki?53633) |
| [GeneXus for SAP Systems - First Rules definitions](https://wiki.genexus.com/commwiki/wiki?34181) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [Null function](https://wiki.genexus.com/commwiki/wiki?8421) |
| [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) |

---
