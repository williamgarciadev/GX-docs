---
title: "Justify Content property"
source_id: 36108
source_url: https://wiki.genexus.com/commwiki/wiki?36108
genexus_version: "18"
---

# Justify Content property

Controls the alignment along the main-axis.

### [Values](#Values)

|  |  |
| --- | --- |
| **Center** | Controls are positioned at the center of the container |
| **Flex End** | Controls are positioned at the end of the container |
| **Flex Start** | Default value. Controls are positioned at the beginning of the container |
| **Space Around** | Controls are positioned with space before, between, and after the lines |
| **Space Between** | Controls are positioned with space between the lines |

### [Description](#Description)

Specifies how flex controls are aligned along the main-axis of the flex container (layout or grid) after any flexible lengths and auto margins are resolved.

The following examples have as main-axis the row (column axis is analogous).

|  |
| --- |
| **Flex Start value** |
|  |
|  |
| **Flex End value** |
|  |
|  |
| **Center value** |
|  |
|  |
| **Space Between** **value** |
|  |
|  |
| **Space Around value** |
|  |

### [FlexJustifyContent domain](#FlexJustifyContent+domain)

Possible options for setting the JustifyContent property at runtime.

**Note**: JustifyContent property is only available at runtime for a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) with [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) as 'SD Flex Grid' or [Custom Render property](https://wiki.genexus.com/commwiki/wiki?11407) as 'Flex'.

|  |  |
| --- | --- |
| **Center** | Justify center. |
| **FlexEnd** | Justify at the end. |
| **FlexStart** | Justify at the start. |
| **SpaceAround** | Justify content before, after and between items. |
| **SpaceBetween** | Justify with a space between items. |

### [Notes](#Notes)

* When using Flex Layout, in order to appreciate an effect of this property, [Max Width](https://wiki.genexus.com/commwiki/wiki?39718)/[Max Height](https://wiki.genexus.com/commwiki/wiki?39719) properties must be set, or [Flex Grow property](https://wiki.genexus.com/commwiki/wiki?39715) must be off (0 value) with [Width](https://wiki.genexus.com/commwiki/wiki?38374)/[Height](https://wiki.genexus.com/commwiki/wiki?8792) already set, depending on the main-axis value (row/column respectively).

### [FAQ](#FAQ)

**Why naming flex-start and flex-end values instead of left and right?**

Because naming left and right we are assuming that the layout is always from left to right, and there are devices supporting right to left layouts.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [Scope](#Scope)

**Platforms:** Web(.Net, Java), Smart Devices(Android, IOS)  
**Controls:** Grid, Table


|  |
| --- |
| **Backlinks** |
| [Align Content property](https://wiki.genexus.com/commwiki/wiki?36110) | [Flex control](https://wiki.genexus.com/commwiki/wiki?40521) | [Toc:Flex Layout Container](https://wiki.genexus.com/commwiki/wiki?35354) |

---
