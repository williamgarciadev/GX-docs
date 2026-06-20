---
title: "Offline Database object"
source_id: 22509
source_url: https://wiki.genexus.com/commwiki/wiki?22509
genexus_version: "18"
---

# Offline Database object

As mentioned in the [Offline Architecture document](https://wiki.genexus.com/commwiki/wiki?22221), the offline applications need a **local Database** in the device. The Offline Database object is shown in GeneXus as a child node of the offline [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) (with [connectivity support](https://wiki.genexus.com/commwiki/wiki?20911) offline), and this object is used to define when and how to synchronize the local database with the server's database.

This object appears only after building an offline main object for the first time, and it is automatically set in [Offline Database property](https://wiki.genexus.com/commwiki/wiki?17817) for the Mobile main object.

This object is a very simple object that contains the following parts:

* [Offline Database Object events](https://wiki.genexus.com/commwiki/wiki?23566)
* [Offline Database Object conditions](https://wiki.genexus.com/commwiki/wiki?23570)
* [Offline Database Object properties](https://wiki.genexus.com/commwiki/wiki?25196)

### [Local Database creation and Reorganization](#Local+Database+creation+and+Reorganization)

When GeneXus creates the Offline Database object also creates automatically some programs to create the local Database in the device once the application is installed. For more information, please refer to the [Offline Database reorganization](https://wiki.genexus.com/commwiki/wiki?27121) document.

### [Table selection](#Table+selection)

As this object will be in charge of creating a local database in the device, it is necessary to the object to know **which tables** are going to be created in the local database. GeneXus has the intelligence to make that selection automatically, and it is resolved and explained in the [Offline Database Object Table selection](https://wiki.genexus.com/commwiki/wiki?23561) document.

### [Configuring the Synchronization](#Configuring+the+Synchronization)

As mentioned before, this object has Events, Conditions, and Properties to handle the synchronization. Because synchronization is about receiving and sending data between the application and the web server, it is possible to change some setting about how the application will receive and send data.

#### [Receiving settings](#Receiving+settings)

The device will receive a subset of the selected tables from the webserver database, and it is possible to filter what of that data is needed in the local database. To do so, it is available the Conditions and Events sections in the Offline Database object.  
There are also some properties that may be useful to configure the received settings, those properties are:

* [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223)
* [Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541)

#### [Sending settings](#Sending+settings)

As mentioned in the [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) document, the device will internally save all the events in the local database in order to send all the changes to the server when the device is again connected. It is possible to manage when to send those changes, and the [Send Changes property](https://wiki.genexus.com/commwiki/wiki?23392,,) allows setting that.

### [Navigation Report](#Navigation+Report)

The navigation report of the Offline Database shows what offline tables are populated with which conditions. To understand more about this check out the [Offline Database Object Navigation Report](https://wiki.genexus.com/commwiki/wiki?23568) document.

### [Availability](#Availability)

This feature is available since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

### [See Also](#See+Also)

[Offline Database Object events](https://wiki.genexus.com/commwiki/wiki?23566)  
[Offline Database Object conditions](https://wiki.genexus.com/commwiki/wiki?23570)  
[Offline Database Object properties](https://wiki.genexus.com/commwiki/wiki?25196)
