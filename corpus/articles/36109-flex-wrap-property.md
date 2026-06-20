---
title: "Flex Wrap property"
source_id: 36109
source_url: https://wiki.genexus.com/commwiki/wiki?36109
genexus_version: "18"
---

# Flex Wrap property

Controls whether the flex container is single-line or multi-line, and the direction of the cross axis.

### [Values](#Values)

|  |  |
| --- | --- |
| **No Wrap** | Default value. Controls will not wrap. |
| **Wrap** | Controls will wrap if necessary. |
| **Wrap Reverse** | Controls will wrap, if necessary, in reverse order. |

### [Description](#Description)

This property applies to containers and controls and specifies what happens when children overflow the size of the container along the main-axis of the layout container.

The following examples have as main-axis the row (column axis is analogous).

|  |
| --- |
| **No Wrap value** |
|  |
|  |
| **Wrap value** |
|  |
|  |
| **Wrap Reverse value** |
|  |

### [FlexWrap domain](#FlexWrap+domain)

Possible flex wrap options for setting the FlexWrap property at runtime.

**Note**: FlexWrap property is only available at runtime for a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) with [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) as 'SD Flex Grid' or [Custom Render property](https://wiki.genexus.com/commwiki/wiki?11407) as 'Flex'.

|  |  |
| --- | --- |
| **NoWrap** | No wrap content. |
| **Wrap** | Wrap content. |
| **WrapReverse** | Wrap content in reverse order. |

### [Notes](#Notes)

* 'Autogrow' concept does not apply to flex containers when this property is different from "No Wrap".
* 'Pagination' concept does not apply to flex grid when this property is different from "No Wrap".

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [Scope](#Scope)

**Platforms:** Web(.Net, Java), Smart Devices(IOS)  
**Controls:** Grid, Table


|  |
| --- |
| **Backlinks** |
| [Align Content property](https://wiki.genexus.com/commwiki/wiki?36110) | [Flex control](https://wiki.genexus.com/commwiki/wiki?40521) | [Toc:Flex Layout Container](https://wiki.genexus.com/commwiki/wiki?35354) |

---
