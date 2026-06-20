---
title: "Smart Devices API (GeneXus 18 Upgrade 3 or prior)"
source_id: 55174
source_url: https://wiki.genexus.com/commwiki/wiki?55174
genexus_version: "18"
---

# Smart Devices API (GeneXus 18 Upgrade 3 or prior)

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
