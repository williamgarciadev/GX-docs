---
title: "ItemCollapse Event"
source_id: 19552
source_url: https://wiki.genexus.com/commwiki/wiki?19552
genexus_version: "18"
---

# ItemCollapse Event

It allows programming actions when the user collapses a QueryElement with nested data, hiding its values.

### [Syntax](#Syntax)

**&ItemCollapseData.**{ *ExpandedValues* | *Name* | *Value* }

When the event is triggered, its parameters are queried in the "ItemCollapseData" property. It returns an SDT with the following data:

* **Name.** Name of the element that was collapsed.
* **ExpandedValues.** These are the values of the element indicated in Name that remain expanded.
* **Value.** The value contained in the collapsed cell.

### [Example](#Example)

In this example, when an investor's row is collapsed in the ClientId QueryElement, its amount must be taken into account in the total represented in the WebLinearGauge control. Therefore, when the Collapse action is performed, the client is searched for in the LoadDataClientsSDT –this SDT was loaded in the Start event–, the amount is subtracted from the total and sent to the WebLinearGauge control.

The &ItemCollapseData variable is based on the QueryViewerItemCollapseData SDT.

```
Event QueryClients.ItemCollapse
    If &ItemCollapseData.Name = 'ClientId'
       for &TheClient in &LoadDataClientsSDT
           &ClientId = Val(&ItemCollapseData.Value)
           if &TheClient.ClientId = &ClientId
              &Amount = &TheClient.ClientAmount
           endif
      endfor
      &GaugeSDT.Value = &UCLinear - &Amount
EndEvent
```

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Chart type:** | PivotTable |

### [See Also](#See+Also)

[ItemExpand Event](https://wiki.genexus.com/commwiki/wiki?19563,,)  
[Item Collapse Data property](https://wiki.genexus.com/commwiki/wiki?19548)


|  |
| --- |
| **Backlinks** |
| [Item Collapse Data property](https://wiki.genexus.com/commwiki/wiki?19548) | [Category:QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) |

---
