---
title: "Permissions external object for Apple applications"
source_id: 31311
source_url: https://wiki.genexus.com/commwiki/wiki?31311
genexus_version: "18"
---

# Permissions external object for Apple applications

The Permissions external object allows you to request runtime permission on [Apple](https://wiki.genexus.com/commwiki/wiki?14917) applications.

|  |  |
| --- | --- |
|  |  |

### [Properties](#Properties)

#### [UserTrackingPermissionStatus property](#UserTrackingPermissionStatus+property)

The tracking authorization status that is current for the application.

Returns a value of the [APIAuthorizationStatus domain](https://wiki.genexus.com/commwiki/wiki?39656) depending on the authorization status of the [AppTrackingTransparency setting](https://wiki.genexus.com/commwiki/wiki?48327,,).

This property is available as from [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/wiki?47659,,).

### [Methods](#Methods)

Any method can receive any parameter and does not return any information. Their only purpose is to request permissions from users.

**Note**: According to the [Apple documentation](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649527-requestauthorization), the end-user can grant or deny permission for the interactions requested by the app, and the system stores the responses. So if the end-user denies permission first but then decided to grant them, they will have to configure it from the application. It will not be possible to use these methods for setting those permissions again. The methods ask for permission when invoked, as long as the app hasn't asked for permission before.

#### [RequestUserNotificationsPermission method](#RequestUserNotificationsPermission+method)

Requests permission to alert the user. Typically, you make this request if your app uses local or push notifications to alert the user regarding new information involving your app.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

#### [RequestLocationPermissionWhenInUse method](#RequestLocationPermissionWhenInUse+method)

Requests permission to use location services while the app is in the foreground.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

#### [RequestLocationPermissionAlways method](#RequestLocationPermissionAlways+method)

Requests permission to use location services whenever the app is running.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

#### [RequestRemoteNotificationsPermission method](#RequestRemoteNotificationsPermission+method)

Request permission to use remote notifications.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | None |

**Warning**: The **RequestRemoteNotificationPermission** method is deprecated, use **RequestUserNotificationsPermission** instead.

#### [RequestUserTrackingPermission method](#RequestUserTrackingPermission+method)

Request permission to the user to collect tracking information.

See [AppTrackingTransparency in iOS](https://wiki.genexus.com/commwiki/wiki?48327,,) for more information.

This methods is available as from [GeneXus 17 upgrade 3](https://wiki.genexus.com/commwiki/wiki?47659,,).

### [Events](#Events)

It does not have any.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917) |

### [See Also](#See+Also)

[Purpose Strings properties group](https://wiki.genexus.com/commwiki/wiki?32755)


|  |
| --- |
| **Backlinks** |
| [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) |
| [HowTo: Use Badge operations in Apple](https://wiki.genexus.com/commwiki/wiki?19356) | [HowTo: Use LocalNotifications external object in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?19294) | [HowTo: Use LocalNotifications external object in Native Mobile apps (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54591) | [Permissions external object for Android applications](https://wiki.genexus.com/commwiki/wiki?50045) |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
