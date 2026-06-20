---
title: "Primary Key"
source_id: 1868
source_url: https://wiki.genexus.com/commwiki/wiki?1868
genexus_version: "18"
---

# Primary Key

Attribute (or set of Attributes) that identify univocally a row of a relation. A Primary Key must follow these properties:

* Univocally identify a row. In other words, it can't exist two rows with the sames values of the Primary Key.

* The value of the Primary Key must be known since the row creation. Sometimes an Attribute can be unique, but its value isn't know when creating the row. Ex. in the Person relation the Social Security Number is unknown for newborns.

* The value of the Primary Key must be unmutable. This property is optional, but very desirable. Given the [Relational Database Theory](https://wiki.genexus.com/commwiki/wiki?1811,,) says the relationship between tables must be expressed by the presence of a Primary Key of a table in other table, if the value of the first one is changed, all the rows of the other tables related with this one must be changed. This operation isn't supported in [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) .

### [See also](#See+also)

[Candidate Key](https://wiki.genexus.com/commwiki/wiki?2199,,)  
[Surrogate Key](https://wiki.genexus.com/commwiki/wiki?2197)


|  |
| --- |
| **Backlinks** |
| [Business Component Delete method](https://wiki.genexus.com/commwiki/wiki?23238) | [Business Component Load method](https://wiki.genexus.com/commwiki/wiki?23211) | [Business Component variables properties](https://wiki.genexus.com/commwiki/wiki?2276) |
| [Description attribute](https://wiki.genexus.com/commwiki/wiki?2154) | [DynamoDB - Navigation restrictions](https://wiki.genexus.com/commwiki/wiki?50640) | [Error handling in Business Components](https://wiki.genexus.com/commwiki/wiki?2279) | [Example: New Command](https://wiki.genexus.com/commwiki/wiki?6742) |
| [GeneXus for SAP Systems - Data Model changes](https://wiki.genexus.com/commwiki/wiki?34336) | [GeneXus for SAP Systems Data Model changes (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54688) | [Image Attribute Property](https://wiki.genexus.com/commwiki/wiki?15153) |
| [New command](https://wiki.genexus.com/commwiki/wiki?6714) | [Surrogate Key](https://wiki.genexus.com/commwiki/wiki?2197) |

---
