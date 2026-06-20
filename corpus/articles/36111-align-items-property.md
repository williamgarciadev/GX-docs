---
title: "Align Items property"
source_id: 36111
source_url: https://wiki.genexus.com/commwiki/wiki?36111
genexus_version: "18"
---

# Align Items property

Controls the alignment along the cross axis.

### [Values](#Values)

|  |  |
| --- | --- |
| **Baseline** | Controls are aligned such as their baselines align. This is useful to have several texts from diferents controls aligned taking into account different font sizes. |
| **Center** | Controls are positioned at the center of the container. |
| **Flex End** | Controls are positioned at the end of the container. |
| **Flex Start** | Controls are positioned at the beginning of the container. |
| **Stretch** | Default value. Controls are stretched to fit the container. In other words, children match the size of their container in the cross axis. |

### [Description](#Description)

Describes how to align children along the cross axis of their container.

The following examples have as main-axis the row (column axis is analogous) and wrap the content.

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
| **Baseline** **value** |
| Not represented in the panel designer. |

### [FlexAlignItems domain](#FlexAlignItems+domain)

Possible options for setting the AlignItems property at runtime.

**Note**: AlignItems property is only available at runtime for a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) with [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) as 'SD Flex Grid' or [Custom Render property](https://wiki.genexus.com/commwiki/wiki?11407) as 'Flex'.

|  |  |
| --- | --- |
| **Baseline** | Align at the baseline. |
| **Center** | Align at the center. |
| **FlexEnd** | Align at the end. |
| **FlexStart** | Align at the start. |
| **Stretch** | Stretch controls to fit the container. |

### [Notes](#Notes)

* Any other value different from 'Stretch' for this property requires that the children controls have a non-default value for the [Width](https://wiki.genexus.com/commwiki/wiki?38374)/[Height](https://wiki.genexus.com/commwiki/wiki?8792) property depending on which is the cross-axis (if the main axis is 'row', it requires height; but if the main axis is 'column', it requires width)

### [Limitations](#Limitations)

* This property does not have any effect with **Flex Grid** in iOS.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [Scope](#Scope)

**Platforms:** Web(.Net, Java), Smart Devices(Android, IOS)  
**Controls:** Grid, Table

### [See Also](#See+Also)

* [Align Content property](https://wiki.genexus.com/commwiki/wiki?36110)


|  |
| --- |
| **Backlinks** |
| [Align Content property](https://wiki.genexus.com/commwiki/wiki?36110) | [Flex control](https://wiki.genexus.com/commwiki/wiki?40521) | [Toc:Flex Layout Container](https://wiki.genexus.com/commwiki/wiki?35354) |

---
