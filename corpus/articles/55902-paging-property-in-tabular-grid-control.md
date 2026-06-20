---
title: "Paging property in Tabular Grid Control"
source_id: 55902
source_url: https://wiki.genexus.com/commwiki/wiki?55902
genexus_version: "18"
---

# Paging property in Tabular Grid Control

Sets if a Tabular Grid control will offer Infinite scrolling or Paging to navigate through it.

### [Values](#Values)

|  |  |
| --- | --- |
| **Infinite scrolling** | Only scroll is offered (there are no buttons to move from page to page). As the user scrolls down, more content is automatically loaded and added at the end of the page. |
| **One page at a time** | Breaks the content into individual pages, with a fixed number of items per page. End users can navigate between pages by clicking on buttons that indicate the page number or by using arrows to move back and forward. |

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Controls:** [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449)

### [Description](#Description)

This property is offered when the [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) value is different from <unlimited> or when it is set to <default> or a specific value is assigned to it.

When the **Paging property** is set to "One page at a time", the [Paging Controls property](https://wiki.genexus.com/commwiki/wiki?55744) is available to be set.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).

### [See Also](#See+Also)

[Paging property in Grids and Free Style Grids](https://wiki.genexus.com/commwiki/wiki?55903)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?54240) | [Paging Controls property](https://wiki.genexus.com/commwiki/wiki?55744) |

---
