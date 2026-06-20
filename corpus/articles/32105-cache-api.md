---
title: "Cache API"
source_id: 32105
source_url: https://wiki.genexus.com/commwiki/wiki?32105
genexus_version: "18"
---

# Cache API

Applications often have a set of data that is accessed globally; i.e. data that is the same for any user, which is the result of an initialization process. Once calculated, it is useful to have this data accessible and updated only when the application requires it.

A possible use scenario is one in which the data does not change too often (it can be obtained from the database or by calling a service), and accessing the database or retrieving the data by calling a web service is too expensive.

The Web Session could be a solution, but it is defined for each user of the application. On the contrary, the Cache API is defined and accessible for all the users of the application.

The Cache API allows storing global data of an application, access the data and invalidate it when necessary. The Cache can be local to the application server, or it can be a [distributed cache](https://wiki.genexus.com/commwiki/wiki?28136) depending on the [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147).

## [How to use the Server Cache API](#How+to+use+the+Server+Cache+API)

Cache is a data type and it exposes different methods to manage the application server or the distributed cache. Below are the methods exposed:

|  |  |
| --- | --- |
| [Method name](#Method+name) | [Description](#Description) |
| **Server Cache static methods** | |
| Cache.GetCache(Character:Name): Cache | Retrieves a cache instance or creates a new one if it does not exist. |
| Cache.ClearAllCaches() | Clears all the caches, both the ones created by the user and the others (the Smart Devices cache and the Database Cache (\*)). |
| **Server Cache non static methods** |  |
| &Cache.Set(Character: Key, Character: Value, [Numeric: DurationMinutes]) | Stores the value in the cache under the specified key. If the duration value is 0 (the default), the item never expires (although it may be deleted from the server to make room for other items).  The function can be called in two ways:   ``` &Cache.Set("key", "value", 1) &Cache.Set("key", "value") ```   In the second case, the duration will be set to the default value 0 and the item won't expire. |
| &Cache.Get(Character:Key): Character | If the item is found it returns the item that was previously stored under the key. Otherwise, an empty string is returned. |
| &Cache.Contains(Character:Key): Boolean | If the item is found it returns true; otherwise, false is returned. |
| &Cache.Remove(Character:Key) | Removes an item from the cache. |
| &Cache.Clear() | Clears the cache, removing all the items from it. |

### [Example](#Example)

Consider an application which shows the value of the currency.

```
&CacheName = "CurrencyValueCache"  
&Cache=Cache.GetCache(&CacheName)  //&Cache is Cache data type

if(&Cache.Contains("Dollar"))
    &Value=&Cache.Get("Dollar")
else
    //Here call a service which returns the currency value and loads the &value variable.
    &Cache.Set("Dollar",&value,&expTime)
endif
```

## [(\*)Smart devices and database Cache API](#%28*%29Smart+devices+and+database+Cache+API)

In GeneXus, there is a caching mechanism, explained in detail in [Caching in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?28166,,). For the [Native Mobile caching](https://wiki.genexus.com/commwiki/wiki?18602) as well as the [ResultSet caching](https://wiki.genexus.com/commwiki/wiki?28167,,) there are also some useful methods to manage the cache expiration.

In some cases, it may be necessary to forcefully clear the cache (for example, if you need the SQL query to be re-executed and not to retrieve the data from the database cache). This is especially useful when using any [distributed cache](https://wiki.genexus.com/commwiki/wiki?28136) mechanism.

In order to reset the cache, you can use the *Cache.SmartDevices.Clear* method and the *Cache.Database.**Clear* method for SD and ResultSet caching respectively.

|  |  |
| --- | --- |
| [Method name](#Method+name) | [Description](#Description) |
| **SmartDevices** | |
| Cache.SmartDevices.Clear() | Clears the smart devices cache, removing all the items from it. |
| Cache.SmartDevices.Remove(Character:Key) | Removes the SD cache of the indicated Key. The Key is a table name.  e.g: Cache.SmartDevices.Remove(&TableName) |
| **Database** | |
| Cache.Database.Clear() | Clears the database cache, removing all the items from it. |

### [Example](#Example)

### [Clearing the database cache](#Clearing+the+database+cache)

```
Cache.Database.Clear()
```

Download the sample from [Cache API sample](https://wiki.genexus.com/commwiki/wiki?32113,,).

Keyword : global session


|  |
| --- |
| **Backlinks** |
| [Cache Provider property](https://wiki.genexus.com/commwiki/wiki?31147) | [Clear method](https://wiki.genexus.com/commwiki/wiki?7084) |
| [Distributed cache in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?28136) | [Native Mobile caching](https://wiki.genexus.com/commwiki/wiki?18602) |

---
