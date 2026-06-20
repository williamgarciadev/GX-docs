---
title: "Flip.Start event (GeneXus 18 Upgrade 4 or prior)"
source_id: 55467
source_url: https://wiki.genexus.com/commwiki/wiki?55467
genexus_version: "18"
---

# Flip.Start event (GeneXus 18 Upgrade 4 or prior)

It defines an action to be performed when the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770) starts running if *Flip Navigation Style* is selected. It is a [Client Event](https://wiki.genexus.com/commwiki/wiki?17042) that takes place before the Server Events (Start, Refresh and Load) and the ClientStart Event.

Since it is a Client Event, the possibilities and limitations are the same as for any other Client Event.

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

It is important to note that, by default, the [Menu object](https://wiki.genexus.com/commwiki/wiki?16321)s are shown as tabs. Therefore, if you have a Menu object with the default control type and the [Navigation Style property](https://wiki.genexus.com/commwiki/wiki?16229) is set to Flip, the event executed will be the [Tabs.Start event](https://wiki.genexus.com/commwiki/wiki?25596).

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects:** | [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Menu](https://wiki.genexus.com/commwiki/wiki?16321) |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917) |

### [See also](#See+also)

* [Navigation Start Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?25668)
* [ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044)
* [Navigation Style property](https://wiki.genexus.com/commwiki/wiki?16229)
