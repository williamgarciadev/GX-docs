---
title: "Permissions external object for Android applications"
source_id: 50045
source_url: https://wiki.genexus.com/commwiki/wiki?50045
genexus_version: "18"
---

# Permissions external object for Android applications

The Permissions external object allows you to request runtime permission on Android applications.

|  |  |
| --- | --- |
|  |  |

## [**Properties**](#Properties)

## [**Methods**](#Methods)

### [**Request**](#Request)

Requests a permission from the user. Returns True if the answer is affirmative, or False otherwise. When the user had permission already, it immediately returns True. When the user has permission blocked, it automatically returns False.

There is the option of entering a text with the reason for requesting use of the permission.

**Return value:** [Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

**Parameters:**Permission, [VarChar(100)](https://wiki.genexus.com/commwiki/wiki?6778).

### [**RequestMany**](#RequestMany)

Enables the request of several permissions, and returns True when **all** permissions are granted. Otherwise it returns False.

**Return value:** [Boolean](https://wiki.genexus.com/commwiki/wiki?4374).

**Parameters:**Permission.

### [**GetStatus**](#GetStatus)

Returns information on the status of permissions.

**Return value:** [APIAuthorizationStatus](https://wiki.genexus.com/commwiki/wiki?39656).

**Parameters:**Permission.

## [**Domains**](#Domains)

**Permission**

Contains the permissions that may be requested.

* Location Background
* Location Coarse
* Location Fine
* Bluetooth
* Calendar
* Camera
* Contacts (Android Read/Write)
* Microphone
* Storage (Android Read/Write)
* Notification

## [**Examples**](#Examples)

```
Event 'Request'

&Permission = Permission.Camera

&Granted = GeneXus.SD.Permissions.Request(&Permission)

//Some code...

EndEvent
```

## [**Availability**](#Availability)

This external object is available as from [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/wiki?49301,,).

## [**Scope**](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

## [**See also**](#See+also)

* [Permissions external object for Apple applications](https://wiki.genexus.com/commwiki/wiki?31311)
