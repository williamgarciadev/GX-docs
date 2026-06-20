---
title: "LocalNotifications external object (GeneXus 18 Upgrade 2 or prior)"
source_id: 54527
source_url: https://wiki.genexus.com/commwiki/wiki?54527
genexus_version: "18"
---

# LocalNotifications external object (GeneXus 18 Upgrade 2 or prior)

The LocalNotifications external object enables you to alert users of scheduled events or alarms in the background, with no servers required.

|  |  |
| --- | --- |
|  |  |

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

### [Properties](#Properties)

It does not have any.

### [Methods](#Methods)

#### [CreateAlerts method](#CreateAlerts+method)

Creates a set of local notifications (or alerts) by indicating when each of them will be triggered and the text which will be displayed. It returns 0 if the operation ends successfully.

|  |  |
| --- | --- |
| **Return value** | Numeric(5.0) |
| **Parameters** | alerts:LocalNotificationsInfo |

#### ListAlerts method

Lists every local notification (or alert) previously created.

|  |  |
| --- | --- |
| **Return value** | LocalNotificationsInfo |
| **Parameters** | None |

#### RemoveAlerts method

Removes a set of local notifications (or alerts), each of them identified by its triggered timestamp and its text. It returns 0 if the operation ends successfully.

|  |  |
| --- | --- |
| **Return value** | Numeric(5.0) |
| **Parameters** | alerts:LocalNotificationsInfo |

#### RemoveAllAlerts method

Removes every local notification (or alerts) from the device.  It returns 0 if the operation ends successfully.

|  |  |
| --- | --- |
| **Return value** | Numeric(5.0) |
| **Parameters** | None |

### LocalNotificationsInfo Structured Data Type

#### [Information about a local notification. It is a collection of the following pairs:](#Information+about+a+local+notification.+It+is+a+collection+of+the+following+pairs%3A)

* DateTime:[DateTime](https://wiki.genexus.com/commwiki/wiki?7370)  
  When the local notification will be triggered. If you do not set this field (leave it empty), the notification will be triggered instantly.
* Text:[VarChar(128)](https://wiki.genexus.com/commwiki/wiki?6778)  
  The text displayed on the local notification.

### [See Also](#See+Also)

[HowTo: Use LocalNotifications external object in Native Mobile apps](https://wiki.genexus.com/commwiki/wiki?19294)
