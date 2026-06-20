---
title: "SetEmpty method"
source_id: 9646
source_url: https://wiki.genexus.com/commwiki/wiki?9646
genexus_version: "18"
---

# SetEmpty method

Assigns the empty value in an attribute, variable, or business component depending on its types.

### [Syntax](#Syntax)

*AttributeName* | ***&****VarName***.SetEmpty()**

**Where:**

*AttributeName*Is the [Attribute](https://wiki.genexus.com/commwiki/wiki?7240) name to which the method is applied.

***&****VarName*Is the [Variable](https://wiki.genexus.com/commwiki/wiki?7375) name to which the method is applied.

### [Scope](#Scope)

**Data Types:** [Audio](https://wiki.genexus.com/commwiki/wiki?16529), [Blob](https://wiki.genexus.com/commwiki/wiki?6704), [BlobFile](https://wiki.genexus.com/commwiki/wiki?40420), [Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371), 
[Date](https://wiki.genexus.com/commwiki/wiki?7373), 
[Date](https://wiki.genexus.com/commwiki/wiki?7373), [DateTime](https://wiki.genexus.com/commwiki/wiki?7370), 
[Geography](https://wiki.genexus.com/commwiki/wiki?32408), GeoLine, GeoPoint, GeoPolygon, [GUID](https://wiki.genexus.com/commwiki/wiki?31772), [Image](https://wiki.genexus.com/commwiki/wiki?15204), [Numeric](https://wiki.genexus.com/commwiki/wiki?6793), [Video](https://wiki.genexus.com/commwiki/wiki?16608), [Extended data types](https://wiki.genexus.com/commwiki/wiki?6560)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

The following table shows the corresponding empty value for each data type

|  |  |
| --- | --- |
| **Data Type** | **Empty value** |
| Boolean | False |
| Character(N), VarChar(N), LongVarChar(N) | N-blanks |
| Date | 001-01-01 |
| DateTime | 0001-01-01 00:00:00 |
| Numeric | 0.0 |
| Time | 00:00:00 |

### [Samples](#Samples)

Rule defined in an Owner [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
OwnerCel.SetEmpty() if OwnerName.IsEmpty();
```

Code defined inside a [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664) or inside an object Event:

```
If OwnerName.IsEmpty()
   OwnerCel.SetEmpty()
EndIf
```

**Notes:**

* Since [GeneXus 15 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?37491,,),
  [Apple](https://wiki.genexus.com/commwiki/wiki?14917) offline apps will consider Date/DateTime empty value as 0001-01-01 instead of 1970-01-01. In case you use an empty value for displaying data, those records with the old empty date value (1970-01-01) will start to be displayed. The following offline Procedure script will fix the problem in the Offline Database:

  ```
  &oldEmptyDate = ymdtod(1970,1,1)
  For each
      where DocumentDate = &oldEmptyDate
        DocumentDate.SetEmpty()
  endfor
  commit
  ```
* Since [GeneXus 16 upgrade 2](https://wiki.genexus.com/commwiki/wiki?41525,,), this method can be used in [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) for [Apple](https://wiki.genexus.com/commwiki/wiki?14917).

### [See Also](#See+Also)

[Attribute Empty Value for each DBMS and Data Type](https://wiki.genexus.com/commwiki/wiki?19150)  
[Nullvalue function](https://wiki.genexus.com/commwiki/wiki?8226)  
[IsNull function](https://wiki.genexus.com/commwiki/wiki?2357)


|  |
| --- |
| **Backlinks** |
| [Cosmos DB nulls handling](https://wiki.genexus.com/commwiki/wiki?53633) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) |

---
