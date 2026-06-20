---
title: "GXflow Performance Tips"
source_id: 29277
source_url: https://wiki.genexus.com/commwiki/wiki?29277
genexus_version: "18"
---

# GXflow Performance Tips

## [Abstract](#Abstract+)

After using GXflow for some time, you may start to notice a slowdown in some operations.

This document is intended as a guide to determine the cause of the problem and to make some suggestions and recommendations.

## [Recommendations](#Recommendations)

### [Development Environment](#Development+Environment)

* When using APIs that list objects of one of these types: {ProcessInstance, Workitem, DocumentInstance, Event}, keep in mind that they handle a very large volume of data (around millions). Use filters with appropriate date ranges that allow you to narrow your search.
* Excessive creation of connections with the Workflow engine can lead to performance problems. Therefore, the Server.Connect() API must be used sparingly.
  + When programming an inbox or similar type of application, it is recommended to create a connection in the login and then reuse it –as long as it is valid– caching the session identifier and using the Server.Load() method.
  + Keep in mind that the sessions expire. The default value is 30 minutes, but it can be changed in the GXflow Client Settings.
  + When you need to run operations anonymously with the Workflow API (for example, in Script Tasks, Event Managers, etc.), using the WFADMINISTRATOR user is recommended because it allows reusing the connection. Also, special users with exclusive access for APIs can also be used. To configure a user for this purpose, run this SQL statement: UPDATE WFUsers SET WFUsrAccType = "A" Where WFUsrCod ="MY\_USER". Users configured for exclusive API access are not allowed to enter the GXflow client.

### [Production Environment](#Production+Environment)

### [Maintenance](#Maintenance)

* Periodically empty the WFSessions table (read [Maintenance Utility](https://wiki.genexus.com/commwiki/wiki?43314)).
* Review instances that show no activity. If there are process instances that have been inactive for a long time, it may be time to evaluate whether they will be attended or not, so as not to slow down the system. A first option is to suspend them temporarily; if at any later time you want to process them, they can be activated. The other option is to terminate them if it has already been decided that they will not be processed.

### [DBMS Monitoring](#DBMS+Monitoring)

* Frequently review the following queries:
  + The slowest statements.
  + The statements run the most times.
* Review the execution plans of the slowest statements and see if there are suggested indexes (if so, create them).
* Confirm that there are no locks affecting the queries.

## [See Also](#See+Also)

[Optimization to build the worklist](https://wiki.genexus.com/commwiki/wiki?47305)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow Maintenance Script](https://wiki.genexus.com/commwiki/wiki?43314) | [GXflow Performance Settings](https://wiki.genexus.com/commwiki/wiki?10119) |

---
