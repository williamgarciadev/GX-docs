---
title: "HowTo: Select a Location on a Map"
source_id: 59365
source_url: https://wiki.genexus.com/commwiki/wiki?59365
genexus_version: "18"
---

# HowTo: Select a Location on a Map

This article explains how to implement Map navigation to select a Location (in other words, how to use the Selection Layer).

When you include in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) with its Control Type property set to Maps, it is possible to enable a navigation mode that allows you to select a location (a [GeoPoint](https://wiki.genexus.com/commwiki/wiki?58058)). In this navigation, there is an icon in the center that remains fixed and you can move the map to select a position (and get its coordinates). This is handled with the [Selection Layer property](https://wiki.genexus.com/commwiki/wiki?42223).

## [Scope](#Scope)

**Controls:**[Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

## [Description](#Description)

First, set the Grid [Selection Layer property](https://wiki.genexus.com/commwiki/wiki?42223) to True. This will make it possible to move on the map at runtime, having a fixed icon in the center that obtains the position and triggers an event.

The navigation is similar to what is achieved using the [PickLocation Method](https://wiki.genexus.com/commwiki/wiki?36729).

`[imagen omitida: wiki id 40805]`

The icon can be configured using the [Location Selection Target Image property](https://wiki.genexus.com/commwiki/wiki?42224).Also, by setting the [Selection Layer property](https://wiki.genexus.com/commwiki/wiki?42223) = True, the [Selection Target Image Class property](https://wiki.genexus.com/commwiki/wiki?40670) is enabled to associate a class to that image (by default, there is a class created under the name: SDMapPinImage).

In addition, by setting the [Selection Layer property](https://wiki.genexus.com/commwiki/wiki?42223) = True, two events are available: ControlValueChanging and ControlValueChanged.

#### [**ControlValueChanging(GeoPoint) event**](#ControlValueChanging%28GeoPoint%29+event)

This event is triggered while the map is moving. For example:

```
Event Grid1.ControlValueChanging(&geoPoint)
       composite
            msg(&geoPoint.Tostring())
      endcomposite
Endevent
```

#### [**ControlValueChanged(GeoPoint) event**](#ControlValueChanged%28GeoPoint%29+event)

This event is triggered when you stop moving the map. For example:

```
Event Grid1.ControlValueChanged(&geoPoint)
       composite
            msg(&geoPoint.Tostring())
       endcomposite
Endevent
```

You get the position to which the map was moved in the GeoPoint type parameter.

The code in the example shows the string corresponding to the position to which the map was moved (i.e.: POINT(Long Lat)).  
  
The event ControlValueChanged is overloaded with values; therefore, the parameter could be of Character type (instead of GeoPoint).

### [Showcase](#Showcase)

[GeoCity](https://wiki.genexus.com/commwiki/wiki?49231):In this Knowledge Base you can find the "Pruning" section, where the "RecoleccionPodas" (Pruning Collection) [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) uses Selection.

### [See Also](#See+Also)

[Layers in Maps](https://wiki.genexus.com/commwiki/wiki?40763)


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeoSuite](https://wiki.genexus.com/commwiki/wiki?52770) | [Layers in Maps](https://wiki.genexus.com/commwiki/wiki?40763) |

---
