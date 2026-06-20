---
title: "GotoPage method (GeneXus 18 Upgrade 5 or prior)"
source_id: 55994
source_url: https://wiki.genexus.com/commwiki/wiki?55994
genexus_version: "18"
---

# GotoPage method (GeneXus 18 Upgrade 5 or prior)

Allows direct access to a specific group of records, when the automatic paging of Grids and Free Style Grids is used.

### [Syntax](#Syntax)

*Grid.***GotoPage(***page-number***)**  
  
**Where:**  
*Grid*  
    Grid control

*page-number*  
    Is a numeric value

### [Scope](#Scope)

**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

This method can be used in [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916), but only when the grid has [Base Table](https://wiki.genexus.com/commwiki/wiki?6347). The [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) must have a value different from 0. Grids may be nested.

This method's efficiency is associated with the efficiency of the definition of the corresponding grid navigation. In other words, if the grid has good response times without paging, these times will be similar to with paging.

### [Values](#Values)

This method may return some of the following values:

|  |  |
| --- | --- |
| **Value** | **Result** |
| **0** | Successful operation |
| **1** | The paging is not enabled in the grid |

### [Samples](#Samples)

In this example, there is a grid (GSearchResults) with the result of a search and, another one (GPages) with the number of pages of the first one, so as to allow a fast access paging.

```
Event Refresh
    &PageCounts = GSearchResults.PageCount
EndEvent  

Event GPages.Load
    if &PageCounts > 1
       &Count = 1
       Do while &Count <= &PageCounts
          &PageNumber = &Count
           SFPages.Load()
          &Count += 1
       EndDo
    EndIf
EndEvent  

Event &PageNumber.Click
    GSearchResults.GotoPage(&PageNumber)
EndEvent
```

### [See Also](#See+Also)

[FirstPage](https://wiki.genexus.com/commwiki/wiki?8768)  
[NextPage](https://wiki.genexus.com/commwiki/wiki?8769)  
[LastPage](https://wiki.genexus.com/commwiki/wiki?8771)  
[PreviousPage Method](https://wiki.genexus.com/commwiki/wiki?8770)  
[Rows property](https://wiki.genexus.com/commwiki/wiki?2452)  
[Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064)
