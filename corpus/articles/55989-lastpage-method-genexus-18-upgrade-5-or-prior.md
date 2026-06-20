---
title: "LastPage method (GeneXus 18 Upgrade 5 or prior)"
source_id: 55989
source_url: https://wiki.genexus.com/commwiki/wiki?55989
genexus_version: "18"
---

# LastPage method (GeneXus 18 Upgrade 5 or prior)

Goes to the last group of records when paging of Grids and Free Style Grids is used.

### [Syntax](#Syntax)

*Grid***.LastPage()**

### [Scope](#Scope)

**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

This method is available in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s, but it can only be used when the Grid has [Base Table](https://wiki.genexus.com/commwiki/wiki?6347).

The [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) must have a value different than 0.

Grids may be nested.   
  
The LastPage method determines what the last page will be. To this end, it uses the [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) and the Grid RecordCount property. Using the RecordCount property implies that the **DBMS** (not the generated code) sweeps the Grid base table twice (the first time to count and the second to "load").   
  
The LastPage method makes it possible to have just one Load command executed per each record in the base table. Thus, if there are Ifs in the Grid.Load event, which may condition the execution of the command, or if the Load method is executed more than once for each record, outcomes may be unexpected.

### [Values](#Values)

|  |  |
| --- | --- |
| **Value** | **Result** |
| **0** | Successful operation |
| **1** | Paging is not enabled in the Grid |
| **3** | The Grid does not have a base table. |

### [Samples](#Samples)

```
Event Last.Click
    MyGrid.LastPage()
EndEvent
```

### [See Also](#See+Also)

[FirstPage method](https://wiki.genexus.com/commwiki/wiki?8768)  
[NextPage method](https://wiki.genexus.com/commwiki/wiki?8769)  
[PreviousPage method](https://wiki.genexus.com/commwiki/wiki?8770)  
<[GotoPage method|>]  
[RecordCount property](https://wiki.genexus.com/commwiki/wiki?8757)  
[PageCount Property](https://wiki.genexus.com/commwiki/wiki?8755,,)  
[Rows property](https://wiki.genexus.com/commwiki/wiki?2452)  
[Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064)
