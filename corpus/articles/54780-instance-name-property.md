---
title: "Instance Name property"
source_id: 54780
source_url: https://wiki.genexus.com/commwiki/wiki?54780
genexus_version: "18"
---

# Instance Name property

Specifies the name of the instance used to connect to a distributed Redis provider.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** Generator

### [Description](#Description)

It is common to have multiple applications using a single Redis server, so it is necessary to assign an arbitrary and unique name to each application to differentiate them from each other. This ensures that each has its own session storage space on the Redis server and avoids conflicts between sessions of different applications.

Therefore, if there are multiple applications connecting to the same Redis, it is necessary to enter an arbitrary name in this property. However, if you have only one application connecting to the Redis server, you can leave the property empty or enter an optional name to identify it.

To store the web session in Redis with multi-tenant support, you can set the **Instance Name** property to **%SUBDOMAIN%**. This makes the instance name dynamic, taking the value of the application's subdomain. It is intended for multi-tenant applications, where the same application is accessed through different URLs, and you want the values stored in Redis to remain isolated between tenants.

For example, if the multi-tenant application is accessed from the following domains:

http://a.com.uy/app/home  
http://b.com.uy/app/home  
http://c.com.uy/app/home

The sessions from a.com.uy will be stored under the "a" namespace in Redis, b.com.uy under "b", and c.com.uy under "c". Internally, this namespace is used as a prefix in the Redis keys, ensuring isolation between sessions from different tenants.

**Note**: You must select the "Redis" value in the [Session State Provider property](https://wiki.genexus.com/commwiki/wiki?54782) in order to specify the Instance Name property.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at runtime.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [See Also](#See+Also)

[HowTo: Configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626)


|  |
| --- |
| **Backlinks** |
| [HowTo: Configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626) | [Instance Name property (GeneXus 18 Upgrade 13 or prior)](https://wiki.genexus.com/commwiki/wiki?61040) | [Password property at Back end Generator level](https://wiki.genexus.com/commwiki/wiki?54884) |

---
