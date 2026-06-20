---
title: "Determining the Base Table for the Form and Grid in Panels"
source_id: 24807
source_url: https://wiki.genexus.com/commwiki/wiki?24807
genexus_version: "18"
---

# Determining the Base Table for the Form and Grid in Panels

This article describes how GeneXus determines the tables to browse for information that will be loaded on a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

For each Layout (either for a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), or [Work With object](https://wiki.genexus.com/commwiki/wiki?15974) node -List, Detail or Section-), you have a fixed part, and possibly one or more grids (not considering grids associated with [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021)s).

If there are attributes in certain places (described below) related to the Layout, the plain (or fixed) part will have a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347). Similarly, if there are attributes in certain places related to a grid, there will be a Base table for it. Each base table is determined independently of one another, and navigations are independent as well (it is similar to having a pair of parallel [For Each command](https://wiki.genexus.com/commwiki/wiki?24744)s).

The attributes involved in determining the **fixed part base table** are:

* The attributes included in the fixed part of the Layout.
* The attributes referenced in Order, Search, Advanced search, and Conditions.
* The attributes used in some of the Events, outside the For Each commands. Which events? **Refresh**, and all events related to buttons or control events in the fixed part of the layout, and in the Application Bar.

The attributes involved in determining the **grid base table** are:

* The attributes included in the grid.
* The attributes referenced in Order, Search, Advanced search, and Conditions.
* The attributes used in some of the Events, outside the For Each commands. Which events? **Load**, and all events related to buttons or control events **inside the grid**.

### [Example](#Example)

Suppose you have the following relationship among database tables:

`[imagen omitida: wiki id 24321]`

Suppose you have created a Panel (named SDPanel1), where you want to display the Country received by parameter, and the Customers from that country. To this end, you have defined the following layout:

`[imagen omitida: wiki id 24322]`

**Rules:**

```
parm( in: CountryId);
```

Furthermore, when the country has signed trade agreements, you indicate it by setting image1 as visible. Similarly, if the customer being loaded onto the grid has over 1,000 dollars invoiced, you will want to indicate thisby setting image2 as visible.

You have also inserted three buttons: one in the Application Bar ("Add"), one on the form (ViewInfo), and the third one on the grid (Billing...). Each button will have a user event.

This is the corresponding Event tab:

`[imagen omitida: wiki id 24323]`

**Determining fixed part base table:**

The attributes taken into account are:

* From the layout: CountryName.
* From conditions tab: none (assume no conditions are set).
* From events: CountryId from 'ViewInfo', (note that there are no attibutes inside 'Add'), CountryAggrement from Refresh.

So, the form base table is Country. Since Panel is receiving the country identifier in the attribute (CountryId), an automatic filter by equal will be specified.

**Determining grid base table:**

The attributes taken into account are:

* From the layout: CustomerName (grids attribute).
* From conditions tab: none (assume no conditions are set).
* From events: CustomerId from 'Billing...' and none from Load (because there are no attributes outside For Each).

So, the grid base table is Customer. And again, since Panel is receiving the country identifier in the attribute (CountryId), an automatic filter by equal will be specified.

Note that both navigations are independent, as if they corresponded to two parallel For Each commands.

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Data loading logic and base tables in a Panel](https://training.genexus.com/en/learning/courses/genexus-for-mobile/v18/course-genexus-for-mobile-genexus-18/26080/data-loading-logic-and-base-tables-in-a-panel)

### [See Also](#See+Also)

[Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042)  
[Server-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24234)  
[Event Triggering Order in Panels](https://wiki.genexus.com/commwiki/wiki?17614)  
[Orders and Filters in Grids of Panels](https://wiki.genexus.com/commwiki/wiki?24805)


|  |
| --- |
| **Backlinks** |
| [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) | [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
