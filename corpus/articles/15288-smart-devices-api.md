---
title: "Smart Devices API"
source_id: 15288
source_url: https://wiki.genexus.com/commwiki/wiki?15288
genexus_version: "18"
---

# Smart Devices API

This document is the API specification for [Smart Devices](https://wiki.genexus.com/commwiki/wiki?20427,,) development provided by GeneXus platform.

[Smart Devices](https://wiki.genexus.com/commwiki/wiki?20427,,) have powerful hardware and operating systems. You can take advantage of its features by using [External Objects](https://wiki.genexus.com/commwiki/wiki?17880) and [Procedure Objects](https://wiki.genexus.com/commwiki/wiki?6293), both packaged in a [GeneXus's built-in module](https://wiki.genexus.com/commwiki/wiki?31268). Also, you can create your own set of APIs and easily integrate them in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

**Warning**: [GeneXus's built-in module](https://wiki.genexus.com/commwiki/wiki?31268) is available as of [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,). Previous versions of GeneXus have a subset of these APIs in the *SmartDevicesApi*  folder (automatically imported when a Smart Device object is created).

[External Objects](https://wiki.genexus.com/commwiki/wiki?17880) are not the only alternative that allows integration with other device's features. Take a look at [Domains with Special Semantics](https://wiki.genexus.com/commwiki/wiki?14610), [User Controls](https://wiki.genexus.com/commwiki/wiki?15301) and [Extension Library concept](https://wiki.genexus.com/commwiki/wiki?33545).

|  |  |  |
| --- | --- | --- |
| **External objects** | | |
| **Module** | **Object** | **Description** |
| GeneXus.Client | [ClientInformation](https://wiki.genexus.com/commwiki/wiki?31271) | Access client device information. |
| [ClientStorage](https://wiki.genexus.com/commwiki/wiki?31272) | Stores information on the device. |
| [Socket](https://wiki.genexus.com/commwiki/wiki?41299) | Allows establishing, from the client, a bidirectional connection with the WebSocket Server |
| GeneXus.Common | [Analytics](https://wiki.genexus.com/commwiki/wiki?31415) | Measures the app usage by using an analytics provider. |
| [Clipboard](https://wiki.genexus.com/commwiki/wiki?31273) | Primitives for managing the device's clipboard. |
| [DynamicCall](https://wiki.genexus.com/commwiki/wiki?47056) | Setting the call options to a dynamically called object. |
| [Geolocation](https://wiki.genexus.com/commwiki/wiki?31274) | DEPRECATED - Access to GPS information. |
| [Log](https://wiki.genexus.com/commwiki/wiki?37872) | Write your own log messages in different levels of importance. |
| [Maps](https://wiki.genexus.com/commwiki/wiki?44309) | Provides several Location Services. |
| [Runtime](https://wiki.genexus.com/commwiki/wiki?33076) | Differentiates when the app executes on client or server side. |
| [CrashAnalytics](https://wiki.genexus.com/commwiki/wiki?55161) | Customizes and enhances crash reports in your mobile app by interacting with Firebase Crashlytics |
| [Server](https://wiki.genexus.com/commwiki/wiki?39589) | Manages caching from server. |
| GeneXus.Common.UI | [Progress](https://wiki.genexus.com/commwiki/wiki?39341) | Manages activity progress bar. |
| [Navigation](https://wiki.genexus.com/commwiki/wiki?32395) | Hides or displays content in some sections on the device's screen. |
| GeneXus.SD | [Actions](https://wiki.genexus.com/commwiki/wiki?31350) | A set of common actions (e.g. go home, return, save, etc). |
| [AppLifecycle](https://wiki.genexus.com/commwiki/wiki?42056) | Track application state changes. |
| [ARPreview](https://wiki.genexus.com/commwiki/wiki?42590) | Display 3D objects. |
| [Beacons](https://wiki.genexus.com/commwiki/wiki?27025) | Manages beacons through the device's bluetooth. |
| [Calendar](https://wiki.genexus.com/commwiki/wiki?39346) | Schedules end-user's tasks on its calendar. |
| [Contacts](https://wiki.genexus.com/commwiki/wiki?31276) | Manages end-user's contact on the device. |
| [DeepLink](https://wiki.genexus.com/commwiki/wiki?36160) | Manages deep links on the application. |
| [DeviceAuthentication](https://wiki.genexus.com/commwiki/wiki?39252) | Manages local authentication using biometrics sensors. |
| [Interop](https://wiki.genexus.com/commwiki/wiki?23734) | A set of miscellanous funcionalities (e.g. display messages or confirmations, send emails or SMS, etc.) |
| MapsOffline |  |
| [Network](https://wiki.genexus.com/commwiki/wiki?31310) | Checks device's network status. |
| [Printer](https://wiki.genexus.com/commwiki/wiki?48131) | Print files directly to a Bluetooth printer connected. |
| [RemoteConfig](https://wiki.genexus.com/commwiki/wiki?48160) | Change application parameters in runtime. |
| [Scanner](https://wiki.genexus.com/commwiki/wiki?31316) | Scans barcodes by using device's camera. |
| [Search](https://wiki.genexus.com/commwiki/wiki?39378,,) | Enhances search behaviors on the application. |
| [WebBrowser](https://wiki.genexus.com/commwiki/wiki?36384) | Handles embedded web browser actions. |
| GeneXus.SD.iOS | [Permissions](https://wiki.genexus.com/commwiki/wiki?31311) | Requests iOS permissions manually. |
| GeneXus.SD.Media | [Audio](https://wiki.genexus.com/commwiki/wiki?30041) | Manages audio streaming. |
| [AudioRecorder](https://wiki.genexus.com/commwiki/wiki?34096) | Manages audio recording. |
| [Camera](https://wiki.genexus.com/commwiki/wiki?31296) | Uses device's camera. |
| [Files](https://wiki.genexus.com/commwiki/wiki?44917) | Programmatically select files from your device. |
| [PhotoLibrary](https://wiki.genexus.com/commwiki/wiki?39397) | Access to device's photo library. |
| VideoOperations | Convert videos or reduce quality. |
| [LocalNotifications](https://wiki.genexus.com/commwiki/wiki?39554) | Triggers local notifications (or alerts). |
| [NotificationsConfiguration](https://wiki.genexus.com/commwiki/wiki?39411,,) | Configures remote push notifications by GeneXus's mechanism. |
| [NotificationParameters](https://wiki.genexus.com/commwiki/wiki?39559) | Settings for remote push notifications status by GeneXus's mechanism. |
| [RemoteNotificationResult](https://wiki.genexus.com/commwiki/wiki?39412) | Handles remote push notifications status by GeneXus's mechanism. |
| [RemoteNotifications](https://wiki.genexus.com/commwiki/wiki?39399) | Triggers remote notifications by using GeneXus's mechanism |
| GeneXus.SD.Offline | [Database](https://wiki.genexus.com/commwiki/wiki?45171) | Backup and restore the Offline Database. |
| GeneXus.SD.Store | [StoreManager](https://wiki.genexus.com/commwiki/wiki?31320) | Manage In App Purchases. |
|  | [StoreInterop](https://wiki.genexus.com/commwiki/wiki?53952) | Integrates and uses the ratings and reviews within their applications. |
| GeneXus.SD.Synchronization | [SynchronizationEvents](https://wiki.genexus.com/commwiki/wiki?31341) | Manages syncrhonization status of offline application. |
| GeneXus.Social | [Facebook](https://wiki.genexus.com/commwiki/wiki?38432) | Interacts with Facebook app. |
| [Share](https://wiki.genexus.com/commwiki/wiki?29800) | Shares content with third-party apps. |
| [Twitter](https://wiki.genexus.com/commwiki/wiki?39432) | Interacts with Twitter app. |

|  |  |  |
| --- | --- | --- |
| **Procedures** | | |
| **Module** | **New name** | **Description** |
| GeneXus.Synchronization | [OfflineEventReplicator](https://wiki.genexus.com/commwiki/wiki?26218) | Internally manage |
| Genexus.Common.Notifications | [AddDeviceGroups](https://wiki.genexus.com/commwiki/wiki?33687) | Adds a new target group for sending notifications by using an external provider. |
| Genexus.Common.Notifications | [AddDeviceTargetFilter](https://wiki.genexus.com/commwiki/wiki?33687) | Adds a new target filter for sending notifications by using an external provider. |
| Genexus.Common.Notifications | [RemoveDeviceGroups](https://wiki.genexus.com/commwiki/wiki?33687) | Removes a group that receives notifications by using an external provider. |
| Genexus.Common.Notifications | [RemoveDeviceTargetFilter](https://wiki.genexus.com/commwiki/wiki?33687) | Removes a filter that receives notifications by using an external provider. |
| Genexus.Common.Notifications | [SendEvent](https://wiki.genexus.com/commwiki/wiki?33687) | Sends a silent notification by using an external provider. |
| Genexus.Common.Notifications | [SendEventTargets](https://wiki.genexus.com/commwiki/wiki?33687) | Sends a silent notification to some targets by using an external provider. |
| Genexus.Common.Notifications | [SendNotification](https://wiki.genexus.com/commwiki/wiki?33687) | Sends a push notification by using an external provider |
| Genexus.Common.Notifications | [SendNotificationTarget](https://wiki.genexus.com/commwiki/wiki?33687) | Sends a push notification to some targets by using an external provider |


|  |
| --- |
| **Pages** |
| [Access Contacts Notes property](https://wiki.genexus.com/commwiki/wiki?46110) | [Actions external object](https://wiki.genexus.com/commwiki/wiki?31350) | [Analytics external object](https://wiki.genexus.com/commwiki/wiki?31415) |
| [Analytics external object (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54509) | [Analytics external object (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57371) | [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) |
| [AudioRecorder external object](https://wiki.genexus.com/commwiki/wiki?34096) | [Calendar external object](https://wiki.genexus.com/commwiki/wiki?39346) | [Camera external object](https://wiki.genexus.com/commwiki/wiki?31296) |
| [Camera external object (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53919) | [ClientInformation API external object (X Evolution 3)](https://wiki.genexus.com/commwiki/wiki?19948,ClientInformation+API+external+object+%28X+Evolution+3%29,) | [ClientInformation external object](https://wiki.genexus.com/commwiki/wiki?31271) |
| [ClientInformation.Id Property](https://wiki.genexus.com/commwiki/wiki?20198) | [ClientStorage external object](https://wiki.genexus.com/commwiki/wiki?31272) | [ClientStorage.Clear method](https://wiki.genexus.com/commwiki/wiki?24135) |
| [ClientStorage.Get method](https://wiki.genexus.com/commwiki/wiki?24134) | [ClientStorage.Remove method](https://wiki.genexus.com/commwiki/wiki?24136) | [ClientStorage.Set method](https://wiki.genexus.com/commwiki/wiki?24133) |
| [Clipboard external object](https://wiki.genexus.com/commwiki/wiki?31273) | [Clipboard.getText method](https://wiki.genexus.com/commwiki/wiki?23958) | [Clipboard.setText method](https://wiki.genexus.com/commwiki/wiki?23957) |
| [Contacts external object](https://wiki.genexus.com/commwiki/wiki?31276) | [CrashAnalytics external object](https://wiki.genexus.com/commwiki/wiki?55161) | [DeepLink external object](https://wiki.genexus.com/commwiki/wiki?36160) |
| [DeviceAuthentication external object](https://wiki.genexus.com/commwiki/wiki?39252) | [Facebook external object](https://wiki.genexus.com/commwiki/wiki?38432) | [Files external object](https://wiki.genexus.com/commwiki/wiki?44917) |
| [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) | [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) | [HowTo: In-app search in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?31862) |
| [HowTo: Open a Web Page in a New Browser Window from a Smart Devices Application](https://wiki.genexus.com/commwiki/wiki?18555) | [HowTo: Sending Notifications to Smart Devices Applications](https://wiki.genexus.com/commwiki/wiki?18150,HowTo%3A+Sending+Notifications+to+Smart+Devices+Applications,) | [HowTo: Solve Tracking with GeneXus](https://wiki.genexus.com/commwiki/wiki?20832) |
| [HowTo: Use a Progress Indicator in a Panel](https://wiki.genexus.com/commwiki/wiki?19338) | [HowTo: Use AddContact method from Contacts external object](https://wiki.genexus.com/commwiki/wiki?15792) | [HowTo: Use Audio in Smart Devices](https://wiki.genexus.com/commwiki/wiki?20114) |
| [HowTo: Use Badge operations in Apple](https://wiki.genexus.com/commwiki/wiki?19356) | [HowTo: Use Camera external object in GeneXus](https://wiki.genexus.com/commwiki/wiki?31298) | [HowTo: Use Camera external object in GeneXus for Native Mobile apps (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53920) |
| [HowTo: Use Confirm method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17334) | [HowTo: Use LocalNotifications external object in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?19294) | [HowTo: Use LocalNotifications external object in Native Mobile apps (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54591) |
| [HowTo: Use Msg method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17328) | [HowTo: Use PlaceCall method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17309) | [HowTo: Use PlayAudio method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17339) |
| [HowTo: Use PlayVideo method from Interop external object](https://wiki.genexus.com/commwiki/wiki?15986) | [HowTo: Use Radio Button in Panels](https://wiki.genexus.com/commwiki/wiki?18434) | [HowTo: Use RemoveContact method from Contacts external object](https://wiki.genexus.com/commwiki/wiki?15895) |
| [HowTo: Use Save method from Actions external object](https://wiki.genexus.com/commwiki/wiki?16015) | [HowTo: Use ScanBarcode method from Scanner external object in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?21661) | [HowTo: Use SendEmail method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17321) |
| [HowTo: Use SendEmailAdvanced method from Interop external object in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?18193) | [HowTo: Use SendMessage method from Interop external object](https://wiki.genexus.com/commwiki/wiki?15528) | [HowTo: Use SendSMS method from Interop external object](https://wiki.genexus.com/commwiki/wiki?17310) |
| [HowTo: Use the Cancel Method from Actions in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?18363) | [HowTo: Use the Return method from SDActions external object in SDApi for Smart Devices](https://wiki.genexus.com/commwiki/wiki?15836,HowTo%3A+Use+the+Return+method+from+SDActions+external+object+in+SDApi+for+Smart+Devices,) | [HowTo: Use ViewContact method from Contacts external object](https://wiki.genexus.com/commwiki/wiki?15856) |
| [HowTo: Using ClearCache Method From Interop in Smart Devices Api](https://wiki.genexus.com/commwiki/wiki?22580) | [HowTo: Using PhotoLibrary external object for Smart Devices](https://wiki.genexus.com/commwiki/wiki?26933) | [HowTo: Using ScanBarcode Method from Interop in SDApi for Smart Devices](https://wiki.genexus.com/commwiki/wiki?15882,HowTo%3A+Using+ScanBarcode+Method+from+Interop+in+SDApi+for+Smart+Devices,) |
| [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) | [Interop.CanOpen method](https://wiki.genexus.com/commwiki/wiki?23732) |
| [Interop.Open method](https://wiki.genexus.com/commwiki/wiki?23733) | [LocalNotifications external object](https://wiki.genexus.com/commwiki/wiki?39554) | [LocalNotifications external object (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54527) |
| [Log external object](https://wiki.genexus.com/commwiki/wiki?37872) | [Navigation external object](https://wiki.genexus.com/commwiki/wiki?32395) | [Network external object](https://wiki.genexus.com/commwiki/wiki?31310) |
| [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687) | [NotificationParameters external object](https://wiki.genexus.com/commwiki/wiki?39559) | [NotificationsConfiguration external object](https://wiki.genexus.com/commwiki/wiki?39411,NotificationsConfiguration+external+object,) |
| [Permissions external object for Apple applications](https://wiki.genexus.com/commwiki/wiki?31311) | [PhotoLibrary external object](https://wiki.genexus.com/commwiki/wiki?39397) | [Printer external object](https://wiki.genexus.com/commwiki/wiki?48131) |
| [Progress external object](https://wiki.genexus.com/commwiki/wiki?39341) | [Remote Notifications External Object](https://wiki.genexus.com/commwiki/wiki?39316) | [RemoteNotificationResult external object](https://wiki.genexus.com/commwiki/wiki?39412) |
| [RemoteNotifications external object](https://wiki.genexus.com/commwiki/wiki?39399) | [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076) | [Scanner external object](https://wiki.genexus.com/commwiki/wiki?31316) |
| [Server external object](https://wiki.genexus.com/commwiki/wiki?39589) | [Share external object](https://wiki.genexus.com/commwiki/wiki?29800) | [StoreManager external object](https://wiki.genexus.com/commwiki/wiki?31320) |
| [SynchronizationEvents external object](https://wiki.genexus.com/commwiki/wiki?31341) | [Twitter external object](https://wiki.genexus.com/commwiki/wiki?39432) |

---
