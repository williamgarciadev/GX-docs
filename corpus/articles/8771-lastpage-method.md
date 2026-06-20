---
title: "LastPage method"
source_id: 8771
source_url: https://wiki.genexus.com/commwiki/wiki?8771
genexus_version: "18"
---

# LastPage method

Goes to the last group of records when paging of Grids / Free Style Grids / Tabular Grids is used.

### [Syntax](#Syntax)

*GridName***.LastPage()**

**Where:**

*GridName*  
    Is the name of the control to which the method is applied.

### [Scope](#Scope)

**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058), [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

When the automatic paging of a certain Grid is used (its [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) must be set to a value other than 0), and automatic paging buttons are also provided, if, for some reason, you do not want to use those buttons, or any of them, and you want to define a specific paging action, you can then use the LastPage method as well as others related.

This method is available for:

* Grids / Free Style Grids in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s
* Grids / Tabular Grids (generated with Angular) in [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s

It can only be used when the Grid has [Base Table](https://wiki.genexus.com/commwiki/wiki?6347).

Nested grids support this method.   
  
The LastPage method determines what the last page will be. To this end, it uses the [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) and the Grid [RecordCount property](https://wiki.genexus.com/commwiki/wiki?8757). Using the RecordCount property implies that the **DBMS** (not the generated code) sweeps the Grid base table twice (the first time to count, and the second time to "load").   
  
The LastPage method makes it possible to have just one Load command executed per each record in the base table. Thus, if there are Ifs in the Grid.Load event, which may condition the execution of the command, or if the Load method is executed more than once for each record, the outcomes may be unexpected.

### [Values](#Values)

For Web Panel objects, this method may return some of the following values:

|  |  |
| --- | --- |
| **Value** | **Result** |
| **0** | Successful operation |
| **1** | Paging is not enabled in the Grid |
| **3** | The Grid does not have a base table. |

### [Samples](#Samples)

```
Event Last.Click       //Last is the name of a control included in the screen.
    MyGrid.LastPage()
EndEvent
```

### [See Also](#See+Also)

[FirstPage method](https://wiki.genexus.com/commwiki/wiki?8768)  
[NextPage method](https://wiki.genexus.com/commwiki/wiki?8769)  
[PreviousPage method](https://wiki.genexus.com/commwiki/wiki?8770)  
[GotoPage method](https://wiki.genexus.com/commwiki/wiki?8772)  
[RecordCount property](https://wiki.genexus.com/commwiki/wiki?8757)  
[PageCount Property](https://wiki.genexus.com/commwiki/wiki?8755,,)  
[Rows property](https://wiki.genexus.com/commwiki/wiki?2452)  
[Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064)


|  |
| --- |
| **Backlinks** |
| [Automatic paging in Grid control](https://wiki.genexus.com/commwiki/wiki?6086) | [FirstPage method](https://wiki.genexus.com/commwiki/wiki?8768) | [FirstPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55984) |
| [GotoPage method](https://wiki.genexus.com/commwiki/wiki?8772) | [GotoPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55994) | [Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064) | [LastPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55989) |
| [NextPage method](https://wiki.genexus.com/commwiki/wiki?8769) | [NextPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55985) | [Paging in apps](https://wiki.genexus.com/commwiki/wiki?31280) | [PreviousPage method](https://wiki.genexus.com/commwiki/wiki?8770) |
| [PreviousPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55992) |

---
