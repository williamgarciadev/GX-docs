---
title: "Date data type definition property"
source_id: 53796
source_url: https://wiki.genexus.com/commwiki/wiki?53796
genexus_version: "18"
---

# Date data type definition property

Indicates the data type to be used in the DBMS for attributes defined as Date in GeneXus.

### [Values](#Values)

|  |  |
| --- | --- |
| **Char(8)** | The data type in the database will be Character(8). |
| **Date** | The data type in the database will be Date. |

### [Scope](#Scope)

Available at the Data Store.  
**Data Store:** iSeries

### [Description](#Description)

When working with DB2 for iSeries as a DBMS, the attributes based on the [Date data type](https://wiki.genexus.com/commwiki/wiki?7373) in GeneXus are generated as characters in the database.

The **Date data type definition property** is offered at the Data Store level when the Data Store is DB2 for iSeries. It allows setting the format to use in the database for the attributes defined as Date in GeneXus. The possible values ​​are:

- Date: The data type in the database will be Date.  
- Char(8): The data type in the database will be Character(8).

The default value is Char(8).

This property is not supported by RPG or Cobol (they would only accept the value Character). This implies that if you want to call some procedure generated in RPG/Cobol as stored procedures you cannot change the default value of the preference.

This property applies to all generators that access AS/400 (C/SQL, VB, VFP, Java, C#).

**Notes:**

* This applies only to the [Date data type](https://wiki.genexus.com/commwiki/wiki?7373) and not to the [DateTime data type](https://wiki.genexus.com/commwiki/wiki?7370).
* The null value is 01/01/0001.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.


|  |
| --- |
| **Backlinks** |
| [Date data type](https://wiki.genexus.com/commwiki/wiki?7373) | [Date data type (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55760) | [GAM - Troubleshooting](https://wiki.genexus.com/commwiki/wiki?22815) |

---
