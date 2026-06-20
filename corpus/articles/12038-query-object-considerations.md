---
title: "Query Object Considerations"
source_id: 12038
source_url: https://wiki.genexus.com/commwiki/wiki?12038
genexus_version: "18"
---

# Query Object Considerations

In order to preview a [Query Object](https://wiki.genexus.com/commwiki/wiki?9026) within the [IDE](https://wiki.genexus.com/commwiki/wiki?5272) make sure the database connection is set and there's no pending reorganization. In addition, please keep in mind the following considerations:

* [Dameng](https://wiki.genexus.com/commwiki/wiki?50988) displays sample data instead of the data from your Database.
* If you are using Oracle, DB2 iSeries or [SAP HANA](https://wiki.genexus.com/commwiki/wiki?31713), you must make sure to copy certain dependencies to the preview folder. Otherwise, the output window may display a message with the files to be copied and where to copy them to.

### [Interacting with multiple Datastores](#Interacting+with+multiple+Datastores)

By default the [Query Object](https://wiki.genexus.com/commwiki/wiki?9026) supports querying a unique Database referenced by the [default Data Stores](https://wiki.genexus.com/commwiki/wiki?7117). If you are using several [Data Stores](https://wiki.genexus.com/commwiki/wiki?7117) to connect to different database engines, it is not possible to reference attributes from different data stores in a query definition. There's a special case which is supported when several data stores references the same database engine instance.


|  |
| --- |
| **Backlinks** |
| [Query Object Considerations (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54655) | [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |

---
