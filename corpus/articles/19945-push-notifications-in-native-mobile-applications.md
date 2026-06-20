---
title: "Push Notifications in Native Mobile Applications"
source_id: 19945
source_url: https://wiki.genexus.com/commwiki/wiki?19945
genexus_version: "18"
---

# Push Notifications in Native Mobile Applications

[Push](http://en.wikipedia.org/wiki/Push_technology) Notifications allow receiving alerts in Native Mobile applications from our remote servers (web applications) even when the Native Mobile applications are not running. This mechanism describes a style of communication where the request for a given Transaction is initiated by the publisher or central server. It is usually contrasted with [Pull](http://en.wikipedia.org/wiki/Pull_technology) communications.

In the Native Mobile arena, this is an essential piece to create effective communication between devices and server-side applications.

The basic idea is that after the Server knows its clients, it is able to send dedicated messages or broadcast a general message to all of them. The canonical case is an Email Client Application, which receives notifications from the server side every time a new message arrives at the Inbox.

### [Available technologies](#Available+technologies)

Each Native Mobile platform has its own technology to implement this mechanism, Apple has the [Apple Push Notifications Service (APNS)](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?35452,,) and Google has [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging) ([Google Cloud Messaging](https://developers.google.com/cloud-messaging/)) has been deprecated as of April 10, 2018).

In addition, there are some Notifications Providers, which provide interfaces that can be used by the applications to easily set up and use Push Notifications for all mobile platforms in a scalable and portable way. Some of these Notification Providers are [One Signal](https://onesignal.com/) and [JPush](https://docs.jiguang.cn/en/jpush/guideline/intro/) (Chinese provider).

#### [Architecture](#Architecture)

There are four main components:

* **Native Mobile Application**, which will be the "client-side" (receiver) of the Push Notification messages.
* **Web Application**, which will be the "server-side" (sender) of the Push Notification messages.
* **Push Notification Service**, an external resource that provides Push Notification delivery for each platform.
* **Notification Provider**, an external resource that provides an interface to easily interact with the Push Notification Services.

### [Push Notifications in GeneXus Native Mobile applications](#Push+Notifications+in+GeneXus+Native+Mobile+applications)

Want to know how to include Push Notifications in GeneXus-generated Smart Device applications?

Start here:

* [HowTo: Configure Push Notifications in Apple Applications](https://wiki.genexus.com/commwiki/wiki?17451)
* [HowTo: Configure Push Notifications in Android Applications](https://wiki.genexus.com/commwiki/wiki?18147)
* [Notifications Provider property](https://wiki.genexus.com/commwiki/wiki?33670)
* [HowTo: Push Notifications using an External Provider](https://wiki.genexus.com/commwiki/wiki?30621)
* [HowTo: Use a Device's Registration Service for Push Notifications](https://wiki.genexus.com/commwiki/wiki?18149)


|  |
| --- |
| **Backlinks** |
| [HowTo: Configure Push Notifications in Android Applications](https://wiki.genexus.com/commwiki/wiki?18147) | [HowTo: Configure Push Notifications in Android Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54521) |
| [HowTo: Configure Push Notifications in Apple Applications](https://wiki.genexus.com/commwiki/wiki?17451) | [HowTo: Configure Push Notifications in Apple Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54517) | [HowTo: Push Notifications using an External Provider](https://wiki.genexus.com/commwiki/wiki?30621) | [HowTo: Register an application to use JPush services](https://wiki.genexus.com/commwiki/wiki?37021) |
| [HowTo: Use Badge operations in Apple](https://wiki.genexus.com/commwiki/wiki?19356) | [iOS Applications Wireless Prototyping](https://wiki.genexus.com/commwiki/wiki?15576) | [LocalNotifications external object](https://wiki.genexus.com/commwiki/wiki?39554) |
| [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) | [Registration Handler property](https://wiki.genexus.com/commwiki/wiki?22981) | [Remote Notifications External Object](https://wiki.genexus.com/commwiki/wiki?39316) |
| [RemoteNotifications external object](https://wiki.genexus.com/commwiki/wiki?39399) |

---
