---
title: "Object property in QueryViewer control"
source_id: 19664
source_url: https://wiki.genexus.com/commwiki/wiki?19664
genexus_version: "18"
---

# Object property in QueryViewer control

Contains the name of the Query object or Data Provider object displayed in the QueryViewer control.

### [Scope](#Scope)

**Controls:** [QueryViewer](https://wiki.genexus.com/commwiki/wiki?9075)

### [Description](#Description)

Write the name of the object that you want to relate –the existing matches will be suggested- or click on the three dots button to open the [Select Object dialog](https://wiki.genexus.com/commwiki/wiki?9889) window, which will show the list of all the Queries and Data Providers in the Knowledge Base.

**Output type:**  Table, PivotTable, Chart

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at run-time and at design-time.

### [Samples](#Samples)

Lets say *Attractions* is a QueryViewer control on a Form; to set the *AttractionsByCountry* [Query object](https://wiki.genexus.com/commwiki/wiki?9026) or [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270) use the following syntax:

```
Event Start 
  Attractions.Object = AttractionsByCountry(<Parameter1>, <Parameter2>, ...)
EndEvent
```

### [See Also](#See+Also)

[When to use Query and when to use Data Provider with the QueryViewer control](https://wiki.genexus.com/commwiki/wiki?19645)  
[Query object](https://wiki.genexus.com/commwiki/wiki?9026)  
[Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)  
[QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075)


|  |
| --- |
| **Backlinks** |
| [Parameters QueryViewer property](https://wiki.genexus.com/commwiki/wiki?19808) | [Category:QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) | [QueryViewer control properties](https://wiki.genexus.com/commwiki/wiki?32920) |
| [When to use Query and when to use Data Provider with the QueryViewer control](https://wiki.genexus.com/commwiki/wiki?19645) |

---
