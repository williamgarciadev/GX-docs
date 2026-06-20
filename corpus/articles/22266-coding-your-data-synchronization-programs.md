---
title: "Coding your Data Synchronization programs"
source_id: 22266
source_url: https://wiki.genexus.com/commwiki/wiki?22266
genexus_version: "18"
---

# Coding your Data Synchronization programs

This document explains one of the [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) criterias to choose regarding [Offline Native Mobile Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262). It establishes that all the synchronization processes are going to be invoked and executed on demand.

When generating [Offline Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?22237) Genexus generates code to execute the synchronization.  
For example:

* Scripts to generate the database
* Scripts to initialize the database
* Code to execute on the device the scripts
* Scripts to synch the data of the data bases.
* Web services on the server side

Apart from developing this objects the user has to solve the following problems:

* When is the synchronization going to take place?
* Which data is going to be synchronized?
* How is the synchronization done?

There are two ways to do Manual Synchronization, and they differ of aid the developer receives from GeneXus:

* Using generated programs to Synchronize.
* Manually program and synchronize.

### [Option 1: Using generated programs to synchronize](#Option+1%3A+Using+generated+programs+to+synchronize)

Even though the [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223) or the [Send Changes property](https://wiki.genexus.com/commwiki/wiki?23392,,) are **manual** GeneXus generates programs and scripts to do the synchronization. This programs are generated and are on hold until the smart device application calls them to be executed. The easiest way of calling this programs is using the [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602). You can check out the [HowTo: Use the Synchronization API](https://wiki.genexus.com/commwiki/wiki?23605) for further reading about the Synchronization API.

### [Option 2: Manually program and synchronize](#Option+2%3A+Manually+program+and+synchronize)

The GeneXus user needs to code all the objects needed for the synchronization and also decides some factors of the synchronization strategy.  
What do you have to code:

* Procedures that will be executed offline
* The web services (REST or SOAP) that the server is going to expose
* The consumption of those REST or SOAP services via HttpClient

What this code has to do:

* Insert on the local database the data brought by the invoked services
* Send the local Events registered offline to the server

A generic sample code can be seen [here](https://wiki.genexus.com/commwiki/wiki?22543).  
In this scenario it is very important to [check the network status](https://wiki.genexus.com/commwiki/wiki?22526,,), this is going to be a key factor to define which is the best moment to do the synchronization. Also, this [sample](https://wiki.genexus.com/commwiki/wiki?20698,,)  is based on Manual Synchronization.  
Lastly, there are some [Best Practices for Manual Synchronization](https://wiki.genexus.com/commwiki/wiki?22276) to take into consideration for optimal resource usage.

### [See also](#See+also)

[Automatic Offline Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22267)


|  |
| --- |
| **Backlinks** |
| [Automatic Offline Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22267) | [Best Practices for Manual Synchronization](https://wiki.genexus.com/commwiki/wiki?22276) | [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223) |
| [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [HowTo: Use the Synchronization API](https://wiki.genexus.com/commwiki/wiki?23605) | [Manual Synchronization Code Sample](https://wiki.genexus.com/commwiki/wiki?22543) |
| [Network external object](https://wiki.genexus.com/commwiki/wiki?31310) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |

---
