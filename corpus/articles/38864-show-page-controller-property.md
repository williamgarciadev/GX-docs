---
title: "Show Page Controller property"
source_id: 38864
source_url: https://wiki.genexus.com/commwiki/wiki?38864
genexus_version: "18"
---

# Show Page Controller property

Specifies whether the page controller will be displayed.

### [Syntax](#Syntax)

**control.** ShowPageController

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Horizontal Grid](https://wiki.genexus.com/commwiki/wiki?18180))

### [Description](#Description)

This property is available for [Horizontal Grids](https://wiki.genexus.com/commwiki/wiki?18180) included in [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s.

It allows hiding the page controller in a [Horizontal Grid](https://wiki.genexus.com/commwiki/wiki?18180).

Also, it can be either read or write. For example:

```
Grid1.ShowPageController = True

&isPageControllerVisible = Grid1.ShowPageController //&isPageControllerVisible will be true.
```

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [Samples](#Samples)

Consider a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) defined in the [Real Estate](https://wiki.genexus.com/commwiki/wiki?23631,,) KB that contains a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) with its [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) set to "Horizontal Grid".

If the Grid property is set to True, the Page Controller is visible:

|  |  |
| --- | --- |
| **Android** | **Apple** |
|  |  |

On the other hand, if it is set to False, the Page Controller disappears:

|  |
| --- |
|  |

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

* [HowTo: Use Horizontal Grid control in Panels](https://wiki.genexus.com/commwiki/wiki?18180)


|  |
| --- |
| **Backlinks** |
| [HowTo: Use Horizontal Grid control in Panels](https://wiki.genexus.com/commwiki/wiki?18180) |

---
