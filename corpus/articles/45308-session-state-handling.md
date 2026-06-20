---
title: "Session state handling"
source_id: 45308
source_url: https://wiki.genexus.com/commwiki/wiki?45308
genexus_version: "18"
---

# Session state handling

Business applications typically need to maintain some session state. That means, there is information that requires to be saved so that it can be used in the next request of that user.

Between requests, some things may happen:

* Sever becomes unresponsive
* In a load balancing environment, the load balancer may decide to not assign all the requests from the same user to the same server

Depending on the service levels of high availability or fault tolerance that are required, and for the well functioning of the application, some actions have to be taken:

1. Use [Session Replication](https://wiki.genexus.com/commwiki/wiki?45283,,)
2. Use [Server Affinity (Sticky Sessions)](https://wiki.genexus.com/commwiki/wiki?45282,,)
3. Move the session information to an external point (e.g. a state server like Redis or the database)

**Notes:**

* A drawback of the second (2.) approach, it has not so high fault tolerance, compared to the first one. Anyway, it can be used together with some of the other approaches
* Storing the web session in the database is generally not good for performance or scalability because it creates an extra workload on the database.

### [See Also](#See+Also)

<https://stackoverflow.com/questions/10278683/how-safe-is-it-to-store-sessions-with-redis>  
<https://github.com/ran-jit/tomcat-cluster-redis-session-manager>  
<https://stackoverflow.com/a/11045462/382145> - Sticky Sessions and Session Replication  
[SAC #15071 - Session State in .NET](https://www.genexus.com/developers/websac?es,,,15071)  
[SAC #52313 - Session State Troubleshooting](https://www.genexus.com/developers/websac?es,,,52313)


|  |
| --- |
| **Backlinks** |
| [Considerations for building and deploying applications to containers](https://wiki.genexus.com/commwiki/wiki?45309) | [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) | [Toc:Scalability and Performance of GeneXus Applications](https://wiki.genexus.com/commwiki/wiki?45280) |
| [Stateless vs Statefull](https://wiki.genexus.com/commwiki/wiki?45284) |

---
