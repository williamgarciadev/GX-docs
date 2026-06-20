---
title: "RecordCount property"
source_id: 8757
source_url: https://wiki.genexus.com/commwiki/wiki?8757
genexus_version: "18"
---

# RecordCount property

Obtains or sets the number of records of a Grid or Freestyle Grid.

### [Scope](#Scope)

**Objects:** [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058), [Grid](https://wiki.genexus.com/commwiki/wiki?24817)

### [Description](#Description)

The RecordCount property returns the number of records of the Grid that meet the selection conditions. It may return -1 if the program could not determine it (it was not assigned and it could not be calculated automatically).  

|  |  |  |
| --- | --- | --- |
| **Value** | **Comment** | **Suggestion** |
| -1 | It could not be determined. Typically, the Grid does not have a base table or the loading conditions are evaluated client side. | Since the program could not calculate it automatically, you should set its value in the Refresh event. |
| >= 0 | Number of records of the Grid base table |  |

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at runtime.

### [Samples](#Samples)

1) Grid with base table (GridCount could be calculated automatically)

```
Event Refresh
msg(str(Grid1.RecordCount))
msg(str(grid1.PageCount))
EndEvent
```

2) Grid is based on SDT (GridCount could be calculated automatically)

```
Event Refresh
   &Clients = ClientsGet()
   msg(str(grid1.RecordCount))    
   msg(str(grid1.PageCount))
EndEvent
Event Load
    for &Client in &Clients
        &Clientid = &Client.ClientId
        &ClientName = &Client.ClientName
        load
    endfor
EndEvent
```

3) Grid is loaded from external sources (RecordCount could not be calculated automatically)  
This case requires that RecordCount is assigned in the Refresh Event. If not, the Pagecount could not be determined when the Web Panel loads.

```
Event Refresh
   grid1.Rows = 5
   grid1.RecordCount = 12
   msg(str(grid1.PageCount))
   msg(str(grid1.RecordCount))
Event Load
   for &i = 1 to 12
      &ClientId = GetClientId(&i)
      &ClientName = GetClientName(&i)
      load
   endfor
EndEvent
```

### [See Also](#See+Also)

[PageCount Property](https://wiki.genexus.com/commwiki/wiki?8755,,)  
[Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064)  
[Paging in apps](https://wiki.genexus.com/commwiki/wiki?31280)


|  |
| --- |
| **Backlinks** |
| [Automatic paging in Grid control](https://wiki.genexus.com/commwiki/wiki?6086) | [FirstPage method](https://wiki.genexus.com/commwiki/wiki?8768) | [FirstPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55984) |
| [LastPage method](https://wiki.genexus.com/commwiki/wiki?8771) | [LastPage method (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55989) |

---
