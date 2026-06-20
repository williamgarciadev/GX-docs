---
title: "External Objects for Native Mobile Applications"
source_id: 17880
source_url: https://wiki.genexus.com/commwiki/wiki?17880
genexus_version: "18"
---

# External Objects for Native Mobile Applications

The implementation of [External object](https://wiki.genexus.com/commwiki/wiki?5669)s for Native Mobile Applications can be used to solve any combination of the following:

* Execute code within User-events for online applications.
* Be integrated in the generated offline code; for Procedures; Start, Refresh and Load events from Offline Panels.
* Execute online code on the server-side.

For Native Mobile execution of an External Object, the appropriate implementations must be provided.

In the case of an External Object that will be called from offline generated code, the following properties section are needed

`[imagen omitida: wiki id 33864]`

The implementation also changes depending on the target platform; check the following links:

[External Object for Android](https://wiki.genexus.com/commwiki/wiki?17878)  
[External Object for iOS Devices](https://wiki.genexus.com/commwiki/wiki?18072)

### [Considerations](#Considerations)

InOut parameters are not supported, all parameters are considered as In. To return more than one value, use a SDT object.


|  |
| --- |
| **Backlinks** |
| [Audio external object](https://wiki.genexus.com/commwiki/wiki?30041) | [Extension Library concept for Extending GeneXus for Native Mobile](https://wiki.genexus.com/commwiki/wiki?33545) | [HowTo: Debug User Control for Apple](https://wiki.genexus.com/commwiki/wiki?15905) |
| [HowTo: Use Audio in Smart Devices](https://wiki.genexus.com/commwiki/wiki?20114) | [HowTo: Using ClearCache Method From Interop in Smart Devices Api](https://wiki.genexus.com/commwiki/wiki?22580) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [Remote Notifications External Object](https://wiki.genexus.com/commwiki/wiki?39316) | [RemoteNotifications external object](https://wiki.genexus.com/commwiki/wiki?39399) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) |
| [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
