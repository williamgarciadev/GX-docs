---
title: "Flip.Start event"
source_id: 25571
source_url: https://wiki.genexus.com/commwiki/wiki?25571
genexus_version: "18"
---

# Flip.Start event

Defines an action to be performed when the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) starts running if the Navigation Style property is set to Flip.

It is a [Client Event](https://wiki.genexus.com/commwiki/wiki?17042) that takes place before the Server Events ([Start](https://wiki.genexus.com/commwiki/wiki?8043), [Refresh](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?8195,,), and [Load](https://wiki.genexus.com/commwiki/wiki?8188)) and the [ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044).

Since it is a Client Event, it has the same possibilities and limitations as any other Client Event.

### [Syntax](#Syntax)

**Event Flip.Start**  
*Event\_code*  
**EndEvent**  
  
**Where:**  
  
*Event\_code*  
   Code associated with the event.

### [Samples](#Samples)

```
Event Flip.Start  
//Calls the tab where you want to start the application
      PanelStart()  
EndEvent
```

### [Considerations](#Considerations)

It is important to note that when using the Apple generator, [Menu object](https://wiki.genexus.com/commwiki/wiki?16321)s are shown by default as [Tabs](https://wiki.genexus.com/commwiki/wiki?55318). Therefore, if you have a Menu object with the default control type and the [Navigation Style property](https://wiki.genexus.com/commwiki/wiki?16229) is set to Flip, the event executed will be [Tabs.Start event](https://wiki.genexus.com/commwiki/wiki?25596).

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects:** | [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Menu](https://wiki.genexus.com/commwiki/wiki?16321) |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

### [See Also](#See+Also)

[Navigation Start Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?25668)  
[ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044)  
[Navigation Style property](https://wiki.genexus.com/commwiki/wiki?16229)


|  |
| --- |
| **Backlinks** |
| [Flip.Start event (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55467) | [Navigation Start Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?25668) |

---
