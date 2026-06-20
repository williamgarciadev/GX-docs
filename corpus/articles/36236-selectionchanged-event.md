---
title: "SelectionChanged Event"
source_id: 36236
source_url: https://wiki.genexus.com/commwiki/wiki?36236
genexus_version: "18"
---

# SelectionChanged Event

This event is triggered when the end user selects a new item in a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) or [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449), both programmatically (by using [Select](https://wiki.genexus.com/commwiki/wiki?36234)/[Deselect](https://wiki.genexus.com/commwiki/wiki?36235) methods) or interactively (by [tapping](https://wiki.genexus.com/commwiki/wiki?24120) on a row). In this last case, the event will be executed before the [default action](https://wiki.genexus.com/commwiki/wiki?20424).

### [Syntax](#Syntax)

Event *GridControlName***.SelectionChanged**  
   *<event code>*  
EndEvent

**Where:**  
*GridControlName*  
       Is the Grid control name.  
  
*<event code>*   
       Code executed when the event is triggered.

**Note**: This event will not be triggered when the [Selection Type property](https://wiki.genexus.com/commwiki/wiki?24120) is set to 'No selection'.

### [Limitations](#Limitations)

The SelectionChanged event cannot access attribute values. Use the [default action](https://wiki.genexus.com/commwiki/wiki?20424) event for that.

### [Scope](#Scope)

**Controls:** [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449)  
**Generators:** 
[Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [See Also](#See+Also)

[Grids with Selection By Code for Panels](https://wiki.genexus.com/commwiki/wiki?35987)  
[Select method](https://wiki.genexus.com/commwiki/wiki?36234)  
[SelectedItem property](https://wiki.genexus.com/commwiki/wiki?36232)  
[Deselect method](https://wiki.genexus.com/commwiki/wiki?36235)


|  |
| --- |
| **Backlinks** |
| [Deselect method](https://wiki.genexus.com/commwiki/wiki?36235) | [Deselect method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54487) | [Grids with Selection By Code for Panels](https://wiki.genexus.com/commwiki/wiki?35987) |
| [Maps Control Type Events](https://wiki.genexus.com/commwiki/wiki?54185) | [Select method](https://wiki.genexus.com/commwiki/wiki?36234) | [Select method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54486) | [SelectedItem property](https://wiki.genexus.com/commwiki/wiki?36232) |
| [Selection Type property](https://wiki.genexus.com/commwiki/wiki?24120) | [Selection Type property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54490) | [SelectionChanged Event (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54483) |

---
