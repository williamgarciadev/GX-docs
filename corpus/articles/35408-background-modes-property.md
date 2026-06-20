---
title: "Background Modes property"
source_id: 35408
source_url: https://wiki.genexus.com/commwiki/wiki?35408
genexus_version: "18"
---

# Background Modes property

Specifies the background modes supported by the application.

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

iOS imposes some limitations on the functionality that an application can use when running in the background unless the developer explicitly indicates the features required to run when the application is not active (e.g. audio playback, when the end user is executing another app or the device is blocked).

The Background Modes property allows the GeneXus developer to indicate which background features are required by the application. This property is available for Smart Device Main objects, under the iOS > Permissions group.

### [Values](#Values)

Every value corresponds to a string indicating the name of the functionality that the developer wants to execute in background mode.

Some of the available background modes correspond to GeneXus functionality and need to be added depending on the features used in the application. Some other background modes have no mapping to GeneXus features but are also supported in case the applications use a [User Control](https://wiki.genexus.com/commwiki/wiki?18330) or [External Object](https://wiki.genexus.com/commwiki/wiki?18072) that requires them.

The following values are supported by GeneXus features, and should be added in the cases described below:

|  |  |
| --- | --- |
| **audio** | Play or record audio in background mode.  Can be used for [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041), [AudioController control](https://wiki.genexus.com/commwiki/wiki?31046), [AudioRecorder external object](https://wiki.genexus.com/commwiki/wiki?34096), [iPad Video player in Picture-in-Picture mode](https://wiki.genexus.com/commwiki/wiki?15986). |
| **location** | Get location updates when the device location changes.  Can be used for [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) ([Tracking](https://wiki.genexus.com/commwiki/wiki?20832)). |
| **remote-notification** | Download and process content when a silent push notification arrives.  Can be used for [OneSignal API](https://wiki.genexus.com/commwiki/wiki?33687) when the push notification includes media content (such as video). |

It is not supported natively by GeneXus but could be required by a [custom External Object](https://wiki.genexus.com/commwiki/wiki?18072) or [custom User Control](https://wiki.genexus.com/commwiki/wiki?18330) developer for iOS.

|  |  |
| --- | --- |
| **voip** | Use the Internet to make and receive phone calls. |
| **newsstand-content** | Download and process magazine or newspaper content. |
| **external-accessory** | Update data from a hardware accessory. |
| **bluetooth-central** | Update data from a Bluetooth accessory. |
| **bluetooth-peripheral** | Communicate through peripheral Bluetooth. |
| **fetch** | Download and process small content regularly. |
| **processing** | A class for scheduling tasks run by submitting task requests that launch your app in the background. [Apple - BGTaskScheduler Doc](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler). This property is available as from [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,) |

These values can be composed by adding a ',' (comma). For example, suppose that the application needs to execute the following features when running in background mode:

* audio playback
* remote notifications
* fetching content

Then, the value of this property should be:

Background Modes property = audio,remote-notification,fetch

### [Notes](#Notes)

For previous versions of GeneXus, this process must be done manually from the generated XCode project as follows:

|  |  |
| --- | --- |
| **By XCode** | **By GeneXus template** |
| 1) Locate the "Capabilities" tab.  2) Enable the "Background Modes" switch.  3) Check the proper value. For example, the "Audio, AirPlay and Picture in Picture" option enables the 'audio' value. | 1) Locate the *MainName-Info.plist* in the *<GeneXus\_installation>\iOS\Templates\iOS\_Genexus* directory, and open it.  2) Add the entry *UIBackgroundModes* with an array of string values (an entry for each property value desired). For example, in case that developer wants to enable the 'audio' value, include it as a <string> value   ``` <key>UIBackgroundModes</key>  <array>     <string>audio</string> </array> ``` |

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Availability](#Availability)

This property is available since [GeneXus 15 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?34646,,).

### [See Also](#See+Also)

* [Apple Documentation. Section: Declaring Your App’s Supported Background Tasks](https://developer.apple.com/library/content/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/BackgroundExecution/BackgroundExecution.html).


|  |
| --- |
| **Backlinks** |
| [Audio Controller control](https://wiki.genexus.com/commwiki/wiki?31046) | [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) |
| [Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274) | [Geolocation external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55149) | [HowTo: Solve Tracking with GeneXus](https://wiki.genexus.com/commwiki/wiki?20832) |
| [HowTo: Use Audio in Smart Devices](https://wiki.genexus.com/commwiki/wiki?20114) | [HowTo: Use Badge operations in Apple](https://wiki.genexus.com/commwiki/wiki?19356) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) | [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687) |

---
