---
title: "GeneXus Core module (GeneXus 18 Upgrade 2 or prior)"
source_id: 54413
source_url: https://wiki.genexus.com/commwiki/wiki?54413
genexus_version: "18"
---

# GeneXus Core module (GeneXus 18 Upgrade 2 or prior)

GeneXus provides a set of built-in APIs, Structured Data Types, and Domains to manage abstract concepts and interact with different technologies, devices, sensors, etc.

They are currently read-only and encapsulated in modules, all under one: 'GeneXus'. The developer can find them under 'References' in the 'KB Explorer', in the 'Domains' tool window, and in the 'Standard Variables' section.

`[imagen omitida: wiki id 31346]`

Main Benefits

* It is clear for all the developers that these objects are maintained by GeneXus
* Making them read-only avoids occasional errors and compatibility issues.
* Their implementation is already built and is also shipped built-in with GeneXus. So GeneXus does not need to build (specify, generate, compile) them on every KB/Version/Environment.

Some of them have not just been moved to a module but also been renamed to improve usability. But note: Their internal identification (GUID) remains the same in all cases to minimize compatibility issues when migrating from previous versions (eg.: code that referenced "ClientInformation" now automatically references "GeneXus.Client.ClientInformation" ).

## [Renamed built-in objects](#Renamed+built-in+objects)

|  |  |  |  |
| --- | --- | --- | --- |
| **External objects** | | | |
| **Previous name** | **New name** | **Module** | **As of** |
| ClientInformation | [ClientInformation](https://wiki.genexus.com/commwiki/wiki?31271) | GeneXus.Client | Release |
| ClientStorageAPI | [ClientStorage](https://wiki.genexus.com/commwiki/wiki?31272) | GeneXus.Client | Release |
| SDSession | [ClientStorage](https://wiki.genexus.com/commwiki/wiki?31272) | GeneXus.Client | Release |
| AnalyticsAPI | [Analytics](https://wiki.genexus.com/commwiki/wiki?31415) | GeneXus.Common | Release |
| Clipboard | [Clipboard](https://wiki.genexus.com/commwiki/wiki?31273) | GeneXus.Common | Release |
| GeoLocationAPI | [Geolocation](https://wiki.genexus.com/commwiki/wiki?31274) | GeneXus.Common | Release |
| - | [Log](https://wiki.genexus.com/commwiki/wiki?37872) | GeneXus.Common | Upgrade 11 |
| ServerAPI | [Server](https://wiki.genexus.com/commwiki/wiki?39589) | GeneXus.Common | Release |
| - | [Runtime](https://wiki.genexus.com/commwiki/wiki?33076) | GeneXus.Common | Release |
| ProgressIndicator | [Progress external object](https://wiki.genexus.com/commwiki/wiki?39341) | GeneXus.Common.UI | Release |
| - | [Navigation](https://wiki.genexus.com/commwiki/wiki?32395) | GeneXus.Common.UI | Release |
| SDActions | [Actions](https://wiki.genexus.com/commwiki/wiki?31350) | GeneXus.SD | Release |
| AddressBook | [Contacts](https://wiki.genexus.com/commwiki/wiki?31276) | GeneXus.SD | Release |
| Calendar | [Calendar](https://wiki.genexus.com/commwiki/wiki?39346) | GeneXus.SD | Release |
| - | [DeepLink](https://wiki.genexus.com/commwiki/wiki?36160) | GeneXus.SD | Upgrade 6 |
| - | [DeviceAuthentication](https://wiki.genexus.com/commwiki/wiki?39252) | GeneXus.SD | Upgrade 11 |
| Interop | [Interop](https://wiki.genexus.com/commwiki/wiki?23734) | GeneXus.SD | Release |
| NetworkAPI | [Network](https://wiki.genexus.com/commwiki/wiki?31310) | GeneXus.SD | Release |
| LocationAPI | [Beacons](https://wiki.genexus.com/commwiki/wiki?27025) | GeneXus.SD | Release |
| ScannerAPI | [Scanner](https://wiki.genexus.com/commwiki/wiki?31316) | GeneXus.SD | Release |
| - | [Search](https://wiki.genexus.com/commwiki/wiki?39378,,) | GeneXus.SD | Release |
| - | [WebBrowser](https://wiki.genexus.com/commwiki/wiki?36384) | GeneXus.SD | Upgrade 7 |
| IOSPermissions | [Permissions](https://wiki.genexus.com/commwiki/wiki?31311) | GeneXus.SD.iOS | Release |
| AudioAPI | [Audio](https://wiki.genexus.com/commwiki/wiki?30041) | GeneXus.SD.Media | Release |
| - | [AudioRecorder](https://wiki.genexus.com/commwiki/wiki?34096) | GeneXus.SD.Media | Upgrade 5 |
| CameraAPI | [Camera](https://wiki.genexus.com/commwiki/wiki?31296) | GeneXus.SD.Media | Release |
| PhotoLibraryAPI | [PhotoLibrary](https://wiki.genexus.com/commwiki/wiki?39397) | GeneXus.SD.Media | Release |
| LocalNotifications | [LocalNotifications](https://wiki.genexus.com/commwiki/wiki?39554) | GeneXus.SD.Notifications | Release |
| NotificationParamters | [NotificationParameters](https://wiki.genexus.com/commwiki/wiki?39559) | GeneXus.SD.Notifications | Release |
| Notifications | [RemoteNotifications](https://wiki.genexus.com/commwiki/wiki?39399) | GeneXus.SD.Notifications | Release |
| NotificationConfiguration | [NotificationsConfiguration](https://wiki.genexus.com/commwiki/wiki?39411,,) | GeneXus.SD.Notifications | Release |
| RemoteNotificationResult | [RemoteNotificationResult](https://wiki.genexus.com/commwiki/wiki?39412) | GeneXus.SD.Notifications | Release |
| StoreAPI | [Store](https://wiki.genexus.com/commwiki/wiki?31320) | GeneXus.SD.Store | Release |
| SynchronizationEventsAPI | [SynchronizationEvents](https://wiki.genexus.com/commwiki/wiki?31341) | GeneXus.SD.Synchronization | Release |
| Facebook | [Facebook](https://wiki.genexus.com/commwiki/wiki?38432) | GeneXus.Social | Release |
| TwitterAPI | [Twitter](https://wiki.genexus.com/commwiki/wiki?39432) | GeneXus.Social | Release |
| SharingAPI | [Share](https://wiki.genexus.com/commwiki/wiki?29800) | GeneXus.Social | Release |
| WebNotification | [WebNotifications](https://wiki.genexus.com/commwiki/wiki?22442) | GeneXus.Web.Notifications | Release |

|  |  |  |  |
| --- | --- | --- | --- |
| **Structured Data Types** | | | |
| **Previous name** | **New name** | **Module** | **As of** |
| AnalyticsPurchase | AnalyticsPurchase | GeneXus.Common | Release |
| GeoLocationInfo | GeolocationInfo | GeneXus.Common | Release |
| GeoLocationProximityAlert | GeolocationProximityAlert | GeneXus.Common | Release |
| Messages | Messages | GeneXus.Common | Release |
| - | Configuration | Genexus.Common.Notifications | Upgrade 3 |
| - | Delivery | Genexus.Common.Notifications | Upgrade 3 |
| - | Event | Genexus.Common.Notifications | Upgrade 3 |
| - | LocalizedText | Genexus.Common.Notifications | Upgrade 3 |
| - | Notification | Genexus.Common.Notifications | Upgrade 3 |
| - | Target | Genexus.Common.Notifications | Upgrade 3 |
| AddressBookContact | ContactInfo | GeneXus.SD | Release |
| LoginExternalAddionalParameters | LoginExternalAddionalParameters | GeneXus.SD | Release |
| BeaconInfo | BeaconInfo | GeneXus.SD | Release |
| BeaconProximityAlert | BeaconProximityAlert | GeneXus.SD | Release |
| BeaconRegion | BeaconRegion | GeneXus.SD | Release |
| BeaconState | BeaconState | Genexus.SD | Release |
| ScannedBarcodes | ScannedBarcodes | GeneXus.SD | Release |
| - | SearchScope | GeneXus.SD | Release |
| MediaItem | MediaItem | GeneXus.SD.Media | Release |
| MediaQueue | MediaQueue | GeneXus.SD.Media | Release |
| MediaQueueState | MediaQueueState | GeneXus.SD.Media | Release |
| LocalNotificationsInfo | LocalNotificationsInfo | GeneXus.Notifications | Release |
| RemoteNotification | RemoteNotification | GeneXus.Notifications | Release |
| PuchaseReceiptInformation | PurchaseReceiptInformation | GeneXus.SD.Store | Release |
| PuchaseResult | PurchaseResult | GeneXus.SD.Store | Release |
| StoreProductCollection | StoreProductCollection | GeneXus.SD.Store | Release |
| GxSyncrhoEventResultSDT | SynchonizationEventResult | GeneXus.SD.Synchronization | Release |
| GxSyncrhoEventSDT | SyncrhonizationEvent | GeneXus.SD.Synchronization | Release |
| GxSynchroInfoSDT | SynchronizationInfo | GeneXus.SD.Synchronization | Release |
| NotificationInfo | NotificationInfo | GeneXus.Web.Notification | Release |

|  |  |  |  |
| --- | --- | --- | --- |
| **Procedures** | | | |
| **Previous name** | **New name** | **Module** | **As of** |
| GxOfflineEventReplicator | [OfflineEventReplicator](https://wiki.genexus.com/commwiki/wiki?26218) | GeneXus.Synchronization | Release |
| - | [AddDeviceGroups](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications | Upgrade 3 |
| - | [AddDeviceTargetFilter](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications | Upgrade 3 |
| - | [RemoveDeviceGroups](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications | Upgrade 3 |
| - | [RemoveDeviceTargetFilter](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications | Upgrade 3 |
| - | [SendEvent](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications | Upgrade 3 |
| - | [SendEventTargets](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications | Upgrade 3 |
| - | [SendNotification](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications | Upgrade 3 |
| - | [SendNotificationTarget](https://wiki.genexus.com/commwiki/wiki?33687) | Genexus.Common.Notifications | Upgrade 3 |

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

## [Compatibility](#Compatibility)

* Refer to [GeneXus 15 Compatibility Section](https://wiki.genexus.com/commwiki/wiki?29813,,)

## [Notes](#Notes)

[Semantic Domains](https://wiki.genexus.com/commwiki/wiki?17227) do not change their names, but they are distributed with the GeneXus module too.

### [Troubleshooting](#Troubleshooting)

1. When building, you may get "error: 'GeneXus' version 0.19 cannot be downloaded. Is it a built-in module? Try execute "genexus.exe /install" command. Otherwise, you need to update the module version to an accessible one."  
   Solution: Close GeneXus, execute genexus.exe /install, open GeneXus, then the menu Knowledge / Manage Modules and install the highest available GeneXus module.
2. When importing, you may get "Cannot import '{0}', it is already defined in referenced module '{1}'".   
   Solution: That is not a problem. GeneXus is just preventing importing an object that is already in a referenced module. To get a newer version of that object you may ask the provider for it and install it using the Module Manager.
