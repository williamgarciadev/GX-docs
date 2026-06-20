---
title: "Display property (Web Theme object)"
source_id: 46386
source_url: https://wiki.genexus.com/commwiki/wiki?46386
genexus_version: "18"
---

# Display property (Web Theme object)

Defines how fonts should be displayed in an element when the font is not already downloaded and ready to use.

### [Values](#Values)

|  |
| --- |
|  |
| **auto** | The font display strategy is defined by the user agent. |
| **block** | Gives the font face a short block period and an infinite swap period. |
| **fallback** | Gives the font face an extremely small block period and a short swap period. |
| **optional** | Gives the font face an extremely small block period and no swap period. |
| **swap** | Gives the font face an extremely small block period and an infinite swap period. |

### [Scope](#Scope)

**Objects:** [Web Theme](https://wiki.genexus.com/commwiki/wiki?6420)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)

### [Description](#Description)

Setting this property is optional.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,).

### [See Also](#See+Also)

<https://developer.mozilla.org/es/docs/Web/CSS/@font-face/font-display>
