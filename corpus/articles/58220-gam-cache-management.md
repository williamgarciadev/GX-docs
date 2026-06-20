---
title: "GAM - Cache Management"
source_id: 58220
source_url: https://wiki.genexus.com/commwiki/wiki?58220
genexus_version: "18"
---

# GAM - Cache Management

This document describes the different cache types used by [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), both for Web and Native Mobile applications.

GAM uses three cache types to reduce database access:

1. Take into account the generator's [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147) (GAM considers this property since GeneXus 17 Upgrade 2). By default, this property is set to use a Local cache (per virtual directory). If the cache is recycled in a virtual directory (web apps), the other virtual directories will not be affected. You can set this property to an external cache, such as [Redis](https://redis.io/) or [Memcached](http://memcached.org/).  
     
   GAM uses this cache to optimize the database queries of the most used entities: Repositories, Applications, Authentication Types, Event Subscription; for Authorization, the calculation of an access permission is cached. When GAM updates something related to this cache, it recycles all that is necessary.  
     

   **Note**: GAM generates cache based on the combination of user roles and permissions. This means that if several users share the same combination, an individual cache will not be created for each one, but one for each distinct combination. In practice, it is common for most users to belong to the same groups, which avoids overloading the system.

   You can force the cleaning of this cache using the **GAMRepository.ClearCache()** method in each virtual directory where it is executed.

   Configuring a maximum expiration time for this type of cache is also possible through the [CacheTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?21863). Using the GAM Backoffice, it can be configured by selecting **Repository > Configuration > General** and, finally, completing the **Cache timeout (minutes)**.

   `[imagen omitida: wiki id 58221]`

   The above image shows an example in which the cache of all virtual directories and/or servers will expire every 60 minutes.
2. GAM also uses caching at the table SQL statements level. For this, you have to set the generator [Database access caching property](https://wiki.genexus.com/commwiki/wiki?8968) = Yes, and configure the [Change frequency property](https://wiki.genexus.com/commwiki/wiki?7156) for each table.  
     
   In particular, GAM sets the [Change frequency property](https://wiki.genexus.com/commwiki/wiki?7156) to:  

   |  |  |
   | --- | --- |
   | **Value** | **Tables** |
   | 'Hardly Ever' | Application, Authentication Type, Repository, Security Policy |
   | 'Time to Time' | Role |

     
   When GAM updates something related to this cache, it does NOT recycle anything.
3. In turn, the application token is cached in the web session of the authenticated user, who can configure the validity timeout of this cache and avoid the web session to be validated against the database.

   This cache is configured through the [UserSessionCacheTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18582).

   In the example below, the web session will be validated every 60 seconds. This implies that if the user's Roles or Permissions are updated, they will not see it for that configured period.  
     
   Using the GAM Backoffice, the property can be configured by selecting **Repository** **> Configuration > General Security Policy**.It is shown with the description "User session cache timeout (seconds)".  
     
   `[imagen omitida: wiki id 58222]`


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
