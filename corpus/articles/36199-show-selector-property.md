---
title: "Show Selector property"
source_id: 36199
source_url: https://wiki.genexus.com/commwiki/wiki?36199
genexus_version: "18"
---

# Show Selector property

Sets the user interface behavior that will have the Grid control when it allows multiple selection.

### [Values](#Values)

|  |  |
| --- | --- |
| **Always** | The selector is always visible in the Grid. The end user selects a set of rows first and then executes the action with a "for each selected line" command for processing each row. |
| **On Action** | The selector becomes visible only when the end user selects the action having a "for each selected line" command over the Grid. Then, the end user selects a set of rows, allowing the user to confirm or cancel the action execution for processing each row selected. |
| **Platform Default** | Default value. For Apple generator, the behavior of On Action value is assumed. For Android generator, the behavior of Always value is assumed. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Enable Multiple Selection property](https://wiki.genexus.com/commwiki/wiki?36197)  
[Grids with Multiple Selection for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?16149)


|  |
| --- |
| **Backlinks** |
| [Enable Multiple Selection property](https://wiki.genexus.com/commwiki/wiki?36197) | [Enable Multiple Selection property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54466) | [Grids with Multiple Selection for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?16149) |
| [Select method](https://wiki.genexus.com/commwiki/wiki?36234) | [Select method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54486) |

---
