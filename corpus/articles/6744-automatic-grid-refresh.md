---
title: "Automatic Grid Refresh"
source_id: 6744
source_url: https://wiki.genexus.com/commwiki/wiki?6744
genexus_version: "18"
---

# Automatic Grid Refresh

The refresh behavior of the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) depends on the [Automatic refresh property](https://wiki.genexus.com/commwiki/wiki?6803).

An "Automatic refresh" occurs when changes are made to any variable in the web form that is used in the Refresh, Load event or conditions.

There is no restriction to the grid, which can be bound to an SDT as well.

The variable in the form that changes and triggers the grid refresh does not need to have any direct relation to the grid itself, only to be instantiated in any of these events:

* Refresh
* Load
* or the conditions of any of the grids or the web panel.

## [Availability](#Availability)

It is available in GeneXus X Evolution 2 upgrade 2. For previous versions, see [Automatic Refresh Grid (X Evolution 1)](https://wiki.genexus.com/commwiki/wiki?27897,,).  
Support for automatically refreshing grids bound to an SDT is available as from GeneXus X Evolution 3.

## [Automatic Refresh Property](#Automatic+Refresh+Property)

The purpose of the Automatic Refresh property is to give users the option to decide whether to load the grid automatically or to have the end user enter the filters and press a "Refresh" button afterwards.  
  
The possible values for this property are as follows:

* Yes (default value)
* No

`[imagen omitida: wiki id 27901]`

### [Automatic Refresh](#Automatic+Refresh)

As the user enters filters, the grid is automatically refreshed without the user having to click a "Refresh" button.

#### [Example](#Example+)

Suppose you have a grid which loads different employees of a company, and the following condition:

EmployeeName like &EmployeeName when not &EmployeeName.IsEmpty();

The variable &EmployeeName is in the form. When it's empty, no filters are applied, so all the records are shown:

`[imagen omitida: wiki id 27899]`

As the user enters key letters in the &EmployeeName filter, the grid automatically filters the corresponding records without the user having to click a "Refresh" button. The refresh is done automatically.

`[imagen omitida: wiki id 27900]`

Note: Depending on the data type of the filter, and the web control used for the filter, the condition will be applied as it is being entered or when leaving the field. In the case of filters in edit controls, for character filters, they are applied as the user enters them. For date, datetime, and numeric fields, conditions are evaluated when leaving the field. In the case of filters in combo boxes, dynamic combos, conditions are evaluated when leaving the field. For Checkboxes and radio buttons, conditions are evaluated when the value is changed. Note that only the grid is refreshed, not the rest of the page. If a checkbox is part of the filters, its start, refresh and load events won't be executed upon selecting it (because only the grid is refreshed by AJAX).

### [No Automatic Refresh: How to force a grid refresh when Automatic Refresh= NO](#No+Automatic+Refresh%3A+How+to+force+a+grid+refresh+when+Automatic+Refresh%3D+NO)

User action is needed to make the grid load the records that meet the conditions. Depending on whether the grid has a base table or not, there are two possible user actions to have the grid refreshed after entering the filters:

* Pressing Enter (only if the grid has a base table)
* Clicking on a button or image to trigger the refresh operation (in this case, the grid may or may not have a base table).   
  [See here for more information](https://wiki.genexus.com/commwiki/wiki?6760)

**[How to apply changes?](https://wiki.genexus.com/commwiki/wiki?17719)** Rebuild all objects


|  |
| --- |
| **Backlinks** |
| [Refresh Behavior in grids](https://wiki.genexus.com/commwiki/wiki?6760) |

---
