---
title: "Dashboard widgets"
source_id: 36779
source_url: https://wiki.genexus.com/commwiki/wiki?36779
genexus_version: "18"
---

# Dashboard widgets

A [Dashboard Layout](https://wiki.genexus.com/commwiki/wiki?40116) is composed of different kind of widgets available on the toolbar. The available options are:

* Filter
* Image
* Object
* TextBlock
* Table

`[imagen omitida: wiki id 40525]`

### [Filter](#Filter)

Its function is to filter the data in the dashboard remaining widgets. All the filters in the dashboard are global in a sense they broadcast its value to every widget in the dashboard. It's the definition of the widget that determines if a filter on the screen is accepted as a widget parameter or ignored. All filtering is done taking into account its name. So, if you have a filter name called "*CustomerId*"; when changing its value, all queries with a parameter matching "CustomerId" will be updated.

The most important properties are:

* [Control name](https://wiki.genexus.com/commwiki/wiki?40117): name assigned to the control.
* [Name](https://wiki.genexus.com/commwiki/wiki?40472): filter name to be used in query widgets.
* [Visible](https://wiki.genexus.com/commwiki/wiki?40493): Whether the filter is visible or not (boolean). It is useful if you want to leave a filter with a fixed value and it cannot be changed.
* [Caption](https://wiki.genexus.com/commwiki/wiki?40402): text to be displayed.
* [Data type](https://wiki.genexus.com/commwiki/wiki?40439): filter data type (enumerated: numeric without decimals, numeric with decimals, boolean, character, date or datetime).
* Control Group
  + [Type](https://wiki.genexus.com/commwiki/wiki?40424): control type (edit, radio button, combo box, drop-down list).
  + [Dynamic](https://wiki.genexus.com/commwiki/wiki?40137): if possible values are fixed or are calculated by an expression (boolean).
  + [Values](https://wiki.genexus.com/commwiki/wiki?40437): applies to non-dynamic filters and is a collection of fixed values, you need to set for each item a Name and Value.

The filters may be static or dynamic. When static, the list of possible values must be provided in the filter's definition. When dynamic, you must provide an attribute for the filter values ([Item values](https://wiki.genexus.com/commwiki/wiki?40410)), another one for the filter value descriptions ([Item descriptions](https://wiki.genexus.com/commwiki/wiki?40138)) and the set of [conditions](https://wiki.genexus.com/commwiki/wiki?40405) that may be necessary to navigate the database in search of the filter possible values. For example; if you have a *Brand* and *Model* filters, the condition for Model would be: *MakeDsc = &MakeDsc* (anywhere in the Dashboard filters are referenced with & + <FilterName>).

### [Image](#Image)

Inserts a standard [Image object](https://wiki.genexus.com/commwiki/wiki?23387) on the layout.

### [Object](#Object)

Displays a selector to choose a [Query object](https://wiki.genexus.com/commwiki/wiki?9026) or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270). The main properties are:

* [Object](https://wiki.genexus.com/commwiki/wiki?40488): referenced query object.
* [Type](https://wiki.genexus.com/commwiki/wiki?40467): Visual output type ([Card](https://wiki.genexus.com/commwiki/wiki?31810), Chart, PivotTable, or Table); depending on the type of output chosen, the associated properties are the same as in the [QueryViewer properties section](https://wiki.genexus.com/commwiki/wiki?32920).
* [On item click](https://wiki.genexus.com/commwiki/wiki?40126): Action to be executed when clicking an item (partially implemented!).

### [TextBlock](#TextBlock)

Inserts a reduced version of a [Text Block control](https://wiki.genexus.com/commwiki/wiki?5948). The main properties are:

* Frame: to define if the filter has a frame.
* Caption: text to be displayed.

The properties include the caption of the text and it may reference any filter in the dashboard, for example, "List of &CustomerName orders:"

### [Table](#Table)

Inserts a reduced version of a [Table control](https://wiki.genexus.com/commwiki/wiki?6001) to organize and position other widgets.

### [Standard Variables](#Standard+Variables)

The following standard variables are supported

* [Today](https://wiki.genexus.com/commwiki/wiki?8873)
* [Time](https://wiki.genexus.com/commwiki/wiki?8102)
* [Pgmdesc](https://wiki.genexus.com/commwiki/wiki?7672)
* Pgmname


|  |
| --- |
| **Backlinks** |
| [Aggregation property](https://wiki.genexus.com/commwiki/wiki?40145) | [Axis property](https://wiki.genexus.com/commwiki/wiki?40144) | [Background color property](https://wiki.genexus.com/commwiki/wiki?40149) |
| [Border color property](https://wiki.genexus.com/commwiki/wiki?40151) | [Border width property](https://wiki.genexus.com/commwiki/wiki?40150) | [Can drag to pages property](https://wiki.genexus.com/commwiki/wiki?40147) | [Chart type property](https://wiki.genexus.com/commwiki/wiki?40120) |
| [Conditional styles property in Dashboard](https://wiki.genexus.com/commwiki/wiki?40153) | [Container class property](https://wiki.genexus.com/commwiki/wiki?40127) | [Control name property](https://wiki.genexus.com/commwiki/wiki?40117) | [Custom order property](https://wiki.genexus.com/commwiki/wiki?40157) |
| [Dashboard Card Include max and min property](https://wiki.genexus.com/commwiki/wiki?40462) | [Dashboard Card Include sparkline property](https://wiki.genexus.com/commwiki/wiki?40463) | [Dashboard Card Include trend property](https://wiki.genexus.com/commwiki/wiki?40464) | [Dashboard Chart X axis intersection at zero property](https://wiki.genexus.com/commwiki/wiki?40514) |
| [Dashboard Element Font property](https://wiki.genexus.com/commwiki/wiki?40417) | [Dashboard Element Order property](https://wiki.genexus.com/commwiki/wiki?40458) | [Dashboard Gauge Maximum value property](https://wiki.genexus.com/commwiki/wiki?40485) | [Dashboard Layout property](https://wiki.genexus.com/commwiki/wiki?40116) |
| [Dashboard Main color property](https://wiki.genexus.com/commwiki/wiki?41116) | [Category:Dashboard object](https://wiki.genexus.com/commwiki/wiki?36769) | [Dashboard object Parameters](https://wiki.genexus.com/commwiki/wiki?42662) | [Dashboard Object property](https://wiki.genexus.com/commwiki/wiki?40488) |
| [Dashboard Object Usage Example](https://wiki.genexus.com/commwiki/wiki?36800) | [Dashboard Orientation property](https://wiki.genexus.com/commwiki/wiki?40465) | [Dashboard widget cell class property](https://wiki.genexus.com/commwiki/wiki?40403) | [Dashboard Widget Image property](https://wiki.genexus.com/commwiki/wiki?40461) |
| [Dashboard Widget Page size property](https://wiki.genexus.com/commwiki/wiki?40469) | [Dashboard Widget Paging property](https://wiki.genexus.com/commwiki/wiki?40489) | [Dashboard widget plot series property](https://wiki.genexus.com/commwiki/wiki?40498) | [Dashboard widget row class property](https://wiki.genexus.com/commwiki/wiki?40499) |
| [Dashboard Widget Show data labels in property](https://wiki.genexus.com/commwiki/wiki?40503) | [Dashboard Widget Show values property](https://wiki.genexus.com/commwiki/wiki?40506) | [Dashboard Widget Target value property](https://wiki.genexus.com/commwiki/wiki?40500) | [DashboardViewer Control Events](https://wiki.genexus.com/commwiki/wiki?43263) |
| [Day of week title property](https://wiki.genexus.com/commwiki/wiki?40162) | [Expand/collapse property](https://wiki.genexus.com/commwiki/wiki?40155) | [Expanded values property](https://wiki.genexus.com/commwiki/wiki?40156) | [Filter (Date) value property](https://wiki.genexus.com/commwiki/wiki?40510) |
| [Filter caption class property](https://wiki.genexus.com/commwiki/wiki?40141) | [Filter caption property](https://wiki.genexus.com/commwiki/wiki?40402) | [Filter conditions property](https://wiki.genexus.com/commwiki/wiki?40405) | [Filter control type property](https://wiki.genexus.com/commwiki/wiki?40424) |
| [Filter control values property](https://wiki.genexus.com/commwiki/wiki?40437) | [Filter data type property](https://wiki.genexus.com/commwiki/wiki?40439) | [Filter dynamic property](https://wiki.genexus.com/commwiki/wiki?40137) | [Filter empty item property](https://wiki.genexus.com/commwiki/wiki?40139) |
| [Filter empty item text property](https://wiki.genexus.com/commwiki/wiki?40140) | [Filter invite message property](https://wiki.genexus.com/commwiki/wiki?40409) | [Filter item descriptions property](https://wiki.genexus.com/commwiki/wiki?40138) | [Filter item values property](https://wiki.genexus.com/commwiki/wiki?40410) |
| [Filter lower (Date) value property](https://wiki.genexus.com/commwiki/wiki?40466) | [Filter lower value property](https://wiki.genexus.com/commwiki/wiki?40134) | [Filter maximum (Date) value property](https://wiki.genexus.com/commwiki/wiki?40487) | [Filter maximum value property](https://wiki.genexus.com/commwiki/wiki?40486) |
| [Filter minimum (Date) value property](https://wiki.genexus.com/commwiki/wiki?40470) | [Filter minimum value property](https://wiki.genexus.com/commwiki/wiki?40136) | [Filter picture property](https://wiki.genexus.com/commwiki/wiki?40491) | [Filter sort descriptions property](https://wiki.genexus.com/commwiki/wiki?40423) |
| [Filter type property](https://wiki.genexus.com/commwiki/wiki?40131) | [Filter upper (Date) value property](https://wiki.genexus.com/commwiki/wiki?40511) | [Filter upper value property](https://wiki.genexus.com/commwiki/wiki?40135) | [Filter value class property](https://wiki.genexus.com/commwiki/wiki?40142) |
| [Filter value property](https://wiki.genexus.com/commwiki/wiki?40495) | [Filter values property](https://wiki.genexus.com/commwiki/wiki?40515) | [Filter visible property](https://wiki.genexus.com/commwiki/wiki?40493) | [Filters position property](https://wiki.genexus.com/commwiki/wiki?40115) |
| [Foreground color property](https://wiki.genexus.com/commwiki/wiki?40148) | [Frame Allow Collapsing property](https://wiki.genexus.com/commwiki/wiki?40119) | [Frame body class property](https://wiki.genexus.com/commwiki/wiki?40130) | [Frame class property](https://wiki.genexus.com/commwiki/wiki?40128) |
| [Frame collapsed property](https://wiki.genexus.com/commwiki/wiki?40419) | [Frame title class property](https://wiki.genexus.com/commwiki/wiki?40129) | [Frame title property](https://wiki.genexus.com/commwiki/wiki?40422) | [Frame visible property](https://wiki.genexus.com/commwiki/wiki?40426) |
| [Group by day of week property](https://wiki.genexus.com/commwiki/wiki?40428) | [Group by month property](https://wiki.genexus.com/commwiki/wiki?40429) | [Group by quarter property](https://wiki.genexus.com/commwiki/wiki?40432) | [Group by semester property](https://wiki.genexus.com/commwiki/wiki?40433) |
| [Group by year property](https://wiki.genexus.com/commwiki/wiki?40434) | [Hide value property](https://wiki.genexus.com/commwiki/wiki?40163) | [Month title property](https://wiki.genexus.com/commwiki/wiki?40161) | [Name (lower value) property](https://wiki.genexus.com/commwiki/wiki?40132) |
| [Name (upper value) property](https://wiki.genexus.com/commwiki/wiki?40133) | [Objects class property](https://wiki.genexus.com/commwiki/wiki?41094) | [On item click property](https://wiki.genexus.com/commwiki/wiki?40126) | [PivotTable Main color](https://wiki.genexus.com/commwiki/wiki?41081) |
| [Quarter title property](https://wiki.genexus.com/commwiki/wiki?40160) | [QueryElement Border style property](https://wiki.genexus.com/commwiki/wiki?40400) | [Refresh period property](https://wiki.genexus.com/commwiki/wiki?40114) | [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |
| [Semester title property](https://wiki.genexus.com/commwiki/wiki?40159) | [Show data as property](https://wiki.genexus.com/commwiki/wiki?40124) | [Showed values property](https://wiki.genexus.com/commwiki/wiki?40154) | [Subtotals property](https://wiki.genexus.com/commwiki/wiki?40146) |
| [Table Main color property](https://wiki.genexus.com/commwiki/wiki?41115) | [Table responsive sizes property](https://wiki.genexus.com/commwiki/wiki?40492) | [Title property in Dashboard Layout](https://wiki.genexus.com/commwiki/wiki?40508) | [Trend period property](https://wiki.genexus.com/commwiki/wiki?40125) |
| [Type property in Dashboard widget element](https://wiki.genexus.com/commwiki/wiki?47143) | [Values styles property](https://wiki.genexus.com/commwiki/wiki?40152) | [Visible property in Dashboard widget element](https://wiki.genexus.com/commwiki/wiki?47161) | [Widget class property](https://wiki.genexus.com/commwiki/wiki?40118) |
| [Widget output type property](https://wiki.genexus.com/commwiki/wiki?40467) | [X axis labels property](https://wiki.genexus.com/commwiki/wiki?40121) | [X axis title property](https://wiki.genexus.com/commwiki/wiki?40122) | [Y axis title property](https://wiki.genexus.com/commwiki/wiki?40123) |
| [Year title property](https://wiki.genexus.com/commwiki/wiki?40158) |

---
