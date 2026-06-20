---
title: "Native Mobile caching"
source_id: 18602
source_url: https://wiki.genexus.com/commwiki/wiki?18602
genexus_version: "18"
---

# Native Mobile caching

There are several scenarios that call for offline storing (from now on referred to as “caching”) in an application generated for Native Mobile.

Below is a detailed description of some of these scenarios.

### [Scenario 1: Query Cache](#Scenario+1%3A+Query+Cache)

The idea is to avoid data traffic between the client and the server when data on the server remains unchanged. This is the most basic case you want to solve: that is: in a fully online application, repeated queries to the server should be avoided.

Avoiding unnecessary network traffic is desirable because it implies savings, mainly in:

* bandwidth use (particularly in the use of telephone networks instead of Wi-fi)
* the device’s consumption of energy (cordless communications, data de-serialization)
* web server load.

In order to solve this, for a query made from the Native Mobile application, you must know if the data involved has been modified since it was last used.

### [Scenario 2: Offline application (read-only)](#Scenario+2%3A+Offline+application+%28read-only%29)

This is an extension of the case described above, assuming that there's no connectivity. The basic idea is that, with a cache like the one described above— where it will not be necessary to go to the server if the queried data has not been changed— when there is no connectivity, it will be possible to browse the sections of the application already visited using the data stored in the device.

### [Implementation of the solution](#Implementation+of+the+solution)

To solve the two scenarios described above, you will need two things:

* Storage in a local database.

The data returned by the server must be stored on a database to avoid over-consumption of memory and to survive the closing of the application. Since the result of the server queries is what should be stored, the data model for this base would be a "table for each [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)" and not the GeneXus normalized data model.

The database used for this purpose is [SQLite](https://www.sqlite.org/), which is included in all devices.

* A mechanism for determining whether the data has changed on the server.

When the client makes a query to the server, it also sends, together with the query, the timestamp of the last reply (that is to say, the time when the query was last made).

The server must control whether any of the tables involved in the query has changed since then, in order to define what must be returned. It can be either a new result when the last query made by the client is older than the data update (that is, when the tables associated with the query have been modified) or a message indicating that the client's data continues to be valid, in which case the client shows the cached result. In this last case, it returns a special reply (HTTP 304).

On the server, in order to determine whether the client data is still valid, two elements become necessary (these are the elements stored in the server cache):

1. A list of tables.
2. The timestamp of the tables' last modification.

Therefore, the cache of Native Mobile applications will always include the data needed to know whether it is possible to use the cache or if the query must be made once again.

The server cache is updated when there is an insert or update in any record of a table.  
The table update can be performed using any GeneXus object (it doesn't need to be a Rest Procedure). In fact, if the KB has two generators (web and Native Mobile) when a web-generated object updates a table, the Native Mobile cache is updated as well. The web generator checks the [Smart Devices Cache Management property](https://wiki.genexus.com/commwiki/wiki?18370) of the Native Mobile generator.

The only exception is when a table in the system’s database is updated outside the applications developed with GeneXus.

### [How to activate the Native Mobile caching](#How+to+activate+the+Native+Mobile+caching)

First, you need to activate the [Smart Devices Cache Management property](https://wiki.genexus.com/commwiki/wiki?18370), and the [Enable Data Caching property](https://wiki.genexus.com/commwiki/wiki?18302) for each object for which the cache is going to be used.

When the Enable Data Caching object property is True, the [Check For New Data property](https://wiki.genexus.com/commwiki/wiki?18322) is enabled, as well as the [Check For New Data After Minutes Elapsed property](https://wiki.genexus.com/commwiki/wiki?18329).

### [Disabling the cache](#Disabling+the+cache)

In some scenarios, you specifically need to disable the cache. For example, when having to force the application to refresh the device’s form, or when the data has been changed from an application other than GeneXus, among other possibilities.

Consider the following case:

Upon a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) whose form shows a variable and attributes of the database, in an action of the panel a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) is called, and a refresh is done after the return. During the refresh operation, the variable on the form is loaded with the contents of the web session modified in the Procedure.

The events of the Panel will be as follows:

```
Event ‘CallProc’
   Composite
      ModifyWebSession.Call()
      refresh
   EndComposite
EndEvent

Event Refresh
   &FormVar =&websession.get(‘Sample’)
Endevent
```

If the Procedure ModifyWebSession simply does the following:

```
&websession.set(‘Sample’, &time)
```

Then, upon returning to the [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), the &FormVar variable on the panel will never be viewed as modified (unless the attributes present on the form have actually been modified). The reason is that, after running the query to the database, the Panel will receive a reply indicating that the data has not been modified. As a result, the refresh will not be executed, and consequently, no changes will be viewed in the &FormVar variable.

In order to solve this situation, a way of programmatically invalidating the cache has been implemented. Therefore, regardless if the data has been changed, the query to the database will be made anyway (as if the data had been subject to changes).

This was implemented as an external object, imported when theNative Mobile generator is used (the same as with all external objects that are automatically consolidated within the SmartDevicesApi folder). This class is called ServerAPI and contains the InvalidateCache method.

Therefore, the ModifyWebSession Procedure in the above example should use it in order to invalidate the cache, and upon returning to the Panel, the data should be deemed changed, and the query should be made again (with the corresponding refresh). The Procedure would then be the following:

```
&websession.set(‘Sample’, &time)
ServerAPI.InvalidateCache()
```

For [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?27605,,) see [Cache API](https://wiki.genexus.com/commwiki/wiki?32105) and the Cache.SmartDevices.Clear() method.

### [See Also](#See+Also)

[Caching in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?28166,,)  
[Cache API](https://wiki.genexus.com/commwiki/wiki?32105)


|  |
| --- |
| **Backlinks** |
| [Cache API](https://wiki.genexus.com/commwiki/wiki?32105) | [Check For New Data After Minutes Elapsed property](https://wiki.genexus.com/commwiki/wiki?18329) |
| [Check For New Data property](https://wiki.genexus.com/commwiki/wiki?18322) | [Distributed cache in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?28136) | [Enable Data Caching property](https://wiki.genexus.com/commwiki/wiki?18302) | [Event Triggering Order in Panels](https://wiki.genexus.com/commwiki/wiki?17614) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Server-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24234) | [Smart Devices Cache Management property](https://wiki.genexus.com/commwiki/wiki?18370) |
| [Video data type](https://wiki.genexus.com/commwiki/wiki?16608) | [Video data type (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53910) |

---
