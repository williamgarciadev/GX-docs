---
title: "Session Timeout property"
source_id: 54781
source_url: https://wiki.genexus.com/commwiki/wiki?54781
genexus_version: "18"
---

# Session Timeout property

Determines how long a session can remain active before automatically terminating it.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)  
**Level:** Generator

### [Description](#Description)

In the context of applications that are deployed across multiple nodes or containers, it is essential to manage session state in a distributed manner.

The Session Timeout property allows specifying an appropriate timeout value so that a balance between security and end user convenience can be achieved. In this way, it is possible to ensure that sessions do not remain active for an excessive period of time.

The Session Timeout is measured in minutes, with a default value of 20 minutes. When a session expires, the end user will be prompted to re-authenticate or log in again to continue their session.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at runtime.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute [Build any object](https://wiki.genexus.com/commwiki/wiki?17719) with the purpose of generating the \*.config files.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?54238).

### [See Also](#See+Also)

[HowTo: Configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626)


|  |
| --- |
| **Backlinks** |
| [HowTo: Configure Session State In ASP.NET Core](https://wiki.genexus.com/commwiki/wiki?50626) |

---
