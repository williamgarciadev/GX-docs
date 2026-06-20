---
title: "First extent size property"
source_id: 7124
source_url: https://wiki.genexus.com/commwiki/wiki?7124
genexus_version: "18"
---

# First extent size property

Lets you indicate the size in Kbytes of the first and/or the following extension(s) assigned to the table or index.

### [Description](#Description)

#### [Values](#Values)

Number of KBytes assigned to the first (and/or following) extension(s) as it expands.

|  |  |  |
| --- | --- | --- |
| **DBMS** | **Use** | **Usage** |
| Oracle | First extension | NEXT parameter for the STORAGE clause |
| SQL Server | N/A |  |
| DB2 Common Servers | N/A |  |
| Informix | First and following extensions | NEXT SIZE clause of the CREATE TABLE command |
| DB2/400 | N/A |  |

**Notes:**

* The value of this property is only considered when the table is created.
* If no value is specified for this property then no clause that indicates the size of table extensions will be generated (there is no default value). Each DBMS, in this case, has its own default values (refer to the DBMS documentation).

#### [Scope](#Scope)

**Objects:** Tables, Indexes

### [See Also](#See+Also)

[Initial Size Property](https://wiki.genexus.com/commwiki/wiki?7125,,)  
[Next Extents Percentage Increase Property](https://wiki.genexus.com/commwiki/wiki?7126,,)  
[Minimum Number of Extents Property](https://wiki.genexus.com/commwiki/wiki?7127,,)


|  |
| --- |
| **Backlinks** |
| [Index Properties](https://wiki.genexus.com/commwiki/wiki?7131) |

---
