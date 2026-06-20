---
title: "HowTo: Overlay attributes"
source_id: 22510
source_url: https://wiki.genexus.com/commwiki/wiki?22510
genexus_version: "18"
---

# HowTo: Overlay attributes

This document explains how to use the [Canvas control](https://wiki.genexus.com/commwiki/wiki?22452) to show overlay attributes.

In this case, the canvas within a grid to show an attribute over an image will be used. The [Event Day](https://wiki.genexus.com/commwiki/wiki?22550,,) application will be used as example, starting from the following layout:

`[imagen omitida: wiki id 22515]``[imagen omitida: wiki id 22516]`

The first thing to be done is to empty the grid table and insert a canvas container. To do that, modify the canvas’ properties so that it takes up 100% of the screen’s width, with a height of 160dips.

`[imagen omitida: wiki id 22517]`

Then, move the attributes inside the canvas, placing them and setting their absolute positioning properties for each one of them.

`[imagen omitida: wiki id 22521]``[imagen omitida: wiki id 22522]`

Note that the table that contains the image is located at 10dips from the upper part -**Top = 10-** of the canvas and its height is 120dips -ending at **130dips** from the upper part. So, the table that contains the name with coordinate **Top = 110** and **ZOrder = 2** is overlaid on the image.

The following video shows the feature in action:

### [See Also](#See+Also)

[LightCRM Sample KB](https://wiki.genexus.com/commwiki/wiki?22592,,)


|  |
| --- |
| **Backlinks** |
| [Canvas control](https://wiki.genexus.com/commwiki/wiki?22452) | [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [gx-elevation property](https://wiki.genexus.com/commwiki/wiki?28180) |
| [HowTo: Adding Material Design to Android applications](https://wiki.genexus.com/commwiki/wiki?31004) |

---
