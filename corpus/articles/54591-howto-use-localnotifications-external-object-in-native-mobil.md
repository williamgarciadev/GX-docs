---
title: "HowTo: Use LocalNotifications external object in Native Mobile apps (GeneXus 18 Upgrade 2 or prior)"
source_id: 54591
source_url: https://wiki.genexus.com/commwiki/wiki?54591
genexus_version: "18"
---

# HowTo: Use LocalNotifications external object in Native Mobile apps (GeneXus 18 Upgrade 2 or prior)

This document is a brief guide on how to use Local Notifications in GeneXus Native Mobile apps.

### [Step 1: Checking the objects that will let you add Local Notifications](#Step+1%3A+Checking+the+objects+that+will+let+you+add+Local+Notifications)

There are two objects on the [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) that are used to enable Local Notifications.

`[imagen omitida: wiki id 39557]`

**LocalNotificationsInfo Structured Data Type**  
This [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) is used to define the configuration of the Local Notification.

It is a collection of Items, each one with a DateTime and a Text.

The DateTime will be used to know when that Local Notification will be triggered, and the text will be the info shown to the user.

`[imagen omitida: wiki id 39558]`

You can define as many Local Notifications as you want. A single item on the LocalNotificationsInfo collection is equivalent to one Local Notification.

**LocalNotifications external object**

`[imagen omitida: wiki id 39556]`

The [LocalNotifications external object](https://wiki.genexus.com/commwiki/wiki?39554) includes a method called **CreateAlerts** that expects a variable based on the LocalNotificationsInfo SDT as an input parameter.

When this action is executed, the app will schedule all the local notifications passed in the LocalNotifications SDT variable.

### Step 2: Programming the Local Notifications

To make them work, just create the following [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) (e.g: named "SendLocalNotificationsServer").

In this example, this Procedure is created to load the LocalNotificationsInfo SDT. Bear in mind that this can be done differently, as it is not compulsory to do it with a Procedure.

Parm:

```
parm(out: &MySdtLocalNotifications);
```

Source:

```
&MySdtLocalNotificationsItems.DateTime = ymdhmstot(2012,06,07,16,56,00) 
&MySdtLocalNotificationsItems.Text = "My Local Test"
&MySdtLocalNotifications.Add(&MySdtLocalNotificationsItems)
```

Variables:

```
MySdtLocalNotifications -> SDTLocalNotifications
MySdtLocalNotificationsItems -> SDTLocalNotifications.Item
```

Next, create a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829):

Layout:

`[imagen omitida: wiki id 19297]`

Events:

```
 Event 'SendNotification'
      Composite
          &MySdtLocalNotifications = SendLocalNotificationsServer()
          LocalNotifications.CreateAlerts(&MySdtLocalNotifications)
      EndComposite
 EndEvent
```

### [Step 3: Execution](#Step+3%3A+Execution)

Run your application.

First, press the Panel button to start scheduling Local Notifications.

After that, the Notifications will be scheduled and they will appear on your device at the time specified.

When the local notification is added:

`[imagen omitida: wiki id 19295]`

When the local notification is triggered.

`[imagen omitida: wiki id 19296]`

### [Sample](#Sample)

A working example of this method can be downloaded from: [WorkingWithLocalNotifications](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?20392,,).

### [Troubleshooting](#Troubleshooting)

The **Create method** of the external object returns a numeric value. If the returned value is 0, it means that there was no error in the execution. Otherwise, if the numeric value is different than 0, an execution error occurred.

### [Availability](#Availability)

This feature has been added to GeneXus in:

* [Apple](https://wiki.genexus.com/commwiki/wiki?14917) since GeneXus Evolution 2 Upgrade 1
* [Android](https://wiki.genexus.com/commwiki/wiki?14453) since GeneXus Evolution 2 Upgrade 3

### [Notes](#Notes)

* Since iOS 8, the local notifications require an authorization from the user. The user will be automatically asked for this authorization the first time you use this API. In case that the developer wants to do it manually, it can be done by using [Permissions external object for Apple applications](https://wiki.genexus.com/commwiki/wiki?31311) (e.g. when the app is in the background).
* If the DateTime field of the LocalNotification SDT is empty, the notification will be triggered instantly.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917),  [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

### [See Also](#See+Also)

[LocalNotifications external object](https://wiki.genexus.com/commwiki/wiki?39554)
