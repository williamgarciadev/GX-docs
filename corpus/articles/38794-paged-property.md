---
title: "Paged property"
source_id: 38794
source_url: https://wiki.genexus.com/commwiki/wiki?38794
genexus_version: "18"
---

# Paged property

Indicates whether the view will display items page by page, with each page displaying as many elements as possible, using the available space and the previously defined row and column layout.

### [Syntax](#Syntax)

**control.** Paged

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Horizontal Grid](https://wiki.genexus.com/commwiki/wiki?18180))

### [Description](#Description)

This property is available for [Horizontal Grid Control](https://wiki.genexus.com/commwiki/wiki?30592)s included in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s.

If the property is set to True, the Horizontal Grid will show the content using paging. If it is set to False, the Horizontal Grid will use scrolling.

It can be both read and write. For example:

```
Grid1.Paged = True
&isPaged = Grid1.Paged // &isPaged will be True
```

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [See Also](#See+Also)

[HowTo: Use Horizontal Grid control in Panels](https://wiki.genexus.com/commwiki/wiki?18180)


|  |
| --- |
| **Backlinks** |
| [HowTo: Use Horizontal Grid control in Panels](https://wiki.genexus.com/commwiki/wiki?18180) |

---
