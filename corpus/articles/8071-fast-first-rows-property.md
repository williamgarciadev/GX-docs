---
title: "Fast first rows property"
source_id: 8071
source_url: https://wiki.genexus.com/commwiki/wiki?8071
genexus_version: "18"
---

# Fast first rows property

Controls the generation of a 'hint' (this helps the DBMS’ optimizer) as it is used to indicate to the DBMS that it should optimize the data return in such a way that the first few rows of the SELECT evaluation are returned as quickly as possible.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | The hint is not generated. |
| **Use Environment property value** |
| **Yes** | The hint is generated. This is the default value. |

### [Description](#Description)

It is NOT generated for [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) nor [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916) because they process all the records that are selected.  
  
It applies over the following DBMS:

|  |  |
| --- | --- |
| **DBMS** | **Hint** |
| Oracle | /\*+ FIRST\_ROWS(n1) \*/ |
| SQL Server | FASTFIRSTROW |
| DB2 Universal Database | OPTIMIZE FOR n ROWS |
| DB2 UDB for iSeries | OPTIMIZE FOR n ROWS |

DBMS optimizers usually have a way of optimizing the processing of all files so that it is as efficient as possible. In some cases this heuristic, however, may not be as good as intended when used by real time applications because total record processing is not required and the most important thing is return the first few results as quickly as possible so that they are presented to the user.

DBMS HINTS are used by the DBMS to know whether it should return the first few rows as soon as possible or not, however, this facility may affect the overall performance of the application (in the case all files are processed).  
  
In general, you will not notice an improved response time of all the application after it is regenerated again. This is because GeneXus databases are correctly indexed and normally the optimization used to retrieve the first few rows rapidly coincides with the one generated to improve the overall process time.  
  
It is possible to improve the performance of transactions when they use filters (generated when equals or parameters are used). The improvement is noticed when data is loaded (going to the first record) or when moving to the next record.  
  
Hints improve query response times (returning the first row) but it can worsen the overall execution time if all rows need to be processed.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Re-Build All.

### [Scope](#Scope)

**Objects:** Transaction, Web Panel  
**Platforms:** Web(.Net, Java)
