---
title: "Use Cache property"
source_id: 19595
source_url: https://wiki.genexus.com/commwiki/wiki?19595
genexus_version: "18"
---

# Use Cache property

### [**Deprecated** since: [GeneXus 15 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?32886,,)](#Deprecated+since%3A+wiki%3F32886%2CGeneXus%2B15%2BUpgrade%2B2+GeneXus+15+Upgrade+2)

Every time that a user executes a query, there is a data selection process on the database. The cost, in resources and/or time needed, to solve it may be too high. Selecting data to satisfy the conditions of a query from among millions of records might take up a lot of processing time.

It is common for users to execute a query several times in periods of time that are considerably short. If the query consumes a significant amount of resources, these will be consumed in every execution, unless we can “activate” the “Use Cache” property.

If the data selected by a query is considered static because it does not change or it does not matter if it does change (in what regards the time of data analysis), then we can set the value “true” to the “Use Cache” property. Otherwise, we must keep the value as “false” for that property.

When the value of the “Use Cache” property is “true”, and we have a [Query object](https://wiki.genexus.com/commwiki/wiki?9026) or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) associated with the Query Viewer control, then the query or data provider will be executed and it will access the database only the first time that the user uses it. For a given period of time (see below), the result of the Query will be stored in the server and any other execution by the same user will have a reply from that same storage (without accessing the database).

### [What is the period for keeping data on the server?](#What+is+the+period+for+keeping+data+on+the+server%3F)

In the case of web applications, the data resulting from the execution of a Query or Data Provider when the value of the "Use Cache" property is True is kept in the user’s web session and maintained while that session lasts.

### [Values](#Values)

|  |  |
| --- | --- |
| **False** | Data will always be read by accessing the database. This is the default value. |
| **True** | The database will only be accessed the first time that the [Query object](https://wiki.genexus.com/commwiki/wiki?9026) or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) is executed. |

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Output type:** | Table, PivotTable, Chart |
