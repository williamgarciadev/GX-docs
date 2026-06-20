---
title: "Split.Start event"
source_id: 25586
source_url: https://wiki.genexus.com/commwiki/wiki?25586
genexus_version: "18"
---

# Split.Start event

Defines an action to be performed when the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) starts running if the Navigation Style property is set to Split.

It is a [Client Event](https://wiki.genexus.com/commwiki/wiki?17042) that takes place before the Server Events ([Start](https://wiki.genexus.com/commwiki/wiki?8043), [Refresh](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8195,,) and [Load](https://wiki.genexus.com/commwiki/wiki?8188)) and the [ClientStart Event](https://wiki.genexus.com/commwiki/wiki?24044).

Since it is a Client Event, the possibilities and limitations are the same as for any other Client Event.

### [Syntax](#Syntax)

**Event Split.Start**  
*Event\_code*  
**EndEvent**  
  
**Where:**

*Event\_code*  
        The code to be executed when the event is triggered.

### [Samples](#Samples)

```
Event Split.Start
  //Call a Panel to be displayed.
  Panel.CallOptions.Target = 'Right'
  Panel.Call()
EndEvent
```

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Object:** | [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) |
| **Generator:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917) |

### [See Also](#See+Also)

[Navigation Start Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?25668)  
[Navigation Style property](https://wiki.genexus.com/commwiki/wiki?16229)  
[ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044)


|  |
| --- |
| **Backlinks** |
| [Navigation Start Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?25668) |

---
