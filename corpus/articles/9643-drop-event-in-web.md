---
title: "Drop event in Web"
source_id: 9643
source_url: https://wiki.genexus.com/commwiki/wiki?9643
genexus_version: "18"
---

# Drop event in Web

Code that is run when dropping content from another control.

### [Syntax](#Syntax)

**Event** *<control>.***Drop(***&parameter1*, *&parameter2*, ..., *&parametern***)**

*Event\_code*

**Endevent**

Where:

*control*

The name of the form control over the drop operation is performed.

*&parameteri*

Can only be variable. Each parameter will be loaded with the corresponding value from the Drag operation (from a grid with [Allow Drag property](https://wiki.genexus.com/commwiki/wiki?9766) or another control with [Drag event in Web](https://wiki.genexus.com/commwiki/wiki?9642) coded). If you are intending to drop information from a grid whose [Allow Drag property](https://wiki.genexus.com/commwiki/wiki?9766) is set (without having coded its Drag event), then the drop parameters (&parameter1, &parameter2, ..., &parametern) have to match exactly (in name and datatype) with **n** columns of the source grid. The columns order is not relevant. If any parameter is a SDT, the match is only by datatype, not by name.

*Event\_code*

Code associated with the event. The parameters will be used in order to take some action based on that data received from Drag operation

Note: There is no difference between the navigation of any user event and the navigation of the Drop Event/Drag Event. The rules that apply to the former also apply to the latter.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Controls** | [Image control](https://wiki.genexus.com/commwiki/wiki?5939), [Text Block control](https://wiki.genexus.com/commwiki/wiki?5948), [Table control](https://wiki.genexus.com/commwiki/wiki?6001), [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058), [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), [Web Component control](https://wiki.genexus.com/commwiki/wiki?31172), [Button control](https://wiki.genexus.com/commwiki/wiki?6011) |
| **Interfaces** | Web |
|  |  |

### [Examples](#Examples)

[Drag and Drop in Applications Sample 1](https://wiki.genexus.com/commwiki/wiki?6584)  
[Drag and Drop in Applications Sample 2](https://wiki.genexus.com/commwiki/wiki?6585)  
[Drag and Drop in Applications Sample 3](https://wiki.genexus.com/commwiki/wiki?6586)  
[Drag and Drop in Applications Sample 4](https://wiki.genexus.com/commwiki/wiki?6587)

### [See also](#See+also)

[Drag event in Web](https://wiki.genexus.com/commwiki/wiki?9642)  
[Developing Drag and Drop in Web Panels](https://wiki.genexus.com/commwiki/wiki?5579)


|  |
| --- |
| **Backlinks** |
| [Allow Drag property](https://wiki.genexus.com/commwiki/wiki?9766) | [Allow Drop property](https://wiki.genexus.com/commwiki/wiki?9765) | [Drag event in Web](https://wiki.genexus.com/commwiki/wiki?9642) |
| [Drop event](https://wiki.genexus.com/commwiki/wiki?24080) |

---
