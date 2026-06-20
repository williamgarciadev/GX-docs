---
title: "Select method"
source_id: 36234
source_url: https://wiki.genexus.com/commwiki/wiki?36234
genexus_version: "18"
---

# Select method

Selects an item in the Grid by giving its index value (starting at 1).

## [Syntax](#Syntax)

<GridControlName>.**Select(**<index>**)**

**Where:**

*GridControlName*  
     Is the name of the grid control or Tabular Grid Control.

*index*  
     Is a Numeric expression (attribute, variable or constant value).

### [Scope](#Scope)

**Controls:** [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449)  
**Generators:**

[Apple](https://wiki.genexus.com/commwiki/wiki?14917),
[Android](https://wiki.genexus.com/commwiki/wiki?14453),
[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

**Notes:**

* If the index is out of the Grid's scope (i.e. larger value than the number of rows loaded), it will not have any effect. If the selected index's corresponding item is not visible, the content will scroll automatically so that the item is shown on the screen.

**Notes for Grids in Panels:**

* Will not execute the [default action](https://wiki.genexus.com/commwiki/wiki?20424) associated with the Grid.
* Will properly switch the [default selected item layout](https://wiki.genexus.com/commwiki/wiki?22556).
* In
  [Apple](https://wiki.genexus.com/commwiki/wiki?14917), when the method is triggered, it will apply the *Highlight Background Color property* from the GridRow theme class.  
  In
  [Android](https://wiki.genexus.com/commwiki/wiki?14453), there is no user feedback when selection is done by code.  
  In order to achieve the same behavior on both platforms, make sure that the Highlight Background Color property is empty.
* When Grid control allows [Multiple Selection](https://wiki.genexus.com/commwiki/wiki?16149), this method has different behaviors depending on the [Show Selector property](https://wiki.genexus.com/commwiki/wiki?36199) value.
  + *Always*  
    Will be accumulative.
  + *On Action*  
    Won't be accumulative and the UI effect depends on [Selection Type property](https://wiki.genexus.com/commwiki/wiki?24120) value.

### [See Also](#See+Also)

[Grids with Selection By Code for Panels](https://wiki.genexus.com/commwiki/wiki?35987)  
[SelectedItem property](https://wiki.genexus.com/commwiki/wiki?36232)  
[SelectionChanged Event](https://wiki.genexus.com/commwiki/wiki?36236)  
[Deselect method](https://wiki.genexus.com/commwiki/wiki?36235)


|  |
| --- |
| **Backlinks** |
| [Deselect method](https://wiki.genexus.com/commwiki/wiki?36235) | [Deselect method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54487) |
| [Grids with Selection By Code for Panels](https://wiki.genexus.com/commwiki/wiki?35987) | [Maps Control Type Methods](https://wiki.genexus.com/commwiki/wiki?54095) | [Select method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54486) | [SelectedItem property](https://wiki.genexus.com/commwiki/wiki?36232) |
| [SelectionChanged Event](https://wiki.genexus.com/commwiki/wiki?36236) | [SelectionChanged Event (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54483) |

---
