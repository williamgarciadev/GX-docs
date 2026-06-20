---
title: "QueryViewer control"
source_id: 9075
source_url: https://wiki.genexus.com/commwiki/wiki?9075
genexus_version: "18"
---

# QueryViewer control

QueryViewer is an [Extended Control](https://wiki.genexus.com/commwiki/wiki?5273) that must be included in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) to allow viewing the data obtained as a result of executing a [Query object](https://wiki.genexus.com/commwiki/wiki?9026) or a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270). The possible viewing options are:

1. **[Card](https://wiki.genexus.com/commwiki/wiki?31810):**is a static representation of the query value that can show its trend.
2. **Chart:** several kinds of charts can be selected, including [Timeline chart](https://wiki.genexus.com/commwiki/wiki?29936), [Circular Charts](https://wiki.genexus.com/commwiki/wiki?30369), [Polar Charts](https://wiki.genexus.com/commwiki/wiki?30374,,), and more.
3. **[Map](https://wiki.genexus.com/commwiki/wiki?48199):** is a map of the world, a continent, or a country for queries containing a geographic axis (available since GeneXus 17 upgrade 4).
4. **Pivot Table:** is a table that allows swapping columns and grouping information.
5. **Table:** is a static table, with fixed rows and columns.

**Important note**: Support for mobile applications has been available since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,).

### [Main features:](#Main+features%3A)

* Compatible with all browsers, including smartphones.
* Allows exporting data to PDF, HTML, XML, and XLSX formats (only valid for Table and Pivot Table options).
* Intuitive handling of Pivot Tables by using drag and drop.
* Programmatically configurable as well.

**Note:** Attributes can be hidden in the Table and Pivot Table just by right-clicking on the right corner of the attribute. In the Pivot Table case, remember that if all the Data attributes are hidden, the Quantity field will appear and it will not be possible to hide it.

### [How to work with this control?](#How+to+work+with+this+control%3F)

The following steps describe how to work with this control for a web application (for Native Mobile applications, it works in the same way).

1) Drag the QueryViewer control from the Toolbox to the Web Layout of a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916).

`[imagen omitida: wiki id 52573]`

2) Complete the [Object property](https://wiki.genexus.com/commwiki/wiki?19664) of the QueryViewer control with the [Query object](https://wiki.genexus.com/commwiki/wiki?9026) or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) that will generate the data to be displayed.

`[imagen omitida: wiki id 52575]`

3) Set the **Type** property below the **Output** group. This allows you to select one of the five ways in which the output can be displayed:

`[imagen omitida: wiki id 52577]`

When selecting the Chart option, you can choose a specific type of chart by setting the **Chart Type** property:

`[imagen omitida: wiki id 52579]`

4) This is enough to execute the object that contains the QueryViewer control to see the result at runtime.

In addition, you may set other QueryViewer properties. For example, the following properties related to a column chart:

* XAxis Title = Country Name
* YAxis Title = Population

As a result, the following query is displayed at runtime:

`[imagen omitida: wiki id 52578]`

**Note:** The first time that a QueryViewer control is dragged to a web form in a Knowledge Base, GeneXus will include the GeneXusReporting module containing the [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021) necessary for using the control, as well as a set of new [GeneXus Domains](https://wiki.genexus.com/commwiki/wiki?7221). Also, a set of variables is automatically created in the Object Variables section, and a sample source is added in the Object Events section. This code is intended to guide you in using and setting the control at runtime.

### [Scenarios](#Scenarios)

Below are some scenarios you can find when using the QueryViewer control:

* Dynamic filter to obtain new views of a query

New views of a single query are possible by changing the value shown of one participant in the query ([Query Element](https://wiki.genexus.com/commwiki/wiki?19788)). This is done by passing parameters between the QueryViewer control and the query.

* Customizing a QueryViewer control at runtime

Through the associated variable in the Axes property, it is possible to change programmatically some of the properties that have an impact on the control’s view.

* Changing queries at runtime

It is possible to change the query associated with the control by replacing it with a different one, by altering the control’s Object property, as in the following example:

```
Event Start
  Attractions.Object = AttractionsByCountry(<Parameter1>, <Parameter2>, ...)
EndEvent
```

In this example, *Attractions* is the QueryViewer control’s name, Object is the control’s property that stores the name of the [Query object](https://wiki.genexus.com/commwiki/wiki?9026) that performs the query, and *AttractionsByCountry* is the name of that Query object. The same applies if the associated object is a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270).

* Changing aggregation by code

If a [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) is associated with the Quer Viewer, aggregation can be changed by code using the QueryViewerElements.Element Aggregation field.

The default aggregation is Sum.

### [Control properties](#Control+properties)

Please refer to [QueryViewer control properties](https://wiki.genexus.com/commwiki/wiki?32920).

### [Control events](#Control+events)

|  |  |
| --- | --- |
| [DragAndDrop Event](https://wiki.genexus.com/commwiki/wiki?19546,,) | Allows programming actions when a drag and drop action is found. |
| [ItemExpand Event](https://wiki.genexus.com/commwiki/wiki?19563,,) | Allows programming actions when the user expands a Query Element that contains nested data. |
| [ItemCollapse Event](https://wiki.genexus.com/commwiki/wiki?19552) | Allows programming actions when the user collapses a Query Element with nested data. |
| [FilterChanged Event](https://wiki.genexus.com/commwiki/wiki?19646) | It is executed every time values are removed from or added to the list of possible values for an attribute, whether it’s located in the rows, columns, or pages area. |
| [ItemClick Event](https://wiki.genexus.com/commwiki/wiki?19570) | It is executed upon clicking on a query element. |
| [ItemDoubleClick Event](https://wiki.genexus.com/commwiki/wiki?19567) | It is executed upon double-clicking on a query element. (This event is not supported if you are running the control on a mobile device) |

### [Methods](#Methods)

|  |  |
| --- | --- |
| GetMetadata() | Returns a QueryViewerElements type object which contains the list of attributes (properties included). (More information about [Elements Property](https://wiki.genexus.com/commwiki/wiki?19577)) |
| GetData() | Returns an XML on a string variable containing all the data for the attributes loaded in the Pivot Table. |
| GetFilteredData() | Returns an XML on a string variable containing the data that is being viewed at the moment (the difference with the GetData() method is seen on the Pivot Table; data can be different because of filter application). |
| NotifyMetadata() | Makes a list of attributes (properties included). This method doesn't return an object as a result but generates a QueryViewerElements type variable that can be captured later by a TrackContext event. |
| NotifyData() | Loads all the data referenced by the attributes loaded in the Pivot Table. This method doesn't return an object as a result but generates a variable that can be captured later by a TrackContext event. |
| NotifyFilteredData() | Loads the data that is being viewed at the moment with filters applied (it can be different from the data loaded by the method NotifyData()). This method doesn't return an object as a result but generates a variable that can be captured later by a TrackContext event. |

### [Using methods](#Using+methods)

As an example of usage, see how to save/restore metadata to/from the Database. To do so, define the following events in the Web Panel where the QueryViewer is embedded:

Saving the metadata

```
Event 'NotifyMetadata'
  QueryViewer.NotifyMetadata() 
Endevent

Event TrackContext(&Metadata)
  SaveMetadata(&Metadata)
EndEvent
```

Restoring the metadata

```
Event Refresh 
   &Axes = RestoreMetadata() 
EndEvent
```

**Notes:**

* The *SaveMetadata* and *RestoreMetadata* [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)s have to be implemented.
* The *&Metadata* variable has to be defined based on the *QueryViewerElements* SDT.
* The [Remember Layout property](https://wiki.genexus.com/commwiki/wiki?19619) of the QueryViewer control has to be set to *False*.

### [See Also](#See+Also)

[QueryViewer control compatibility](https://wiki.genexus.com/commwiki/wiki?40015)


|  |
| --- |
| **Pages** |
| [Background opacity property](https://wiki.genexus.com/commwiki/wiki?41078) | [Color 1 property](https://wiki.genexus.com/commwiki/wiki?41061) | [Color 10 property](https://wiki.genexus.com/commwiki/wiki?41070) |
| [Color 2 property](https://wiki.genexus.com/commwiki/wiki?41062) | [Color 3 property](https://wiki.genexus.com/commwiki/wiki?41063) | [Color 4 property](https://wiki.genexus.com/commwiki/wiki?41064) |
| [Color 5 property](https://wiki.genexus.com/commwiki/wiki?41065) | [Color 6 property](https://wiki.genexus.com/commwiki/wiki?41066) | [Color 7 property](https://wiki.genexus.com/commwiki/wiki?41067) |
| [Color 8 property](https://wiki.genexus.com/commwiki/wiki?41068) | [Color 9 property](https://wiki.genexus.com/commwiki/wiki?41069) | [Continent property in QueryViewer](https://wiki.genexus.com/commwiki/wiki?48138) |
| [Country property in QueryViewer](https://wiki.genexus.com/commwiki/wiki?48137) | [Font family property](https://wiki.genexus.com/commwiki/wiki?41072) | [Font size property](https://wiki.genexus.com/commwiki/wiki?41073) |
| [Font style property](https://wiki.genexus.com/commwiki/wiki?41074) | [Font variant property](https://wiki.genexus.com/commwiki/wiki?41076) | [gx-qv-map-background-color property](https://wiki.genexus.com/commwiki/wiki?48277) |
| [gx-qv-map-background-opacity property](https://wiki.genexus.com/commwiki/wiki?48278) | [gx-qv-map-title-font property](https://wiki.genexus.com/commwiki/wiki?48279) | [gx-qv-map-title-font-family property](https://wiki.genexus.com/commwiki/wiki?48280) |
| [gx-qv-map-title-font-size property](https://wiki.genexus.com/commwiki/wiki?48281) | [gx-qv-map-title-font-style property](https://wiki.genexus.com/commwiki/wiki?48282) | [gx-qv-map-title-font-weight property](https://wiki.genexus.com/commwiki/wiki?48283) |
| [HowTo: Customize the QueryViewer control](https://wiki.genexus.com/commwiki/wiki?40026) | [Map Type property in QueryViewer](https://wiki.genexus.com/commwiki/wiki?48161) | [Opacity property](https://wiki.genexus.com/commwiki/wiki?41071) |
| [Query Viewer: Font weight property](https://wiki.genexus.com/commwiki/wiki?41075) | [QueryViewer control compatibility](https://wiki.genexus.com/commwiki/wiki?40015) | [Raise ItemClick event property](https://wiki.genexus.com/commwiki/wiki?42812) |
| [Region property in QueryViewer](https://wiki.genexus.com/commwiki/wiki?48162) | [Selecting between a Query Object or Data Provider when using the QueryViewer User Control](https://wiki.genexus.com/commwiki/wiki?36751) | [Show rows per page property](https://wiki.genexus.com/commwiki/wiki?41079) |
| [Text decoration property](https://wiki.genexus.com/commwiki/wiki?41077) | [Title background color property](https://wiki.genexus.com/commwiki/wiki?41080) | [Value class property](https://wiki.genexus.com/commwiki/wiki?41060) |

---
