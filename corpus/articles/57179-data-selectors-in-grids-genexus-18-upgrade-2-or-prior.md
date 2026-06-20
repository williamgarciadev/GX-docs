---
title: "Data Selectors in Grids (GeneXus 18 Upgrade 2 or prior)"
source_id: 57179
source_url: https://wiki.genexus.com/commwiki/wiki?57179
genexus_version: "18"
---

# Data Selectors in Grids (GeneXus 18 Upgrade 2 or prior)

A [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) or [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058) can have a [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271) associated through its [Data Selector property](https://wiki.genexus.com/commwiki/wiki?5361).

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908):

```
Airline
{
  AirlineId*
  AirlineName
}
```

Now, look at the structure of the *DSExampleInGrid* [Data Selector object](https://wiki.genexus.com/commwiki/wiki?5271):

`[imagen omitida: wiki id 5367]`

Note below that the grid contained in the [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) has the previous Data Selector assigned in its [Data Selector property](https://wiki.genexus.com/commwiki/wiki?5361):

`[imagen omitida: wiki id 5368]`  
  
The behavior is just like having a [For Each with a USING clause](https://wiki.genexus.com/commwiki/wiki?5312). This means that the Data Selector doesn't have an associated navigation (it doesn't have a base table by itself). Therefore, at specification time, the Data Selector definition is combined with the Grid definition to determine the table that will be navigated, taking into account the attributes of both definitions:

* If the Grid and the Data Selector have Conditions, both are considered
* If the Grid and the Data Selector have Order clause(s), the resulting Order will be a combination of them. The Grid order has priority, so in the event that GeneXus discards a Data Selector Order, a warning spc0135 will be triggered at specification time

Thus, in the example shown, the grid will be loaded with all the Airline records that fulfill the grid conditions and the Data Selector conditions. The order with which the data will be retrieved will result from a combination of the specified orders in both definitions:

`[imagen omitida: wiki id 5716]`

### [**Notes**](#Notes)

* If parameters need to be provided to the DS, list them in the Parameters property and separate them with commas.
* Data Selector does not work in a Transaction's Grid.

### [See also](#See+also)

[Data Selectors in Aggregations](https://wiki.genexus.com/commwiki/wiki?5432)  
[Data Selectors in Data Providers](https://wiki.genexus.com/commwiki/wiki?6501)  
[Data Selectors in For Each command](https://wiki.genexus.com/commwiki/wiki?5312)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Data Selectors](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/data-selectors-v16?p=5414)
