---
title: "Tabs.Start event"
source_id: 25596
source_url: https://wiki.genexus.com/commwiki/wiki?25596
genexus_version: "18"
---

# Tabs.Start event

Defines an action to be performed when the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) starts running, and it is a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) with Tabs Control Type.

It is a [Client Event](https://wiki.genexus.com/commwiki/wiki?17042) that takes place before the Server Events (Start, Refresh and Load) and the ClientStart Event.

Since it is a Client Event, the possibilities and limitations are the same as for any other Client Event.

As a Client Event, it shares the same possibilities and limitations as any other Client Event.

### [Syntax](#Syntax)

**Event Tabs.Start**  
*Event\_code*  
**EndEvent**  
  
**Where:**  
*Event\_code*  
Code associated to the event.

### [Examples](#Examples)

```
Event Tabs.Start
  //Call a welcome panel to be displayed.
  SDWelcomePanel.Call()
EndEvent
```

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) |
| **Platforms** | IOS |

### [See also](#See+also)

* [Navigation Start Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?25668)
* [Navigation Style property](https://wiki.genexus.com/commwiki/wiki?16229)
* [ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044)


|  |
| --- |
| **Backlinks** |
| [Flip.Start event](https://wiki.genexus.com/commwiki/wiki?25571) | [Flip.Start event (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55467) | [Navigation Start Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?25668) |

---
