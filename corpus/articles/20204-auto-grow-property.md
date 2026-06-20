---
title: "Auto Grow property"
source_id: 20204
source_url: https://wiki.genexus.com/commwiki/wiki?20204
genexus_version: "18"
---

# Auto Grow property

Configures whether to automatically adjust the height of the control when the content (i.e. text) is larger than the size of the container.

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

This property allows you to automatically adjust the height of the control (included in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)) when the content (i.e. text) is larger than the size of the container.

### [Values](#Values)

|  |  |
| --- | --- |
| **True** | The height of the control grows automatically, as much as necessary to show all the content. |
| **False** | The height of the control does not grow automatically. It is up to the control to adjust the content when it is larger than the container; e.g. containers may add scroll bars if possible, text controls may clip text or add scroll bars, etc. |

### [Controls - Default Value](#Controls+-+Default+Value)

This property applies to different types of controls: containers and text. The default value depends on the type of control. The following table lists the controls that support this property and their default values.

|  |  |
| --- | --- |
| **Container** **Controls** | **Default Value** |
| Grid | False |
| Table | True |
| Group | True |
| **Text Controls** | |
| Attribute | False |
| Variable | False |
| LongVarChar (Attribute or variable) | True |
| Texblock | False |

### [Tips](#Tips)

The following table shows the combination of *Auto Grow property* and its effect.

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | **ATTRIBUTE** | |
|  |  | *True* | *False* |
| **T  A  B  L  E** | *T  r  u  e* | The attribute grows if the item is bigger than the cell where it is contained. The table grows and has scroll bars. | The table might grow, but since the attribute does not, the table does not. |
| *F  a  l  s  e* | The table doesn't grow; therefore, the attributes inside it are limited by the table. In other words, the auto grow property of the attributes is ignored. (\*) | None of them grow. |

### [Samples](#Samples)

|  |  |
| --- | --- |
|  |  |
| [Attribute Auto Grow=False](#Attribute+Auto+Grow%3DFalse) | [Attribute Auto Grow=true](#Attribute+Auto+Grow%3Dtrue) |

In some cases, you may wish to see many records in the grid, although the text does not fit; in other cases, you may wish to see the whole text, although the grid is larger and fewer rows are shown.

### [See Also](#See+Also)

[Auto Grow in Grids for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22697)


|  |
| --- |
| **Backlinks** |
| [Auto Grow in Grids for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22697) | [DateTime picker for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?34167) | [Design Patterns to reduce CLS and improve performance in Angular applications](https://wiki.genexus.com/commwiki/wiki?53585) |
| [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [gx-overflow-style property](https://wiki.genexus.com/commwiki/wiki?51796) |
| [HowTo: Use Check Box for Smart Devices](https://wiki.genexus.com/commwiki/wiki?18482) | [HowTo: Use Combo Box in Panels](https://wiki.genexus.com/commwiki/wiki?18408) | [HowTo: Use Radio Button in Panels](https://wiki.genexus.com/commwiki/wiki?18434) | [HowTo: Use the Invisible Mode property](https://wiki.genexus.com/commwiki/wiki?22838) |
| [Scroll properties group](https://wiki.genexus.com/commwiki/wiki?40618) | [Switch Control](https://wiki.genexus.com/commwiki/wiki?29973) |

---
