---
title: "UserSessionCacheTimeout property in GAMRepository EO"
source_id: 18582
source_url: https://wiki.genexus.com/commwiki/wiki?18582
genexus_version: "18"
---

# UserSessionCacheTimeout property in GAMRepository EO

Establishes a time during which the user data associated with a particular session is managed in the server memory (and in the user's web session). As a result, the database is not accessed for this purpose.

### [Syntax](#Syntax)

*&GAMRepository*.***UserSessionCacheTimeout***= *Number\_Seconds*

**Where:**

*&GAMRepository*  
    Is a variable based on the GAMRepository data type.

*Number\_Seconds*  
    Number of seconds during which the user data associated with a particular session is managed in the server memory (and in the user's web session). As a result, the database is not accessed for this purpose.

### [Description](#Description)

To increase performance, the time specified in this property implies that during this period the GAM application does not need to query the database to check the user session.

Every time the application queries the database to get information on the user session, the time is reset. Therefore, while the User Session Cache Timeout does not expire, the user information is retrieved from the web session if possible. When the time expires, and the user session is needed, the information is retrieved from the database and the cache is reloaded.

The cache is reset when the user logs out and logs in again.

The information cached is that of the GAMSession external object; it belongs to a specific user and so it is stored in the web session.

`[imagen omitida: wiki id 36408]`

**Note**: When using the GAM Backoffice, the UserSessionCacheTimeout property can be configured by selecting **Repository > Configuration > General Security Policy**. It is shown with the description "User Session Cache Timeout (seconds)".

### [Samples](#Samples)

To set this property in the GeneXus code (by using the [GAM API](https://wiki.genexus.com/commwiki/wiki?16535)), the syntax is as follows:

```
&Repository.UserSessionCacheTimeout = &UserSessionCacheTimeout
```

The GAMRepositoryConfiguration [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) is an example of where this property is used.

### [See Also](#See+Also)

[GAM Repository features and properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,)  
[CacheTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?21863)


|  |
| --- |
| **Backlinks** |
| [AllowMultipleConcurrentWebSessions property in GAMSecurityPolicy EO](https://wiki.genexus.com/commwiki/wiki?18939) | [CacheTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?21863) | [GAM - Cache Management](https://wiki.genexus.com/commwiki/wiki?58220) |
| [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) |

---
