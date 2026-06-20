---
title: "SelectionChanged Event (GeneXus 18 Upgrade 2 or prior)"
source_id: 54483
source_url: https://wiki.genexus.com/commwiki/wiki?54483
genexus_version: "18"
---

# SelectionChanged Event (GeneXus 18 Upgrade 2 or prior)

This event is triggered when the end user selects a new item in a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), both programmatically (by using [Select](https://wiki.genexus.com/commwiki/wiki?36234)/[Deselect](https://wiki.genexus.com/commwiki/wiki?36235) methods) or interactively (by [tapping](https://wiki.genexus.com/commwiki/wiki?24120) on a row). In this last case, the event will be executed before the [default action](https://wiki.genexus.com/commwiki/wiki?20424).

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

The SelectionChanged event cannot access attributes values. Use the [default action](https://wiki.genexus.com/commwiki/wiki?20424) event for achieving that aim.

### [Scope](#Scope)

**Controls:** [Grid control](https://wiki.genexus.com/commwiki/wiki?24817)  
**Generators:** 
[Apple](https://wiki.genexus.com/commwiki/wiki?14917), 
[Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Availability](#Availability)

This Grid control event is available since  [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,) for [Apple](https://wiki.genexus.com/commwiki/wiki?14917) and [GeneXus 15 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?36355,,) for [Android](https://wiki.genexus.com/commwiki/wiki?14453).

### [See Also](#See+Also)

[Grids with Selection By Code for Panels](https://wiki.genexus.com/commwiki/wiki?35987)  
[Select method](https://wiki.genexus.com/commwiki/wiki?36234)  
[SelectedItem property](https://wiki.genexus.com/commwiki/wiki?36232)  
[Deselect method](https://wiki.genexus.com/commwiki/wiki?36235)
