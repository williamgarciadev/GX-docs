---
title: "Session State Provider property"
source_id: 54782
source_url: https://wiki.genexus.com/commwiki/wiki?54782
genexus_version: "18"
---

# Session State Provider property

Sets where session state data will be stored in a web application.

### [Values](#Values)

|  |  |
| --- | --- |
| **Database** | The session state data will be stored in a SQL database. |
| **In Process** | The session state will be stored in the memory of the web server process. |
| **Redis** | The session state data will be stored in a Redis-based distributed cache. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** Generator

### [Description](#Description)

It is important to note that the choice of session state provider depends on the requirements and infrastructure of the application. For containerized deployments, it is recommended to use distributed solutions such as Redis to ensure the availability and persistence of session data. In addition, please note the following:

* Select the "In Process" value if your application runs on a single server and does not require high availability. Note that if the application is restarted or recycled, session data will be lost.
* If your application runs on multiple servers and requires high availability, it is recommended to select the "Redis" setting. Redis allows session data to be shared and synchronized between server instances, which improves scalability in distributed environments. In addition, Redis offers fast in-memory storage.
* Select the "Database" option if your application requires persistence and scalability. By using a database, more comprehensive storage options with advanced query capabilities are provided.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute [Build any object](https://wiki.genexus.com/commwiki/wiki?17719) with the purpose of generating the \*.config files.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).

### [See Also](#See+Also)

[HowTo: Configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626)


|  |
| --- |
| **Backlinks** |
| [Database Table Name property](https://wiki.genexus.com/commwiki/wiki?54777) | [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238) | [HowTo: Configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626) |
| [Instance Name property](https://wiki.genexus.com/commwiki/wiki?54780) | [Location property at Back end Generator level](https://wiki.genexus.com/commwiki/wiki?54883) | [Password property at Back end Generator level](https://wiki.genexus.com/commwiki/wiki?54884) | [SQL Server Data Store property](https://wiki.genexus.com/commwiki/wiki?55060) |

---
