---
title: "DashboardViewer Control Events"
source_id: 43263
source_url: https://wiki.genexus.com/commwiki/wiki?43263
genexus_version: "18"
---

# DashboardViewer Control Events

The following events can be used in a [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770):

### [FiltersChanged](#FiltersChanged)

This event is triggered every time the value of a filter is changed.  
The Filters can be as follows:

* On-screen control of filter type (see [Dashboard widgets](https://wiki.genexus.com/commwiki/wiki?36779)).
* Filters originating from a [Query object](https://wiki.genexus.com/commwiki/wiki?9026) with the [On item click property](https://wiki.genexus.com/commwiki/wiki?40126): ApplyFilters.

The event data can be queried in the variable &FiltersChangedData that is created and associated with the [FiltersChangedData property](https://wiki.genexus.com/commwiki/wiki?42905) in the "Event parameters" category when inserting a [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770) in a Web Panel.

In some cases, a user's action changes more than one filter at the same time:

* Filters with [Filter type property](https://wiki.genexus.com/commwiki/wiki?40131): Range and [Filter control type property](https://wiki.genexus.com/commwiki/wiki?40424): Slider, where you can change the lower and upper values at the same time (so, the event reports that two filters were changed).
* [Query object](https://wiki.genexus.com/commwiki/wiki?9026) with several dimensions and the [On item click property](https://wiki.genexus.com/commwiki/wiki?40126): ApplyFilters, where clicking on an item causes several filters to change at the same time (one for each dimension).

In queries with [On item click property](https://wiki.genexus.com/commwiki/wiki?40126): ApplyFilters, where the clicked item is used as a dashboard filter, a second click on the item disables the filter.   
For this case, the reported filter that changed in the FiltersChanged event has a property called Enabled to indicate if it is active or not (this doesn't apply to filter-type controls that are always enabled).

### [ItemClick](#ItemClick)

It is triggered every time a value is clicked on a [Query object](https://wiki.genexus.com/commwiki/wiki?9026) (graph, table, pivot or card).  
When a [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770) is inserted in a Web Panel, the variable &ItemClickData is automatically created and associated with the [ItemClickData property](https://wiki.genexus.com/commwiki/wiki?42946) of this control. The item information is loaded in this variable when the event is executed.  
The loaded data includes:

* The name of the Query you clicked on.
* The [Query Element](https://wiki.genexus.com/commwiki/wiki?19788) and its value.
* Also, information is provided about the values of the other [Query Element](https://wiki.genexus.com/commwiki/wiki?19788)s associated with the clicked value (through the Context property).

### [ValuesHighlighted](#ValuesHighlighted)

It is triggered in the [Query object](https://wiki.genexus.com/commwiki/wiki?9026) with [On item click property](https://wiki.genexus.com/commwiki/wiki?40126): HighlightValues every time a value is marked or unmarked.  
When a [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770) is inserted in a Web Panel, the variable &ValuesHighlightedData is automatically created and associated with the [ValuesHighlightedData property](https://wiki.genexus.com/commwiki/wiki?42906)  of this control. The information is loaded in this variable when the event is executed.  
The information returned is a Name-Value collection for each of the dimensions of the clicked query.

## [Notes](#Notes)

The variables &ItemClickData, &FiltersChangedData, and &ValuesHighlightedData also contain information about the value of the other Dashboard filters at the time the event is executed, which can be queried from the AllFilters collection.

If the Web Panel was created using [GeneXus 16 upgrade 3](https://wiki.genexus.com/commwiki/wiki?42129,,) or lower, and already had the [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770), the properties [ItemClickData](https://wiki.genexus.com/commwiki/wiki?42946), [FiltersChangedData](https://wiki.genexus.com/commwiki/wiki?42905) and [ValuesHighlightedData](https://wiki.genexus.com/commwiki/wiki?42906) will be empty.  
Therefore, when the event is triggered, it will not be able to query its parameters.  
In this case, you have to manually create the variables (&ItemClickData, &FiltersChangedData and &ValuesHighlightedData) and associate them with the corresponding property.  
The reason is that these variables are created and associated with the corresponding properties in the [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770) when it is inserted in a Web Panel.

### [Sample](#Sample)

[TestWebQueryViewer](https://wiki.genexus.com/commwiki/wiki?36747,,)

### [See also](#See+also)

[Dashboard object](https://wiki.genexus.com/commwiki/wiki?36769)  
[DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770)  
[Query object](https://wiki.genexus.com/commwiki/wiki?9026)


|  |
| --- |
| **Backlinks** |
| [Category:DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770) | [DashboardViewer control Methods](https://wiki.genexus.com/commwiki/wiki?43316) |

---
