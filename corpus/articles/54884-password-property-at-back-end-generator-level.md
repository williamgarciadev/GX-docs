---
title: "Password property at Back end Generator level"
source_id: 54884
source_url: https://wiki.genexus.com/commwiki/wiki?54884
genexus_version: "18"
---

# Password property at Back end Generator level

Sets the authentication password required when connecting to a Redis provider.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** Generator

### [Description](#Description)

When using Redis as a [Session State Provider](https://wiki.genexus.com/commwiki/wiki?54782), a password may be required to authenticate and access the Redis server.

By correctly setting the "Password" property, the application will be able to connect to the password-protected Redis server and use it to securely store and retrieve session data.

It is important to note that this property is part of the broader configuration related to session state management, which includes other properties such as [Location](https://wiki.genexus.com/commwiki/wiki?54883) and [Instance Name](https://wiki.genexus.com/commwiki/wiki?54780), among others. These properties are necessary to establish the proper connection and communication with the Redis server to manage application session state in distributed or container-based environments.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).

### [See Also](#See+Also)

[HowTo: Configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626)


|  |
| --- |
| **Backlinks** |
| [HowTo: Configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626) |

---
