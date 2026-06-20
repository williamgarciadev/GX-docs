---
title: "Session Expires On IP Change property"
source_id: 18925
source_url: https://wiki.genexus.com/commwiki/wiki?18925
genexus_version: "18"
---

# Session Expires On IP Change property

The value of this property controls whether a GAM session is kept or discarded when a change to the original IP (the IP of the machine a user logs in) occurs. Discarding (or invalidating) the GAM Session when a change to the IP is detected increases security, as it is a signal that the machine has changed location. It may have been stolen or just moved to another network and be accessible to unauthorized users.

Note that a change in a machine IP does not necessarily mean its location was changed. Machines connected to the Internet, for example, do change their IP as part of the normal process.

This is a [repository](https://wiki.genexus.com/commwiki/wiki?17568) property that can be configured using [GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935).

### [Values](#Values)

|  |  |
| --- | --- |
| **False** | If a user logs in from a machine and the machine changes its IP in the meantime (while the session is active), the session will still be valid, so the user will remain logged in. This is the default value. |
| **True** | If a user logs in from a machine and the machine changes its IP in the meantime (while the session is active), the user will be logged out if "Keep Session from original IP" is set to TRUE. |

### [Example](#Example)

It can be set by coding the following (using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)):

```
&Repository.SessionExpiresOnIPChange = &SessionExpiresOnIPChange (GAMBoolean data type)
```

The GAMRepositoryConfiguration web panel (located in GAM Example folder) is an example where this property is used.

### [See Also](#See+Also)

[GAM Repository features and properties](https://wiki.genexus.com/commwiki/wiki?18463,,)


|  |
| --- |
| **Backlinks** |
| [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) |

---
