---
title: "Purpose Strings properties group"
source_id: 32755
source_url: https://wiki.genexus.com/commwiki/wiki?32755
genexus_version: "18"
---

# Purpose Strings properties group

This group of properties is available for Main Smart Device objects and is located under the Apple/Permissions properties group.

As of iOS 10, Apple forces developers to indicate the *usage reason* of device features (e.g. GPS, microphone, calendar, etc.).  
This decision bets in favor of the user's privacy, allowing them to choose when some feature is allowed for use or not.

The effect for the end user is a message displayed on the screen saying that the app is trying to use some feature for the reasons described by the developer.  
`[imagen omitida: wiki id 32764]`

## [Properties](#Properties)

By default, any of these properties are empty. Their values are strings indicating the purpose of usage for each feature used by the developer (it must be set).

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Usage description property** | **It must be set if the app...** | **Required as of...** | **GeneXus uses it for...** | **Available as of [GX15](https://wiki.genexus.com/commwiki/wiki?28265,,)**  **...** | **Available as of [GXEv3](https://wiki.genexus.com/commwiki/wiki?20247,,) ...** |
| **Apple Music** | Access the user's media library. | iOS 10.0 | N/A | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |
| **Bluetooth Peripherical** | Uses Bluetooth device. | iOS 10.0 | N/A | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |
| **Calendars** | Access the user's calendar. | iOS 10.0 | [Calendar external object](https://wiki.genexus.com/commwiki/wiki?39346) | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |
| **Camera** | Uses the camera device. | iOS 10.0 | [Camera external object](https://wiki.genexus.com/commwiki/wiki?31296), [Scanner external object](https://wiki.genexus.com/commwiki/wiki?31316), [Scanner control](https://wiki.genexus.com/commwiki/wiki?15310), [Editable Image data type](https://wiki.genexus.com/commwiki/wiki?15204), [Ediatable Video data type](https://wiki.genexus.com/commwiki/wiki?16608) | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |
| **Contacts** | Access the user's contacts. | iOS 10.0 | [Contacts external object](https://wiki.genexus.com/commwiki/wiki?31276) | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |
| **Health** **Share** | Reads the user's health data. | iOS 10.0 | N/A | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |
| **Health Update** | Makes changes to the user's health data. | iOS 10.0 | N/A | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |
| **Home** **Kit** | Access the user's HomeKit configuration. | iOS 10.0 | N/A | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |
| **Location** **Always** | Access the user's location at all times ([Read more](https://wiki.genexus.com/commwiki/wiki?27084)). | iOS 8.0 | [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274), [Map control](https://wiki.genexus.com/commwiki/wiki?5029) | Release | Upgrade 2 |
|  |  |  |  |  |  |
| **Location Always And When In Use** | Access the user's location at all times and when it is used. Substitution of "Location Always usage description" as of iOS 11. | iOS 11.0 | [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274), [Map control](https://wiki.genexus.com/commwiki/wiki?5029) | Upgrade 7 | - |
|  |  |  |  |  |  |
| **Location When** **In Use** | Access the user's location while it is used ([Read more info](https://wiki.genexus.com/commwiki/wiki?27085)). | iOS 8.0 | [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274), [Map control](https://wiki.genexus.com/commwiki/wiki?5029) | Release | Upgrade 2 |
|  |  |  |  |  |  |
| **Microphone** | Uses the microphone device. | iOS 10.0 | [Editable Audio data type](https://wiki.genexus.com/commwiki/wiki?16529), [AudioRecorder external object](https://wiki.genexus.com/commwiki/wiki?34096), [Camera external object (RecordVideo method)](https://wiki.genexus.com/commwiki/wiki?31296) | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |
| **Motion** | Uses the accelerometer device. | iOS 10.0 | N/A | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |
| **NFC Scan** | Uses the NFC sensor. | iOS 11.0 | N/A | Upgrade 7 | - |
|  |  |  |  |  |  |
| **Photo Library** | Access the user's photo library. | iOS 10.0 | [PhotoLibrary external object](https://wiki.genexus.com/commwiki/wiki?39397), [Editable Image data type](https://wiki.genexus.com/commwiki/wiki?15204), [Ediatable Video data type](https://wiki.genexus.com/commwiki/wiki?16608). As of [GeneXus 16 upgrade 5](https://wiki.genexus.com/commwiki/wiki?43446,,) it is necessary for [Camera external object](https://wiki.genexus.com/commwiki/wiki?31296) also. | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |
| **Photo Library Additions** | Write permission for photos and videos. | iOS 11.0 | [PhotoLibrary external object (Save and SaveVideo methods)](https://wiki.genexus.com/commwiki/wiki?39397). | Upgrade 7 | - |
|  |  |  |  |  |  |
| **Remainders** | Uses the user's remainders | iOS 10.0 | N/A | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |
| **Siri** | Send data to Siri. | iOS 10.0 | N/A | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |
| **Speech Recognition** | Send data to Apple's speech recognition. | iOS 10.0 | N/A | Upgrade 1 | Upgrade 11 |
|  |  |  |  |  |  |

Column value "N/A" means there is not built-in GeneXus, but can be applied if the developer implements a custom User Controls or External Objects that requires that permission.

**Warning**: Developers who incorporate any of **built-in User Controls or External Objects** in their Knowledge Base must set the appropriate Usage Description property. In the same way, it must be set when developers use **custom User Controls or External Objects**.

## [Notes](#Notes)

* A warning message like this will be displayed if the developer uses location services but this property is not set.  
  warning: In iOS 10.0 or later, a value for one of these properties is required when you use location services. ('% Usage Description' of <Menu|Panel> for Smart Devices instance '%')  
  The iOS version may vary depending on which XCode version is used. Most of them are required as of iOS 10.0.
* As of [Genexus 15 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?36355,,) the message is similar to:  
  warning: In iOS 11.0 or later, 'Location When In Use usage description' property value is required when you use location services. See descriptions of these properties: ‘Location When In Use’, 'Location Always' and 'Location Always and When In Use'.

## [Troubleshooting](#Troubleshooting)

If the appropriate Usage Description is not set, the behavior when the application is executed changes by GeneXus version because the iOS project is different:

|  |  |
| --- | --- |
| **GeneXus Evolution 3** | **GeneXus 15** |
| Application crash. XCode indicates a message:  "*The app's Info.plist must contain an <feature\_key\_name> key with a string  value explaining to the user how the app uses this data*" | The application displays a pop-up message:  "*<feature> usage description not found*" |

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Panel for Smart Devices](https://wiki.genexus.com/commwiki/wiki?24829), [Work With for Smart Devices](https://wiki.genexus.com/commwiki/wiki?15974), [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) |
| **Level** | [Main object](https://wiki.genexus.com/commwiki/wiki?17817) |
| **SD Generators** | iOS |
| **Languages** | .NET, Java |

## [Availability](#Availability)

This group of properties is available as of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,) upgrade 11 / [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,) upgrade 1.


|  |
| --- |
| **Backlinks** |
| [Bonjour Services property](https://wiki.genexus.com/commwiki/wiki?46590) |
| [HowTo: Use Location Proximity Alerts](https://wiki.genexus.com/commwiki/wiki?25194) | [Local Network Usage Description property](https://wiki.genexus.com/commwiki/wiki?46589) | [Location Always Usage Description property](https://wiki.genexus.com/commwiki/wiki?27084) | [Location When In Use Usage Description property](https://wiki.genexus.com/commwiki/wiki?27085) |
| [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) | [Permissions external object for Apple applications](https://wiki.genexus.com/commwiki/wiki?31311) |

---
