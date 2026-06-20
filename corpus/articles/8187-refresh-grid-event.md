---
title: "Refresh Grid event"
source_id: 8187
source_url: https://wiki.genexus.com/commwiki/wiki?8187
genexus_version: "18"
---

# Refresh Grid event

Defines an action that must be taken before the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) is loaded. It is executed immediately before loading the grid. Data shown in the form is loaded from the database into the grid.

### [Syntax](#Syntax)

**Event** *grid\_control***.Refresh**  
     *event\_code*  
**EndEvent**

**Where:**  
*grid\_control*  
     Name of the grid control.  
*event\_code*  
     Code associated with the event.

### [Example](#Example)

A [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) or a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) displays Customer Invoices for a certain date range.

The conditions are:

SupplierId = &SupplierId;  
PoDate >= &Date1;  
PoDate <= &Date2;

So, if the end-user were to change the values of &SupplierId, &Date1, or &Date2, the grid must be reloaded to display the new information that satisfies the new condition.  
Thus, the refresh event associated with that grid is executed.

### [Notes](#Notes)

The Refresh event is triggered (i.e. the grid is reloaded):

* After the Start Event.
* When the Refresh command has been executed from within another Event (usually the Enter event, or a User Defined event).
* On Web Generator:
  + When executing Refresh command and [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) is Smooth, the Refresh of the grid is not executed in a POST HTTP unless the [Refresh method for Grid controls](https://wiki.genexus.com/commwiki/wiki?22578) is executed.
  + Anytime the user chooses the Refresh option from the Menu Bar (or presses F5).
  + If [Automatic refresh property](https://wiki.genexus.com/commwiki/wiki?6803) of the web panel is "When variables in conditions change" when a variable appearing in Conditions is modified by the user (a Web Panel that displays attribute values) the Refresh event of the grid is triggered. This is because the value of the variables used in conditions will determine the range of attributes to be displayed in the Grid.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) |
| **Controls** | [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) |
| **Platforms** | Web (.NET, Java), Smart Devices (iOS, Android) |

### 

### [See Also](#See+Also)

* [Refresh command](https://wiki.genexus.com/commwiki/wiki?25069)
* [Pull To Refresh property](https://wiki.genexus.com/commwiki/wiki?29993,,) (on Smart Devices)
