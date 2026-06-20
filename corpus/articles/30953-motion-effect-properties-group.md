---
title: "Motion Effect properties group"
source_id: 30953
source_url: https://wiki.genexus.com/commwiki/wiki?30953
genexus_version: "18"
---

# Motion Effect properties group

This group of properties is under the [Theme for Smart Devices](https://wiki.genexus.com/commwiki/wiki?16595) classes (see Scope) to provide the end user with a UI/UX improvement called *Motion Effect*, closely relatedwith [*Parallax Effect*](https://wiki.genexus.com/commwiki/wiki?29875). This effect is a result of the multilayered design incorporated in iOS 7 UI, affecting the appearance of the interface when the end user device is tilted horizontally and vertically, giving the impression of depth and movement.

The properties under this group allow you to easily incorporate this impressive effect in the application.

|  |  |
| --- | --- |
| **Property** | **Description** |
| **Max Horizontal Offset** | It indicates the maximum offset that the control can reach when the end user tilts his device horizontally (left to right or right to left). It can be interpreted as a factor of movement - higher values imply more movement. |
| **Max Vertical Offset** | Likewise, when the end user tilts his device vertically (front to back or back to front). |

Both properties accept ***integer*** values, allowing for smooth movements of the control layer and its container layer.  
Depending on the effect that you want to achieve, its value can be in one of the three categories listed below.

* ***Negative value***: It makes the control move in the *opposite direction* to the movement of the physical device.
* ***Zero value (0)***: No effect (default value)
* ***Positive value***: It makes the control move in the *same direction* to the movement of the physical device.

## [Usage example](#Usage+example)

In [EventDay](https://wiki.genexus.com/commwiki/wiki?22550,,), suppose you want to apply this UI/UX feature to each speaker picture on the list.

First, open the [List section](https://wiki.genexus.com/commwiki/wiki?15984) of the WorkWithDevicesSpeaker object.

Since the aim is to have a moving image, it should be embedded in a Canvas control, expanded beyond the edge limits and filled when the picture moves.  
So, the layout could be designed as follows:

`[imagen omitida: wiki id 30987]`

The details of this decision are listed below.

* *TableImageSpeaker* class makes the Canvas rounded, setting Border Radius with an appropriate value.
* The *Absolute Position properties* of the Canvas image make it expanded and centered.
* *ImageSpeakerMotion* class makes the image keep its aspect and adds the motion effect setting both offsets.

Just by setting a few properties, the runtime behavior will be as shown below.

|  |
| --- |
| **Horizontal tilt** |
|  |
| **Vertical tilt** |
|  |
| Horizontal & Vertical tilt |
|  |

## [Note](#Note)

* Only supported in iOS 7 or higher.
* If the tiled control is embedded in a [Table control](https://wiki.genexus.com/commwiki/wiki?6001) or [Canvas control](https://wiki.genexus.com/commwiki/wiki?22452) ensure to set [Border Radius property](https://wiki.genexus.com/commwiki/wiki?27143) (whose value could be 1 or higher, depending on your requirements). These settings will avoid the control scapes from its limits when motion effect is applied (e.g. a tiled image inside a canvas as it is shown in the Usage Example section).

## [Scope](#Scope)

**Theme class:**[Image](https://wiki.genexus.com/commwiki/wiki?20460), Table, Calendar, Group  
**Generators:** Smart Device ([iOS](https://wiki.genexus.com/commwiki/wiki?14917))

## [Availability](#Availability)

This property is available as from [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,)


|  |
| --- |
| **Backlinks** |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
