---
title: "Grid paging on the Web"
source_id: 6064
source_url: https://wiki.genexus.com/commwiki/wiki?6064
genexus_version: "18"
---

# Grid paging on the Web

For usability and performance reasons, it is convenient to display grid results in a fixed-size grid and provide buttons to browse the pages (Grid paging).

Paging applies to Grids and Free Style Grids, as well as to nested grids.

Paging can be [automatic](https://wiki.genexus.com/commwiki/wiki?6086) or manual, when the grid [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) has a value other than zero.  
  
For manual paging, you have methods associated with the Grid control.

Below are the methods available to handle manual paging:

### [FirstPage](#FirstPage)

The FirstPage method takes the user to the first set of returned records. For example, in the code below, when the user clicks on the button associated with the Enter event, the first set of records will be displayed in the grid.

```
Event Enter

    MyGrid.FirstPage()

Endevent
```

### [NextPage](#NextPage+)

The NextPage method displays the set of records that follow.

```
Event 'NextList'

    &err = MyGrid.NextPage()

    if &err = 2

       Message.Caption = 'Last page already displayed'

    endif

Endevent
```

In this example, when the user clicks on the NextList button, the Grid will display the set of records that follow. If the last page is already loaded, the message  "Last page already displayed" will be shown in the Message text block.

### [PreviousPage](#PreviousPage)

The PreviousPage method displays the previous set of records.

```
Event 'BackList'

    &err = MyGrid.PreviousPage()

    if &err = 2

        Message.Caption = ‘First page already displayed’

    endif

Endevent
```

In this example, when the user clicks on the BackList button, the Grid will show the previous set of records. If the first page is already loaded, the "First page already displayed" message will be displayed in the Message textblock.

### [LastPage](#LastPage)

The LastPage method takes the user to the last set of records. It can be used only if the grid has a base table.

```
Event 'Last'

    MyGrid.LastPage()

Endevent
```

In this example, when the user clicks on the Last button, the grid will display the last set of records.

### [GoToPage](#GoToPage)

The GotoPage(PageNumber) method gives direct access to a particular set of records. It can be used only if the grid has a base table. The following example shows a call to the page corresponding to a set of data.

```
Event 'GoTo'

MyGrid.GoToPage(&PageNbr)

EndEvent
```

Methods return a value after execution.

* 0: Successful operation.
* 1: Grid paging is not enabled.
* 2: Last page already displayed or First page already displayed (according to the NextPage or PreviousPage method, respectively).
* 3: The grid doesn't have a base table.

### [Considerations](#+Considerations)

* If paging is applied to a web panel that has filters, the FirstPage method should be used in the event that applies the filter so as not to display the result corresponding to the previous page.
* The efficiency of the FirstPage, NextPage, PreviousPage and GotoPage(N) methods is related to the efficiency of the navigation defined for the corresponding Grid. In other words, if the grid has good response times without paging, the response times with paging will be similar.   
  Consider that [Server Paging](https://wiki.genexus.com/commwiki/wiki?15589) is used when it's possible: when any of the conditions used to navigate the Grid (Where conditions) is evaluated in the client, [Server Paging](https://wiki.genexus.com/commwiki/wiki?15589) optimization is not performed.
* The RecordCount, LastPage, and GotPage methods are not implemented for Grids without a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347), or Grids that have a Base table but any of their conditions are evaluated on the client side (cannot be evaluated by the DBMS).

### [Implementation](#Implementation)

When [Server Paging](https://wiki.genexus.com/commwiki/wiki?15589) cannot be used, Paging is done per "record number". To show page N, the records in previous pages (N-1) are read without being displayed.

### [Given the implementation, it is recommended:](#Given+the+implementation%2C+it+is+recommended%3A)

* Having good data filtering (so that there aren't many pages).
* Avoiding, when the cost is high, the use of GotoPage(N) with high N values, as well as the use of LastPage.
* Saving the value of the RecordCount property in a variable, since each call to the property implies a COUNT in the database.

### [See Also](#See+Also)

[FirstPage method](https://wiki.genexus.com/commwiki/wiki?8768)  
[NextPage method](https://wiki.genexus.com/commwiki/wiki?8769)  
[PreviousPage method](https://wiki.genexus.com/commwiki/wiki?8770)  
[LastPage method](https://wiki.genexus.com/commwiki/wiki?8771)  
[GotoPage method](https://wiki.genexus.com/commwiki/wiki?8772)  
[CurrentPage property](https://wiki.genexus.com/commwiki/wiki?10328)


|  |
| --- |
| **Backlinks** |
| [Automatic paging in Grid control](https://wiki.genexus.com/commwiki/wiki?6086) | [CurrentPage property](https://wiki.genexus.com/commwiki/wiki?10328) | [FirstPage method](https://wiki.genexus.com/commwiki/wiki?8768) |
| [FirstPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55984) | [GotoPage method](https://wiki.genexus.com/commwiki/wiki?8772) | [GotoPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55994) | [LastPage method](https://wiki.genexus.com/commwiki/wiki?8771) |
| [LastPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55989) | [NextPage method](https://wiki.genexus.com/commwiki/wiki?8769) | [NextPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55985) |
| [Paging in apps](https://wiki.genexus.com/commwiki/wiki?31280) | [PreviousPage method](https://wiki.genexus.com/commwiki/wiki?8770) | [PreviousPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55992) | [RecordCount property](https://wiki.genexus.com/commwiki/wiki?8757) |
| [Server Paging](https://wiki.genexus.com/commwiki/wiki?15589) |

---
