---
title: "Indexes"
source_id: 7121
source_url: https://wiki.genexus.com/commwiki/wiki?7121
genexus_version: "18"
---

# Indexes

GeneXus automatically creates indices that efficiently access [Tables](https://wiki.genexus.com/commwiki/wiki?7120) and permits a more efficient [Referential Integrity](https://wiki.genexus.com/commwiki/wiki?1984,,) control. There are three types of indices: Primary, Foreign, and User.

  
**Primary Index:** The primary index defines the primary key and it is used to control record uniqueness. It also controls, when records are created in a subordinated table, that the corresponding record exists in the superordinated table. GeneXus automatically defines all primary indices from [Transactions](https://wiki.genexus.com/commwiki/wiki?1908) identifiers.  
  
**Foreign Index:** Foreign Indices are used to make more efficient inter-table integrity controls. They are also automatically defined. When a record is removed from the subordinated table, there should be no corresponding record in the subordinated table.  
  
**User Index:** User Indices are mainly defined to query data in an efficient way.

`[imagen omitida: wiki id 7850]`  
  
  
In a relational database, indices are used for performance reasons, but it is always possible to access table data using any of its attributes. This is always true because it is possible to order a table based on any of its attributes whenever necessary. For example, by either creating a temporary index or by using the resources provided by the database you use.


|  |
| --- |
| **Sub Categories** |
| [Category:Table and Index Properties](https://wiki.genexus.com/commwiki/wiki?7122,Category%3ATable+and+Index+Properties,) |

---
