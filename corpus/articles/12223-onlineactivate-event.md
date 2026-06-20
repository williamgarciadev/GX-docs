---
title: "OnLineActivate event"
source_id: 12223
source_url: https://wiki.genexus.com/commwiki/wiki?12223
genexus_version: "18"
---

# OnLineActivate event

Triggered when a [Grid](https://wiki.genexus.com/commwiki/wiki?24817) line is activated, that is, when clicking over the line with the mouse or moving through the grid with the keyboard keys and also when the grid is refreshed.

This is useful for example when enabling or disabling buttons based on the values of the actual Grid line, etc.

### [Syntax](#Syntax)

Event Grid**.OnlineActivate**  
*Code*  
EndEvent

### [Example](#Example)

Information on articles is displayed and depending on the type of article that is selected the 'see detail' button will or will not be enabled.

```
Event Articles.OnLineActivate 
    If ArtType = 'X' 
       Details.Enabled = 1 
    Else 
       Details.Enabled = 0 
    Endif
EndEvent
```

**Tip:** "Articles" is the name of the grid control. If no name is assigned to the grid then you will not be able to use this event.

The values of the attributes/variables made available to the event come from the selected row. That is, if the cursor is positioned over line one and then the cursor moves down to line two, then the values that are considered will be those of line two.

All for each groups included in that event will be nested to the work panel's base table, that is, they behave as [For Each](https://wiki.genexus.com/commwiki/wiki?24744) groups do when included.

**Note:** The grid [Allow Selection property](https://wiki.genexus.com/commwiki/wiki?8680) must be set to True.

### [Considerations](#Considerations)

This event can be executed on client side or server side, depending of the code programmed on it. Check [this](https://wiki.genexus.com/commwiki/wiki?6563,,) document for more details.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel object](https://wiki.genexus.com/commwiki/wiki?7387,,) |
| **Controls** | [Grids](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grids](https://wiki.genexus.com/commwiki/wiki?6058) |
| **Languages** | .Net, Java, Ruby, Visual FoxPro |
| **Interfaces** | Web, Win |
|  |  |

### [See also](#See+also)

[Allow Selection property](https://wiki.genexus.com/commwiki/wiki?8680)


|  |
| --- |
| **Backlinks** |
| [Allow Selection property](https://wiki.genexus.com/commwiki/wiki?8680) |

---
