---
title: "Save State property"
source_id: 46017
source_url: https://wiki.genexus.com/commwiki/wiki?46017
genexus_version: "18"
---

# Save State property

Enables or disables automatic state saving and loading. When it is enabled, Grid state information such as pagination position, filtering, and sorting will be automatically saved in the Web Session. When the Grid container page is reloaded, the Grid state will be automatically restored to the last known configuration.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058)

### [Description](#Description)

Default value: False.

Applies to [Grid](https://wiki.genexus.com/commwiki/wiki?24817) and [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058) controls included in a [Transaction Web Layout](https://wiki.genexus.com/commwiki/wiki?8057) and a [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132).

When the property is set to 'True', the state information (such as pagination position, filtering, and sorting) is automatically stored in the web session and retrieved from it.

The program loads the stored information after the [Start event](https://wiki.genexus.com/commwiki/wiki?8043), provided it exists and the page is loaded for the first time (\*), and also stores it before the Refresh Event when some related information changes.

(\*) That is to say, on an HTTP Get.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[State persistence of grids](https://wiki.genexus.com/commwiki/wiki?46491)


|  |
| --- |
| **Backlinks** |
| [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) | [State persistence of grids](https://wiki.genexus.com/commwiki/wiki?46491) |

---
