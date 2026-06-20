---
title: "GXflow Performance Settings"
source_id: 10119
source_url: https://wiki.genexus.com/commwiki/wiki?10119
genexus_version: "18"
---

# GXflow Performance Settings

This menu allows you to set some performance options to optimize your GXflow application.

`[imagen omitida: wiki id 52408]`

**Rebuild worklist when Org. Struct. changes**: It allows setting whether user task lists must be rebuilt every time user roles or processes and user restrictions are changed. In this way, users obtain better response times when managing the organizational model.

**Enable Deferred Task Completion**: When a user completes an interactive task workitem, the workflow engine doesn't immediately complete it, but removes it from the user worklist and queues it for deferred completion by a batch application that is periodically run in the server. Every time it is run, the procedure will complete queued workitems, create the corresponding successive workitems and update the user worklists.

**Fetch**: It determines the number of pages shown in the grids of the different GXflow client applications. For example, if the application is set up to show 10 rows per page and the Fetch property has a value of 50, the grid can have up to 5 pages.

**Max fetch**: It determines the maximum number of elements that any query that GXflow client makes to the system database can recover.

For example, if the Inbox has 1000 elements and the Max Fetch value is 500, no task will be shown in the grid; instead, search filters will be automatically displayed to allow the user to establish criteria that would reduce the number of tasks to be shown.

**Maximum number of elements in a SQL list**: It determines the maximum number of elements in a SQL list, the value is 1000 by default because the Oracle DBMS cannot have more than 1000 elements in an IN.

**Enable Organizational Model Cache**: When the cache is enabled, the data structures are populated with information related to the Organizational Model, which increases performance because the structures are no longer loaded from the data. See more in [Optimization to build the worklist](https://wiki.genexus.com/commwiki/wiki?47305).

**Organizational Model Cache Timeout (seconds)**: It determines how often the cache is refreshed. This setting is only available if "Enable Organizational Model Cache" is set to yes.

### [See Also:](#See+Also%3A)

[GXflow Performance Tips](https://wiki.genexus.com/commwiki/wiki?29277)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [Workflow Client Settings](https://wiki.genexus.com/commwiki/wiki?15097) | [WorkflowUser Data Type](https://wiki.genexus.com/commwiki/wiki?17273) |

---
