---
title: "HowTo: Use SD Geolocation Control in Smart Devices"
source_id: 16756
source_url: https://wiki.genexus.com/commwiki/wiki?16756
genexus_version: "18"
---

# HowTo: Use SD Geolocation Control in Smart Devices

**Deprecated**: Since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46873,,). Replaced by [Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309).

This document provides a brief overview about SD Geolocation and explains how to use it.

SD Geolocation is a control applicable to a geolocation field. This control will show the geolocation field over a map, indicating the position with a pin. It can be applied to an attribute from a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) based on [Geolocation domain](https://wiki.genexus.com/commwiki/wiki?14644) and also to a variable with same [domain](https://wiki.genexus.com/commwiki/wiki?14610).

### [Samples](#Samples)

**1.** Create a Transaction (called "TRNGeolocation") with two Attributes (Id and Description**)** as shown in the image.

`[imagen omitida: wiki id 16763]`

**2.** Apply the [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) pattern to the Transaction (for further information see [Applying Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975)).

`[imagen omitida: wiki id 16765]`

**3.** Change the [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) of the attribute "TRNGeolocationDescription" to SD Geolocation.

`[imagen omitida: wiki id 16774]`

**4.** Create the following dashboard and add the WorkWithDevicesTRNGeolocation as an item.

`[imagen omitida: wiki id 16770]`

Done!

**5.** Deploy your application on different devices (don't forget to set your dashboard as main object).

### [Android](#Android)

`[imagen omitida: wiki id 16758]` `[imagen omitida: wiki id 16759]`

`[imagen omitida: wiki id 16760]` `[imagen omitida: wiki id 16761]`

`[imagen omitida: wiki id 16762]`

### [iOS](#iOS)

`[imagen omitida: wiki id 16766]` `[imagen omitida: wiki id 16767]`

In this case, there's already an item on the list.

`[imagen omitida: wiki id 16768]`

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), 
[Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [See Also](#See+Also)

[Geolocation external object](https://wiki.genexus.com/commwiki/wiki?31274)  
[Geolocation - Show points near me](https://wiki.genexus.com/commwiki/wiki?16473)  
[Geolocation - Showing My Location](https://wiki.genexus.com/commwiki/wiki?16433)  
[HowTo: Solve Tracking with GeneXus](https://wiki.genexus.com/commwiki/wiki?20832)


|  |
| --- |
| **Backlinks** |
| [Category:Control Types](https://wiki.genexus.com/commwiki/wiki?20402) | [HowTo: Configure Google Places API in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?30810) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
