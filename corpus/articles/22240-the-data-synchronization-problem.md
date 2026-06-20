---
title: "The Data Synchronization Problem"
source_id: 22240
source_url: https://wiki.genexus.com/commwiki/wiki?22240
genexus_version: "18"
---

# The Data Synchronization Problem

As mentioned in the [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221) document, an offline application may interact with a server. This interaction is done to send or receive information to keep the devices and the server information synchronized. This mechanism of sending and receiving data is called: Synchronization.

### [Why do you need to synchronize?](#Why+do+you+need+to+synchronize%3F)

Because:

* The application might be a subset of a bigger system, so the interaction with this system is required.
* Having the whole system's database on the devices is sometimes unnecessary. In most cases, only a subset of tables and registers are needed for the device to fulfill the tasks.
* The server may have more power to do some heavy processing, tasks that can't be done on the devices, or consume too many resources.
* There is some business logic that can only be executed on the main application. For example inventory management.
* The devices need to have updated data, so from time to time, there is data that should be sent from the server to the devices.

### [How can this synchronization be done?](#How+can+this+synchronization+be+done%3F)

Via web services. The devices can consume and execute web services, and this will get or take data to and from the server.  
**Note**: Not all the services may be hosted on the same server.

#### [**Strategy**](#Strategy)

First things is to define:

* What does the application need to do when offline?
* Which of the involved tables are going to be used offline?
* Which records of the tables are needed offline?

### [Who starts the Synchronization?](#Who+starts+the+Synchronization%3F+)

The synchronization always begins with the device by asking for information or sending it. This is because the device is the one that knows when it is connected to the internet and when the connection is good enough. So the ability to ask for the information or send the information is from the device.

In this context is that the name of the synchronization operations is defined. The operations are named as seen from the device:

* Receive: the process of getting data FROM the server
* Send: the process of uploading local modifications TO the server.

### [When to Synchronize?](#When+to+Synchronize%3F)

The best moment to synchronize depends on the application context. There are no rules that can be followed, different scenarios will have different requirements, some will need to stay as synchronized as possible while others may require less frequent synchronizations.

Even though there is no recipe, there are several things to take into consideration on this matter:

* To be able to synchronize, the device needs to have a network connection.
* Sending information: The device knows exactly how much data is going to be sent. If a lot of data is required to be sent, then a good internet connection is needed.
* Receiving information: The device has no clue on how much information he is going to receive. An intermediate step may be recommended so the device can decide if the synchronization can be done or not. Taking into consideration the network connection status and the amount of data needed to be transported.
* Synchronization may need to stop before finishing since a moving device may lose connection at some point, so the synchronization has to be able to recap if the connection was lost during the process.

### [Other issues to be aware of](#Other+issues+to+be+aware+of)

#### [What data is going to be received?](#What+data+is+going+to+be+received%3F)

For data reception, you have two possibilities:

* always receive all the required information and replace the existing data.
* only receive the modifications and apply them to the existing data.

The first option may involve more data being transferred while the second option may require more server processing.

#### [Security of the communication](#Security+of+the+communication)

When data has to travel forward and backward from the server to the device it may involve data over a LAN or even the Internet. So the security in this matter is crucial.

#### [Synchronization conflicts](#Synchronization+conflicts)

There are some cases where our apps can present synchronization conflicts. Some of those problems and the solutions are explained in the following document:

* [Automatically generated identifiers synching conflicts](https://wiki.genexus.com/commwiki/wiki?23543)

#### [Orders of actions](#Orders+of+actions)

The actions executed offline have to be replicated on the server in the same order as they were executed on the device. This will ensure the coherence of the actions. Some actions that were registered offline can invalidate future events. For example, when a device inserts purchase orders, and the product went out of stock, future events will have to fail because of this.

#### [Failure Feedback](#Failure+Feedback)

It is necessary to give feedback to the device after the synchronization. When events fail because of some server validation, the device has to be notified that this happened so the user can take an action or at least knows that an error occurred on the synchronization.

#### [Images synchronization](#Images+synchronization)

Multimedia (image, video, audio) can be a source of problems for synchronization.

Multimedia files are likely to be massive and depending on the number of images or videos they may take lots of space and time to synchronize.

### [See Also](#See+Also)

[Offline Native Mobile Applications Generation](https://wiki.genexus.com/commwiki/wiki?22262)  
[Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269)


|  |
| --- |
| **Backlinks** |
| [Automatically generated identifiers synching conflicts](https://wiki.genexus.com/commwiki/wiki?23543) | [Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223) | [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) |
| [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [Offline Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?22237) | [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221) |
| [Synchronization by Chunks](https://wiki.genexus.com/commwiki/wiki?42733) |

---
