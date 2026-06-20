---
title: "PreviousPage method (GeneXus 18 Upgrade 5 or prior)"
source_id: 55992
source_url: https://wiki.genexus.com/commwiki/wiki?55992
genexus_version: "18"
---

# PreviousPage method (GeneXus 18 Upgrade 5 or prior)

Takes the user to the previous group of returned records when the automatic paging of Grids and Free Style Grids is used.

### [Syntax](#Syntax)

*Grid***.PreviousPage()**

### [Scope](#Scope)

**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

This method is available in Grids in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s, whether the Grid has [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) or not.

The [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) must have a value different from 0.

This method's efficiency is associated to the efficiency of the definition of the corresponding grid navigation. In other words, if the grid without paging has good response times, these times will be similar with paging.

Grids may be nested.

### [Values](#Values)

This method may return some of the following values:

|  |  |
| --- | --- |
| **Value** | **Result** |
| **0** | Successful operation |
| **1** | The paging is not enabled in the grid |
| **2** | Already on the first page |

### [Samples](#Samples)

```
Event Back.click
    &err = MyGrid.PreviousPage()
    If &err = 2
       Message.Caption = ‘You already are in the first page’
     EndIf
EndEvent
```

### [See Also](#See+Also)

[FirstPage method](https://wiki.genexus.com/commwiki/wiki?8768)  
[NextPage method](https://wiki.genexus.com/commwiki/wiki?8769)  
[LastPage method](https://wiki.genexus.com/commwiki/wiki?8771)  
[GotoPage method](https://wiki.genexus.com/commwiki/wiki?8772)  
[Rows property](https://wiki.genexus.com/commwiki/wiki?2452)  
[Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064)
