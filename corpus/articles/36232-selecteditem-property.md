---
title: "SelectedItem property"
source_id: 36232
source_url: https://wiki.genexus.com/commwiki/wiki?36232
genexus_version: "18"
---

# SelectedItem property

Read-only property for getting the index of the selected item in the Grid. When there is no selected item or the Grid admits [multiple selections](https://wiki.genexus.com/commwiki/wiki?16149) it will return 0 (empty value).

**Warning**: If this property is read in the ClientStart event after executing the [Select method](https://wiki.genexus.com/commwiki/wiki?36234), it will return the empty value (i.e. 0) because the Grid's content will not be loaded until after the execution of the Load event..

## [Syntax](#Syntax)

<index> = Grid.SelectedItem

**Where:**

*Grid*  
    Is the Grid control name.

*<index>*   
    Is a Numeric [expression](https://wiki.genexus.com/commwiki/wiki?51320,,) (variable or attribute).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Controls:** | [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

## [Run-time/Design-time](#Run-time%2FDesign-time)

This property applies only at design-time.

## [Availability](#Availability)

This property is available as of [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,) for iOS and [GeneXus 15 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?36355,,) for Android..

## [See also](#See+also)

* [Grids with Selection By Code for Panels](https://wiki.genexus.com/commwiki/wiki?35987)
* [Select method](https://wiki.genexus.com/commwiki/wiki?36234)
* [Deselect method](https://wiki.genexus.com/commwiki/wiki?36235)
* [SelectionChanged Event](https://wiki.genexus.com/commwiki/wiki?36236)


|  |
| --- |
| **Backlinks** |
| [Deselect method](https://wiki.genexus.com/commwiki/wiki?36235) | [Deselect method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54487) | [Grids with Selection By Code for Panels](https://wiki.genexus.com/commwiki/wiki?35987) |
| [Select method](https://wiki.genexus.com/commwiki/wiki?36234) | [Select method (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54486) | [SelectionChanged Event](https://wiki.genexus.com/commwiki/wiki?36236) | [SelectionChanged Event (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54483) |

---
