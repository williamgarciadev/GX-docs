---
title: "Cache Location property (GeneXus 18 Upgrade 12 or prior)"
source_id: 60180
source_url: https://wiki.genexus.com/commwiki/wiki?60180
genexus_version: "18"
---

# Cache Location property (GeneXus 18 Upgrade 12 or prior)

Configures the location of the Distributed Cache server. You must specify space-separated host:port pairs for Memcached, a comma-separated host:port list for Redis on .NET or .NET Framework, or a complete Redis URI for Redis on Java (i.e. redis://clientid:password@localhost:6379?ssl=true&db=1).

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** Generator

### [Description](#Description)

In a [distributed caching](https://wiki.genexus.com/commwiki/wiki?28136) environment, the **Cache Location property** allows configuring the server and port where the Cache system is operating.

Therefore, after configuring the [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147) to 'Redis' or 'Memcached', the **Cache Location property** will be available to enter any valid location depending on the distributed caching system specified in the [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147).

If more than one location has to be specified, the locations should be separated by empty spaces.

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

  **Note**: The cache must always target logical database 1. Keep db=1 unchanged.

Memcached uses port 11211 by default, and Redis uses 6379. Change them only if your servers use different ones.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [See Also](#See+Also)

[Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147)  
[Cache Username property](https://wiki.genexus.com/commwiki/wiki?31332)  
[Cache Password property](https://wiki.genexus.com/commwiki/wiki?31333)
