---
title: "Image variation by Tokens options"
source_id: 49372
source_url: https://wiki.genexus.com/commwiki/wiki?49372
genexus_version: "18"
---

# Image variation by Tokens options

This article explains how images can vary by [Design System Tokens Options](https://wiki.genexus.com/commwiki/wiki?49381).

The [Image object](https://wiki.genexus.com/commwiki/wiki?23387) allows you to vary its content (the specific image to be displayed at runtime) according to the [Theme](https://wiki.genexus.com/commwiki/wiki?4375) or [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) (DSO) associated with the object containing the image. To do so, the specific image is entered into the object, and the Theme or Design System Object is specified in the [Style property in Map User Control](https://wiki.genexus.com/commwiki/wiki?42433). It can also be varied by language, screen density, layer, and, exclusively in the case of a DSO that has parameterized options for the [Tokens](https://wiki.genexus.com/commwiki/wiki?47378), by the values of these [options](https://wiki.genexus.com/commwiki/wiki?49381).

In the following example, the Chatbot image of the [KB](https://wiki.genexus.com/commwiki/wiki?2428) is being edited. It contains 5 variations, and the last one of them will be applied if none of the others is chosen.

Note that when the Style is the DSO named "TravelAgencyFrontendExtended," the language is any language, and the density is 100%, an image with red color has been defined when the color-scheme option is Light. On the other hand, a green one is defined when all other parameters match but the color-scheme option is Dark.

`[imagen omitida: wiki id 49374]`

This will cause one or the other to be used depending on the value of the option at runtime:

`[imagen omitida: wiki id 49375]`

So, you can think of the image as a Token that is defined elsewhere, in another way, in the image editor.

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See Also](#See+Also)

[Options property](https://wiki.genexus.com/commwiki/wiki?48091)


|  |
| --- |
| **Backlinks** |
| [Design System Tokens Options](https://wiki.genexus.com/commwiki/wiki?49381) | [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |

---
