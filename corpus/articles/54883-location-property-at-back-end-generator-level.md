---
title: "Location property at Back end Generator level"
source_id: 54883
source_url: https://wiki.genexus.com/commwiki/wiki?54883
genexus_version: "18"
---

# Location property at Back end Generator level

Specifies the address of the Redis server to which applications should connect to store and retrieve web session data.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** Generator

### [Description](#Description)

The host name and port number must be included. You can also include multiple servers and additional configurations, such as:

"redis0:6380,redis1:6380,ssl=true"

That is, it may contain a comma-separated list of multiple servers, indicating a high availability or scalability configuration for session storage. In addition, it can have additional settings, such as indicating whether SSL is used for the connection.

You must select the "Redis" value in the [Session State Provider property](https://wiki.genexus.com/commwiki/wiki?54782) in order to specify the Location property.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build any object.

### [See Also](#See+Also)

[How to configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626)


|  |
| --- |
| **Backlinks** |
| [HowTo: Configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626) | [Password property at Back end Generator level](https://wiki.genexus.com/commwiki/wiki?54884) |

---
