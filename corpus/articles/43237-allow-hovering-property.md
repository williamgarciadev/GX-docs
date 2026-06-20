---
title: "Allow Hovering property"
source_id: 43237
source_url: https://wiki.genexus.com/commwiki/wiki?43237
genexus_version: "18"
---

# Allow Hovering property

Highlights Grid lines with a background color while scanning them with the cursor. Only taken into account if the Allow Selection property of the Grid is enabled.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817)

### [Description](#Description)

In a web application, if you want to allow the end-user to mark inside a Grid a row as selected, you can set the [Allow Selection property](https://wiki.genexus.com/commwiki/wiki?8680) of a [Grid](https://wiki.genexus.com/commwiki/wiki?24817) defined in a [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132) or [Transaction Web Layout](https://wiki.genexus.com/commwiki/wiki?8057) to True.

This also enables the **Allow Hovering** property with True value by default. So, when the mouse passes over each row, it is painted in one color.

Below you can see the effect in runtime:

`[imagen omitida: wiki id 43235]`

The colors can be set in the Theme object, in the classes assigned to the properties Selected Row Class and Hover Row Class of the Grid class.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [See Also](#See+Also)

[Allow Selection property](https://wiki.genexus.com/commwiki/wiki?8680)  
[HoveringColor property](https://wiki.genexus.com/commwiki/wiki?8681)


|  |
| --- |
| **Backlinks** |
| [Allow Selection property](https://wiki.genexus.com/commwiki/wiki?8680) | [HoveringColor property](https://wiki.genexus.com/commwiki/wiki?8681) |

---
