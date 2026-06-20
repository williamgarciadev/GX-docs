---
title: "Auto Resize property in QueryViewer control"
source_id: 19597
source_url: https://wiki.genexus.com/commwiki/wiki?19597
genexus_version: "18"
---

# Auto Resize property in QueryViewer control

Sets whether the size of the PivotTable, Table, Chart, or Card is automatically adjusted or not.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Controls:** [QueryViewer](https://wiki.genexus.com/commwiki/wiki?9075)

### [Description](#Description)

This property is valid only when the [Type property](https://wiki.genexus.com/commwiki/wiki?19612) of the QueryViewer control is set to PivotTable, Table, Chart, or Card.

Its default value is False. However, it may be necessary to automatically adjust the size of the PivotTable, Table, Chart, or Card to show all the data without scrollbars and without wasting empty space because you need that space for other controls or objects.

**Values**

|  |  |
| --- | --- |
| **False** | The control will take the space determined by the [Width](https://wiki.genexus.com/commwiki/wiki?38374) and [Height](https://wiki.genexus.com/commwiki/wiki?8792) properties. This is the default value. |
| **True** | The control will adjust the container to the minimum size required to show all the data. If the container is larger than that, the container's size is reduced to fit in. If the container is smaller than the space required, it is enlarged so that the content fits. |


|  |
| --- |
| **Backlinks** |
| [QueryViewer control properties](https://wiki.genexus.com/commwiki/wiki?32920) |

---
