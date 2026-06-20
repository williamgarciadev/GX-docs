---
title: "Deploy Java application to Docker and Kubernetes using Redis"
source_id: 57627
source_url: https://wiki.genexus.com/commwiki/wiki?57627
genexus_version: "18"
---

# Deploy Java application to Docker and Kubernetes using Redis

To set up a Java application to be deployed in a Kubernetes cluster, you may use the deployment tool as explained in [HowTo: Deploy an Application to a Kubernetes cluster](https://wiki.genexus.com/commwiki/wiki?45416).

This document provides some details on having Redis support for that cluster.

If you want, GeneXus deploys an additional container with a [Redis](https://wiki.genexus.com/commwiki/wiki?45467,,) server. This allows the application to save the session on that Redis server, so if you don't have server affinity or if one of your nodes (or pods) goes down, your clients can reach a new node without losing their session.

The property you should set is *Enable Redis Management,* as shown in the figure below.

`[imagen omitida: wiki id 57629]`

In the case of Java, the session manager used is [Redisson](https://github.com/redisson/redisson).

### [Considerations](#Considerations)

1. Take a look at the <deployment path>\DOCKER\context\redis folder.  
There you have some files that are copied from <GeneXus installation>\DeploymentTargets\Docker\java\redis

* context.xml  
  RedissonSessionManager configuration.
* redis-data-cache.properties  
  Redis settings.
* redisson.yaml  
  Configuration of Redis server connection.
* web.xml  
  It has the session-timeout configuration and is copied to the global configuration.

All of them can be edited at their source (in the DeploymentTargets folder) and changed as you need.

2. Depending on the [Tomcat version property](https://wiki.genexus.com/commwiki/wiki?48352) of the Java Generator, the deployment tools download the required Redisson dependencies. The Jar dependencies are copied to <deployment path>\DOCKER\context\tomcat\lib, and they are as follows:

* redisson-all-<Latest>.jar
* redisson-tomcat-<Ver>.jar  
  Where Ver depends on the Tomcat Version and the Reddison version.  
    
  **Limitation:** In the case of Tomcat 8, it is a known issue that the redisson-tomcat<ver>.jar distributed is the one of Tomcat 9. This is because Tomcat Version in GeneXus does not enable to distinguish between 8 and 9.   
  You can download the jar (https://mvnrepository.com/artifact/org.redisson/redisson-tomcat-8/3.27.2) and replace it in <deployment path>\DOCKER\context\redis folder.

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243)

**Note:**

During the deployment, you need an internet connection because the dependencies are downloaded from Maven central using Gradle.

**Important:**  
All the deployment target solutions are extensible and available at [github](https://github.com/genexuslabs/deployment-targets/tree/master).


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) |

---
