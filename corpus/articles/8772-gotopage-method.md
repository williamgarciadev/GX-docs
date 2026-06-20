---
title: "GotoPage method"
source_id: 8772
source_url: https://wiki.genexus.com/commwiki/wiki?8772
genexus_version: "18"
---

# GotoPage method

Takes the end user to a specific group of records, when the automatic paging of Grids / Free Style Grids / Tabular Grids is used.

### [Syntax](#Syntax)

*GridName.***GotoPage(***page-number***)**  
  
**Where:**  
*GridName*  
    Is the name of the control to which the method is applied.

*page-number*  
    Is a numeric value that indicates the number of the specific page to which the method will take the end user.

### [Scope](#Scope)

**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058), [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

When the automatic paging of a particular Grid is used (its [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) must be set to a value other than 0), the GotoPage method allows accessing a specific group of records.

This method is available for:

* Grids / Free Style Grids in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s
* Grids / Tabular Grids (generated with Angular) in [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s

whether the control has [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) or not.

Nested grids support this method.

This method's efficiency relates to the efficiency of the definition of the corresponding grid navigation. In other words, if the grid has good response times without paging, then such times will be similar to when you have paging.

### [Values](#Values)

For Web Panel objects, this method may return some of the following values:

|  |  |
| --- | --- |
| **Value** | **Result** |
| **0** | Successful operation |
| **1** | The paging is not enabled in the grid |

### [Samples](#Samples)

In this example, there is a Grid (GSearchResults) with the result of a search, and another one (GPages) with the number of pages of the first one in a [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132).

```
Event Refresh
    &PageCounts = GSearchResults.PageCount
EndEvent  

Event GPages.Load
    if &PageCounts > 1
       &Count = 1
       Do while &Count <= &PageCounts
          &PageNumber = &Count
           GPages.Load()
          &Count += 1
       EndDo
    EndIf
EndEvent  

Event &PageNumber.Click
    GSearchResults.GotoPage(&PageNumber)
EndEvent
```

### [See Also](#See+Also)

[FirstPage method](https://wiki.genexus.com/commwiki/wiki?8768)  
[NextPage method](https://wiki.genexus.com/commwiki/wiki?8769)  
[LastPage method](https://wiki.genexus.com/commwiki/wiki?8771)  
[PreviousPage method](https://wiki.genexus.com/commwiki/wiki?8770)  
[Rows property](https://wiki.genexus.com/commwiki/wiki?2452)  
[Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064)


|  |
| --- |
| **Backlinks** |
| [Automatic paging in Grid control](https://wiki.genexus.com/commwiki/wiki?6086) | [FirstPage method](https://wiki.genexus.com/commwiki/wiki?8768) | [FirstPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55984) |
| [GotoPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55994) | [Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064) | [LastPage method](https://wiki.genexus.com/commwiki/wiki?8771) | [NextPage method](https://wiki.genexus.com/commwiki/wiki?8769) |
| [NextPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55985) | [PreviousPage method](https://wiki.genexus.com/commwiki/wiki?8770) | [PreviousPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55992) |

---
