---
title: "Rows property"
source_id: 2452
source_url: https://wiki.genexus.com/commwiki/wiki?2452
genexus_version: "18"
---

# Rows property

Sets the number of records to be loaded by the Grid or Free Style Grid in Web Panels and Panels, or the number of empty lines in Transactions Grids.

### [Syntax](#Syntax)

**control.** Rows = number   

#### [Values](#Values)

Any positive number or zero (Unlimited).

#### [Effects of Rows = 0 (Unlimited)](#Effects+of+Rows+%3D+0+%28Unlimited%29)

The effect of Rows = 0 (Unlimited)is the following:

* Rows = 0 (Unlimited) in Web Panels as well as in Panels, indicates that there will be as many lines displayed as records resulting from the associated query.
* The 0 value in Transactions indicates that there will be no empty lines in the grid.

#### [Default values](#Default+values)

|  |  |  |
| --- | --- | --- |
| **Object** | **Default Value** |  |
| Transactions | 5 | Indicates the number of empty lines to be shown on the grid. |
| Web Panels and Panels | 0 (Unlimited) | Indicates the number of records to be loaded in the grid. Zero means all the records. |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058)

### [Description](#Description)

When Rows is set to a value different than zero (unlimited), it's assumed that some type of paging is going to be implemented for the grid. Paging type can be [automatic](https://wiki.genexus.com/commwiki/wiki?6086) or [manual](6064'.html).

For mobile apps, [Infinite scrolling](https://wiki.genexus.com/commwiki/wiki?31231) is always performed and the Rows property determines the page size of the grid which is brought to the client. Data is brought to the client on demand, as the user swipes (up or down) in the grid.

For Web applications, when the Rows property is set to a value different than zero (unlimited), the [Paging](https://wiki.genexus.com/commwiki/wiki?55903) is enabled, so the user can decide if the grid will show paging buttons or if it will perform [Infinite scrolling](https://wiki.genexus.com/commwiki/wiki?31231). Infinite scrolling is supported for the [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209) only.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [Samples](#Samples)

#### [Example: adding lines to a web transaction's grid](#Example%3A+adding+lines+to+a+web+transaction%27s+grid)

To allow the end user to enter lines one by one in a web transaction, you can set this property by combining it with the [AddLines method](https://wiki.genexus.com/commwiki/wiki?10123) at execution time, as follows:

```
Event Start
    if &Mode = 'INS'
        Grid1.Rows = 1
    else    // &Mode = UPD / DLT / DSP
        Grid1.Rows = 0
    endif
EndEvent

Event 'AddLines'
    Grid1.AddLines(1)
EndEvent  // 'Addlines'
```

Then, the end user can press the AddLines button in Insert Mode to add empty lines one by one to the Transaction.

### [See Also](#See+Also)

[HowTo: Configure Infinite Scrolling in web applications](https://wiki.genexus.com/commwiki/wiki?31232)  
[Infinite scrolling](https://wiki.genexus.com/commwiki/wiki?31231)


|  |
| --- |
| **Backlinks** |
| [Auto Grow in Grids for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22697) | [Automatic paging in Grid control](https://wiki.genexus.com/commwiki/wiki?6086) | [Columns property for Free Style Grids in RWD](https://wiki.genexus.com/commwiki/wiki?26600) |
| [CurrentPage property](https://wiki.genexus.com/commwiki/wiki?10328) | [Dimensions property](https://wiki.genexus.com/commwiki/wiki?7380) | [FirstPage method](https://wiki.genexus.com/commwiki/wiki?8768) | [FirstPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55984) |
| [Fixed Grid header with vertical scroll](https://wiki.genexus.com/commwiki/wiki?36036) | [GotoPage method](https://wiki.genexus.com/commwiki/wiki?8772) | [GotoPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55994) | [Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064) |
| [HowTo: Configure Infinite Scrolling in web applications](https://wiki.genexus.com/commwiki/wiki?31232) | [HowTo: Work with rows in a Transaction Grid](https://wiki.genexus.com/commwiki/wiki?6816) | [Infinite scrolling](https://wiki.genexus.com/commwiki/wiki?31231) | [LastPage method](https://wiki.genexus.com/commwiki/wiki?8771) |
| [LastPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55989) | [Load event](https://wiki.genexus.com/commwiki/wiki?8188) | [Maximum workFile lines property](https://wiki.genexus.com/commwiki/wiki?8966) | [NextPage method](https://wiki.genexus.com/commwiki/wiki?8769) |
| [NextPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55985) | [Paging property in Grids and Free Style Grids](https://wiki.genexus.com/commwiki/wiki?55903) | [Paging property in Tabular Grid Control](https://wiki.genexus.com/commwiki/wiki?55902) | [PreviousPage method](https://wiki.genexus.com/commwiki/wiki?8770) |
| [PreviousPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55992) | [Scroll Bar property](https://wiki.genexus.com/commwiki/wiki?31236) |

---
