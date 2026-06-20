---
title: "For each Line command"
source_id: 8605
source_url: https://wiki.genexus.com/commwiki/wiki?8605
genexus_version: "18"
---

# For each Line command

Forces the processing of every line loaded in a Grid.

### [Syntax](#Syntax)

**For each** **line [ in** *<GridName>* **]**  
*code*  
**Endfor**  
  
**Where:**  
  
*<GridName>*  
     Is the name of the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058) or [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) that you want to scan. If there is only one Grid you may avoid mentioning it (as indicated in the syntax), but in the case of multiple Grids, you must indicate the name of the Grid to be scanned.

*code*  
     Is the sequence of valid language commands you want to execute for each line.

### [Scope](#Scope)

**Objects:** [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

This command allows you to process all lines in a Grid (regardless of whether they have been modified or not).

In [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916):

* It only processes the records that have been loaded in the Grid. Take into consideration that if the Grid has Paging it will only process the current active page rows.
* This command is supported in nested Grids. The parent row must be instantiated. In other words, the button that triggers the event must be inside the parent's Grid or the event must be programmed as follows:

  ```
  For each Line in ExternalGrid
     For each Line in InternalGrid
     ...
     Endfor
  Endfor
  ```

In [Panels](https://wiki.genexus.com/commwiki/wiki?24829):

* If the Grid has base table, it only processes the records that have been loaded in the Grid. Take into consideration that if the Grid has Paging it will only process the current active page rows.
* If the Grid has no base table, the For each line command processes all the records (regardless of whether the grid has paging or other factors).

### [Samples](#Samples)

#### [**Sample #1**](#Sample+%231)

Consider a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) containing only one Grid that shows a few lines with tickets (fewer than 8). When the end user presses a button associated with the 'Used Tickets' event, all the Grid's lines are scaned and, for each line, a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) is called to update the corresponding ticket record.

```
Event 'Used Tickets'  
    For each line
        UpdateTicketAsUsed(TicketId)   //TicketId is a Primary Key attribute included in the Grid. It is sent to the Procedure as a parameter. 
    Endfor
EndEvent
```

#### **Sample #2**

Consider a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) with only one Grid. The Grid contains the &Op variable (as a column). When the end user presses the Enter key or the 'Confirm' button, the Enter event is triggered. So, all the Grid's lines are scanned and, for each line, the code written inside the 'For each line' command is executed:

```
Event Enter // The &Op variable is included in a Grid that is in a Web Panel Web Layout. 
    For each line
        If &Op = '*' 
            ...  //action you want to execute
            ...  //action you want to execute                   
        Endif
    Endfor
EndEvent
```


|  |
| --- |
| **Backlinks** |
| [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) | [Event execution on the client side since X Evolution 3](https://wiki.genexus.com/commwiki/wiki?22529) |
| [For Each Line command (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57248) | [Category:Grid control](https://wiki.genexus.com/commwiki/wiki?24817) |

---
