---
title: "Instance Name property (GeneXus 18 Upgrade 13 or prior)"
source_id: 61040
source_url: https://wiki.genexus.com/commwiki/wiki?61040
genexus_version: "18"
---

# Instance Name property (GeneXus 18 Upgrade 13 or prior)

Specifies the name of the instance used to connect to a distributed Redis provider.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** Generator

### [Description](#Description)

It is common to have multiple applications using a single Redis server, so it is necessary to assign an arbitrary and unique name to each application to differentiate them from each other. This ensures that each has its own session storage space on the Redis server and avoids conflicts between sessions of different applications.

Therefore, if there are multiple applications connecting to the same Redis, it is necessary to enter an arbitrary name in this property. However, if you have only one application connecting to the Redis server, you can leave the property empty or enter an optional name to identify it.

You must select the "Redis" value in the [Session State Provider property](https://wiki.genexus.com/commwiki/wiki?54782) in order to specify the Instance Name property.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at runtime.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).

### [See Also](#See+Also)

[HowTo: Configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626)
