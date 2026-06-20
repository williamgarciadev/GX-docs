---
title: "Max Zoom Relative To property (GeneXus 18 Upgrade 7 or prior)"
source_id: 57252
source_url: https://wiki.genexus.com/commwiki/wiki?57252
genexus_version: "18"
---

# Max Zoom Relative To property (GeneXus 18 Upgrade 7 or prior)

Indicates how much you can enlarge an image in relation to its original size or the size of the controller.

### [Values](#Values)

|  |
| --- |
| **Control** |
| **Image** |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** Attribute/Variable (Control Type: [Advanced Image](https://wiki.genexus.com/commwiki/wiki?20497))

### [Description](#Description)

Indicates whether the applied zoom will take into account the resolution of the image or the size of the image container.

There is an image with 200 x 300 dimensions within a table measuring 100dip high and 100dip wide; the Max Zoom property has the value 200 and the Max Zoom Relative To property is set to Control.

`[imagen omitida: wiki id 46559]`

When zooming in, the maximum image size will be the equivalent of viewing the image in a 200dip x 200dip table.

`[imagen omitida: wiki id 46573]`

If the Max Zoom Relative To property has the Image value, zooming in will make the image as large as 400 x 600.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [See Also](#See+Also)

[Advanced Image Control](https://wiki.genexus.com/commwiki/wiki?20497)
