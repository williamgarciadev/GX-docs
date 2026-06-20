---
title: "CacheTimeout property in GAMRepository EO"
source_id: 21863
source_url: https://wiki.genexus.com/commwiki/wiki?21863
genexus_version: "18"
---

# CacheTimeout property in GAMRepository EO

Sets the GAM Repository cache timeout. Its default value is zero, indicating that the cache never expires. The purpose of this property is to avoid querying the database every time the repository information is needed.

### [Syntax](#Syntax)

*&GAMRepository*.**CacheTimeout** = *&RepositoryCacheTimeout*

**Where:**

*&GAMRepository*  
   Is a variable base on the GAMRepository data type.

*&RepositoryCacheTimeout*Timeout in minutes.

### [Description](#Description)

The timeout of the [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) cache, which stores information of the [Repository](https://wiki.genexus.com/commwiki/wiki?17568), [Applications](https://wiki.genexus.com/commwiki/wiki?15910), [Permissions](https://wiki.genexus.com/commwiki/wiki?15912) and [Events subscription](https://wiki.genexus.com/commwiki/wiki?32698) data, is configured in the application server to improve performance. In this way, there's no need to query the database every time the information is needed. While the Cache does not expire, the information is managed in the server memory.

The information stored in cache is as follows:

* Repository data, for example, UserIdentification (name, email, or both).
* Repository Authentication Types data.
* The connection.gam file information.
* Applications data (the general information, Client Application Data, Remote Authentication and Environment Settings)
* Permissions of the applications in the repository.
* Role Permissions of each application in the repository.
* User Permissions of each application in the repository.
* EventSubscriptions data.

The purpose of this property is to avoid querying the database every time the repository information is needed.

Its default value is zero, indicating that the GAM cache never expires.

The cache information is reset every time the data is updated. For example, if a permission is associated with a role, this cache information is automatically updated. So, the information retrieved is always updated.

In load balancing architectures, you should set the [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147) to use a distributed caching.

**Note**: Previous to GeneXus 17 upgrade 2, it's necessary to adjust the Cache Timeout property so that all the nodes have coherence in the information used for the repository because distributed caching is not supported in GAM. If you need to change any repository settings in a clustered environment, you may need to clean the cache for the changes to take effect in all nodes.

When the following lines of code are executed, the Repository cache is forced to clear:

```
&Repository.Load(&Id) //&Repository is based on the GAMRepository data type. The current Repository is loaded.
&Repository.Save()
if &Repository.Success()
  Commit
endif
```

When the Repository settings are changed, using [GAM API](https://wiki.genexus.com/commwiki/wiki?16535) or just using the [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993) of [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935), the Repository cache of the web server is cleared. Consider that you need to update the repository settings in all the nodes of the cluster.

Use the **ClearCache method** of the GAMRepository object to force the cache clear in every web app where you run the code. Since GeneXus 15 upgrade 7, this method clears all the cache (not only the repository cache).

```
GAMRepository.GetId(&Id)
&Repository.load(&Id)
&Repository.ClearCache()
```

### [See Also](#See+Also)

[UserSessionCacheTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18582)  
[GAM Repository features and properties](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?18463,,)


|  |
| --- |
| **Backlinks** |
| [GAM - Cache Management](https://wiki.genexus.com/commwiki/wiki?58220) | [Going into production: checklist for Applications using GAM](https://wiki.genexus.com/commwiki/wiki?18574) | [UserSessionCacheTimeout property in GAMRepository EO](https://wiki.genexus.com/commwiki/wiki?18582) |

---
