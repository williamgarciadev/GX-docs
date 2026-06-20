---
title: "HowTo: Use Badge operations in Apple"
source_id: 19356
source_url: https://wiki.genexus.com/commwiki/wiki?19356
genexus_version: "18"
---

# HowTo: Use Badge operations in Apple

Badges are a very common UI feature that
[Apple](https://wiki.genexus.com/commwiki/wiki?14917) users are used to seeing in almost every native application which has any of the [Push Notifications](https://wiki.genexus.com/commwiki/wiki?17451) or [Local Notifications](https://wiki.genexus.com/commwiki/wiki?19294) feature.

### [What is a badge?](#What+is+a+badge%3F)

`[imagen omitida: wiki id 19358]`

As you can see, there are five applications in this screen with the badge feature on and many more in which it is not activated. The badge feature shows a number above the app icon in white and red. It is typically used by the iOS native framework to show:

a. The number of unread emails you have on your inboxes.

b. New text messages in your SMS/iMessage application.

c. New upgrades available in the Apple App Store.

d. New iOS upgrades available.

e. And many more.

So, this feature is really useful and important if an application has [push](https://wiki.genexus.com/commwiki/wiki?19945) or [local](https://wiki.genexus.com/commwiki/wiki?19294) notifications and expects the user to react because it has recognized that some action is pending on the application.

This document is a simple tutorial to add this feature and some more related to an
[Apple](https://wiki.genexus.com/commwiki/wiki?14917) application generated with GeneXus.

### [Step 1. Resources needed](#Step+1.+Resources+needed)

A few methods are provided in the Interop external object to enable and use this feature.

`[imagen omitida: wiki id 32348]`

|  |  |
| --- | --- |
| **SetBadgeNumber (Number)** | Sets the number to show over the application icon on the Home Screen of the iOS device. If the Number passed as a parameter is 0, the red badge icon should disappear. |
| **iOSSetBadgeTextToTab (Text,TabIndex)** | Sets a text over the tab in the index passed as a parameter. This control is used for the [tabs of a Dashboard](https://wiki.genexus.com/commwiki/wiki?16098), it is not valid for the [tabs of a TabControl](https://wiki.genexus.com/commwiki/wiki?16800) which is enabled by making drag and drop from the toolbar. The index starts at 1 from left to right. |
| **iOSSetSelectedTabIndex (TabIndex)** | Sets the tab in the TabIndex position as active. The indexes start at 1 from left to right. |

### [Step 2. Coding Sample](#Step+2.+Coding+Sample)

This example uses a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) with 4-5 items and sets the Control to Tabs on the Dashboard properties.

Create the following [Panel object](https://wiki.genexus.com/commwiki/wiki?24829):

#### [Layout:](#Layout%3A)

`[imagen omitida: wiki id 19360]`

#### [Events:](#Events%3A)

```
Event 'iosSetBadgetext'
    Interop.IOSSetBadgeTextToTabIndex('test',2)
Endevent
```

```
Event 'iosSetTabIndex'
    Interop.IOSSetSelectedTabIndex(3)
Endevent
```

```
Event 'RemoveBadge'
    Interop.IOSSetBadgeTextToTabIndex("",2)
Endevent
```

```
Event 'iosSetBadgeNum'
    Interop.SetBadgeNumber(&varnum)
Endevent
```

```
Event 'iosSetBadge0'
    Interop.SetBadgeNumber(0)
Endevent
```

Add that Panel to the Dashboard and hit F5.

### [Step 3. Execution](#Step+3.+Execution)

SetBadgeNumber()  
Result:

`[imagen omitida: wiki id 19361]`

`[imagen omitida: wiki id 19362]`

iosSetBadgeText()  
Result:

`[imagen omitida: wiki id 19363]`

### [Step 4. Complement the Local and Push Notifications](#Step+4.+Complement+the+Local+and+Push+Notifications)

One of the most common uses of this feature is combined with [Local](https://wiki.genexus.com/commwiki/wiki?19294) and [Push](https://wiki.genexus.com/commwiki/wiki?19945) notifications. When a Notification is sent to the user, the badge number is automatically set to +1. So, when the user performs the action expected of the notification, the app should subtract one to the current badge number.

The subtraction is not automatically done yet, because the action performed after the notification has to be tracked by the application logic.

If this isn't done, the badge number over the app icon will never change and look like some notifications are pending.

**Notes:**

* In order to use the SetBadgeNumber method in iOS, you must include the remote notification background mode capability on the generated XCode project.
  + Since [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,), this feature can be added automatically by using [Background Modes property](https://wiki.genexus.com/commwiki/wiki?35408) with value "remote-notification".
  + For lower upgrades, you must call the RequestRemotenotificationsPermission method of [Permissions external object for Apple applications](https://wiki.genexus.com/commwiki/wiki?31311) before calling the SetBadgeNumber (see the example below).

    ```
    Event 'MyEventForSettingBadgeNumber'
              Composite
                      Permissions.RequestRemoteNotificationsPermission()
                      Interop.SetBadgeNumber(&Numeric)
              EndComposite
    EndEvent
    ```
  + When the [KB](https://wiki.genexus.com/commwiki/wiki?1836) uses [LocalNotifications external object](https://wiki.genexus.com/commwiki/wiki?19294) functionalities, since [GeneXus 15 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?33278,,) the permission will be generated automatically


|  |
| --- |
| **Backlinks** |
| [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) |
| [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) |

---
