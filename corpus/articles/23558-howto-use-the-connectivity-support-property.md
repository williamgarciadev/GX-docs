---
title: "HowTo: Use the Connectivity Support property"
source_id: 23558
source_url: https://wiki.genexus.com/commwiki/wiki?23558
genexus_version: "18"
---

# HowTo: Use the Connectivity Support property

As explained in the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911)'s documentation, this property has 3 possible values: Online, Offline and Inherit.

By changing this property's value in a per-object basis, it is possible to decide whether some sections of the application are going to work with the local Database (Offline) or by calling REST services to get the panel's data (Online).

### [How it works](#How+it+works)

As an example, a simple Event application containing information about Sessions and Speakers and that displays a list of Tweets related to the Event will be used.

This simple Event application has the following 3 Transaction objects with their corresponding [Work With objects](https://wiki.genexus.com/commwiki/wiki?15974):

`[imagen omitida: wiki id 54131]`

Now that the app is designed, let's turn it into an Offline application. To do that, all you have to do is set the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) of the main [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) to "Offline".

**Note**: Remember that for all non-Main objects, the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) is set to inherit by default.

`[imagen omitida: wiki id 54134]`

After building the Menu object, the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) is created with the Speakers, Session and Tweets tables (as explained in the [Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509) documentation), as those are the tables that are accessed by the offline objects.

`[imagen omitida: wiki id 54132]`

After this, the Event application will have all the tables stored locally and all the Database access will be performed on the local Database.

But what if instead of storing the Tweets locally, you make that WW to work Online? This is for a very simple reason: Tweets will vary much more often than the rest of the application's information, and you may want to have them available as soon as they are published. It's better than waiting for a synchronization to get the latest tweets or synchronizing more often just to get them.

Having this configuration is as simple as setting the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) of the Tweets' [Work With object](https://wiki.genexus.com/commwiki/wiki?15974) to "Online".

Then the tables that are going to be in the OfflineDatabase are only "Speakers" and "Sessions" as shown in the image below:

`[imagen omitida: wiki id 54133]`

### [Using the Connectivity Support property over Procedures or Data Providers](#Using+the+Connectivity+Support+property+over+Procedures+or+Data+Providers)

As explained in the [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) documentation, this property is also available for [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) and [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270). This makes it much easier for the developer to call Online Procedures or Data Providers from Offline objects.

An intricate way of calling an online Procedure, which is exposed as a REST service, from an offline panel is by using the [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932). On the other hand, a much simpler way of doing the same is to set the Connectivity Support property of the Procedure into "Online". This forces the offline application to always call this Procedure via REST services. The device executes the same process as if the HttpClient data type is used instead, however this property gives a cleaner and simpler solution.

Following the scenario mentioned in this document, suppose you want to call a Procedure, which is exposed as a REST service, and which also returns all new Tweets that mention your event.  
As mentioned in the [Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221), if an application is set into offline architecture, by default, it calls all Procedures locally. To avoid this behavior when calling our Tweets Procedure, you just need to change the Connectivity Support property of that Procedure into "Online".

### [About Connectivity Support's "Inherit" value](#About+Connectivity+Support%27s+%22Inherit%22+value)

Inherit value adds flexibility to your solution, since it makes it possible that an object "A" works either Online or Offline, depending on the Connectivity Support property of the caller object.

For instance, if there are three mobile objects: objectA, objectB, and objectC that have the following properties configuration:

* Object A connectivity Support : Inherit
* Object B connectivity Support : Online
* Object C connectivity Support : Offline

If B calls A, then A will work as an Online object (Works with data of the web server)  
If C calls A, then A will work as an Offline object (Works with data of the offline Database)

**Note**: This applies only to the case that the connectivity Support of the Main object is Offline. If that is online, the whole architecture changes and, in the sample above, B cannot call C. So you cannot call an offline object in an online application.

### [See Also](#See+Also)

[Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911)  
[Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509)  
[Offline Database Object Table selection](https://wiki.genexus.com/commwiki/wiki?23561)


|  |
| --- |
| **Backlinks** |
| [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [My first Offline Native Mobile application](https://wiki.genexus.com/commwiki/wiki?20249) |
| [Offline Database Object Table selection](https://wiki.genexus.com/commwiki/wiki?23561) | [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) |

---
