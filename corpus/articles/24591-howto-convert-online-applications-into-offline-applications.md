---
title: "HowTo: Convert online applications into offline applications"
source_id: 24591
source_url: https://wiki.genexus.com/commwiki/wiki?24591
genexus_version: "18"
---

# HowTo: Convert online applications into offline applications

At some point, you may need to turn your online apps into [offline apps](https://wiki.genexus.com/commwiki/wiki?22237) to get the benefits of an offline application.

GeneXus has useful features to handle this conversion quickly. Converting an online application into an offline one is as simple as changing a property value in your application's main object. In addition, it is also available for you to manage several behaviors of your offline applications such as synchronization mechanisms, data storage in the device, and many others.

### [How it works](#How+it+works)

The first thing you should do is to change the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) of the main object to **Offline**. Next, you have to do a "Rebuild All" of the main object.  
You can learn more about this property in the article [HowTo: Use the Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?23558).

When GeneXus has finished building, your offline application is completed and ready to be installed on your device. Read [Offline Native Mobile Applications Requirements](https://wiki.genexus.com/commwiki/wiki?22259) for more details.

You can also change many behaviors as desired.

### [Setting up your offline application](#Setting+up+your+offline+application)

#### [Synchronization receive mechanisms](#Synchronization+receive+mechanisms)

Choose your preferred way of receiving data from the server by changing these properties:

[Data Receive Criteria property](https://wiki.genexus.com/commwiki/wiki?22223): Choose when to receive the data from the server.

[Data Receive Granularity property](https://wiki.genexus.com/commwiki/wiki?23541): Choose how to handle the changes to be synchronized.

#### [Synchronization send mechanisms](#Synchronization+send+mechanisms)

Choose your preferred way of sending data from the device to the server by changing the [Send Changes property](https://wiki.genexus.com/commwiki/wiki?23392,,).

#### [Table selection](#Table+selection)

Choose which tables of your system should be in your offline application. Read the article [Offline Database Object Table selection](https://wiki.genexus.com/commwiki/wiki?23561) to learn more.

#### [Filtering server data to the device](#Filtering+server+data+to+the+device)

Indicate which data the application stores in its offline database. Read the article [Offline Database Object conditions](https://wiki.genexus.com/commwiki/wiki?23570) for more details.

### [Important considerations](#Important+considerations)

To use the GeneXus synchronization programs to send the changes made in the device to the server, the use of [Business Component](https://wiki.genexus.com/commwiki/wiki?5846)s is necessary.

The application sends in the synchronization process only Insertions, Deletions, and Updates made by using Business Components. For this reason, it's important that you exclude the New, Delete, and ForEach commands from your objects for inserting, deleting, and updating data. Otherwise, the [Warning spc0203](https://wiki.genexus.com/commwiki/wiki?6774) message will be shown during the Program Specification.  
If you choose not to use the GeneXus synchronization programs, you can [code your own Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266) to send changes to the server.

### [Tips and Features](#Tips+and+Features)

#### [Use of [WebSession data type](https://wiki.genexus.com/commwiki/wiki?6321) compared to the use of [ClientStorageAPI external object](https://wiki.genexus.com/commwiki/wiki?24132,,)](#Use+of+wiki%3F6321%2CWebSession%2Bdata%2Btype+WebSession+data+type+compared+to+the+use+of+wiki%3F24132%2CClientStorageAPI%2Bexternal%2Bobject%2B%2528X%2BEvolution%2B3%2529+ClientStorageAPI+external+object)

At first sight, they may look the same, but they are different. The main difference is that WebSession data is lost every time the application closes, while the ClientStorage API stores the information to have the same information even if the application launches again.

#### [Using the [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602)](#Using+the+wiki%3F23602%2CSynchronization%2BAPI+Synchronization+API)

Even if you have selected manual or automatic synchronization for receiving or sending data, the [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602) is always available, so that you can call the synchronization programs as needed. Read [HowTo: Use the Synchronization API](https://wiki.genexus.com/commwiki/wiki?23605) for further information.

#### [Using the [SynchronizationEventsAPI external object](https://wiki.genexus.com/commwiki/wiki?23606,,)](#Using+the+wiki%3F23606%2CSynchronizationEventsAPI%2Bexternal%2Bobject%2B%2528X%2BEvolution%2B3%2529+SynchronizationEventsAPI+external+object)

Every time you use Business Components for Inserting, Deleting, or Updating data in your device, those actions, also called events, are stored in an auxiliary table inside the application in order to send the same changes to the server later. You can manage those stored actions with the [SynchronizationEventsAPI external object](https://wiki.genexus.com/commwiki/wiki?23606,,). For instance, you can change the actions' status if something goes wrong in the synchronization process or remove some of the actions if needed.

#### [Creating your offline application with preloaded data](#Creating+your+offline+application+with+preloaded+data)

It is possible to have preloaded data in your application when installed on the device. For more information, read [HowTo: Create offline mobile applications with a preloaded database](https://wiki.genexus.com/commwiki/wiki?22298).

#### [DataTypes compatibility](#DataTypes+compatibility)

There are some non-implemented DataTypes for offline applications, yet. Moreover, the specification error "[spc0106](https://wiki.genexus.com/commwiki/wiki?6433)" occurs for offline objects that use those DataTypes. So it is easy to know which are the non-implemented DataTypes for each platform.

Here is the list of non-implemented DataTypes for offline applications for each platform: [Offline non-implemented DataTypes](https://wiki.genexus.com/commwiki/wiki?25398)

It is recommended to avoid the use of those DataTypes in [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087) and use them in Server-only Procedures or Data Providers instead.

#### [Server-only Procedures, Data Providers or Business Components](#Server-only+Procedures%2C+Data+Providers+or+Business+Components)

Sometimes you may have [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)s or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)s which execute only on the server-side. For instance, Procedures that use components not implemented for mobile platforms yet -like PDF reports, Excel files, among others-, some Procedures that need high computational power, or some Data Providers that use files located in the server file system. However, because of the [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221), if an offline object calls some of these objects, they are going to be called offline and errors may occur while specifying or compiling the client-side application.  
To run these objects online, a possible but more intricate option is to call them via the [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932). However, the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) gives an easier solution for this problem: by setting this property to Online on Procedures, Data Providers or [Business Component](https://wiki.genexus.com/commwiki/wiki?5846)s, whenever you call these objects from an Offline Mobile object, the application calls these objects via REST services automatically. Another important fact is that these objects are generated only for the server-side application, avoiding many possible compilation errors from the client-side application.

#### [Client-only Procedures or Data Providers](#Client-only+Procedures+or+Data+Providers)

In the same way there might be some [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) or [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270) which have to be executed only on the server-side, there might also exist some Procedures or Data Providers which are only executable in the client-side. That means, these objects should be executed only by the device. This is very common in, for example, Procedures that uses [External object](https://wiki.genexus.com/commwiki/wiki?5669)s which are defined only for Mobile platforms. However, because of the [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221), if an offline object calls some of these objects, by default, these objects are generated for both client-side and server-side applications. So errors may occur while specifying or compiling the server-side application.

To avoid generating those objects for the server-side application, first, be sure that the objects are not called by any Web object, and secondly, set the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) of each Procedure or Data Provider to "Offline".

### [GAM and Offline](#GAM+and+Offline)

[GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) is available for [Offline Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?22237). Despite this, it has some restrictions that you should consider when converting your application from Online to Offline. For more details about this topic, read [Offline Native Mobile applications using GAM](https://wiki.genexus.com/commwiki/wiki?23400).

### [Offline applications - Common issues](#Offline+applications+-+Common+issues)

Read [Offline Native Mobile Applications Common Issues](https://wiki.genexus.com/commwiki/wiki?20287) if you are having any trouble.

### [See Also](#See+Also)

[Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221)  
[The Data Synchronization Problem](https://wiki.genexus.com/commwiki/wiki?22240)  
[Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269)  
[Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509)


|  |
| --- |
| **Backlinks** |
| [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |

---
