---
title: "Tab Page Control for Native Mobile Applications"
source_id: 25638
source_url: https://wiki.genexus.com/commwiki/wiki?25638
genexus_version: "18"
---

# Tab Page Control for Native Mobile Applications

In some cases, you may want to show, hide, or change the style -Class- to the tabs on a Tab Control in design or runtime based on different conditions.  
In order to do this, each Tab Page Control on a Tab Control is defined with its own name and can be modified separately.

### [Properties](#Properties)

* Visible
* [Enabled](https://wiki.genexus.com/commwiki/wiki?8765)
* Class
* SelectedClass

### [Examples](#Examples)

Changing a single tab Selected Class

```
Event 'ChangeTabClass'
    TabPage3.SelectedClass = 'TabPageSelected2'
EndEvent
```

Hiding a tab depending on user roles

```
Event Refresh
    UserIsAdmin(&Boolean)
    If &Boolean
        TabConfiguration.Visible = True
    Else
        TabConfiguration.Visible = False
    EndIf
EndEvent
```


|  |
| --- |
| **Backlinks** |
| [HowTo: Adding Material Design to Android applications](https://wiki.genexus.com/commwiki/wiki?31004) | [Tab control for Panels](https://wiki.genexus.com/commwiki/wiki?29986) |

---
