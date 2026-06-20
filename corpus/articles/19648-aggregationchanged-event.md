---
title: "AggregationChanged Event"
source_id: 19648
source_url: https://wiki.genexus.com/commwiki/wiki?19648
genexus_version: "18"
---

# AggregationChanged Event

### [**Deprecated** since: GeneXus Salto.](#Deprecated+since%3A+GeneXus+Salto.)

This event is triggered every time the aggregation function of a QueryElement is changed.

### [Syntax](#Syntax)

**&AggregationChangedData.**{ *Aggregation* | *Name* }

When the event is triggered, its parameters are queried in the "AggregationChangedData" property. It returns an SDT with the following data:

* **Name.** Name of the element in which aggregation has been changed.
* **Aggregation.** Is the selected aggregation. Possible operations are Sum, Average, Quantity, Minimum and Maximum.

### [QueryViewerFilterChangedData SDT Composition](#QueryViewerFilterChangedData+SDT+Composition)

`[imagen omitida: wiki id 19651]`

### [Example](#Example)

In this example, the names of the aggregation that has been changed and of the new one are displayed on screen.

```
Event QueryClients.AggregationChanged
    Msg("Changed aggregation of the field: " + &AggregationChangedData.Name + " to a new aggregation: " + &AggregationChangedData.Aggregation)
EndEvent
```

`[imagen omitida: wiki id 19652]`

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Output type:** | PivotTable |
