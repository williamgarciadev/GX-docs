---
title: "HowTo: Use a Device's Registration Service for Push Notifications"
source_id: 18149
source_url: https://wiki.genexus.com/commwiki/wiki?18149
genexus_version: "18"
---

# HowTo: Use a Device's Registration Service for Push Notifications

This document explains how to use a device's registration service for Push Notifications and provides a brief overview about it.

Every time an end-user executes a GeneXus application that has the [Enable Notifications property](https://wiki.genexus.com/commwiki/wiki?49799) enabled, the service configured in the [Registration Handler property](https://wiki.genexus.com/commwiki/wiki?22981) is automatically executed in order to register and store the device information to be used in the future to send messages to the device.

A [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) called *NotificationsRegistrationHandler* is included as a sample of this service. You can find it in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) under Root Module >  GeneXus > SD > Notificationswith a typical implementation.

```
Rules:
   parm(in:&DeviceType, in:&DeviceId, in:&DeviceToken, in:&DeviceName);

Code: 
   for each
      where DeviceType = &DeviceType
      where DeviceId  = &DeviceId   
      DeviceToken = &DeviceToken    
      DeviceName = &DeviceName      
   when none
      new
         DeviceType  = &DeviceType
         DeviceId = &DeviceId
         DeviceToken = &DeviceToken
         DeviceName = &DeviceName
      endnew
   endfor
```

The [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) must have these four parameters in order to retrieve the device information.

* &DeviceType : SmartDeviceType
* &DeviceId : Character(128)
* &DeviceToken : Character(1000)
* &DeviceName :Character(128).

After the execution of the service, information like the following is registered:

* **DeviceType** :  
     
  [Apple](https://wiki.genexus.com/commwiki/wiki?14917) or
  [Android](https://wiki.genexus.com/commwiki/wiki?14453)
* **DeviceId** :  
     8bb3ud27c7cce885b1c41a3cf5f5bd3m4b22w96d
* **DeviceToken** :  
  When the [Notifications Provider property](https://wiki.genexus.com/commwiki/wiki?33670) has a value different from "None", this token contains information about the device in a JSON format.  
  An example of these data (using OneSignal as Notification Provider) look as follows:

```
  {
       "DeviceToken": "PJy0nafLvZiXvbGlmYuidCpA7JY5ryuW30KoQmpOs=",
       "DeviceId": "8bb3ud27c7cce885b1c41a3cf5f5bd3m4b22w96d",
       "DeviceType": 1,
       "NotificationPlatform": "OneSignal",
       "NotificationPlatformId": fb508412-2f91-46b1-90e1-f052247d1f8c
   }
```

\*If the DBMS is *MySql*, *DeviceToken* must be defined as *VarChar(1000)*, not Char(1000), otherwise it won't record the entire Token

If no Notification Provider is used, the token should look as follows:  
    PJy0nafLvZiXvbGlmYuidCpA7JY5ryuW30KoQmpOs=

* **DeviceName** :  
     iPhone Mary

With this information, you can start [sending](https://wiki.genexus.com/commwiki/wiki?33687) messages to registered devices (those that use your application).

**Notes:**

* If you have a completely offline application, and you need this Registration Handler procedure to be generated offline exclusively, set [Main property](https://wiki.genexus.com/commwiki/wiki?11872) = False and [Connectivity Support property](https://wiki.genexus.com/commwiki/wiki?20911) = Offline
* Device registration does not work if you are prototyping with KBN (Knowledge Base Navigator) or simulators.
* The Registration Handler service is called when the application is opened.

### [Troubleshooting](#Troubleshooting)

#### [**1. Android devices are not being registered**](#1.+Android+devices+are+not+being+registered)

* Android Sender Id and/or Android Sender API Key properties from the main object are not set.
* Simulators without Google Play Services don't support Firebase, so they are not being registered. Use devices instead.

### [See Also](#See+Also)

[HowTo: Configure Push Notifications in Apple Applications](https://wiki.genexus.com/commwiki/wiki?17451)  
[HowTo: Configure Push Notifications in Android Applications](https://wiki.genexus.com/commwiki/wiki?18147)


|  |
| --- |
| **Backlinks** |
| [HowTo: Configure Push Notifications in Android Applications](https://wiki.genexus.com/commwiki/wiki?18147) | [HowTo: Configure Push Notifications in Android Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54521) |
| [HowTo: Configure Push Notifications in Apple Applications](https://wiki.genexus.com/commwiki/wiki?17451) | [HowTo: Configure Push Notifications in Apple Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54517) | [HowTo: Push Notifications using an External Provider](https://wiki.genexus.com/commwiki/wiki?30621) |
| [Push Notifications in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19945) | [Registration Handler property](https://wiki.genexus.com/commwiki/wiki?22981) | [RemoteNotificationResult external object](https://wiki.genexus.com/commwiki/wiki?39412) |
| [RemoteNotifications external object](https://wiki.genexus.com/commwiki/wiki?39399) |

---
