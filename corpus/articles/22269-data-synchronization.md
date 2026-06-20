---
title: "Data Synchronization"
source_id: 22269
source_url: https://wiki.genexus.com/commwiki/wiki?22269
genexus_version: "18"
---

# Data Synchronization

Most offline applications are not usually stand-alone applications but just a subset of a larger server system, as explained in the [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221) document. For that reason, there should be a connection between the offline applications and the server to send and receive data from the device to the server and vice-versa.

This process is defined as "Data Synchronization" and you, as a GeneXus developer, may adopt a strategy to solve [the Data Synchronization Problems](https://wiki.genexus.com/commwiki/wiki?22240).

### [Data flow](#Data+flow)

#### [Initialization](#Initialization)

Once the application is installed in the device, a local database is created. After that, you might fill that database so that the user can start using the offline application. To do that, a possibility is to receive data from the server. This can be done by calling the Receive method of the GeneXus synchronization programs. See the [Synchronization.Receive method](https://wiki.genexus.com/commwiki/wiki?23603) documentation for further information.

After calling this method, the device receives all necessary information and stores it in the local database. Also, if there are any referenced files like images, blobs or whatever, all of them are stored in the device.

Another alternative is to install your application with preloaded data. To do this follow the instructions at the [HowTo: Create offline mobile applications with a preloaded database](https://wiki.genexus.com/commwiki/wiki?22298) document.

#### [Managing data changes](#Managing+data+changes)

When the application data is filled, the user can interact with the application, perform changes (like insertions, deletions and updates) and send them to the server 1; as in the same way, changes made by other users may occur in the server. This may cause the application not to be synchronized with respect to the server.  
In order to handle these problems GeneXus splits the Synchronization process in two: The Data Reception process and the Data Sending process. Both processes can be set up in GeneXus by changing some specific properties of the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509).

The Data Reception behavior is set by following properties:

* [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223)
* [Minimum Time Between Receives property](https://wiki.genexus.com/commwiki/wiki?22224)
* [Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541)

On the other hand, the Data Sending behavior is set by the [Send Changes property](https://wiki.genexus.com/commwiki/wiki?23392,,).

In addition, if you don't want to use the GeneXus generated synchronization programs, you can resolve the synchronization by [Coding your Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266) which, of course, takes a lot more of work.

1 It is important to note that only modifications (insert, update, delete) made by [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) to the local database are considered to be sent when the [Synchronization API Send method](https://wiki.genexus.com/commwiki/wiki?23604) is executed (manually or automatically). See [Advanced Concepts of Offline Applications architecture](https://wiki.genexus.com/commwiki/wiki?25536) for more details.

### [See Also](#See+Also)

* [Synchronization by Chunks](https://wiki.genexus.com/commwiki/wiki?42733)


|  |
| --- |
| **Backlinks** |
| [Advanced Concepts of Offline Applications architecture](https://wiki.genexus.com/commwiki/wiki?25536) | [Best Practices for Manual Synchronization](https://wiki.genexus.com/commwiki/wiki?22276) | [Coding your Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266) |
| [Getting Started with tvOS](https://wiki.genexus.com/commwiki/wiki?40787) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [Manual Synchronization Code Sample](https://wiki.genexus.com/commwiki/wiki?22543) | [Minimum Time Between Receives property](https://wiki.genexus.com/commwiki/wiki?22224) |
| [Minimum Time Between Table Purges property](https://wiki.genexus.com/commwiki/wiki?31160) | [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) | [Category:Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |
| [Offline Native Mobile Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262) | [Offline Native Mobile applications using GAM](https://wiki.genexus.com/commwiki/wiki?23400) | [Receive Timeout property](https://wiki.genexus.com/commwiki/wiki?39968) | [Send Timeout property](https://wiki.genexus.com/commwiki/wiki?39969) |
| [Synchronization by Chunks](https://wiki.genexus.com/commwiki/wiki?42733) | [The Data Synchronization Problem](https://wiki.genexus.com/commwiki/wiki?22240) |

---
