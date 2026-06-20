---
title: "FirstPage method"
source_id: 8768
source_url: https://wiki.genexus.com/commwiki/wiki?8768
genexus_version: "18"
---

# FirstPage method

Takes the end user to the first group of returned records when the automatic paging of Grids / Free Style Grids / Tabular Grids is used.

### [Syntax](#Syntax)

*GridName***.FirstPage()**

**Where:**

*GridName*  
    Is the name of the control to which the method is applied.

### [Scope](#Scope)

**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058), [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449).  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550).

### [Description](#Description)

When the automatic paging of a particular Grid is used (its [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) must be set to a value other than 0), and automatic paging buttons are also provided, if, for any reason, you do not want to use those buttons, or some of them, and you want to define a specific paging action, you can then use the FirstPage method as well as others related.

This method is available for:

* Grids / Free Style Grids in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s
* Grids / Tabular Grids (generated with Angular) in [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s

whether the control has [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) or not.

Nested grids support this method.

If the Web Panel / Panel that is being paged has filters, then the FirstPage method should be added within the user event that applies the filter, in order to avoid the displayed result correspondence with the page where it was previously located.

This method's efficiency relates to the efficiency of the definition of the corresponding Grid navigation. In other words, if the Grid without paging has good response times, then such times will be similar to when you have paging.

### [Values](#Values)

In Web Panels objects, this method may return some of the following values:

|  |  |
| --- | --- |
| **Value** | **Result** |
| **0** | Successful operation |
| **1** | The paging is not enabled in the grid |

### [Samples](#Samples)

```
Event 'FirstPage'
    MyGrid.FirstPage()
EndEvent
```

In this example, when the end user presses the button associated with the 'FirstPage' event, the Grid / Free Style Grid / Tabular Grid will show the first group of records.

### [See Also](#See+Also)

[NextPage method](https://wiki.genexus.com/commwiki/wiki?8769)  
[PreviousPage method](https://wiki.genexus.com/commwiki/wiki?8770)  
[LastPage method](https://wiki.genexus.com/commwiki/wiki?8771)  
[GotoPage method](https://wiki.genexus.com/commwiki/wiki?8772)  
[RecordCount property](https://wiki.genexus.com/commwiki/wiki?8757)  
[PageCount Property](https://wiki.genexus.com/commwiki/wiki?8755,,)  
[Rows property](https://wiki.genexus.com/commwiki/wiki?2452)  
[Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064)


|  |
| --- |
| **Backlinks** |
| [FirstPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55984) | [GotoPage method](https://wiki.genexus.com/commwiki/wiki?8772) | [GotoPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55994) |
| [Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064) | [LastPage method](https://wiki.genexus.com/commwiki/wiki?8771) | [LastPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55989) | [NextPage method](https://wiki.genexus.com/commwiki/wiki?8769) |
| [NextPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55985) | [Paging in apps](https://wiki.genexus.com/commwiki/wiki?31280) | [PreviousPage method](https://wiki.genexus.com/commwiki/wiki?8770) | [PreviousPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55992) |

---
