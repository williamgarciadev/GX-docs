---
title: "Reorganizations associated to Data Views"
source_id: 43272
source_url: https://wiki.genexus.com/commwiki/wiki?43272
genexus_version: "18"
---

# Reorganizations associated to Data Views

When working in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) with an external table (associated with a [Data View](https://wiki.genexus.com/commwiki/wiki?1914), probably created through the [Database Reverse Engineering](https://wiki.genexus.com/commwiki/wiki?6634)), [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) does not reorganize it (this is informed in the Navigation Report).

In particular when at a certain moment, you delete a Data View, then the next [Reorganization](https://wiki.genexus.com/commwiki/wiki?5288) will create the external table as "internal".

This implies that:

* the table will be created in the default Data Store (in the database associated with your application).
* the data of the external table will be copied from the original Data Store to the new one, preserving the data.

On the other hand, if you do not delete the Data View, but you change its [Data Store](https://wiki.genexus.com/commwiki/wiki?7117) or platform associated with the Data View, the same will occur:

* the table will be created in the new specified Data Store.
* the data of the external table will be copied from the original Data Store to the new one, preserving the data.


|  |
| --- |
| **Backlinks** |
| [Features of Reorganizations](https://wiki.genexus.com/commwiki/wiki?3154) |

---
