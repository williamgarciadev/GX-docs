---
title: "Align Content property"
source_id: 36110
source_url: https://wiki.genexus.com/commwiki/wiki?36110
genexus_version: "18"
---

# Align Content property

Controls the alignment of the flex lines in the flex container.

### [Values](#Values)

|  |  |
| --- | --- |
| **Center** | Lines are packed toward the center of the flex container. |
| **Flex End** | Lines are packed toward the start of the flex container. |
| **Flex Start** | Lines are packed toward the end of the flex container. |
| **Space Around** | Lines are evenly distributed in the flex container, with half-size spaces on either end. |
| **Space Between** | Lines are evenly distributed in the flex container. |
| **Stretch** | Default value. Lines stretch to take up the remaining space. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Table](https://wiki.genexus.com/commwiki/wiki?6001)

### [Description](#Description)

This property applies when the [Flex Wrap property](https://wiki.genexus.com/commwiki/wiki?36109) is different from 'No Wrap' (that makes multiple lines in the flex container) and you want to align these lines. It is similar to [Align Items property](https://wiki.genexus.com/commwiki/wiki?36111), but instead of aligning the embedded controls, it aligns the flex lines.

**Note**: Use the [Justify Content property](https://wiki.genexus.com/commwiki/wiki?36108) to align the items on the main-axis (horizontally or vertically depending on [Flex Direction property](https://wiki.genexus.com/commwiki/wiki?36107)).

|  |
| --- |
| **Stretch value** |
|  |
|  |
| **Flex Start value** |
|  |
|  |
| **Flex End value** |
|  |
|  |
| **Center value** |
|  |
|  |
| **Space Between value** |
|  |
|  |
| **Space Around value** |
|  |

### [FlexAlignContent domain](#FlexAlignContent+domain)

Possible flex wrap options for setting the AlignContent property at runtime.

**Note**: AlignContent property is only available at runtime for a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) with [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) as 'SD Flex Grid' or [Custom Render property](https://wiki.genexus.com/commwiki/wiki?11407) as 'Flex'.

|  |  |
| --- | --- |
| **Center** | Align lines center. |
| **FlexEnd** | Align lines at the end. |
| **FlexStart** | Align lines at the start. |
| **SpaceAround** | Align lines content before, after and between items. |
| **SpaceBetween** | Align lines with a space between items. |
| **Stretch** | Stretch lines to fit the container. |

### [Limitations](#Limitations)

* This property does not have any effect with **Flex Layout** in Android.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [See Also](#See+Also)

* [Align Items property](https://wiki.genexus.com/commwiki/wiki?36111)


|  |
| --- |
| **Backlinks** |
| [Align Items property](https://wiki.genexus.com/commwiki/wiki?36111) | [Flex control](https://wiki.genexus.com/commwiki/wiki?40521) | [Toc:Flex Layout Container](https://wiki.genexus.com/commwiki/wiki?35354) |

---
