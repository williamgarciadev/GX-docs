---
title: "RemoteNotificationResult external object"
source_id: 39412
source_url: https://wiki.genexus.com/commwiki/wiki?39412
genexus_version: "18"
---

# RemoteNotificationResult external object

**Deprecated**: Since [GeneXus 15 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?33278,,). Replaced by [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687).

The RemoteNotificationResult external object encapsulates information about the delivering status to a specific device when a [remote notification](https://wiki.genexus.com/commwiki/wiki?18150,,) has been sent (by using [RemoteNotification.Send method](https://wiki.genexus.com/commwiki/wiki?39399)).

**Note**: This external object must be used dynamically (i.e. as a variable).

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

### [DeviceType property](#DeviceType+property)

The device type, based on [SmartDeviceType domain](https://wiki.genexus.com/commwiki/wiki?39399).

### [DeviceToken property](#DeviceToken+property)

The token (or identifier) of the [registered device](https://wiki.genexus.com/commwiki/wiki?18149).

## [Methods](#Methods)

It does not have any.

## [Events](#Events)

It does not have any.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | Smart Devices (iOS, Android) |

## [See also](#See+also)

* [HowTo: Sending Notifications to Smart Devices Applications](https://wiki.genexus.com/commwiki/wiki?18150,,)
* [RemoteNotifications external object](https://wiki.genexus.com/commwiki/wiki?39399)


|  |
| --- |
| **Backlinks** |
| [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [RemoteNotifications external object](https://wiki.genexus.com/commwiki/wiki?39399) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) |
| [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
