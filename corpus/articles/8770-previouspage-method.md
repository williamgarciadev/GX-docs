---
title: "PreviousPage method"
source_id: 8770
source_url: https://wiki.genexus.com/commwiki/wiki?8770
genexus_version: "18"
---

# PreviousPage method

Takes the end user to the previous group of returned records when the automatic paging of Grids / Free Style Grids / Tabular Grids is used.

### [Syntax](#Syntax)

*GridName***.PreviousPage()**

**Where:**

*GridName*  
    Is the name of the control to which the method is applied.

### [Scope](#Scope)

**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058), [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

When the automatic paging of a particular Grid is used (its [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) must be set to a value different from 0), and automatic paging buttons are also provided, if, for any reason, you do not want to use those buttons, or any of them, and you want to define a specific paging action, you can then use the PreviousPage method as well as others related.

This method is available for:

* Grids / Free Style Grids in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s
* Grids / Tabular Grids (generated with Angular) in [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s

whether the control has [Base Table](https://wiki.genexus.com/commwiki/wiki?6347) or not.

Nested grids support this method.

This method's efficiency relates to the efficiency of the definition of the corresponding grid navigation. In other words, if the Grid without paging has good response times, then such times will be similar to when you have paging.

### [Values](#Values)

For Web Panel objects, this method may return some of the following values:

|  |  |
| --- | --- |
| **Value** | **Result** |
| **0** | Successful operation |
| **1** | The paging is not enabled in the grid |
| **2** | Already on the first page |

### [Samples](#Samples)

The following code may be defined in a Web Panel and MyGid is a Grid or a Free Style Grid. When working with Tabular Grids no values are returned.

```
Event 'Back'                      //Back is the name of a control included in the screen.
    &err = MyGrid.PreviousPage()
    If &err = 2
       msg('You already are in the first page')
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


|  |
| --- |
| **Backlinks** |
| [FirstPage method](https://wiki.genexus.com/commwiki/wiki?8768) | [FirstPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55984) | [GotoPage method](https://wiki.genexus.com/commwiki/wiki?8772) |
| [GotoPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55994) | [Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064) | [HowTo: Configure Infinite Scrolling in web applications](https://wiki.genexus.com/commwiki/wiki?31232) | [LastPage method](https://wiki.genexus.com/commwiki/wiki?8771) |
| [LastPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55989) | [NextPage method](https://wiki.genexus.com/commwiki/wiki?8769) | [NextPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55985) | [Paging in apps](https://wiki.genexus.com/commwiki/wiki?31280) |
| [PreviousPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55992) |

---
