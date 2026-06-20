---
title: "Dashboard Object Usage Example"
source_id: 36800
source_url: https://wiki.genexus.com/commwiki/wiki?36800
genexus_version: "18"
---

# Dashboard Object Usage Example

This document provides a walkthrough of the needed steps to design and run a [Dashboard object](https://wiki.genexus.com/commwiki/wiki?36769).

### [Description](#Description)

The example is based on the [TestWebQueryViewer](https://wiki.genexus.com/commwiki/wiki?36747,,) Knowledge Base, which includes concepts such as Countries, Cities, Cars, Brands, Sales, and Purchases.

You can solve several scenarios with a [Dashboard object](https://wiki.genexus.com/commwiki/wiki?36769), just let's focus on providing a General [KPI](https://wiki.genexus.com/commwiki/wiki?35542,,) panel for the management team. Before getting started you will need to go through these points:

* Carefully design your [query](https://wiki.genexus.com/commwiki/wiki?9026) or [data provider](https://wiki.genexus.com/commwiki/wiki?5270) objects to be included in the dashboard.
* Review its filters and use the same name for those filters associated to the same concept (the meaning is the same). This will ease the creation of [filters](https://wiki.genexus.com/commwiki/wiki?36779) in the dashboard object and how data will be updated.

If you want to skip this walkthrough and directly run the sample, download the KB and run the *Home* object where you can select the *SalesDashboard* sample.

### [1) Object creation](#1%29+Object+creation)

Create a new [Dashboard object](https://wiki.genexus.com/commwiki/wiki?36769) (Reporting Category) with the name *GeneralKPIs*.

### [2) Object definition](#2%29+Object+definition)

Review the dashboard properties and set the following:

`[imagen omitida: wiki id 52903]`

* [Title](https://wiki.genexus.com/commwiki/wiki?40508): set the desired title name, for the case use *GeneralKPIs*.
* [Filters position](https://wiki.genexus.com/commwiki/wiki?40115): keep the default "right" value.
* [Layout](https://wiki.genexus.com/commwiki/wiki?40116): set the "Header + two columns + footer" option.

### [3) Design](#3%29+Design)

There is only one way to design your dashboard; you need to drag the elements from the toolbox you want to incorporate as part of the dashboard onto the form. Notice that the toolbox details the possible [Dashboard widgets](https://wiki.genexus.com/commwiki/wiki?36779) you may use.

When selecting the [objects widget](https://wiki.genexus.com/commwiki/wiki?36779), the following step is to associate it to an existing [Query object](https://wiki.genexus.com/commwiki/wiki?9026) or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270). For the case we will be using the following existing queries:

* Total Sales
* SalesByCity
* SalesByTime

Notice that once you connect the object, it is automatically executed there and when needed filters are automatically created.

Drag two [query widgets](https://wiki.genexus.com/commwiki/wiki?36779) to the"header section" and connect them with the *Total Sales* query and set the following properties

#### [ControlName: Object1](#ControlName%3A+Object1)

* [Type](https://wiki.genexus.com/commwiki/wiki?40467): Card
* [Include Sparkline](https://wiki.genexus.com/commwiki/wiki?33131): True
* [Include trend](https://wiki.genexus.com/commwiki/wiki?40464): True

#### [ControlName: Object2](#ControlName%3A+Object2)

* [Type](https://wiki.genexus.com/commwiki/wiki?40467): Card
* [Include max and min](https://wiki.genexus.com/commwiki/wiki?40462): True

The expected result is:

`[imagen omitida: wiki id 52897]`

Now, add two new [query widgets](https://wiki.genexus.com/commwiki/wiki?36779) in the "central left section" and connect them to the *SalesByCity* query and set the following properties:

#### [ControlName: Object3](#ControlName%3A+Object3)

* [Type](https://wiki.genexus.com/commwiki/wiki?40467): Chart

#### [ControlName: Object4](#ControlName%3A+Object4)

* [Type](https://wiki.genexus.com/commwiki/wiki?40467): Pivot table

This is the expected result.

`[imagen omitida: wiki id 52898]`

Now, add the last [query widget](https://wiki.genexus.com/commwiki/wiki?36779) in the footer section and connect it to the *SalesByTime* query and set the following properties:

#### [ControlName: Object5](#ControlName%3A+Object5)

* [Type](https://wiki.genexus.com/commwiki/wiki?40467): Chart
* [Chart type](https://wiki.genexus.com/commwiki/wiki?40120): Smooth timeline
* [On item click](https://wiki.genexus.com/commwiki/wiki?40126): Highlight values

Right click on the dashboard and use the Collapse | Expand widgets to get a compacted view of you design

`[imagen omitida: wiki id 52899]`

Notice that when clicking on a [widget](https://wiki.genexus.com/commwiki/wiki?36779) you will get a hint its relationship with others; the selected object is marked in blue and the associations will be marked in green:

* select a query, the associated filters are marked in green.
* select a filter, the queries where the filter is used is marked in green.

### [4) Look & Feel](#4%29+Look+%26+Feel)

For this example we will not change the default look and feel, you need to use classes from the associated [Theme for Web](https://wiki.genexus.com/commwiki/wiki?6420).

### [5) Filters](#5%29+Filters)

To enhance the interaction in the object; it is important to add filters and connect them to the different queries; so every time you change a filter the associated queries will be updated.

By default, filters are automatically created when connecting a query with parameters. For this case, the following filter was already created because the *SalesByCity* query includes the following condition:

```
CountryName in &CountryName
```

The output will detail the operation

```
========== SQL statement generation started ==========
Generating GeneralKPIs_CountryName ...
SQL statement generation Success
```

Change the default filter configuration as you wish. Notice that, every time the *Filter1* control is changed, the *Query3* and *Query4* will be updated.

Control Name: Filter1

* Name: CountryName (notice )
* Caption: Country
* Type: Combo box
* Dynamic: True
* [Item values](https://wiki.genexus.com/commwiki/wiki?40410): CountryName
* [Item descriptions](https://wiki.genexus.com/commwiki/wiki?40138): CountryName
* [Empty item](https://wiki.genexus.com/commwiki/wiki?40139): True

`[imagen omitida: wiki id 52900]`

Cool! your dashboard object is done. You have 5 [query widgets](https://wiki.genexus.com/commwiki/wiki?36779) associated to 3 queries and they are related through 1 filter.

### [6) DashboardViewer](#6%29+DashboardViewer)

So far, we refined the dashboard object on the IDE. Now, we need to include it in the application to be visible for the users.

For a [Dashboard object](https://wiki.genexus.com/commwiki/wiki?36769) to be executable, it needs a special [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770). This control needs to be dragged and dropped into a Web Panel object.

So, create a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) called *GeneralKPI.* Drag and drop the [DashboardViewer control](https://wiki.genexus.com/commwiki/wiki?36770) from the toolbar and configure the control properties (set the correct dashboard on the *Object* property).

`[imagen omitida: wiki id 52904]`

### [7) Execution](#7%29+Execution)

There you go, run the application (F5) and open the brand new Web Panel containing the dashboard! You should see something similar to the image below:

`[imagen omitida: wiki id 52901]`


|  |
| --- |
| **Backlinks** |
| [Category:Dashboard object](https://wiki.genexus.com/commwiki/wiki?36769) | [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |

---
