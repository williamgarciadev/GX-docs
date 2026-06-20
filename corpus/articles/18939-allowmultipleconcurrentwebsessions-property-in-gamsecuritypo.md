---
title: "AllowMultipleConcurrentWebSessions property in GAMSecurityPolicy EO"
source_id: 18939
source_url: https://wiki.genexus.com/commwiki/wiki?18939
genexus_version: "18"
---

# AllowMultipleConcurrentWebSessions property in GAMSecurityPolicy EO

Determines whether users will be able to have multiple concurrent sessions or only one. When users can have multiple concurrent sessions, you may specify whether these sessions must be established from the same IP. This is checked when a user logs in.

### [Syntax](#Syntax)

*&GAMSecurityPolicy.***AllowMultipleConcurrentWebSessions***= GAMAllowMultipleConcurrentSessions.Value*

**Where:**

*&GAMSecurityPolicy*  Is a variable based on the GAMSecurityPolicy data type.

*GAMAllowMultipleConcurrentSessions.Value*  
   One of the possible values offered by the *GAMAllowMultipleConcurrentSessions*[domain](https://wiki.genexus.com/commwiki/wiki?7221).

**Values**

|  |  |  |
| --- | --- | --- |
| **Domain value to be used in the code** | **[GAM Web Backoffice](https://wiki.genexus.com/commwiki/wiki?15935)** | **Description** |
| GAMAllowMultipleConcurrentSessions.Unique | No | Multiple concurrent sessions are not allowed. If a session is created and another already exists, the first one is killed. |
| GAMAllowMultipleConcurrentSessions.Diferent\_IP | Yes | Multiple concurrent sessions are allowed. |
| GAMAllowMultipleConcurrentSessions.N\_Same\_IP | Yes, from the same IP | Multiple concurrent sessions are allowed, only from the same IP. |

### Description

This property allows determining whether users will be able to have multiple concurrent sessions or only one.

When users can have multiple concurrent sessions, you may specify whether these sessions must be established from the same IP. This is checked when a user logs in.

**Note**: When using the GAM Backoffice, this property is shown with the description "Allow Multiple Concurrent Web Sessions".

Consider that the property [UserSessionCacheTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18582) determines a delay for the destruction of the session when it is going to be destroyed (because another session was created from another IP, for example).

### [Samples](#Samples)

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&GAMAllowMultipleConcurrentSessions = GAMAllowMultipleConcurrentSessions.Diferent_IP
&GAMSecurityPolicy.AllowMultipleConcurrentWebSessions = &GAMAllowMultipleConcurrentSessions
```

The &GAMAllowMultipleConcurrentSessions variable is based on the GAMAllowMultipleConcurrentSessions [domain](https://wiki.genexus.com/commwiki/wiki?7221).

### [See Also](#See+Also)

[GAM Repository features and properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,)


|  |
| --- |
| **Backlinks** |
| [GAM - Security Policies](https://wiki.genexus.com/commwiki/wiki?18521) | [GAM - Security Policies (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58087) |
| [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) |

---
