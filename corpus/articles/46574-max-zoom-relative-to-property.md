---
title: "Max Zoom Relative To property"
source_id: 46574
source_url: https://wiki.genexus.com/commwiki/wiki?46574
genexus_version: "18"
---

# Max Zoom Relative To property

Indicates how much you can enlarge an image in relation to its original size or the size of the controller.

### [Values](#Values)

|  |  |
| --- | --- |
| **Control** | Controls whether the maximum zoom value is relative to the size of the control. |
| **Image** | Controls whether the maximum zoom value is relative to the size of the image. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** Attribute/Variable (Control Type: Image, [Advanced Image](https://wiki.genexus.com/commwiki/wiki?20497))

### [Description](#Description)

Indicates whether the applied zoom will take into account the resolution of the image or the size of the image container.

**Note:** When the Control Type = **Image,** the [Enable Zoom property](https://wiki.genexus.com/commwiki/wiki?46466) must be set to True to make this property available.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

If there is an image with 200 x 300 dimensions within a table measuring 100dip high and 100dip wide.

The [Max Zoom property](https://wiki.genexus.com/commwiki/wiki?46472) has the value 200 and the Max Zoom Relative To property is set to Control.

`[imagen omitida: wiki id 46559]`

When zooming in, the maximum image size will be the equivalent of viewing the image in a 200dip x 200dip table.

`[imagen omitida: wiki id 46573]`

If the Max Zoom Relative To property has the Image value, zooming in will make the image as large as 400 x 600.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [See Also](#See+Also)

[Enable Zoom property](https://wiki.genexus.com/commwiki/wiki?46466)  
[Max Zoom property](https://wiki.genexus.com/commwiki/wiki?46472)  
[Zoom Outside Control property](https://wiki.genexus.com/commwiki/wiki?43486)


|  |
| --- |
| **Backlinks** |
| [Enable Copy To Clipboard property](https://wiki.genexus.com/commwiki/wiki?46557) | [Enable Zoom property](https://wiki.genexus.com/commwiki/wiki?46466) | [Enable Zoom property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57238) |
| [Max Zoom property](https://wiki.genexus.com/commwiki/wiki?46472) | [Max Zoom Relative To property (GeneXus 18 Upgrade 7 or prior)](https://wiki.genexus.com/commwiki/wiki?57252) | [Zoom Outside Control property](https://wiki.genexus.com/commwiki/wiki?43486) |

---
