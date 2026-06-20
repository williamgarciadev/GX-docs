---
title: "Dashboard object"
source_id: 52680
source_url: https://wiki.genexus.com/commwiki/wiki?52680
genexus_version: "18"
---

# Dashboard object

Defines a Business Dashboard with several key performance indicators.

A good data story brings data and facts to life. Use the Dashboard object to walk your audience through the data and insights you want to make sure they see and informs them.

Dashboards provide at-a-glance views of [KPI](https://wiki.genexus.com/commwiki/wiki?35542,,)s (key performance indicators) relevant to a particular objective or business process. Often, the "dashboard" is displayed on a web page that is linked to a database that allows the report to be regularly updated.

`[imagen omitida: wiki id 36772]`

In just a few clicks, you can combine data from [Query object](https://wiki.genexus.com/commwiki/wiki?9026)s or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)s, add filters, relate them, and drill down into more detail when needed.

`[imagen omitida: wiki id 36771]`

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

### [Availability](#Availability)

This property is available since [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,).

### [Samples](#Samples)

* [BitBitNews](https://wiki.genexus.com/commwiki/wiki?39308)
* [TestWebQueryViewer](https://wiki.genexus.com/commwiki/wiki?36747,,)

### [See also](#See+also)

* [Dashboard object Parameters](https://wiki.genexus.com/commwiki/wiki?42662)
* [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770)
* [Dashboard widgets](https://wiki.genexus.com/commwiki/wiki?36779)
* [Dashboard Object Usage Example](https://wiki.genexus.com/commwiki/wiki?36800)
