---
title: "Notification Provider API"
source_id: 33687
source_url: https://wiki.genexus.com/commwiki/wiki?33687
genexus_version: "18"
---

# Notification Provider API

This API is part of [GeneXus built-in modules](https://wiki.genexus.com/commwiki/wiki?31268) and provides a set of facilities for a GeneXus's developer to send push notifications through some [external notification provider](https://wiki.genexus.com/commwiki/wiki?33670). It allows registered devices management and sending mechanisms for a single device or a group of them.

`[imagen omitida: wiki id 36353]`

## [Domains](#Domains)

#### [**NotificationBadgeType**(2)](#NotificationBadgeType+%282%29)

Possible behaviors of Appearance.Badge field of Notification SDT.

|  |  |  |
| --- | --- | --- |
|  | **Value** | **Description** |
|  | *None* | Leaves the badge count unaffected on the application icon. |
|  | *SetTo* | Sets the badge count on the application icon to the number specified on "Badge" field. |
|  | *Increase* | Adds the "Badge" field number to the badge count on the application icon (a negative number will decrease it). |

#### [**FilterRelationType**](#FilterRelationType)

Possibles relational operators between keys and values.

|  |  |  |
| --- | --- | --- |
|  | **Value** | **Description** |
|  | *Exists* | It is true when there exists a key defined. |
|  | *NotExists* | It is true when a defined key does not exist. |
|  | *Equal* | It is true when the key and value are equals. |
|  | *NotEqual* | It is true when the key and value are not equals. |
|  | *Greater* | It is true when the key is greater than value. |
|  | *Less* | It is true when the key is less than value. |

#### **FilterOperation**

Possible binary logical operations.

|  |  |  |
| --- | --- | --- |
|  | **Value** | **Description** |
|  | *OR* | At least one condition must be satisfied. |
|  | *AND* | Both conditions must be satisfied. |

#### **TargetType**

Target alternatives for sending notifications

|  |  |  |
| --- | --- | --- |
|  | **Value** | **Description** |
|  | *Everybody* | Sends a notification to the default "All" segment of OneSignal. This means that every registered device will receive the notification. |
|  | *Devices* | Sends a notification individually to each device using the OneSignal-specific API called "[CreateNotification](https://documentation.onesignal.com/reference/create-notification#send-to-specific-devices)". |
|  | *Groups* | Sends a notification to the devices that have the specified TAG. This means that only registered devices that belong to a certain group receive the notification. The notification is filtered by [OneSignal Tags](https://documentation.onesignal.com/docs/add-user-data-tags), and the "[CreateNotification Based on Filters](https://documentation.onesignal.com/reference/create-notification#send-to-users-based-on-filters)" API is used. |
|  | *Targets* | Sends a notification to devices that have the given TAG and meet certain filters. It is also resolved using OneSignal Tags, but in this case, filters can be applied to send the notification only to certain devices of a given TAG. |

**Note**: Keep in mind that the OneSignal API does not allow sending notifications to [Segments](https://documentation.onesignal.com/docs/segmentation) created via the OneSignal Console and that the OneSignal Free Plan has a limit of 2 TAGS .

#### **PushNotificationPriority**

The priority of the notification.

|  |  |  |
| --- | --- | --- |
|  | **Value** | **Description** |
|  | *Normal* | Do not wake up the device if it is in doze mode. |
|  | *High* | Wake up the device if it is in doze mode. |

## [Structured data types](#Structured+data+types)

### [**Configuration**](#Configuration)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| ApplicationId | | | Character(100) | [OPTIONAL] Smart device main object name |
| Properties (1) | | | <collection> |  |
|  | | Item | ConfigurationProperty | Set a contextual property of  [Notifications Provider property](https://wiki.genexus.com/commwiki/wiki?33670) dinamically. |
| Debug | | |  |  |
|  | Debug | | Boolean | Enables a debug mode for inspecting messages through a proxy server.  Default: False |
|  | Proxy | | *Substructure* |  |
|  |  | Host | Character(20) | Server name or IP for the proxy. |
|  |  | Port | Numeric(6.0) | Server port number. |
| Advanced | | | *Substructure* |  |
|  | | BackCompatibility | Boolean | Enables compatibility mode for Android/iOS older versions.  Default: False |

### [**ConfigurationProperty**(1)](#ConfigurationProperty%281%29)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| PropertyName | | | Character(100) | The property name.   For example,  - [OneSignal - App ID property](https://wiki.genexus.com/commwiki/wiki?37492) must be "APP\_ID"  - [OneSignal - REST API Key property](https://wiki.genexus.com/commwiki/wiki?37493) must be "REST\_API\_KEY" |
| PropertyValue | | | <collection> | The property value associated with that property name. |

### [**Delivery**](#Delivery)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| Priority | | | PushNotificationPriority | (Android-only)  Indicates the priority of the notification.   Default: High |
| Expiration | | | Numeric(18.0) | Time in seconds that the notification provider tries to send the message.  Default: 0 (no expiration) |

### [**Event**](#Event)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| *Name* | | | Character(100) | Name of the event defined in the smart device main object which receives the notification. |
| *Parameter* | | | <*Collection*> | [OPTIONAL] Set of parameter sent with the notification. |
|  | *Name* | | Character(100) | Name of a variable in the smart device main object that will be used as a parameter of the notification. |
|  | *Value* | | Character(100) | Value for the parameter sent to the event on the client-side. |

### [**LocalizedText**](#LocalizedText)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Field** | | | **Domain** | **Description** |
| *DefaultText* | | | Character(100) | Text used when there is any localized item. |
| *Text* | | | <*Collection*> | [OPTIONAL] Set of text by languages (localized). |
|  | *Language* | | Character(100) | Language name for which the text is written. (Supported Languages Names: Spanish, English, Portuguese, Chinese, Japanese, Arabic) |
|  | *Text* | | Character(100) | Text written in the language defined above. |

### [**Notification**](#Notification)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Field** | | | | **Domain** | **Description** |
| *Id* | | | | Character(20) | [OPTIONAL] Assigns an identification to the sent notification and allows to rewrite it if it necessary by sending it again with the same Id. |
| *Title* | | | | LocalizedText | The title content of the notification. |
| *Text* | | | | LocalizedText | The text content (below the title) of the notification. |
| *Appearance* | | | | *Substructure* | [OPTIONAL] UI customization. |
|  | *Badge* | | | Character(4) | (iOS-only)  A numeric character to set a badge in the application icon |
|  | *BadgeType*(2) | | | NotificationBadgeType | Behavior of "Badge" field. It can be "None", "Set to" or "Increase" (in this case, negative values will decreaste badge number). |
|  | *Icon* | | |  |  |
|  |  | *Large* | | Url | (Android-only)  Url for an image resource that will be used. |
|  |  | *Small* | | Character(100) | (Android-only)  Name of an Image object embedded in the KB used for a small icon in the notification.  Some restrictions apply, see *Notification Icon* section on [Images in Panels](https://wiki.genexus.com/commwiki/wiki?31379)  The [Android Asset Studio tool](http://romannurik.github.io/AndroidAssetStudio/icons-notification.html#source.type=image&source.space.trim=1&source.space.pad=0&name=ic_stat_icono_96) by romannuric may be useful. |
|  | *Sound* | | | *Substructure* |  |
|  |  | *Sound* | | Boolean | Enables the sound when the notification arrives at the end-user.  Default: True |
|  |  | *CustomSound* | | Character(100) | Name of a project embedded custom sound.  This option is for advanced users, if it's empty, the app will use the default platform sound. |
|  | Channel | | | Character(100) | The Android Oreo Notification Category to send the notification under. |
|  | Picture | | | Character(100) | (Android-only)  Picture to display in the expanded view. Can be a drawable resource name or a URL. |
| *Actions* | | | | *Substructure* |  |
|  | | *DefaultAction* | | *Substructure* | Default action that will be executed on Notification Tapping. |
|  | |  | *Event* | Event | Settings for the default action that will be executed when the end user taps on the notification. |
|  | | *CustomUIActions* | | <*Collection*> | Typically when a user receives a notification, there is only a single action available - tapping on the notification. CustomUIActions allow more than one action to be taken on a notification, allowing for greater interactivity within notifications. [See example here](https://documentation.onesignal.com/docs/action-buttons) |
|  | |  | *Event* | Event | Configuration for the secondary action. |
|  | |  | *Id* | Character(20) | An Id for the custom secondary action. |
|  | |  | *Text* | LocalizedText | Text shown with the option. |
|  | |  | *Icon* | Character(100) | Name of an Image object in the KB. |
| *Advanced* | | | | *Substructure* |  |
|  | | Attachment | | <*Collection*> | (iOS-only) [OPTIONAL] Set of rich content (like media, e.g. videos in mp4 format). Must be a public URL resource. |
|  | |  | Type | Character(100) | Any identifier for the resource (e.g. myvideo.mp4). |
|  | |  | URL | Url | The link to the media resource. |
|  | | Group | | *Substructure* | (Android-only) [OPTIONAL]. For stacking Push Notification. |
|  | |  | GroupId | Character(100) | An identifier for stacking notifications in the same box. |
|  | |  | GroupMessage | LocalizedText | Text to be shown when more than one message in the same group arrives to the smart device. |
|  | | Template | | Character(100) | Use a template you setup on One Signal dashboard. You can override the template values by sending other parameters with the request.  This option is useful to personalize many aspects of the notification message, like the icon, sound, color, priority, category, etc. directly from the dashboard.  The template is the UUID found in the URL when viewing a template on One Signal dashboard. Example: be4a8044-bbd6-11e4-a581-000c2940e62c |

### [**Target**](#Target)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Field** | | | | **Domain** | **Description** |
| *TargetType* | | | | TargetType | Indicates which are the target devices determining which of the following collections will be used. |
| *Device* | | | | <*Collection*> | [OPTIONAL] Applies when TargetType is Devices |
|  | | *DeviceToken* | | Character(500) | The DeviceToken of the target device in the set. |
| *Group* | | | | <*Collection*> | [OPTIONAL] Applies when TargetType is Groups and the collection is understood as a disjunction of groups (joined with ORs) |
|  | | *Name* | | Character(100) | Name of the group previously added with AddDeviceGroup procedure. |
| *Filter* | | | | <*Collection*> |  |
|  | | *Name* | | Character(100) | Name of a filter key previously added with AddDeviceTargetFilter procedure. |
|  | | *Value* | | Character(100) | Value associated with the filter key. |
|  | | *Relation* | | FilterRelationType | Relation that associates the Name or Name and Value fields.  Default: Exists. |
|  | | *Operator* | | FilterOperation | Relation of the current item condition with the next one (the last item ignores this field).  Default: AND |

## [Procedures](#Procedures)

#### [**AddDeviceGroups**](#AddDeviceGroups)

Associates a set of groups or categories that a device belongs.

|  |  |  |
| --- | --- | --- |
|  | **Parameters** | *Configuration*:SDT(Configuration), *DeviceToken*:Character(500), *Groups*:Collection(Character(20)) |
|  | **Returns** | *Messages*:SDT(Messages), *Success*:Boolean |

#### **RemoveDeviceGroups**

Disassociates a set of groups or categories from a device.

|  |  |  |
| --- | --- | --- |
|  | **Parameters** | *Configuration*:SDT(Configuration), *DeviceToken*:Character(500), *Groups*:Collection(Character(20)) |
|  | **Returns** | *Messages*:SDT(Messages), *Success*:Boolean |

#### **AddDeviceTargetFilter**

Associates a filter name/value to a device.

|  |  |  |
| --- | --- | --- |
|  | **Parameters** | Configuration:SDT(Configuration), *DeviceToken*:Character(500), *FilterName*:Character(20), *FilterValue*:Character(20) |
|  | **Returns** | *Messages*:SDT(Messages), *Success*:Boolean |

#### **RemoveDeviceTagetFilter**

Disassociates a filter name/value of a device.

|  |  |  |
| --- | --- | --- |
|  | **Parameters** | *Configuration*:SDT(Configuration), *DeviceToken*:Character(500), *FilterName*:Character(20), *FilterValue*:Character(20) |
|  | **Returns** | *Messages*:SDT(Messages), *Success*:Boolean |

#### **SendEvent**

Executes an event on a specific device with delivery preferences.

|  |  |  |
| --- | --- | --- |
|  | **Parameters** | *Configuration*:SDT(Configuration), *DeviceToken*:Character(500), *NotificationEvent*:Event, *Delivery*:Delivery |
|  | **Returns** | *Messages*:SDT(Messages), *Success*:Boolean |

#### **SendEventTargets**

Executes an event on a set of target devices with delivery preferences.

|  |  |  |
| --- | --- | --- |
|  | **Parameters** | *Configuration*:SDT(Configuration), *Target*:Target, *Event*:Event, *Delivery*:Delivery |
|  | **Returns** | *Messages*:SDT(Messages), *Success*:Boolean |

#### **SendNotification**

Sends a push notification to a specific device with delivery preferences.

|  |  |  |
| --- | --- | --- |
|  | **Parameters** | *Configuration*:SDT(Configuration), *DeviceToken*:Character(500), *NotificationMessage*:Notification, *Delivery*:Delivery |
|  | **Returns** | *Messages*:SDT(Messages), *Success*:Boolean |

#### **SendNotificationTargets**

Sends a push notification to a set of target devices with delivery preferences.

|  |  |  |
| --- | --- | --- |
|  | **Parameters** | *Configuration*:SDT(Configuration), *Target*:Target, *NotificationMessage*:Notification, *Delivery*:Delivery |
|  | **Returns** | *Messages*:SDT(Messages), *Success*:Boolean |

#### **SetDeviceTargetMultipleFilters (3)**

Associates a list of filters (name/value collection) to a device.

|  |  |  |
| --- | --- | --- |
|  | **Parameters** | Configuration:SDT(Configuration), *DeviceToken*:Character(500), *FilterTags*:Properties |
|  | **Returns** | *Messages*:SDT(Messages), *Success*:Boolean |

This method is only valid for the OneSignal [Notifications Provider](https://wiki.genexus.com/commwiki/wiki?33670).

## [Sample](#Sample)

Consider that the smart device application's main object is called "MySDApp" and it has the following event defined:

```
Event 'NotificationAction'
     msg(&msg,status) 
EndEvent
```

**Note**: The '*status*' flag on msg function allows the developer to write messages and then inspect them in the [application log](https://wiki.genexus.com/commwiki/wiki?37846) when [Default Log Level property](https://wiki.genexus.com/commwiki/wiki?33333) has *Debug* value.

**Warning**: The event defined in the main app (e.g. 'NotificationAction') cannot contain any command, function or control that includes UI (such as msg, confirm, etc). Remember that this kind of notifications can arrive with the device locked, with the app running in *background mode*, or even when the app *not running*. However, the developer can trigger UI actions if the app is running in *foreground**mode,* but first, the developer must check such state by using the [Interop.ApplicationState property](https://wiki.genexus.com/commwiki/wiki?23734).

Then, from the web-backend, we can write a source code as follows:

*Variables*:

&TheNotification : *Notification, GeneXus.Common.Notifications*  
&TheNotificationDelivery: *Delivery, GeneXus.Common.Notifications*  
&TheNotificationConfiguration : *Configuration, GeneXus.Common.Notifications*

*Source*:

```
&TheNotification.Title.DefaultText = "GeneXus"
&TheNotification.Text.DefaultText  = "Notification Provider API"
&TheNotification.Actions.DefaultAction.Event.Name = "NotificationAction" // Declared in the SD Main object
&TheNotification.Actions.DefaultAction.Event.Parameters.FromJson('[{"Name":"msg","Value":"Hello dear user!"}]')
&TheNotification.Appearance.Icon.Small = !"GX15IconKB"

&TheNotificationDelivery.Expiration = 3000 
&TheNotificationDelivery.Priority   = PushNotificationPriority.Normal

&TheNotificationConfiguration.ApplicationId = !"MySDApp"
   
GeneXus.Common.Notifications.SendNotification(
     &TheNotificationConfiguration,
     DeviceToken, // Target device token
     &TheNotification, 
     &TheNotificationDelivery, 
     &OutMessages,
     &IsSuccessful
)
```

The, when the above code is executed, the device will receive a notification like this:

|  |  |
| --- | --- |
| **Android** | **iOS** |
|  |  |

and if the end user taps on it, the msg command will be print in the console a message saying "Hello dear user!".

#### [Notifications to devices with certain tags](#Notifications+to+devices+with+certain+tags)

If you want to send the previous notification to devices that have certain tags already defined, you can use the *SendNotificationTargets* procedure with the *Target* parameter.

Suppose you have added the tag 'User Type' with the value 'Student' throughout the *AddDeviceTargetFilter* procedure, for those devices that correspond to student users.

Now, to send a notification to those devices, use this code:

```
&TargetFilter = new()
&TargetFilter.Name = !'User Type'
&TargetFilter.Value = !'Student'
&Target.TargetType = TargetType.Targets
&Target.Targets.Add(&TargetFilter)
SendNotificationTargets(&NotificationConfiguration, &Target, &Notification, &NotificationDelivery, &Messages, &Success)
```

## [Notes](#Notes)

* The iOS platform always uses the image set in [Apple Application Icon property](https://wiki.genexus.com/commwiki/wiki?31379) as the notification icon, unlike Android that uses those set in [Android Notification Icon property](https://wiki.genexus.com/commwiki/wiki?31379) and can use a different image for the notification message by the Appearance.Icon field on the Notification SDT.
* In iOS, if the developer wants to download content when the app is in background mode (e.g. a video attached to the notification), it is necessary to include the 'remote-notification' value to the [Background Modes property](https://wiki.genexus.com/commwiki/wiki?35408).
* As of [Genexus 15 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?38023,,), when the developer uses any of the Send methods with OneSignal provider, the Messages parameter will return one item with the response payload in a JSON string in its "description" field. Such JSON includes the notification Id and the quantity recipients.  
  For example,  
  {"id":"5263x49t-ss31-436r-942k-638h111d9g2a","recipients":1}

## [Troubleshooting](#Troubleshooting)

* If the developer removes a device from the provider's console (e.g. OneSignal), the device is still associated with the identifier provided by the provider. In such case, uninstall the application from the device and reinstall it in order to generate a new identifier in the provider platform.
* [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?33798,,) fixes an issue when using more than two filter targets in the Target SDT.  
  For more information, refer to [SAC#41070](https://www.genexus.com/es/developers/websac?data=41070;;)
* Since Android 13 (API 33) it's recommended to set the property [Device Refistration Mode](https://wiki.genexus.com/commwiki/wiki?37295) to Manual and use the exo Permissions to request the notifications permission. Ref.: [SAC #52694](https://www.genexus.com/en/developers/websac?data=52694;;).

### [Push Provider was not specified. Please set a Push Provider](#Push+Provider+was+not+specified.+Please+set+a+Push+Provider)

When sending a notification the following error occurs:

```
Unknown error processing: Push Provider was not specified. Please set a Push Provider
```

Make sure the webapp folder includes the CloudServices.config file (specifically \WEB-INF\CloudServices.config) with valid a notification configuration. If you are running the process in batch mode, the input file should be located in the current working directory. For Java, the input file should be located where "System.getProperty("user.dir")" points to, as this property can be set to specify the directory where the input file is located.

## [FAQ](#FAQ)

* When I build my project that uses One signal, GeneXus gives me the following error.

  ```
  ld: framework not found Pods_OneSignalNotificationServiceExtension
  clang: error: linker command failed with exit code 1 (use -v to see invocation)
  ```

  **Cause**: As of [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,), the generated iOS project is based on [extension libraries](https://wiki.genexus.com/commwiki/wiki?36340).  
  **Solution**: Open the *\*.xcworkspace* file (instead of *\*.xcodeproj*) on the Mac computer.

## [Scope](#Scope)

**Objects:**[Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475)  
**Generators:**[.NET](https://wiki.genexus.com/commwiki/wiki?49815,,), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

## [Availability](#Availability)

This API is available as of [GeneXus 15 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?33278,,)

(1)Available as of [GeneXus 15 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?37491,,)  
(2) Available as of [GeneXus 15 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?38845,,)  
(3) Available as of [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,)


|  |
| --- |
| **Backlinks** |
| [Background Modes property](https://wiki.genexus.com/commwiki/wiki?35408) |
| [GeneXus Cognitive API - Process procedure](https://wiki.genexus.com/commwiki/wiki?41042) | [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [HowTo: Configure Push Notifications in Android Applications](https://wiki.genexus.com/commwiki/wiki?18147) |
| [HowTo: Configure Push Notifications in Android Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54521) | [HowTo: Configure Push Notifications in Apple Applications](https://wiki.genexus.com/commwiki/wiki?17451) | [HowTo: Configure Push Notifications in Apple Applications (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54517) |
| [HowTo: Push Notifications using an External Provider](https://wiki.genexus.com/commwiki/wiki?30621) | [HowTo: Register an application to use OneSignal services](https://wiki.genexus.com/commwiki/wiki?33671) | [HowTo: Use a Device's Registration Service for Push Notifications](https://wiki.genexus.com/commwiki/wiki?18149) |
| [Messages structured data type](https://wiki.genexus.com/commwiki/wiki?40335) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Notifications Provider property](https://wiki.genexus.com/commwiki/wiki?33670) |
| [OneSignal - App ID property](https://wiki.genexus.com/commwiki/wiki?37492) | [OneSignal - REST API Key property](https://wiki.genexus.com/commwiki/wiki?37493) | [Remote Notifications External Object](https://wiki.genexus.com/commwiki/wiki?39316) |
| [RemoteNotificationResult external object](https://wiki.genexus.com/commwiki/wiki?39412) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
