---
title: "HowTo: Configure Push Notifications in Android Applications (GeneXus 18 Upgrade 11 or prior)"
source_id: 61122
source_url: https://wiki.genexus.com/commwiki/wiki?61122
genexus_version: "18"
---

# HowTo: Configure Push Notifications in Android Applications (GeneXus 18 Upgrade 11 or prior)

**Warning**: As GCM was deprecated (April 10, 2018) and removed (April 11, 2019) by Google, Notification Provider is the only method available to integrate Push Notifications in a GeneXus-generated Android application.

This is a step by step guide to set up push notifications for an Android Application. If you need general information on how to use push notifications please see [Push Notifications in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19945).

### [Requirements](#Requirements)

You need to access the [Firebase Console](https://console.firebase.google.com/u/0/) with a Google Account, set up a new project, and then get a Sender ID and a Server Key.

`[imagen omitida: wiki id 42511]`

### [Sender configuration](#Sender+configuration)

Using Push Notifications in a GeneXus-generated application is really simple. It is done by setting the [Enable Notifications property](https://wiki.genexus.com/commwiki/wiki?49799) to True in the Main object properties group. When doing this, a new set of properties is available (under the header *Notifications*):

`[imagen omitida: wiki id 54522]`

Here you need to set the credentials previously configured for the notifications service, Android Sender ID, and Android Server API Key (set with the Server Key obtained before).

### [Intermediate Step](#Intermediate+Step)

From now on, every time you execute a GeneXus application that has Push Notifications enabled in a device, the [Devices Registration Service](https://wiki.genexus.com/commwiki/wiki?18149) is executed in order to register and store the device information to be used in the future to send messages (Push Notifications) to that device.

### [How to send notifications?](#How+to+send+notifications%3F+)

Notifications are sent as shown in this [Sender example](https://wiki.genexus.com/commwiki/wiki?33687).

### [Application execution](#Application+execution)

And that’s it. The messages sent will be shown as notifications in the Android device:

`[imagen omitida: wiki id 18151]`
