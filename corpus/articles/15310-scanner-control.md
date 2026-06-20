---
title: "Scanner Control"
source_id: 15310
source_url: https://wiki.genexus.com/commwiki/wiki?15310
genexus_version: "18"
---

# Scanner Control

Reads barcodes and QR codes directly into an attribute or variable in the [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)'s layout.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)   
**Controls**: Attribute/Variable (Control Type: Scanner)

### [Properties](#Properties)

* [Barcode Types](https://wiki.genexus.com/commwiki/wiki?42176)
* [Display mode](https://wiki.genexus.com/commwiki/wiki?48528)
* [Operation mode](https://wiki.genexus.com/commwiki/wiki?48529)
* [Beep on each read](https://wiki.genexus.com/commwiki/wiki?48530)

### [Events](#Events)

#### [CodeRead event](#CodeRead+event)

When the control is displayed inline (that is, the Display mode property was set to Inline), each time it reads a code, it will trigger the CodeRead event.

Note that the ControlValueChanged event may also be triggered in some cases when the CodeRead event is triggered. The ControlValueChanged event behaves differently from the CoreRead event on that it:

* is triggered regardless of the Display mode,
* **is not triggered** if the same code is read twice.

Example:

In the following code, the &scanner variable is on screen, has the Control Type property set to Scanner, and the Display mode property set to Inline. It may also have the Operation mode property set to Continuous read.

The CodeRead event will be triggered each time a code is read. The example bellow adds the code read to a collection, and also displays a toast message showing the code.

```
Event &scanner.CodeRead
    Composite
        &CodesCollection.Add(&scanner)
        msg( format('Scanner read code %1', &scanner), nowait)
    EndComposite
Endevent
```

### [Using the control](#Using+the+control)

Just go to the relevant *WorkWithDevices<Object>.Edit* instance, select the attribute, and set Scanner for the [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550).

`[imagen omitida: wiki id 15367]`.

### [Notes](#Notes)

* The iOS simulator provided by XCode does not have any camera integrated to test Scanner control. If you want to access the camera you need a physical device.
* It scans the most common of *linear barcodes* and *matrix barcodes* variants (e.g. [QRCodes](https://en.wikipedia.org/wiki/QR_code), [EAN-13](https://en.wikipedia.org/wiki/International_Article_Number), etc).

### [See also](#See+also)

[Scanner external object](https://wiki.genexus.com/commwiki/wiki?31316)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Controls: Maps, Rating, Smart Grids, Switch](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/controls-sd-maps-rating-sd-smart-grids-switch?p=3649)  
`[imagen omitida: wiki id 20668]` [Conceptual model of mobile applications](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/conceptual-model-of-mobile-applications-6103178?p=3628)  
`[imagen omitida: wiki id 20668]` [Architecture of Online applications](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/architecture-of-online-applications?p=3721)  
`[imagen omitida: wiki id 20668]` [Container of sections in the Detail screen of the Work With](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/container-of-sections-in-the-detail-screen-of-the-work-with?p=3658)


|  |
| --- |
| **Backlinks** |
| [Barcode Types property](https://wiki.genexus.com/commwiki/wiki?42176) | [Beep on each read property](https://wiki.genexus.com/commwiki/wiki?48530) | [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) |
| [Category:Control Types](https://wiki.genexus.com/commwiki/wiki?20402) | [Display mode property](https://wiki.genexus.com/commwiki/wiki?48528) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Operation mode property](https://wiki.genexus.com/commwiki/wiki?48529) | [Purpose Strings properties group](https://wiki.genexus.com/commwiki/wiki?32755) | [Scanner external object](https://wiki.genexus.com/commwiki/wiki?31316) |

---
