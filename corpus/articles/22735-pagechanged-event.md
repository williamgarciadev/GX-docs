---
title: "PageChanged event"
source_id: 22735
source_url: https://wiki.genexus.com/commwiki/wiki?22735
genexus_version: "18"
---

# PageChanged event

Takes place right after the user changes the current page of the grid by swiping it.  
It might be helpful for developers who design UI elements such as "Page 9 of 13".

### [Syntax](#Syntax)

**Event** *GridControl***.PageChanged**  
      *Event\_Code*  
**EndEvent**

**Where:**  
*GridControl*  
   Is the name of the grid inserted in a layout and GridControl [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) is one of the controls declared in the Scope below.

*Event\_code*  
   Code executed when the event triggers.

### [Samples](#Samples)

```
Event GridImages.PageChanged
    &CurrentPage = Grid1.CurrentPage
EndEvent
```

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects:** | [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) |
| **Controls:** | [SD Paged Grid](https://wiki.genexus.com/commwiki/wiki?17302,,), [SD Horizontal Grid](https://wiki.genexus.com/commwiki/wiki?18180), [SD Magazine Viewer](https://wiki.genexus.com/commwiki/wiki?17567) |
| **Generators:** | [Apple platform](https://wiki.genexus.com/commwiki/wiki?14917), [Android platform](https://wiki.genexus.com/commwiki/wiki?14453) |

**Note**: On this event, you can access attributes or variables values displayed in the first ítem of the grid and the whole content of the form.

### [See Also](#See+Also)

[CurrentPage property](https://wiki.genexus.com/commwiki/wiki?10328)


|  |
| --- |
| **Backlinks** |
| [Category:Control Events](https://wiki.genexus.com/commwiki/wiki?24271) |

---
