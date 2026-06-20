---
title: "Join management property"
source_id: 7966
source_url: https://wiki.genexus.com/commwiki/wiki?7966
genexus_version: "18"
---

# Join management property

GeneXus Client/Server generators can perform joins in two places: in the DBMS or in each program (once the corresponding code is generated). Normally, doing joins in the DBMS is more efficient than having them done in the program (reduces network traffic, there is less code).
GeneXus will try to generate the join in the DBMS, and when that is not possible for some reason, automatically generates the programs to perform the "join" in the client (server side). This property exists mainly for compatibility reasons, because in prior versions Outer Join was not supported in some DBMS versiones of DB2 Universal Database, Informix and DB2 UDB for iSeries.
Thus, this option allows you to establish where you want the joins to be done.

### [Values](#Values)

|  |  |
| --- | --- |
| **Join tables on the client** | This will cause the GeneXus Client/Server generators to generate code so that the joins will be resolved in the client or server. |
| **Use Environment property value** |
| **Join tables on the server** | This will cause the GeneXus Client/Server generators to try to force the resolution of all joins in the server. This is the default value. |

### [Description](#Description)

#### [Restrictions](#Restrictions)

This optimization is performed automatically with the following restrictions:

* The base table for the [For Each](https://wiki.genexus.com/commwiki/wiki?24744) group must be remote.
* Local tables are excluded from the sentence.
* The tables which are accessed because of the use of subtypes are not included in a For Each's SELECT sentence. SELECT sentences are generated for each specified subtype.
* The tables whose keys must be calculated by means of a formula are not included in the For Each's SELECT. SELECT sentences are generated for each of these types of specifications.
* The tables involved in the navigation of the BREAK groups which are not involved in the navigation of the father For Each group will be accessed via the specified SELECT sentences.

#### [Update and Delete](#Update+and+Delete)

Some DBMSs do not directly support the WHERE CURRENT OF clause which is used by GeneXus to delete or update records, but they are done via the ODBC Driver.

For those DBMSs which do not support these clauses (for example Oracle) the UPDATE and DELETE will be generated using one WHERE (condition) equivalent to the table's primary key over which it is operating.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply changes made by this property, do a Re-Build All.

### [Scope](#Scope)

**Objects:** Procedure, Web Panel  
**Platforms:** Web(.Net, Java)

### [See Also](#See+Also)

[Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719)
