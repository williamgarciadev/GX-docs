---
title: "Pin Image Scale Type property"
source_id: 42227
source_url: https://wiki.genexus.com/commwiki/wiki?42227
genexus_version: "18"
---

# Pin Image Scale Type property

Indicates how the pin image of the map is scaled.

### [Values](#Values)

|  |
| --- |
|  |
| **No Scale** | Keeps the original size of the image, regardless of the control area size. |
| **Fill Keeping Aspect Ratio** | The image width and height is increased or decreased to fill the entire size of the control area, while keeping the aspect of the image. |
| **Fill** | The image width and height is scaled to fill the entire size of the control area. |
| **Fit** | The image width and height is scaled to show it entirely, while keeping the aspect of the image. |
| **Tile** | The image is not scaled. It is repeated horizontally and vertically to fill the control size. |

### [Scope](#Scope)

**Objects:** [Theme](https://wiki.genexus.com/commwiki/wiki?17876,,)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object. |

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,).

### [See Also](#See+Also)

[Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309)  
[gx-content-mode property](https://wiki.genexus.com/commwiki/wiki?23857)
