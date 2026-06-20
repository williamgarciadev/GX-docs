---
title: "Canvas control"
source_id: 22452
source_url: https://wiki.genexus.com/commwiki/wiki?22452
genexus_version: "18"
---

# Canvas control

The Canvas control is a container that allows you to accurately order the elements in the layout by using absolute positioning, which allows you to overlay them.

### [Layout](#Layout)

The canvas container can be added from the toolbox to any layout, and it looks as shown below:

`[imagen omitida: wiki id 22475]`

### [Container properties](#Container+properties)

The canvas container has the same properties as the [Table control](https://wiki.genexus.com/commwiki/wiki?6001), in addition to the properties Canvas width and Canvas height. The canvas width and height depend on the canvas size in the designer; in the device, the canvas will take the size of its container (for example, when it is in a table it will take the size of the cell it is saved in).

### [Properties of the elements in the container](#Properties+of+the+elements+in+the+container)

The controls placed within a canvas have seven new properties:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | **Possible values (**[Panel object](https://wiki.genexus.com/commwiki/wiki?24829)**)** | **Possible values (**[Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)**)** |
| **Left** | Distance from the control to the left side of the canvas | Dips, Percentage | px, Percentage |
| **Width** | Width of the control | Dips, Percentage | px, Percentage |
| **Right** | Distance from the control to the right side of the canvas | Dips, Percentage | px, Percentage |
| **Top** | Distance from the control to the top of the canvas | Dips, Percentage | px, Percentage |
| **Height** | Height of the control | Dips, Percentage | px, Percentage |
| **Bottom** | Distance from the control to the bottom of the canvas | Dips, Percentage | px, Percentage |
| **ZOrder** | The ZOrder property specifies the stack order of a control. (A control with greater stack order is always in front of a control with a lower stack order) | Numeric | Numeric |

### [Notes](#Notes)

1) If the control is not anchored to an axis, its position is calculated in percentages.

For example, an image is added that isn’t anchored to the right nor to the left, positioned at X = 50 in a canvas that is 100dips wide; this image will always be positioned at 50% of the canvas.

2) If the control is anchored to both sides of an axis, the distance between the control and both sides will remain constant and the size of the control will vary.

3) The values for the Left, Right, Top and Bottom properties may be negative numbers. This means that the control will be moved in the opposite direction.

For example, if you set a Top value of -20 dips for an image with height 100 dips, only the lower 80 dips of the image will be visible.

#### [Note for Panels layouts](#Note+for+Panels+layouts)

Setting negative values is useful when you want to animate a control, for example, to make it appear on screen by performing a user action. This can be achieved by setting a [Theme Class](https://wiki.genexus.com/commwiki/wiki?6246) to the control that has the Animated property set to True and a transformation to move the control to another position.

### [Example](#Example)

In the example below, the canvas container is used to position the contacts’ names over the photos.

`[imagen omitida: wiki id 22467]``[imagen omitida: wiki id 22469]`

##### [LightCRM App: Absolute Positioning an Overlaying in action](#LightCRM+App%3A+Absolute+Positioning+an+Overlaying+in+action)

### [Tip](#Tip)

When using the canvas container, it can be very useful to hide the controls during the layout design. This can be done from the Document Outliner, using the checkbox next to each control:

`[imagen omitida: wiki id 23650]`

### [See also](#See+also)

[HowTo: Overlay attributes](https://wiki.genexus.com/commwiki/wiki?22510)  
[Sample KB](https://wiki.genexus.com/commwiki/wiki?22592,,)


|  |
| --- |
| **Backlinks** |
| [Accessible Name Control property](https://wiki.genexus.com/commwiki/wiki?55456) | [Accessible Name Custom property](https://wiki.genexus.com/commwiki/wiki?55469) | [Accessible Name property](https://wiki.genexus.com/commwiki/wiki?55454) |
| [Accessible Role property](https://wiki.genexus.com/commwiki/wiki?55453) | [KB:BitBitNews](https://wiki.genexus.com/commwiki/wiki?39308) | [Col Span property](https://wiki.genexus.com/commwiki/wiki?8752) |
| [Design System Object - What controls do you need to implement the Header?](https://wiki.genexus.com/commwiki/wiki?48683) | [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [Expand Bounds Directions property](https://wiki.genexus.com/commwiki/wiki?37138) | [Expand Bounds Limit property](https://wiki.genexus.com/commwiki/wiki?37137) |
| [Expand Bounds property](https://wiki.genexus.com/commwiki/wiki?37136) | [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) | [gx-elevation property](https://wiki.genexus.com/commwiki/wiki?28180) |
| [HowTo: Adding Material Design to Android applications](https://wiki.genexus.com/commwiki/wiki?31004) | [HowTo: Overlay attributes](https://wiki.genexus.com/commwiki/wiki?22510) | [Is Slot property](https://wiki.genexus.com/commwiki/wiki?51306) | [Layout Behavior properties group](https://wiki.genexus.com/commwiki/wiki?37135) |
| [Motion Effect properties group](https://wiki.genexus.com/commwiki/wiki?30953) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Row Span property](https://wiki.genexus.com/commwiki/wiki?8828) | [Scroll Attachment property](https://wiki.genexus.com/commwiki/wiki?29875) |
| [Scroll behavior properties group](https://wiki.genexus.com/commwiki/wiki?31174) | [Scroll Factor property](https://wiki.genexus.com/commwiki/wiki?29874) | [Slots in Stencils](https://wiki.genexus.com/commwiki/wiki?51385) | [Zoom Factor property](https://wiki.genexus.com/commwiki/wiki?29876) |

---
