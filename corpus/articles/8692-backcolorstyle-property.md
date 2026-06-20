---
title: "BackColorStyle property"
source_id: 8692
source_url: https://wiki.genexus.com/commwiki/wiki?8692
genexus_version: "18"
---

# BackColorStyle property

Allows assigning a style to the Grid.

### [Syntax](#Syntax)

**control.** BackColorStyle   

**Where:**  
*control*  
    Is the name of a control inserted in the form.

### [Values](#Values)

|  |  |
| --- | --- |
| **None** | The Grid is not going to have a particular style, but it will have the design of the form or control that contains it. This is the default value. |
| **Uniform** | It allows specifying a single color for the Grid's background (the title as well as the lines). |
| **Header** | It allows specifying a color for the background of the Grid's titles and another one for its lines. The properties are LinesBackColor and TitleBackColor. |
| **Report** | It allows specifying a color for the background of the titles and alternate colors for the even and odd lines of the Grid. The properties are LinesBackColor, LinesBackColorEven and TitleBackColor. |

### [Description](#Description)

#### [Note](#Note)

As of GeneXus 15, the Background Color Style property is configured in the Theme.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Scope](#Scope)

**Objects:** Procedure, Transaction, Web Panel  
**Platforms:** Web(.Net, Java)  
**Controls:** FreeStyle Grid, Grid

### [See Also](#See+Also)

[BackColor property](https://wiki.genexus.com/commwiki/wiki?8688)  
[LinesBackColor property](https://wiki.genexus.com/commwiki/wiki?8697,,)  
[LinesBackColorEven Property](https://wiki.genexus.com/commwiki/wiki?8698,,)  
[TitleBackColor Property](https://wiki.genexus.com/commwiki/wiki?8699,,)


|  |
| --- |
| **Backlinks** |
| [BackColor property](https://wiki.genexus.com/commwiki/wiki?8688) | [BackColorEven property](https://wiki.genexus.com/commwiki/wiki?8694) | [BackColorOdd property](https://wiki.genexus.com/commwiki/wiki?8702) |
| [Free Style Grid Properties](https://wiki.genexus.com/commwiki/wiki?9760) |

---
