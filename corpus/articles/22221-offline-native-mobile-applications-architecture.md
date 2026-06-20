---
title: "Offline Native Mobile applications architecture"
source_id: 22221
source_url: https://wiki.genexus.com/commwiki/wiki?22221
genexus_version: "18"
---

# Offline Native Mobile applications architecture

The [Offline Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?22237) architecture has to consider two situations where these apps should work:

1. When the application is disconnected.
2. When the application has a connection.

In the first case, the app has to be able to process data and interact with a database without a network connection.

In the second scenario, the app can synchronize data with the server by invoking web services.

Connected or not, all the processing of the application is done on the device, updating the local database. Once the connection is restored, synchronization will be executed.

### [Architecture](#Architecture)

`[imagen omitida: wiki id 22448]`

An Offline Native Mobile application can be split into two components: a local component and a server component.  
The server may have a backend for the application, the database, and a services layer for data synchronization with the devices.  
On the devices, the applications also have a database with a subset of the server data and all the logic that needs to be executed locally. That logic is written in the native code of the device (Objective-c/Swift for Apple, Java for Android, etc.). The application also has all the metadata required for the UI layout and user events.

Both components (device and server) communicate via REST services to perform the required synchronization to fill the local database and to send the modifications performed on the device to the server.

The communication between the Native Mobile application and the server is known as [synchronization](https://wiki.genexus.com/commwiki/wiki?22240).

### [Advanced concepts](#Advanced+concepts)

Read the [Advanced Concepts of Offline Applications architecture](https://wiki.genexus.com/commwiki/wiki?25536) document to learn more about the Offline applications architecture.

**Note**: Offline apps cannot be prototyped with [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974).


|  |
| --- |
| **Backlinks** |
| [Advanced Concepts of Offline Applications architecture](https://wiki.genexus.com/commwiki/wiki?25536) | [Android - FAQ and Common Issues](https://wiki.genexus.com/commwiki/wiki?14575) | [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) |
| [Encrypt Offline Database property](https://wiki.genexus.com/commwiki/wiki?35539) | [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974) | [Getting Started with tvOS](https://wiki.genexus.com/commwiki/wiki?40787) |
| [Getting Started with watchOS](https://wiki.genexus.com/commwiki/wiki?40786) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [HowTo: Use the Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?23558) | [Knowledge Base Navigator (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?56059) |
| [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Category:Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) | [Offline Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?22237) |
| [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [Offline Native Mobile Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262) | [Offline Native Mobile Applications Scenarios](https://wiki.genexus.com/commwiki/wiki?22507) | [Offline Native Mobile synchronization granularity alternatives](https://wiki.genexus.com/commwiki/wiki?37109) |
| [Online Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?14981) | [Point of Sales scenario](https://wiki.genexus.com/commwiki/wiki?23673) | [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076) | [The Data Synchronization Problem](https://wiki.genexus.com/commwiki/wiki?22240) |

---
