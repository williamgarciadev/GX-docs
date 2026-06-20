---
title: "Deselect method (GeneXus 18 Upgrade 2 or prior)"
source_id: 54487
source_url: https://wiki.genexus.com/commwiki/wiki?54487
genexus_version: "18"
---

# Deselect method (GeneXus 18 Upgrade 2 or prior)

Deselects an item in a Grid by giving its index. If the item is not selected or if it is out of the Grid's scope, it will not have any effect.

### [Syntax](#Syntax)

<GridControlName>.**Deselect(**<index>**)**

**Where:**  
*GridControlName*  
    Is the grid control name.

*index*  
    Is a Numeric expression (attribute, variable or constant value).

### [Scope](#Scope)

**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817)  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

**Notes for Grids in Panels objects:**

* This method will not execute the [default action](https://wiki.genexus.com/commwiki/wiki?20424) associated with the Grid.
* This method will properly switch the [default selected item layout](https://wiki.genexus.com/commwiki/wiki?22556).

### [Availability](#Availability)

This method is available since  [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,) for iOS, [GeneXus 15 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?36355,,) for Android and [Genexus 15 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?38023,,) for Web.

### [See Also](#See+Also)

[Grids with Selection By Code for Panels](https://wiki.genexus.com/commwiki/wiki?35987)  
[Select method](https://wiki.genexus.com/commwiki/wiki?36234)  
[SelectedItem property](https://wiki.genexus.com/commwiki/wiki?36232)  
[SelectionChanged Event](https://wiki.genexus.com/commwiki/wiki?36236)
