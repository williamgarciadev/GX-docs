---
title: "Distributed cache in GeneXus applications"
source_id: 28136
source_url: https://wiki.genexus.com/commwiki/wiki?28136
genexus_version: "18"
---

# Distributed cache in GeneXus applications

GeneXus allows retrieving data from the in-memory cache to both web (1) and smart device applications (2); but what happens if the application runs in a distributed environment, or in the cloud?  
In a distributed environment, the local cache of the application server is useless. In this case, you need a distributed memory object caching system to guarantee the validity of the cached information.

The solution in this scenario (mostly applications that run on the cloud or in a clustered environment) is to use a distributed cache.

## [GeneXus implementation for distributed caching](#GeneXus+implementation+for+distributed+caching)

For distributed environments, the GeneXus application can be configured at runtime to use [Redis](http://redis.io/) or [Memcached](http://memcached.org/) for [ResultSet caching in GeneXus](https://wiki.genexus.com/commwiki/wiki?28167,,) and [Smart Devices caching](https://wiki.genexus.com/commwiki/wiki?18602) as well.

See [Distributed Resultset caching in GeneXus](https://wiki.genexus.com/commwiki/wiki?28163,,) and [Smart Devices distributed Caching](https://wiki.genexus.com/commwiki/wiki?28156,,) to understand the cache behavior.

## [How to configure distributed caching in GeneXus](#How+to+configure+distributed+caching+in+GeneXus)

First of all, configure caching in GeneXus. It's the same as configuring the server local cache (1)(2).

The way to configure distributed caching is through the [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147).

Note: The cache is an in-memory key-value store where the key-value pair depends on the application platform. For SD applications, the key corresponds to the database table, and the value is the table modification timestamp. For web and web services, the key corresponds to the query with its parameters and the value is the resultset of the query.

### [Server and client configuration](#Server+and+client+configuration)

On the server, any implementation of Memcached or Redis has to be installed. For example, [AWS ElastiCache](http://aws.amazon.com/elasticache/).

In the client machine, the corresponding API implementation has to be referenced in the classpath for Java or included in the bin directory of the web application for Csharp.

### [Examples](#Examples)

#### [1. Using Csharp and Memcached](#1.+Using+Csharp+and+Memcached)

First, check that the [BeITMemcached](https://code.google.com/archive/p/spymemcached/) client DLLs have been copied to the bin directory.

Additionally, download the [Memcached for Windows](http://s3.amazonaws.com/downloads.northscale.com/memcached-win64-1.4.4-14.zip) server.

Configure the [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147), the [Cache Location Property](https://wiki.genexus.com/commwiki/wiki?31331,,), (and the [Cache UserName Property](https://wiki.genexus.com/commwiki/wiki?31332,,) and [Cache Password Property](https://wiki.genexus.com/commwiki/wiki?31333) if necessary).

#### [2. Using Csharp and Redis](#2.+Using+Csharp+and+Redis)

Download the [Redis](https://github.com/rgl/redis/downloads) server and install it as a service on Windows.

The [ServiceStack](https://github.com/ServiceStack/ServiceStack.Redis) client is used in this case.

Configure the [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147), the [Cache Location Property](https://wiki.genexus.com/commwiki/wiki?31331,,), (and the [Cache UserName Property](https://wiki.genexus.com/commwiki/wiki?31332,,) and [Cache Password Property](https://wiki.genexus.com/commwiki/wiki?31333) if necessary).

Licensing Notice: Refer to [SAC 40283](https://www.genexus.com/developers/websac?es,,,40283).

#### [3. Using Java and Memcached](#3.+Using+Java+and+Memcached)

Download the spymemcached-2.10.3.jar - [spy memcached](https://code.google.com/archive/p/spymemcached/) jar file - and copy it to the lib directory under the web app.

## [How to invalidate the distributed caching](#How+to+invalidate+the+distributed+caching)

You can do it programmatically. See [Cache API](https://wiki.genexus.com/commwiki/wiki?32105).

### [NOTE:](#NOTE%3A)

For the time being, the feature is supported in these combinations:

* JAVA - Memcached - authentication supported
* .NET - Memcached - authentication not supported
* .NET - Redis - authentication supported

### [See Also](#See+Also)

(1) [Database access caching property](https://wiki.genexus.com/commwiki/wiki?8968)  
(2) [Native Mobile caching](https://wiki.genexus.com/commwiki/wiki?18602)  
(3) [Smart Devices distributed Caching](https://wiki.genexus.com/commwiki/wiki?28156,,)  
(4) [Distributed Resultset caching in GeneXus](https://wiki.genexus.com/commwiki/wiki?28163,,)  
(5) [Cache API](https://wiki.genexus.com/commwiki/wiki?32105)


|  |
| --- |
| **Backlinks** |
| [Cache API](https://wiki.genexus.com/commwiki/wiki?32105) | [Cache Password Property](https://wiki.genexus.com/commwiki/wiki?31333) |
|
| [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) |

---
