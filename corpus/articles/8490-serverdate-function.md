---
title: "ServerDate function"
source_id: 8490
source_url: https://wiki.genexus.com/commwiki/wiki?8490
genexus_version: "18"
---

# ServerDate function

Returns a date from a unified source (common to all clients).

### [Syntax](#Syntax)

**ServerDate()**

**Type Returned:**  
Date

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

The [Today function](https://wiki.genexus.com/commwiki/wiki?8334) returns the date where the code is running. [Environments](https://wiki.genexus.com/commwiki/wiki?7115) where there are "clients" (Web or Native Mobile applications) and "servers" (the Database or Application server) execute code on either side. Clients may not be synchronized, for example, leading to unsequenced date values.

The ServerDate function is intended to solve the problem by always returning the date of a given source. Usually, the source is the DBMS (date of the server your DBMS is running) but may be a Web Application Server too, depending on the implementation.

**Note:** The following warning is displayed when using the function in a [Panel](https://wiki.genexus.com/commwiki/wiki?24829) with the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) = Offline.

```
warning: spc0210: 'ServerDate()' not supported, using 'Date()' function instead.
```

### [See Also](#See+Also)

[TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019)  
[ServerNow function](https://wiki.genexus.com/commwiki/wiki?8491)  
[ServerTime function](https://wiki.genexus.com/commwiki/wiki?8492)  
[Sysdate function](https://wiki.genexus.com/commwiki/wiki?8493)  
[Systime function](https://wiki.genexus.com/commwiki/wiki?8494)  
[Today function](https://wiki.genexus.com/commwiki/wiki?8334)  
[GxRemove variable](https://wiki.genexus.com/commwiki/wiki?8495)


|  |
| --- |
| **Backlinks** |
| [Dynamic Transactions Samples](https://wiki.genexus.com/commwiki/wiki?36273) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [ServerNow function](https://wiki.genexus.com/commwiki/wiki?8491) |
| [ServerTime function](https://wiki.genexus.com/commwiki/wiki?8492) | [TimeZone Support - General Considerations](https://wiki.genexus.com/commwiki/wiki?22019) |

---
