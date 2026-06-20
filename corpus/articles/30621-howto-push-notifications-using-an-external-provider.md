---
title: "HowTo: Push Notifications using an External Provider"
source_id: 30621
source_url: https://wiki.genexus.com/commwiki/wiki?30621
genexus_version: "18"
---

# HowTo: Push Notifications using an External Provider

External providers allow you to send Push Notifications to both
[Apple](https://wiki.genexus.com/commwiki/wiki?14917) and
[Android](https://wiki.genexus.com/commwiki/wiki?14453) devices on any platform.  
GeneXus supports push notifications from:

* [OneSignal](http://www.onesignal.com)
* [Jiguang](http://www.jiguang.cn/accounts/login/form)

**Advantages:**

* Infinite scalability (to send thousands of notifications per second)
* Free
* Control panel for managing users and send notifications
* No own infrastructure needed for Push
* Independence from Push Platforms

**Requirements:**

* Registration on the provider website is required.
* Additional configuration for Android and iOS.

### [Configuration Steps](#Configuration+Steps)

**1.** In the [Main object](https://wiki.genexus.com/commwiki/wiki?17817) turn on the [Enable notifications property](https://wiki.genexus.com/commwiki/wiki?19945).  
  
**2.** Register the application on the provider site and get the credentials.

**a.** [HowTo: Register an application to use OneSignal services](https://wiki.genexus.com/commwiki/wiki?33671)  
**b.** [HowTo: Register an application to use JPush services](https://wiki.genexus.com/commwiki/wiki?37021)

**3.** Set the [Notifications Provider property](https://wiki.genexus.com/commwiki/wiki?33670) with your desired provider and set the credentials.

### [Send notifications](#Send+notifications)

GeneXus provides a [built-in API](https://wiki.genexus.com/commwiki/wiki?31268) for sending notifications. Please refer to [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687).

### [Availability](#Availability)

* OneSignal applies since [GeneXus 15 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?33278,,). Those developers who use previous upgrades must download the [PushInterop](https://wiki.genexus.com/commwiki/wiki?30623,,) framework for [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,) and follow the instructions of GeneXus X Evolution 3 (see the previous version of this document). It is highly recommended to migrate your implementation to use this new mechanism.
* JPush applies since [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,).

### [Troubleshooting](#Troubleshooting)

* **OneSignal**
  + In-App Settings - Google Android "Mismatch SenderId".  
    Please check that the "Android Sender ID" property value (within the Main SD app) is correct.  
    Refer to this tutorial: [HowTo: Configure Push Notifications in Android Applications](https://wiki.genexus.com/commwiki/wiki?18147) just in case.

### [See Also](#See+Also)

[HowTo: Use a Device's Registration Service for Push Notifications](https://wiki.genexus.com/commwiki/wiki?18149)  
[HowTo: Register an application to use OneSignal services](https://wiki.genexus.com/commwiki/wiki?33671)  
[HowTo: Register an application to use JPush services](https://wiki.genexus.com/commwiki/wiki?37021)


|  |
| --- |
| **Backlinks** |
|
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [NotificationParameters external object](https://wiki.genexus.com/commwiki/wiki?39559) | [OneSignal - App ID property](https://wiki.genexus.com/commwiki/wiki?37492) | [OneSignal - REST API Key property](https://wiki.genexus.com/commwiki/wiki?37493) |
| [Push Notifications in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19945) | [RemoteNotifications external object](https://wiki.genexus.com/commwiki/wiki?39399) |

---
