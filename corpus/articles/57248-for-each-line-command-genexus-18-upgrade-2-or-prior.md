---
title: "For Each Line command (GeneXus 18 Upgrade 2 or prior)"
source_id: 57248
source_url: https://wiki.genexus.com/commwiki/wiki?57248
genexus_version: "18"
---

# For Each Line command (GeneXus 18 Upgrade 2 or prior)

Forces the processing of every loaded line in a Grid.

### [Syntax](#Syntax)

**For each** **line [ in** *<GridName>* **]**  
*code*  
**Endfor**  
  
**Where:**  
  
*<GridName>*  
    Is the name of the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) or [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058) you want to scan. If there is only one Grid you can avoid mentioning it (as indicated in the syntax). On the other hand, if you have multiple Grids you must indicate the name of the Grid you want to scan.

*code*  
    Is the sequence of valid language commands.

### [Scope](#Scope)

**Objects:** [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

This command allows you to process all lines in a Grid.

This command has the following properties and restrictions:

* It only processes the records that have been loaded and are visible in the grid. Take into consideration that if the Grid has Paging, it will only process the current active page rows.
* It processes all lines whether they have been modified or not.

You can implement to mark certain lines that fulfill a specific condition, and, with this command, you can scan/browse all lines in the Grid and evaluate the marked lines.

**Notes:**

* If the For each line command is used In the Enter event, each line will be processed. However, it is the programmer's responsibility to update the grid values.
* This command is supported in nested Grids. The parent row must be instantiated. In other words, the button that triggers the event must be inside the parent's grid or the event must be programmed in this way:

```
For Each Line in ExternalGrid
   For Each Line in InternalGrid
   ...
   Endfor
Endfor
```

### [Samples](#Samples)

```
Event Enter // The &Op variable is included in a Grid that is in a Web Panel Web Layout. 
    For each line
        If &Op = '*' // If &Op has an *
            ...  //action you want to execute
            ...  //action you want to execute
```

```
        Endif 
    Endfor
EndEvent
```

###
