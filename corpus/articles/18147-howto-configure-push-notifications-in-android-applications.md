---
title: "HowTo: Configure Push Notifications in Android Applications"
source_id: 18147
source_url: https://wiki.genexus.com/commwiki/wiki?18147
genexus_version: "18"
---

# HowTo: Configure Push Notifications in Android Applications

**Warning**: As GCM was deprecated (April 10, 2018) and removed (April 11, 2019) by Google, Notification Provider is the only method available to integrate Push Notifications in a GeneXus-generated Android application.

This is an overview about push notifications for an Android Application. If you need general information on how to use push notifications in Native Mobile applications, please see [Push Notifications in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19945).

**Note**: This guide shows how to integrate Push Notifications using OneSignal. GeneXus does not support or maintain the configuration of this external service. Screenshots, parameters, UI labels, and/or configuration steps in OneSignal may change over time.

### [Requirements](#Requirements)

Before configuring anything in GeneXus, you need to have already completed the OneSignal setup process.

This includes:

* Accessing the [Firebase Console](https://console.firebase.google.com/u/0/) with a Google Account, going to Project Settings > Service Accounts, and clicking the **Generate new private key** button. This Private Key is uploaded to OneSignal during platform configuration.
* Uploading that Private Key in OneSignal during platform configuration.
* Obtaining the following values from OneSignal: **App ID** and **REST API** Key (also called Auth Key or API Authentication Key).

For more details on this, read: [HowTo: Register an application to use OneSignal services](https://wiki.genexus.com/commwiki/wiki?33671).

### [Configure Push Notifications in GeneXus](#Configure+Push+Notifications+in+GeneXus)

To use push notifications in an Android application generated with GeneXus, configure the following properties:

* [Enable Notifications property](https://wiki.genexus.com/commwiki/wiki?49799) = True in the Main object. Indicates that the application will support Push Notifications.

In the Preferences window, at the Backend Generator level, configure:

* [Notifications Provider property](https://wiki.genexus.com/commwiki/wiki?33670): OneSignal.
* [App ID property](https://wiki.genexus.com/commwiki/wiki?37492): Enter the OneSignal App ID from your OneSignal application.
* [REST API Key property](https://wiki.genexus.com/commwiki/wiki?37493) Enter the OneSignal API Authentication Key.

For more details on how to obtain these values, read [HowTo: Register an application to use OneSignal services](https://wiki.genexus.com/commwiki/wiki?33671).

### [Device Registration in GeneXus](#Device+Registration+in+GeneXus)

From now on, every time you execute a GeneXus application that has Push Notifications enabled in a device, the [Devices Registration Service](https://wiki.genexus.com/commwiki/wiki?18149) is executed in order to register and store the device information to be used in the future to send messages (Push Notifications) to that device.

### [How to send notifications?](#How+to+send+notifications%3F+)

Notifications are sent as shown in this [Sender example](https://wiki.genexus.com/commwiki/wiki?33687).

### [Application execution](#Application+execution)

And that’s it. The messages sent will be shown as notifications in the Android device:

`[imagen omitida: wiki id 18151]`


|  |
| --- |
| **Backlinks** |
| [Device Registration Mode property](https://wiki.genexus.com/commwiki/wiki?37295) | [HowTo: Configure Push Notifications in Android Applications (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?61122) |
| [HowTo: Configure Push Notifications in Android Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54521) | [HowTo: Push Notifications using an External Provider](https://wiki.genexus.com/commwiki/wiki?30621) | [HowTo: Register an application to use JPush services](https://wiki.genexus.com/commwiki/wiki?37021) |
| [HowTo: Use a Device's Registration Service for Push Notifications](https://wiki.genexus.com/commwiki/wiki?18149) | [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Notifications Provider property](https://wiki.genexus.com/commwiki/wiki?33670) |
| [Push Notifications in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19945) |

---
