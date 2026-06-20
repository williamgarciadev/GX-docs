---
title: "FirstPage method (GeneXus 18 Upgrade 5 or prior)"
source_id: 55984
source_url: https://wiki.genexus.com/commwiki/wiki?55984
genexus_version: "18"
---

# FirstPage method (GeneXus 18 Upgrade 5 or prior)

Takes the user to the first group of returned records when the automatic paging of Grids and Free Style Grids is used.

### [Syntax](#Syntax)

*Grid***.FirstPage()**

### [Scope](#Scope)

**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

This method is available in Grids in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s, whether the grid has [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) or not.

The [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) must have a value different from 0.

If the Web Panel which is being paged has filters, the FirstPage method should be added within the user event which applies the filter, so as to avoid that the displayed result corresponds to the page where it was previously located.

This method's efficiency is associated to the efficiency of the definition of the corresponding Grid navigation. In other words, if the Grid without paging has good response times, these times will be similar with paging.

Grids may be nested.

### [Values](#Values)

This method may return some of the following values:

|  |  |
| --- | --- |
| **Value** | **Result** |
| **0** | Successful operation |
| **1** | The paging is not enabled in the grid |

### [Samples](#Samples)

```
Event Enter
    MyGrid.FirstPage()
EndEvent
```

In this example when the user presses enter, the Grid will show the first group of records.

### [See Also](#See+Also)

[NextPage method](https://wiki.genexus.com/commwiki/wiki?8769)  
[PreviousPage method](https://wiki.genexus.com/commwiki/wiki?8770)  
[LastPage method](https://wiki.genexus.com/commwiki/wiki?8771)  
[GotoPage method](https://wiki.genexus.com/commwiki/wiki?8772)  
[RecordCount property](https://wiki.genexus.com/commwiki/wiki?8757)  
[PageCount Property](https://wiki.genexus.com/commwiki/wiki?8755,,)  
[Rows property](https://wiki.genexus.com/commwiki/wiki?2452)  
[Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064)
