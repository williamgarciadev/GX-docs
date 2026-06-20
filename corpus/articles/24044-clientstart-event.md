---
title: "ClientStart event"
source_id: 24044
source_url: https://wiki.genexus.com/commwiki/wiki?24044
genexus_version: "18"
---

# ClientStart event

Defines a set of actions to be performed when the object starts running. It is a [Client-side Event](https://wiki.genexus.com/commwiki/wiki?24332) that takes place before the Server Events ([Start](https://wiki.genexus.com/commwiki/wiki?8043), [Refresh](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8195,,), and [Load](https://wiki.genexus.com/commwiki/wiki?8188)).

Since it is a Client-side Event, it has the same possibilities and limitations as any other Client-side Event.

**Important:** To initialize the application layout it is recommended to use [Navigation Start Events](https://wiki.genexus.com/commwiki/wiki?25668) instead of the ClientStart event because it may cause unwanted behavior for some [Navigation Styles](https://wiki.genexus.com/commwiki/wiki?16229).

### [Syntax](#Syntax)

**Event ClientStart**  
*Event\_code*  
**EndEvent**  
  
**Where:**  
*Event\_code*  
   Code associated with the event.

### [Description](#Description)

The object parameters are available on this event.

The variables of this event are available for the rest of the events (that is, you can have a grid filtered by a variable assigned in the ClientStart Event).

This event is ALWAYS executed regardless of the specified [security schema](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?20744,,).

### [Samples](#Samples)

If you need to know the user's location before loading a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), you can call the [Geolocation API](https://wiki.genexus.com/commwiki/wiki?21763):

```
Event ClientStart
       &DeviceLocation = GeoLocationAPI.GetMyLocation(10,10,true,true)
EndEvent
```

### [Considerations about ClientStart Event in Slide Navigation Style](#Considerations+about+ClientStart+Event+in+Slide+Navigation+Style)

In applications using [Slide Navigation Style](https://wiki.genexus.com/commwiki/wiki?21285), the behavior of the ClientStart event differs between Android and iOS:

* **Android:** The ClientStart event of the Slide Panel is triggered each time a new panel is loaded in the main target. This occurs because the Slide Panel is recreated for each new navigation.
* **iOS:** The ClientStart event is triggered only once when the Slide Panel is initially loaded. It does not trigger again for subsequent navigations.

**Notes:**

* To achieve consistent behavior across platforms, use the Slide.Start event for initialization code related to the Slide Navigation, as it is executed only once when the application starts.
* Use ClientStart for panel-specific initialization code, but be aware of the platform-specific behavior differences.

### [Scope](#Scope)

**Objects:**[Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Menu](https://wiki.genexus.com/commwiki/wiki?16321)

### [See Also](#See+Also)

[Event Triggering Order in Panels](https://wiki.genexus.com/commwiki/wiki?17614)


|  |
| --- |
| **Backlinks** |
| [Analytics external object](https://wiki.genexus.com/commwiki/wiki?31415) | [Analytics external object (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54509) | [Analytics external object (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57371) |
| [Cascade.Start event](https://wiki.genexus.com/commwiki/wiki?25587) | [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) | [Event Triggering Order in Panels](https://wiki.genexus.com/commwiki/wiki?17614) |
| [Flip.Start event](https://wiki.genexus.com/commwiki/wiki?25571) | [Flip.Start event (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55467) | [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Category:Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042) |
| [Network external object](https://wiki.genexus.com/commwiki/wiki?31310) | [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076) | [Slide.Start event](https://wiki.genexus.com/commwiki/wiki?25585) | [Split.Start event](https://wiki.genexus.com/commwiki/wiki?25586) |
| [Tabs.Start event](https://wiki.genexus.com/commwiki/wiki?25596) |

---
