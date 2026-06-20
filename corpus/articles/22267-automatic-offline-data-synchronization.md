---
title: "Automatic Offline Data Synchronization"
source_id: 22267
source_url: https://wiki.genexus.com/commwiki/wiki?22267
genexus_version: "18"
---

# Automatic Offline Data Synchronization

By setting the [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223) to 'On Application Launch' or 'After Elapsed Time' GeneXus is going to be in charge of calling the initialization and update processes of the Offline tables of the application.

### [Initialization](#Initialization)

This is the first load of the local database with the records of the server's database. Initialization happens as follows:

1. When the application is installed on the device, the database is created (this is independant of the synchronization criteria)
2. After the database is created the initialization process is started.  
   This process brings the required data from the server and inserts it on the local database. Records can be filtered on the Conditions tab of the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509).
3. After all the data is synchronzed, a set of hashes is also stored on the device. This hashes will make it possible to determinate if a table, in the future, has changed or not.

After this process is done, the application is ready to be used and can start reading, inserting and updating this local database via GeneXus Objects as usual.

### [Updating](#Updating)

The synchronization processes that update the local database are called automatically providing that at least:

* the device can connect to the Server's synchronization services
* the [minimum time between receives](https://wiki.genexus.com/commwiki/wiki?22224) has elapsed

### [How is the Synchronization done?](#How+is+the+Synchronization+done%3F)

On a Receive operation, the server sends the required data to the devices, and also sends a set of hashes identifying the version of the data for each table.

This hashes are stored locally on the devices, and are sent on the next Receive operations, so that the server knows the data stored in the devices.

The server computes the new hashes for the tables, and only sends information from the changed tables. The ones that did not change are not sent.

Depending on the [Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541), the data sent from the server to the device may consist on the full table (after applying the [conditions](https://wiki.genexus.com/commwiki/wiki?23570)), or only the differences with the device's data.

## [See Also](#See+Also)

* [HowTo: Create offline mobile applications with a preloaded database](https://wiki.genexus.com/commwiki/wiki?22298)
* [Advanced Concepts of Offline Applications architecture](https://wiki.genexus.com/commwiki/wiki?25536)
* [Coding your Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266)


|  |
| --- |
| **Backlinks** |
| [Best Practices for Manual Synchronization](https://wiki.genexus.com/commwiki/wiki?22276) | [Coding your Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266) | [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223) |
| [HowTo: Use the Synchronization API](https://wiki.genexus.com/commwiki/wiki?23605) | [Manual Synchronization Code Sample](https://wiki.genexus.com/commwiki/wiki?22543) | [Minimum Time Between Receives property](https://wiki.genexus.com/commwiki/wiki?22224) | [Minimum Time Between Table Purges property](https://wiki.genexus.com/commwiki/wiki?31160) |
| [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [KB:Sales](https://wiki.genexus.com/commwiki/wiki?23672) |

---
