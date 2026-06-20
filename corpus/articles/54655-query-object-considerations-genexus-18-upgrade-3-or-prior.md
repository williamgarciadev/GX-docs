---
title: "Query Object Considerations (GeneXus 18 Upgrade 3 or prior)"
source_id: 54655
source_url: https://wiki.genexus.com/commwiki/wiki?54655
genexus_version: "18"
---

# Query Object Considerations (GeneXus 18 Upgrade 3 or prior)

In order to preview a [Query Object](https://wiki.genexus.com/commwiki/wiki?9026) within the [IDE](https://wiki.genexus.com/commwiki/wiki?5272) make sure the database connection is set and there's no pending reorganization. In addition, please keep in mind the following considerations:

* [Dameng](https://wiki.genexus.com/commwiki/wiki?50988) displays sample data instead of the data from your Database.
* If you are using Oracle, DB2 iSeries or [SAP HANA](https://wiki.genexus.com/commwiki/wiki?31713), you must make sure to copy certain dependencies to the preview folder. Otherwise, a message like the following may appear:   
    
  The following non-distributable dll was not found: 'IBM.Data.DB2.iSeries.dll'. You need to copy it to '<GX\_Installation\_Path>\Packages\GXplorer\Preview\bin' in order to preview this query.  
    
  The following non-distributable dll was not found: 'libmySQL.dll'. You need to copy it to '<GX\_Installation\_Path>\Packages\GXplorer\Preview\bin' in order to preview this query.

### [Interacting with multiple Datastores](#Interacting+with+multiple+Datastores)

By default the [Query Object](https://wiki.genexus.com/commwiki/wiki?9026) supports querying a unique Database referenced by the [default Data Stores](https://wiki.genexus.com/commwiki/wiki?7117). If you are using several [Data Stores](https://wiki.genexus.com/commwiki/wiki?7117) to connect to different database engines, it is not possible to reference attributes from different data stores in a query definition. There's a special case which is supported when several data stores references the same database engine instance.
