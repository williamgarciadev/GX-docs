---
title: "Dashboard object"
source_id: 36769
source_url: https://wiki.genexus.com/commwiki/wiki?36769
genexus_version: "18"
---

# Dashboard object

Defines a Business Dashboard with several key performance indicators.

A good data story brings data and facts to life. Use the Dashboard object to walk your audience through the data and insights you want to make sure they see and informs them.

Dashboards provide at-a-glance views of [KPI](https://wiki.genexus.com/commwiki/wiki?35542,,)s (key performance indicators) relevant to a particular objective or business process. Often, the "dashboard" is displayed on a web page that is linked to a database that allows the report to be regularly updated.

`[imagen omitida: wiki id 52943]`

In just a few clicks, you can combine data from [Query object](https://wiki.genexus.com/commwiki/wiki?9026)s or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)s, add filters, relate them, and drill down into more detail when needed.

`[imagen omitida: wiki id 52935]`

Some of the benefits of using digital dashboards include:

* Visual presentation of performance measures.
* Ability to identify and correct negative trends.
* Quick identification of data outliers and correlations.
* Ability to make more informed decisions based on collected business intelligence.
* Saves time compared to running multiple reports.

## [Technology used](#Technology+used)

The new Dashboard object is based on the [Query object](https://wiki.genexus.com/commwiki/wiki?9026) and the [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075). It allows to integrate into a single screen several queries and filters, takes care of the interactions between those elements.

For a Dashboard object to be displayed at runtime, it must be executed using a [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770).

A Dashboard object is composed of a [layout](https://wiki.genexus.com/commwiki/wiki?40116) and [parameters](https://wiki.genexus.com/commwiki/wiki?42662) where you will add different kinds of [widgets](https://wiki.genexus.com/commwiki/wiki?36779) to it.

## [Definition](#Definition)

Each dashboard has a group of general properties, like the [title](https://wiki.genexus.com/commwiki/wiki?40508), [filters position](https://wiki.genexus.com/commwiki/wiki?40115) or the [refresh period](https://wiki.genexus.com/commwiki/wiki?40114). It also has an editor where you can place all the components of the dashboard (every component in a dashboard is called a [widget](https://wiki.genexus.com/commwiki/wiki?36779)). There are several types of widgets, but the two more relevant are queries and filters.

### [Properties](#Properties)

* **[Title](https://wiki.genexus.com/commwiki/wiki?40508):**  Set the object title.
* **[Refresh Period](https://wiki.genexus.com/commwiki/wiki?40114):** Number of seconds to refresh the dashboard automatically (use 0 to disable it).
* **[Filters Position](https://wiki.genexus.com/commwiki/wiki?40115):**  All the filters are grouped together and can be shown on the right side of the dashboard or the top side.
* **[Layout](https://wiki.genexus.com/commwiki/wiki?40116):** Layout used to arrange the widgets.

The dashboard editor is a live editor. If you have a connection to the database, while editing it, you may see the results of the process as you manipulate the dashboard.

### [Samples](#Samples)

* [BitBitNews](https://wiki.genexus.com/commwiki/wiki?39308)
* [TestWebQueryViewer](https://wiki.genexus.com/commwiki/wiki?36747,,)

### [See Also](#See+Also)

[Dashboard object Parameters](https://wiki.genexus.com/commwiki/wiki?42662)  
[DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770)  
[Dashboard widgets](https://wiki.genexus.com/commwiki/wiki?36779)  
[Dashboard Object Usage Example](https://wiki.genexus.com/commwiki/wiki?36800)


|  |
| --- |
| **Pages** |
| [Aggregation property](https://wiki.genexus.com/commwiki/wiki?40145) | [Alternate text property](https://wiki.genexus.com/commwiki/wiki?40143) | [Average type property](https://wiki.genexus.com/commwiki/wiki?50386) |
| [Axis property](https://wiki.genexus.com/commwiki/wiki?40144) | [Background color property](https://wiki.genexus.com/commwiki/wiki?40149) | [Border color property](https://wiki.genexus.com/commwiki/wiki?40151) |
| [Can drag to pages property](https://wiki.genexus.com/commwiki/wiki?40147) | [Chart type property](https://wiki.genexus.com/commwiki/wiki?40120) | [Conditional styles property in Dashboard](https://wiki.genexus.com/commwiki/wiki?40153) |
| [Container class property](https://wiki.genexus.com/commwiki/wiki?40127) | [Continent property in Dashboard](https://wiki.genexus.com/commwiki/wiki?48167) | [Control name property](https://wiki.genexus.com/commwiki/wiki?40117) |
| [Country property in Dashboard](https://wiki.genexus.com/commwiki/wiki?48169) | [Custom order property](https://wiki.genexus.com/commwiki/wiki?40157) | [Dashboard Card Include max and min property](https://wiki.genexus.com/commwiki/wiki?40462) |
| [Dashboard Card Include sparkline property](https://wiki.genexus.com/commwiki/wiki?40463) | [Dashboard Card Include trend property](https://wiki.genexus.com/commwiki/wiki?40464) | [Dashboard Chart X axis intersection at zero property](https://wiki.genexus.com/commwiki/wiki?40514) |
| [Dashboard Element Font property](https://wiki.genexus.com/commwiki/wiki?40417) | [Dashboard Element Order property](https://wiki.genexus.com/commwiki/wiki?40458) | [Dashboard Gauge Maximum value property](https://wiki.genexus.com/commwiki/wiki?40485) |
| [Dashboard Layout property](https://wiki.genexus.com/commwiki/wiki?40116) | [Dashboard object Parameters](https://wiki.genexus.com/commwiki/wiki?42662) | [Dashboard Object property](https://wiki.genexus.com/commwiki/wiki?40488) |
| [Dashboard Object Usage Example](https://wiki.genexus.com/commwiki/wiki?36800) | [Dashboard Orientation property](https://wiki.genexus.com/commwiki/wiki?40465) | [Dashboard widget cell class property](https://wiki.genexus.com/commwiki/wiki?40403) |
| [Dashboard Widget Image property](https://wiki.genexus.com/commwiki/wiki?40461) | [Dashboard Widget Page size property](https://wiki.genexus.com/commwiki/wiki?40469) | [Dashboard Widget Paging property](https://wiki.genexus.com/commwiki/wiki?40489) |
| [Dashboard widget plot series property](https://wiki.genexus.com/commwiki/wiki?40498) | [Dashboard widget row class property](https://wiki.genexus.com/commwiki/wiki?40499) | [Dashboard Widget Show data labels in property](https://wiki.genexus.com/commwiki/wiki?40503) |
| [Dashboard Widget Show values property](https://wiki.genexus.com/commwiki/wiki?40506) | [Dashboard Widget Target value property](https://wiki.genexus.com/commwiki/wiki?40500) | [Dashboard widgets](https://wiki.genexus.com/commwiki/wiki?36779) |
| [Day of week title property](https://wiki.genexus.com/commwiki/wiki?40162) | [Difference from property](https://wiki.genexus.com/commwiki/wiki?50340) | [Expand/collapse property](https://wiki.genexus.com/commwiki/wiki?40155) |
| [Expanded values property](https://wiki.genexus.com/commwiki/wiki?40156) | [Filter (Date) value property](https://wiki.genexus.com/commwiki/wiki?40510) | [Filter caption class property](https://wiki.genexus.com/commwiki/wiki?40141) |
| [Filter caption property](https://wiki.genexus.com/commwiki/wiki?40402) | [Filter control orientation property](https://wiki.genexus.com/commwiki/wiki?40411) | [Filter control type property](https://wiki.genexus.com/commwiki/wiki?40424) |
| [Filter control values property](https://wiki.genexus.com/commwiki/wiki?40437) | [Filter data type property](https://wiki.genexus.com/commwiki/wiki?40439) | [Filter dynamic property](https://wiki.genexus.com/commwiki/wiki?40137) |
| [Filter empty item property](https://wiki.genexus.com/commwiki/wiki?40139) | [Filter empty item text property](https://wiki.genexus.com/commwiki/wiki?40140) | [Filter invite message property](https://wiki.genexus.com/commwiki/wiki?40409) |
| [Filter item descriptions property](https://wiki.genexus.com/commwiki/wiki?40138) | [Filter item values property](https://wiki.genexus.com/commwiki/wiki?40410) | [Filter lower (Date) value property](https://wiki.genexus.com/commwiki/wiki?40466) |
| [Filter lower value property](https://wiki.genexus.com/commwiki/wiki?40134) | [Filter maximum (Date) value property](https://wiki.genexus.com/commwiki/wiki?40487) | [Filter maximum value property](https://wiki.genexus.com/commwiki/wiki?40486) |
| [Filter minimum (Date) value property](https://wiki.genexus.com/commwiki/wiki?40470) | [Filter minimum value property](https://wiki.genexus.com/commwiki/wiki?40136) | [Filter name property](https://wiki.genexus.com/commwiki/wiki?40472) |
| [Filter picture property](https://wiki.genexus.com/commwiki/wiki?40491) | [Filter sort descriptions property](https://wiki.genexus.com/commwiki/wiki?40423) | [Filter type property](https://wiki.genexus.com/commwiki/wiki?40131) |
| [Filter upper (Date) value property](https://wiki.genexus.com/commwiki/wiki?40511) | [Filter upper value property](https://wiki.genexus.com/commwiki/wiki?40135) | [Filter value class property](https://wiki.genexus.com/commwiki/wiki?40142) |
| [Filter value property](https://wiki.genexus.com/commwiki/wiki?40495) | [Filter values property](https://wiki.genexus.com/commwiki/wiki?40515) | [Filter visible property](https://wiki.genexus.com/commwiki/wiki?40493) |
| [Filters position property](https://wiki.genexus.com/commwiki/wiki?40115) | [Foreground color property](https://wiki.genexus.com/commwiki/wiki?40148) | [Frame body class property](https://wiki.genexus.com/commwiki/wiki?40130) |
| [Frame class property](https://wiki.genexus.com/commwiki/wiki?40128) | [Frame collapsed property](https://wiki.genexus.com/commwiki/wiki?40419) | [Frame title class property](https://wiki.genexus.com/commwiki/wiki?40129) |
| [Frame title property](https://wiki.genexus.com/commwiki/wiki?40422) | [Frame visible property](https://wiki.genexus.com/commwiki/wiki?40426) | [Group by day of week property](https://wiki.genexus.com/commwiki/wiki?40428) |
| [Group by month property](https://wiki.genexus.com/commwiki/wiki?40429) | [Group by quarter property](https://wiki.genexus.com/commwiki/wiki?40432) | [Group by semester property](https://wiki.genexus.com/commwiki/wiki?40433) |
| [Group by year property](https://wiki.genexus.com/commwiki/wiki?40434) | [Hide value property](https://wiki.genexus.com/commwiki/wiki?40163) | [Map type property in Dashboard](https://wiki.genexus.com/commwiki/wiki?48164) |
| [Month title property](https://wiki.genexus.com/commwiki/wiki?40161) | [Name (lower value) property](https://wiki.genexus.com/commwiki/wiki?40132) | [Name (upper value) property](https://wiki.genexus.com/commwiki/wiki?40133) |
| [Number of terms property](https://wiki.genexus.com/commwiki/wiki?50339) | [Number of terms property (for Dashboard widget)](https://wiki.genexus.com/commwiki/wiki?50390,Number+of+terms+property+%28for+Dashboard+widget%29,) | [Objects class property](https://wiki.genexus.com/commwiki/wiki?41094) |
| [On item click property](https://wiki.genexus.com/commwiki/wiki?40126) | [Quarter title property](https://wiki.genexus.com/commwiki/wiki?40160) | [Raise ItemClick event property](https://wiki.genexus.com/commwiki/wiki?42812) |
| [Refresh period property](https://wiki.genexus.com/commwiki/wiki?40114) | [Region property in Dashboard](https://wiki.genexus.com/commwiki/wiki?48165) | [Semester title property](https://wiki.genexus.com/commwiki/wiki?40159) |
| [Show as percentage property](https://wiki.genexus.com/commwiki/wiki?50341) | [Show data as property](https://wiki.genexus.com/commwiki/wiki?40124) | [Show values as property](https://wiki.genexus.com/commwiki/wiki?50338) |
| [Show values as property (for Dashboard widget)](https://wiki.genexus.com/commwiki/wiki?50391,Show+values+as+property+%28for+Dashboard+widget%29,) | [Showed values property](https://wiki.genexus.com/commwiki/wiki?40154) | [Subtotals property](https://wiki.genexus.com/commwiki/wiki?40146) |
| [Table responsive sizes property](https://wiki.genexus.com/commwiki/wiki?40492) | [Title property in Dashboard Layout](https://wiki.genexus.com/commwiki/wiki?40508) | [Trend period property](https://wiki.genexus.com/commwiki/wiki?40125) |
| [Type property in Dashboard widget element](https://wiki.genexus.com/commwiki/wiki?47143) | [Values styles property](https://wiki.genexus.com/commwiki/wiki?40152) | [Visible property in Dashboard widget element](https://wiki.genexus.com/commwiki/wiki?47161) |
| [Widget class property](https://wiki.genexus.com/commwiki/wiki?40118) | [Widget output type property](https://wiki.genexus.com/commwiki/wiki?40467) | [X axis labels property](https://wiki.genexus.com/commwiki/wiki?40121) |
| [X axis title property](https://wiki.genexus.com/commwiki/wiki?40122) | [Y axis title property](https://wiki.genexus.com/commwiki/wiki?40123) | [Year title property](https://wiki.genexus.com/commwiki/wiki?40158) |

---
