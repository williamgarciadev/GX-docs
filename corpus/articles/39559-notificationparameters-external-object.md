---
title: "NotificationParameters external object"
source_id: 39559
source_url: https://wiki.genexus.com/commwiki/wiki?39559
genexus_version: "18"
---

# NotificationParameters external object

**Warning**: This external object has been discontinued in [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853). Since this feature relied on a deprecated implementation by Apple and Google that is no longer functional, it has been removed from the GeneXus module. Read [HowTo: Push Notifications using an External Provider](https://wiki.genexus.com/commwiki/wiki?30621).

The NotificationParameter external object allows you to set parameters when [sending remote notifications](https://wiki.genexus.com/commwiki/wiki?18150,,), which is added to [RemoteNotification.Events substructure](https://wiki.genexus.com/commwiki/wiki?39399).

**Note**: This external object must be used dynamically (i.e. as a variable).

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

It does not have any.

## [Methods](#Methods)

### [SetParameter method](#SetParameter+method)

Set a notification parameter by indicating a key (or name) and its value.  
The *name* parameter must match with the name of a variable used on the event that attends the remote notification on the client-side (Panel or WorkWith object for smart devices).

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | name:Character(100), value:Character(200) |

## [Events](#Events)

It does not have any.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | Smart Devices (iOS, Android) |

## [See also](#See+also)

* [HowTo: Sending Notifications to Smart Devices Applications](https://wiki.genexus.com/commwiki/wiki?18150,,)


|  |
| --- |
| **Backlinks** |
| [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [RemoteNotifications external object](https://wiki.genexus.com/commwiki/wiki?39399) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) |
| [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
