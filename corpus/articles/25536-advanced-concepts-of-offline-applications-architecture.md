---
title: "Advanced Concepts of Offline Applications architecture"
source_id: 25536
source_url: https://wiki.genexus.com/commwiki/wiki?25536
genexus_version: "18"
---

# Advanced Concepts of Offline Applications architecture

[Offline applications](https://wiki.genexus.com/commwiki/wiki?20286) offer a whole new branch of possible scenarios for devices. Because of this, the [offline application architecture](https://wiki.genexus.com/commwiki/wiki?22221) is more complex than online application architectures given by GeneXus. In addition, GeneXus creates auxiliary tables, files, and objects, either on the client-side (the device) or the server-side, in order to perform the synchronization process.

This document is an extension of the [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221) document and explains advanced concepts of how GeneXus generates this type of application.

### [Client-side architecture](#Client-side+architecture)

#### [Auxiliary structures for data sending](#Auxiliary+structures+for+data+sending)

As mentioned in the [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221) document, the device needs a local database in order to work offline. This means that the device can insert, update, or delete data at any time, whether it has a connection to the server or not. In most scenarios, these applications need to synchronize with a central server in order to keep data updated in the device and to send all changes made in the device to the server. This process is described as 'Data Synchronization'.

But, how does the device know what changes did it made?

Here comes the need of storing somehow all the modifications made by the device, so that, once the device is connected, it can send these modifications to the application server.

In order to do that, along with the tables defined by the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509), a table named 'GxPendingEvents' is created in the local database to store all the modifications (insert, update or delete) made in the local database. These modifications are stored as "synchronization events" in the auxiliary table.

**Important note**: Only modifications (insert, update, delete) made by [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) are stored into the GxPendingEvents table.

Every time the device executes a [BC](https://wiki.genexus.com/commwiki/wiki?2416), it stores all the related information of that event into the GxPendingEvents table.

When a device executes the [Synchronization.Send method](https://wiki.genexus.com/commwiki/wiki?23604), it sends all the events with Status "Pending" from the GxPendingEvents table.

It is possible to access this table's data by using the [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341).

#### [Auxiliary structures for data reception](#Auxiliary+structures+for+data+reception)

Another important component of offline applications is the data reception process. This process transfers data from the server into the device in order to keep both systems synchronized.

But, how do the device and the server know if they are not in sync?

The first time the device tries to synchronize, the server sends all necessary data as it is defined in the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509). The server also sends a set of table hashes that are stored in the device in a JSON file.

In the subsequent synchronizations, the device sends the table hashes to the server.

These hashes are used to determine which changes have been made since the last synchronization, so that, in the next synchronization, the server sends only the data that has changed. The behavior on how is the data changes processed in the server depends on the [Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541) of the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509).

### [Server-side architecture](#Server-side+architecture)

In addition to the [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221), the server architecture changes if you set in the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) the [Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541) the value "By Row".

GeneXus gives two alternatives on how data from the server is received in the device. These implementation options are given by the [Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541). You can choose between "By Table" granularity, which is the simplest implementation, or "By Row", which is a little more complex.

If you choose to use "By Row" granularity synchronization (which is the default value of the [Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541)), new specific tables are created in the server database in the [Create Database Tables](https://wiki.genexus.com/commwiki/wiki?7158) process.

The created tables are the following: 'GXPARAMETERS', 'GXDEVICERESULT' and 'GXRESULTROW'

`[imagen omitida: wiki id 33761]`

**Note**: A file named gxrowlevelcache\_ReorganizationScript.txt is generated with the corresponding sentences to create those tables. If the user that executes the programs has no permissions on the database, those sentences have to be executed by the corresponding team, in deployment time.

These tables store all the necessary information to perform the synchronization by row.

To prevent an excessive size increase of these tables, the [Minimum Time Between Table Purges property](https://wiki.genexus.com/commwiki/wiki?31160) is available to periodically purge them.

### [See Also](#See+Also)

[Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221)  
[Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269)  
[Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541)  
[Batch Synchronization](https://wiki.genexus.com/commwiki/wiki?42733)


|  |
| --- |
| **Backlinks** |
| [Automatic Offline Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22267) | [Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541) | [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) |
| [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221) | [Synchronization.ServerStatus method](https://wiki.genexus.com/commwiki/wiki?25839) |

---
