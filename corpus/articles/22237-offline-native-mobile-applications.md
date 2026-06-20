---
title: "Offline Native Mobile applications"
source_id: 22237
source_url: https://wiki.genexus.com/commwiki/wiki?22237
genexus_version: "18"
---

# Offline Native Mobile applications

Offline Native Mobile applications are applications that can execute in scenarios of limited or without connection.

### [Why is this so important?](#Why+is+this+so+important%3F)

Because, even though there are many wifi hotspots and 3G connections, there are still places where the connectivity is limited or null, and some applications have to be able to get, insert, update or delete data on its own, without the intervention of a web server.

Even though offline applications can work on their own, it is very common for this kind of apps to be part of a bigger system. This is why this kind of applications is not thought to work on a completely isolated environment forever, at some point they are going to communicate with a server, at least to check if everything is ok. For this kind of application, for sure, a server counterpart is going to exist and the interaction with it is something the application needs to take care of.

### [Offline Knowledge](#Offline+Knowledge)

The key component of an offline application (and the main difference with Online Applications) is the local database and local processing of the business logic. This local database is a subset of this big system's database. This subset is an independent database where the Native Mobile application reads and writes data. This is different from an Online Native Mobile Application where all the application's data is received from the server in real-time.

Because of this, online applications cannot execute any action involving data when the connection is down or partially down: online applications may use a caché, but cannot insert or update data if the server cannot be reached.

### [Scenarios and architecture](#Scenarios+and+architecture)

Offline Applications, as described in many of the [Offline Native Mobile Applications Scenarios](https://wiki.genexus.com/commwiki/wiki?22507), will have a server backend they are going to communicate with. The architecture of the whole system is going to be very similar to the one explained on the [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221) document. The communication with this server is mainly to send/receive data, for this reason [the data synchronization](https://wiki.genexus.com/commwiki/wiki?22240) is a key concept on this kind of application.

### [See Also](#See+Also)

[Offline Native Mobile Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262)


|  |
| --- |
| **Backlinks** |
| [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) | [Coding your Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266) | [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) |
| [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223) | [HowTo: Augmented Reality in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?42590) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) |
| [Manual Synchronization Code Sample](https://wiki.genexus.com/commwiki/wiki?22543) | [Minimum Time Between Receives property](https://wiki.genexus.com/commwiki/wiki?22224) | [Minimum Time Between Table Purges property](https://wiki.genexus.com/commwiki/wiki?31160) | [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) |
| [Network external object](https://wiki.genexus.com/commwiki/wiki?31310) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221) | [Offline Native Mobile Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262) |
| [Offline Native Mobile Applications Requirements](https://wiki.genexus.com/commwiki/wiki?22259) | [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) |

---
