---
title: "Cache Location property"
source_id: 31331
source_url: https://wiki.genexus.com/commwiki/wiki?31331
genexus_version: "18"
---

# Cache Location property

Configures the location of the Distributed Cache server. You must specify space-separated host:port pairs for Memcached, a comma-separated host:port list for Redis on .NET or .NET Framework, or a complete Redis URI for Redis on Java (i.e. redis://clientid:password@localhost:6379?ssl=true&db=1).

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

In a [distributed caching](https://wiki.genexus.com/commwiki/wiki?28136) environment, the **Cache Location property** allows configuring the server and port where the Cache system is operating.

Therefore, after configuring the [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147) to 'Redis' or 'Memcached', the **Cache Location property** will be available to enter any valid location depending on the distributed caching system specified in the [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147).

If more than one location has to be specified, the locations should be separated by empty spaces.

#### [**Selecting a Logical Database in Redis**](#Selecting+a+Logical+Database+in+Redis)

Redis has sixteen databases, numbered from 0 to 15. If you don't specify one, database 0 is used by default.

To choose a different one, add db=N at the end of the URI (Java) or defaultDatabase=N in the connection string (.NET/.NET Framework). For example, db=1 or defaultDatabase=1 makes your installation write to database 1.

This approach separates each installation that shares the same Redis server—for example, Client A on database 0, Client B on database 1, Client C on database 2. As a result, you can clear one client's cache without affecting the others and avoid key collisions without using prefixes.

Note that there are only sixteen databases, there is no per-database access control, and Redis Cluster only supports database 0.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

The following are valid Cache Location values:

#### [**.NET / .NET Framework**](#.NET+%2F+.NET+Framework)

* Memcached  
  Cache Location = server1:11211 server2:11211
* Redis  
  Cache Location = defaultDatabase=1,localhost:6379

#### [**Java**](#Java)

* Memcached  
  Cache Location = server1:11211 server2:11211
* Redis  
    
  Cache Location = redis://clientid:password@localhost:6379?ssl=true&db=1  
  Uses port 6379, encrypts the connection (ssl=true), and stores the cache in logical database 1.  
    
  Cache Location = redis://clientid:password@localhost:6379/4  
  Points to port 6379  and writes to database 4.   
    
  Cache Location = rediss://localhost:6379  
  The rediss:// scheme enables SSL without ssl=true. It does not specify the database, so it connects to database 0.

Memcached uses port 11211 by default, and Redis uses 6379. Change them only if your servers use different ones.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [See Also](#See+Also)

[Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147)  
[Cache Username property](https://wiki.genexus.com/commwiki/wiki?31332)  
[Cache Password property](https://wiki.genexus.com/commwiki/wiki?31333)


|  |
| --- |
| **Backlinks** |
| [Cache Location property (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60180) | [Cache Password property](https://wiki.genexus.com/commwiki/wiki?31333) | [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147) |
| [Cache Username property](https://wiki.genexus.com/commwiki/wiki?31332) | [Distributed cache in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?28136) | [GeneXus 18 Upgrade 13](https://wiki.genexus.com/commwiki/wiki?59630) |

---
