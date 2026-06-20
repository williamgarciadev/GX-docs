---
title: "GeneXus Core module"
source_id: 31268
source_url: https://wiki.genexus.com/commwiki/wiki?31268
genexus_version: "18"
---

# GeneXus Core module

GeneXus provides a set of built-in APIs, Structured Data Types, and Domains to manage abstract concepts and interact with different technologies, devices, sensors, etc.

They are currently read-only and encapsulated in modules, all under 'GeneXus'. You can find them under 'References' in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210), in the 'Domains' tool window, and in the 'Standard Variables' section.

`[imagen omitida: wiki id 31346]`

Main Benefits

* It is clear to all developers that these objects are maintained by GeneXus.
* Making them read-only avoids occasional errors and compatibility issues.
* Their implementation is already built and is also shipped built-in with GeneXus. Therefore, GeneXus does not need to build (specify, generate, compile) them on every KB/Version/Environment.

Some of them have not only been moved to a module but have also been renamed to improve usability. However, note that their internal identification (GUID) remains the same in all cases to minimize compatibility issues when migrating from previous versions (eg.: code that referenced "ClientInformation" now automatically references "GeneXus.Client.ClientInformation").

## [Renamed built-in objects](#Renamed+built-in+objects)

|  |  |
| --- | --- |
| **External objects** | |
| **Name** | **Module** |
| [ClientInformation](https://wiki.genexus.com/commwiki/wiki?31271) | GeneXus.Client |
| [ClientStorage](https://wiki.genexus.com/commwiki/wiki?31272) | GeneXus.Client |
| [ClientStorage](https://wiki.genexus.com/commwiki/wiki?31272) | GeneXus.Client |
| [Analytics](https://wiki.genexus.com/commwiki/wiki?31415) | GeneXus.Common |
| [Clipboard](https://wiki.genexus.com/commwiki/wiki?31273) | GeneXus.Common |
| [Geolocation](https://wiki.genexus.com/commwiki/wiki?31274) | GeneXus.Common |
| [Log](https://wiki.genexus.com/commwiki/wiki?37872) | GeneXus.Common |
| [Server](https://wiki.genexus.com/commwiki/wiki?39589) | GeneXus.Common |
| [Runtime](https://wiki.genexus.com/commwiki/wiki?33076) | GeneXus.Common |
| [Progress external object](https://wiki.genexus.com/commwiki/wiki?39341) | GeneXus.Common.UI |
| [Navigation](https://wiki.genexus.com/commwiki/wiki?32395) | GeneXus.Common.UI |
| [Actions](https://wiki.genexus.com/commwiki/wiki?31350) | GeneXus.SD |
| [Contacts](https://wiki.genexus.com/commwiki/wiki?31276) | GeneXus.SD |
| [Calendar](https://wiki.genexus.com/commwiki/wiki?39346) | GeneXus.SD |
| [DeepLink](https://wiki.genexus.com/commwiki/wiki?36160) | GeneXus.SD |
| [DeviceAuthentication](https://wiki.genexus.com/commwiki/wiki?39252) | GeneXus.SD |
| [Interop](https://wiki.genexus.com/commwiki/wiki?23734) | GeneXus.SD |
| [Network](https://wiki.genexus.com/commwiki/wiki?31310) | GeneXus.SD |
| [Beacons](https://wiki.genexus.com/commwiki/wiki?27025) | GeneXus.SD |
| [Scanner](https://wiki.genexus.com/commwiki/wiki?31316) | GeneXus.SD |
| [Search](https://wiki.genexus.com/commwiki/wiki?39378,,) | GeneXus.SD |
| [WebBrowser](https://wiki.genexus.com/commwiki/wiki?36384) | GeneXus.SD |
| [Permissions](https://wiki.genexus.com/commwiki/wiki?31311) | GeneXus.SD.iOS |
| [Audio](https://wiki.genexus.com/commwiki/wiki?30041) | GeneXus.SD.Media |
| [AudioRecorder](https://wiki.genexus.com/commwiki/wiki?34096) | GeneXus.SD.Media |
| [Camera](https://wiki.genexus.com/commwiki/wiki?31296) | GeneXus.SD.Media |
| [PhotoLibrary](https://wiki.genexus.com/commwiki/wiki?39397) | GeneXus.SD.Media |
| [LocalNotifications](https://wiki.genexus.com/commwiki/wiki?39554) | GeneXus.SD.Notifications |
| [Store](https://wiki.genexus.com/commwiki/wiki?31320) | GeneXus.SD.Store |
| [SynchronizationEvents](https://wiki.genexus.com/commwiki/wiki?31341) | GeneXus.SD.Synchronization |
| [Facebook](https://wiki.genexus.com/commwiki/wiki?38432) | GeneXus.Social |
| [Twitter](https://wiki.genexus.com/commwiki/wiki?39432) | GeneXus.Social |
| [Share](https://wiki.genexus.com/commwiki/wiki?29800) | GeneXus.Social |
| [WebNotifications](https://wiki.genexus.com/commwiki/wiki?22442) | GeneXus.Web.Notifications |

|  |  |
| --- | --- |
| **Structured Data Types** | |
| **Name** | **Module** |
| AnalyticsPurchase | GeneXus.Common |
| GeolocationInfo | GeneXus.Common |
| GeolocationProximityAlert | GeneXus.Common |
| Messages | GeneXus.Common |
| Configuration | Genexus.Common.Notifications |
| Delivery | Genexus.Common.Notifications |
| Event | Genexus.Common.Notifications |
| LocalizedText | Genexus.Common.Notifications |
| Notification | Genexus.Common.Notifications |
| Target | Genexus.Common.Notifications |
| ContactInfo | GeneXus.SD |
| LoginExternalAdditionalParameters | GeneXus.SD |
| BeaconInfo | GeneXus.SD |
| BeaconProximityAlert | GeneXus.SD |
| BeaconRegion | GeneXus.SD |
| BeaconState | Genexus.SD |
| ScannedBarcodes | GeneXus.SD |
| SearchScope | GeneXus.SD |
| MediaItem | GeneXus.SD.Media |
| MediaQueue | GeneXus.SD.Media |
| MediaQueueState | GeneXus.SD.Media |
| LocalNotificationsInfo | GeneXus.Notifications |
| PurchaseReceiptInformation | GeneXus.SD.Store |
| PurchaseResult | GeneXus.SD.Store |
| StoreProductCollection | GeneXus.SD.Store |
| SynchronizationEventResult | GeneXus.SD.Synchronization |
| SynchronizationEvent | GeneXus.SD.Synchronization |
| SynchronizationInfo | GeneXus.SD.Synchronization |
| NotificationInfo | GeneXus.Web.Notification |

|  |  |
| --- | --- |
| **Procedures** | |
| **Name** | **Module** |
| [OfflineEventReplicator](https://wiki.genexus.com/commwiki/wiki?26218) | GeneXus.Synchronization |
| [AddDeviceGroups](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications |
| [AddDeviceTargetFilter](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications |
| [RemoveDeviceGroups](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications |
| [RemoveDeviceTargetFilter](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications |
| [SendEvent](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications |
| [SendEventTargets](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications |
| [SendNotification](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications |
| [SendNotificationTarget](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications |

## [Built-in objects without changes (They are not read-only)](#Built-in+objects+without+changes+%28They+are+not+read-only%29)

The built-in objects listed below have not changed because their purpose is to be customized by the developer.  
These objects are under the GeneXus folder of the KB.

|  |  |  |
| --- | --- | --- |
| **Objects unchanged** | | |
| **Name** | **Located folder** | **Object type** |
| [Global Events](https://wiki.genexus.com/commwiki/wiki?30201) | /GeneXus/Common | External Object |
| NotificationsRegistrationHandler | /GeneXus/SD/Notifications | Procedure |
| ValidatePurchase | /GeneXus/SD/Store | Procedure |
| GxAfterEventReplicator | /GeneXus/SD/Synchronization | Procedure |
| GxOnPendingEventFailed | /GeneXus/SD/Synchronization | Procedure |
| AppMasterPage | /GeneXus/Web | Master Page |
| LinksList | /GeneXus/Web | Structured Data type |
| PromptMasterPage | /GeneXus/Web | Master Page |
| RecentLinks | /GeneXus/Web | Web Component |
| RwdMasterPage | /GeneXus/Web | Master Page |
| RwdPromptMasterPage | /GeneXus/Web | MasterPage |
| RwdRecentLinks | /GeneXus/Web | WebComponent |

## [Notes](#Notes)

[Semantic Domains](https://wiki.genexus.com/commwiki/wiki?17227) do not change their names, but they are distributed with the GeneXus module too.

### [Troubleshooting](#Troubleshooting)

1. When building, you may get "error: 'GeneXus' version 0.19 cannot be downloaded. Is it a built-in module? Try execute "genexus.exe /install" command. Otherwise, you need to update the module version to an accessible one."  
   Solution: Close GeneXus, execute genexus.exe /install, open GeneXus, then the menu Knowledge / Manage Modules, and install the highest available GeneXus module.
2. When importing, you may get "Cannot import '{0}', it is already defined in referenced module '{1}'".   
   Solution: That is not a problem. GeneXus is just preventing importing an object that is already in a referenced module. To get a newer version of that object you may ask the provider for it and install it using the Module Manager.


|  |
| --- |
| **Backlinks** |
| [Configuration.ExternalStorage External Object](https://wiki.genexus.com/commwiki/wiki?45913) | [Error handling in Synchronization.Send() operations](https://wiki.genexus.com/commwiki/wiki?25454) |
| [Features of Native Mobile App development that Angular generator still misses](https://wiki.genexus.com/commwiki/wiki?46456) |
| [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [HowTo: Push Notifications using an External Provider](https://wiki.genexus.com/commwiki/wiki?30621) | [HowTo: Use LocalNotifications external object in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?19294) | [HowTo: Use LocalNotifications external object in Native Mobile apps (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54591) |
| [Messages structured data type](https://wiki.genexus.com/commwiki/wiki?40335) | [Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376) | [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687) | [OAuth Module](https://wiki.genexus.com/commwiki/wiki?50438) |
| [Offline Data backup and restore](https://wiki.genexus.com/commwiki/wiki?45171) | [OfflineEventReplicator procedure](https://wiki.genexus.com/commwiki/wiki?26218) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |
| [Storage Provider API](https://wiki.genexus.com/commwiki/wiki?32087) | [When and how is the GeneXus module updated in a KB?](https://wiki.genexus.com/commwiki/wiki?47842) |

---
