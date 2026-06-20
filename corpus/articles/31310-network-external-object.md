---
title: "Network external object"
source_id: 31310
source_url: https://wiki.genexus.com/commwiki/wiki?31310
genexus_version: "18"
---

# Network external object

The Network external object allows you to check the devices' network status in order to have more information to take some actions. This API is often used in [Offline Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?22237) to determine the best moment to [perform a synchronization](https://wiki.genexus.com/commwiki/wiki?22266).

This external object must be used in a [Client-side Event](https://wiki.genexus.com/commwiki/wiki?24332) (like the [ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044)) because it is executed on the user's device and not on the server. Errors may occur if you use it in [Server-side Events](https://wiki.genexus.com/commwiki/wiki?24234).

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

### [ApplicationServerURL](#ApplicationServerURL)

It is a read-only property set automatically with the [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146) of the Smart Devices Generator.  
The property is then used by several methods explained below.

## [Methods](#Methods)

### [IsServerAvailable method](#IsServerAvailable+method)

Returns True if the device can access the specified server; otherwise, it returns False. It checks if a package can be routed to the desired URL host; note that no request is made to the current host. The server can be passed as an optional parameter in its URL. If the URL parameter is not present, then the method will check the connection to the server URL of the property ApplicationServerURL.

**Note:** In Android, the device makes an [HTTP connection](https://developer.android.com/reference/java/net/URLConnection#connect()) to the provided URL as part of the

```
IsServerAvailable
```

 method to check the availability of the server.

|  |  |
| --- | --- |
| **Return value** | Boolean |
| **Parameters** | [ Url:[URL](https://wiki.genexus.com/commwiki/wiki?15668) ] |

### [Type method](#Type+method)

Gets the connection type that the device has to a specific server. There are some servers that are only accessed by local networks.

|  |  |
| --- | --- |
| **Return value** | NetworkAPIConnectionType |
| **Parameters** | [ Url:[URL](https://wiki.genexus.com/commwiki/wiki?15668) ] |

### [TrafficBasedCost method](#TrafficBasedCost+method)

Returns true or false depending on whether the connection between the device and the server could cause a monetary cost to the device user.

|  |  |
| --- | --- |
| **Return value** | Boolean |
| **Parameters** | |  |  | | --- | --- | |  | [ Url:[URL](https://wiki.genexus.com/commwiki/wiki?15668) ] | |

### [SetApplicationServerURL](#SetApplicationServerURL)

It allows you to change the application URL dynamically. To do so, set the [Dynamic Services URL property](https://wiki.genexus.com/commwiki/wiki?20366) to True.

|  |  |
| --- | --- |
| **Return value** | None |
| **Parameters** | [ Url:[URL](https://wiki.genexus.com/commwiki/wiki?15668) ] |

Note: In iOS it is available as of [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?42129,,), and in Android as of GeneXus 16 upgrade 7.

## [Events](#Events)

### [NetworkStatusChanged event](#NetworkStatusChanged+event)

Notifies when the network status changes.

|  |  |
| --- | --- |
| **Input** | None |
| **Output** | None |

## [Domains](#Domains)

### [NetworkAPIConnectionType domain](#NetworkAPIConnectionType+domain)

This domain is defined to identify the device's connection type.  
It is based on Numeric(1) with the following enumerated values:

|  |  |
| --- | --- |
| **None** | No connection. |
| **Wifi** | Wi-Fi connection. |
| **WAN** | WAN connection. |

## [Scope](#Scope)

**Generators:**[Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

## [See Also](#See+Also)

[Coding your Data Synchronization programs](https://wiki.genexus.com/commwiki/wiki?22266)  
[Manual Synchronization Code Sample](https://wiki.genexus.com/commwiki/wiki?22543)


|  |
| --- |
| **Backlinks** |
| [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) |
| [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [HowTo: Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway](https://wiki.genexus.com/commwiki/wiki?35355) | [Table of contents:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) |
| [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) | [Specification Codes from spc0150 onwards](https://wiki.genexus.com/commwiki/wiki?6774) |

---
