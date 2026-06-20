---
title: "RemoteNotifications external object"
source_id: 39399
source_url: https://wiki.genexus.com/commwiki/wiki?39399
genexus_version: "18"
---

# RemoteNotifications external object

**Warning**: This external object has been discontinued in [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853). Since this feature relied on a deprecated implementation by Apple and Google that is no longer functional, it has been removed from the GeneXus module. Read [HowTo: Push Notifications using an External Provider](https://wiki.genexus.com/commwiki/wiki?30621).

In order to receive notifications, the devices must be registered before using the device registration structure mentioned in [this article](https://wiki.genexus.com/commwiki/wiki?18149). The [Push Notifications in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?19945) are sent using the [External Objects for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?17880) called RemoteNotifications.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

### [ErrorCode property](#ErrorCode+property)

Gives the error code of the delivered notification. For instance:

* 200: Deliver success.
* 400: Deliver error on client-side.
* 500: Deliver error on server-side.

### [ErrorDescription property](#ErrorDescription+property)

Gives an error description. It is empty when no error occurs.

## [Methods](#Methods)

### [Call method](#Call+method)

Sends a notification. It has poor performance for batch sending, use Send method instead.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | ApplicationId:Character(128), DeviceType:SmartDeviceType, DeviceToken:Character(255), AlertMessage:Character(128) |

### [IOSSetBadge method](#IOSSetBadge+method)

Set the badge number on the application icon in a target iOS device.  
This action is done by indicating the application identifier, the device token (or device identifier), the badge number and optionally the path to a custom sound. It returns 0 if the operation has executed successfully.

|  |  |
| --- | --- |
| **Return value** | Numeric(5.0) |
| **Parameters** | ApplicationId:Character(128), DeviceToken:Character(255), BadgeNumber:Numeric(5.0), Sound:Character(128) |

### [IOSResetBadge method](#IOSResetBadge+method)

Reset the badge of the application icon in a target iOS device. It returns 0 if the operation has executed successfully.

|  |  |
| --- | --- |
| **Return value** | Numeric(5.0) |
| **Parameters** | ApplicationId:Character(128), DeviceToken:Character(255) |

### [CallAction method](#CallAction+method)

Sends a notification to a specific user-defined event (or action) with parameters already set. It has poor performance for batch sending, use Send method instead.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | ApplicationId:Character(128), DeviceType:SmartDeviceType, DeviceToken:Character(255), AlertMessage:Character(128), ActionName:Character(128), Parameters:[NotificationParameters](https://wiki.genexus.com/commwiki/wiki?39559) |

### [OpenSession method](#OpenSession+method)

Indicates which will be the main object that receives the notification.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | ApplicationId:Character(128) |

### [Add method](#Add+method)

Adds a new notification (based on RemoteNotification SDT).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | RemoteNotification:RemoteNotification |

### [Send method](#Send+method)

Sends the notification to the target device (previously set).

|  |  |
| --- | --- |
| **Return value** | Collection( [RemoteNotificationResult](https://wiki.genexus.com/commwiki/wiki?39412) ) |
| **Parameters** | None |

### SetConfiguration method

Allows you to set your notification preferences at runtime.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | ApplicationId:Character(128), Configuration:[NotificationsConfiguration](https://wiki.genexus.com/commwiki/wiki?39411,,) |

## [Events](#Events)

It does not have any.

## [Domains](#Domains)

### [SmartDeviceType domain](#SmartDeviceType+domain)

Indicates Smart Devices platforms.

|  |  |
| --- | --- |
| **Android** | Android device |
| **Blackberry** | Blackberry device (not longer supported in GeneXus 15) |
| **iOS** | iOS device |
| **Windows** | Windows Phone device (not longer supported in GeneXus 15) |

### [ExecutionEvent](#ExecutionEvent)

Indicates how the notification will be executed.

|  |  |
| --- | --- |
| **OnLaunchByUser** | The notification will be lanched by the user. |
| **OnNotificationArrive** | The notification will be launched when the notification arrives. |

PushNotificationPriority

The priority of the notification.

|  |  |
| --- | --- |
| **Normal** | Do not wake up the device if it is in doze mode. |
| **High** | Wake up the device if it is in doze mode. |

## [Structured Data Types](#Structured+Data+Types)

### [RemoteNotification](#RemoteNotification)

Describes a target device with its settings.

* DeviceType: SmartDeviceType  
  For indicating the target device type.
* DeviceToken: Character(256)  
  For indicating the target device identifier (value when it is [registered](https://wiki.genexus.com/commwiki/wiki?18149)).
* Title:Character(127)  
  The notification title.
* Message:Character(127)  
  The notification message.
* Icon:Image  
  The notification icon.
* Sound:Character(20)  
  The audio filename (must be included manually to the Android/iOS project).
* Badge:Character(3)  
  For setting the application badge on iOS devices.
* Event  
  + Name:Character(100)  
    The event/action name on the client-side (Panel or WorkWith for Smart Devices event name)
  + Execution:EventExecution  
    Indicates how the notification will be executed.
  + Parameters: Collection  
    - Name:Character(100)  
      The parameter name. It must be the name of a variable on the client-side (Panel or WorkWith for Smart Devices).
    - Value:Character(100)  
      The parameter value.
  + Delivery
    - Priority:PushNotificationPriority  
      For indicating the priority of the notification.

## [Notes](#Notes)

* The event defined in the main app with OnNotificationArrive mode cannot contain any command, function or control that includes UI (such as msg, confirm, etc). Remember that this kind of notifications can arrive with the device locked, with the app running on *background*, and even when the app *not running*. However, this can be done if the app is running on *foreground*(the developer must check it through [Interop.ApplicationState property](https://wiki.genexus.com/commwiki/wiki?23734)).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | Smart Devices (iOS, Android) |

## [Availability](#Availability)

Add, Send and SetConfiguration methods are only available for .NET as of [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

## [See also](#See+also)

* [HowTo: Sending Notifications to Smart Devices Applications](https://wiki.genexus.com/commwiki/wiki?18150,,)


|  |
| --- |
| **Backlinks** |
| [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [NotificationParameters external object](https://wiki.genexus.com/commwiki/wiki?39559) |
| [RemoteNotificationResult external object](https://wiki.genexus.com/commwiki/wiki?39412) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
