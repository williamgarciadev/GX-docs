---
title: "Load event"
source_id: 8188
source_url: https://wiki.genexus.com/commwiki/wiki?8188
genexus_version: "18"
---

# Load event

This system event is executed immediately after the [Refresh event](https://wiki.genexus.com/commwiki/wiki?8195,,). Its behavior depends on the object ([Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)), on whether there is a grid in the Layout or not, and if there is an associated [Base Table](https://wiki.genexus.com/commwiki/wiki?6347).

However, it always relates to loading the information on the Layout (the plain part in the case of a Web Panel with no grid, or otherwise the grid). It is often used to load variable values on the grid. The values of these variables may be calculated through assignments or by reading the database using the [For Each command](https://wiki.genexus.com/commwiki/wiki?24744).

### [Syntax](#Syntax)

```
Event Load
   Event_code 
EndEvent

Where:
```

*Event\_code:* This is the code that will be executed (on the Server) whenever the event is triggered.

An error will occur if you try to code the Load event having more than one grid in the Layout. The general Load event (meaning that it is not linked to a specific grid control, as *gridName***.Load** event) is allowed only in the case of one grid at the most.

In Panel objects, the Load event will only be executed if there is a grid (not based on an SDT), at the time of loading it. Additionally, in Web Panels, if the Web Panel is plain (with no grid), the Load event will relate to the load of that plain information (unlike Panel objects, where [Refresh event](https://wiki.genexus.com/commwiki/wiki?8195,,) plays that role). The difference is that, while in Web Panels, in all cases there is, regardless of the existence of a grid, one **related** table (base table in the case of attributes) at the most, in Panel objects there will be necessarily two of them (one for the fixed part and one for the grid).

**Web Panels**

* If attributes exist (in the layout, order, conditions, data selector or events outside For Each), there will be a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347). The Load event will be triggered n times, where represents the number of records in the base table meeting the conditions.
  + When the Web Panel is **plain (with no grid)**, there should be a condition that only one record will meet. Otherwise, it is not programmed properly. That record information (and its extended table related records) is what will be loaded when the Load event is triggered. At this point, you must codify any behavior required at the time (such as variable assignments based on the database record that is loaded).
  + When **there is a grid**, attributes on the fixed-part (belonging to [Extended Table](https://wiki.genexus.com/commwiki/wiki?6029) of the grid) only make sense when they have the same value for each line loaded on the grid (otherwise, they would be on the grid). Here, the Load event is triggered once for each extended table 'record' meeting the conditions. At that point, the related line is loaded onto the grid, so it is the perfect moment to set the values of variables that depend on the extended table 'record' that is loaded.
* Otherwise (only variables in the locations mentioned), there will not be a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347). The Load event will be triggered only once, and there is where you must program (in the *Event\_code*) the complete load of the form, using the [Load command](https://wiki.genexus.com/commwiki/wiki?8196) for loading each grid line, (if any grid exists).

**Panels**

* If there is **no grid** (not based on SDT), the Load event will not be executed. To load the fixed part of the Layout, the [Refresh event](https://wiki.genexus.com/commwiki/wiki?8195,,) should be coded, that is: the event associated with the fixed-part base table.
* **Otherwise**, attributes on the fixed-part determine its own base table, other than the grids. So, some conditions (e.g. parameter) have to search from among all possible table registers in order to keep only one of them. When you need to load variables through assignments from that record, the [Refresh event](https://wiki.genexus.com/commwiki/wiki?8195,,) coding is the answer. Meanwhile, if some grid variables are to be loaded for each line, it will be necessary to code the Load event, as it is done in a Web Panel.

If the Web Panel or the Panel grid has an associated **base table** and a [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) is used inside the Load event code, then this For Each will be considered as nested regarding the implicit one (the Load event performs an implicit For Each operation over the Base Table), having a join, control break or cartesian product, as it is the case with nested For Eachs. In the *Event\_code* you may use any of the extended table attributes corresponding to the Load base table, without the need for writing a For Each (since it is implicit!).

In the case of Base table, the total number of executions for this event depends on the total number of grid records to be loaded. And also, the records may be loaded upon the user's request. To such effects, you have the [Rows property](https://wiki.genexus.com/commwiki/wiki?2452) in the grid. When it is set to 10, 10 records are loaded each time (that is known as [automatic paging](https://wiki.genexus.com/commwiki/wiki?6086)).

### [Examples](#Examples)

1. A plain Web Panel shows some customer information (customer received by parameter). Note the attributes in the Layout. The Navigation Report shows the Load event is implicitly navigating the Customer table, and an automatic filter by CustomerId is achieved (since receiving in CustomerId parameter).

`[imagen omitida: wiki id 24302]`

Suppose this Web Panel is invoked from another object, with 2 as the parameter value. Then, the information of CustomerId 2 will be displayed:

`[imagen omitida: wiki id 24303]`

When you must show an image on the screen indicating whether the customer has many associated flights (each flight seat has a CustomerId), you insert that image, (called Image1) on the screen:

`[imagen omitida: wiki id 24304]`

and make it visible when applicable (e.g. customer has more than 10 flights):

```
Event Load
     &total = 0
     for each defined by FlightSetLocation
        &total += 1
     endfor
     if &total >10
        Image1.Visible = True
     else
        Image1.Visible = False
     endif
EndEvent
```

Note the explicit For Each is nested to the implicit (Customer) one.

2. A Web Panel with a grid showing all customers and the total prices of all flights where the passenger has a reserved seat.

`[imagen omitida: wiki id 24305]`

The &flightPrice variable was inserted on the grid to calculate what was necessary for each customer. Note the CustomerFullName attribute is determining the grid has a base table. And it is Customer.

So, every time a line (customer) is loaded on the grid, you must calculate the corresponding variable value:

```
Event Load
   &flightPrices = 0
   for each defined by FlightSeatLocation
      &flightPrices = &flightPrices + FlightFinalPrice
   endfor
   &totalFlightPrices = &totalFlightPrices + &flightPrices //in order to summarize prices for all clients loaded on the grid
EndEvent
```

Note that the for each is nested to the implicit one (for this reason you did not have to specify the filter by CustomerId).

This is how the navigation listing informs that the Web Panel has a base table (Customer):

`[imagen omitida: wiki id 24306]`

This will cause the Load event to be executed for each customer in this table. Since the Load has a For each, you need to navigate its base table, which the navigation report indicates is the one with flight seats, retrieving the records corresponding to that customer, which will be loaded on the grid at that particular moment.

Note the Constraints for a customer to be loaded into the grid. This is because the following condition for the grid was specified:

`[imagen omitida: wiki id 24308]`

3. Similarly, in a Panel object, you have to load a variable on the grid depending on whether a real estate property had more than a certain number of visits or not, in order to classify it as one of the most visited. Additionally, if the property was listed during the last couple of days, suppose you want to display an image indicating that it is a new property.

`[imagen omitida: wiki id 24255]`

To do so, see the [Load example](https://wiki.genexus.com/commwiki/wiki?24296).

4. Consider the two [Transactions](https://wiki.genexus.com/commwiki/wiki?1908): Invoice and Order:

```
Invoice
{
     InvoiceNumber*
     InvoiceDate
}
```

```
Order
{
     OrderNumber*
     OrderDate
}
```

Suppose you want to design a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) with a grid that includes information from orders in some lines, and information from invoices in other lines. This is not possible in a straightforward manner because you cannot define different types of grid lines (one line displays Invoice attributes and the one below it displays Order attributes, etc.)

The solution is to define a Web Panel without a [Base Table](https://wiki.genexus.com/commwiki/wiki?6347), define grid lines made up of variables, and handle the loading of these variables using the Load event together with the [Load command](https://wiki.genexus.com/commwiki/wiki?8196).

To build a Web Panel without a base table you must make sure that there are no attributes mentioned in the Web Layout or Events (except those included in [For Each command](https://wiki.genexus.com/commwiki/wiki?24744)s and Conditions). Either, you can not set the [Base Trn property](https://wiki.genexus.com/commwiki/wiki?36811) for the grid.

#### 

Lastly, you must declare the following Load event:

```
Event Load
    For each
        &InvoiceNumber = InvoiceNumber
        &InvoiceDate   = InvoiceDate
        ...
        Load
    EndFor
    For each
        &OrderNumber = OrderNumber
        &OrderDate   = OrderDate
        ...
        Load
    EndFor
EndEvent
```

The Load command forces the load of the current For Each line into the grid. It is used only in special cases like this.

This is not a regular use for the Load event. In this case, there is no implicit For Each since there is no Base Table defined. All the loading must be done "manually" (using explicit commands) and all at once, instead of using the default loading.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects:** | [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) |
| **Generators:** | [GeneXus .NET Generator](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

### [See Also](#See+Also)

[Refresh event](https://wiki.genexus.com/commwiki/wiki?8195,,)  
[Load command](https://wiki.genexus.com/commwiki/wiki?8196)  
[Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042)  
[Server-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24234)  
[Event Triggering Order in Panels](https://wiki.genexus.com/commwiki/wiki?17614)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Events in Mobile Applications](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/events-in-mobile-applications-6103211?p=3673)


|  |
| --- |
| **Backlinks** |
| [ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044) | [Event Triggering Order in Panels](https://wiki.genexus.com/commwiki/wiki?17614) |
| [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) | [Load command](https://wiki.genexus.com/commwiki/wiki?8196) | [Category:Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042) | [Nested Grids in Web Panels](https://wiki.genexus.com/commwiki/wiki?6062) |
| [Pin Image Attribute property](https://wiki.genexus.com/commwiki/wiki?42213) | [Pin Image Field Specifier property](https://wiki.genexus.com/commwiki/wiki?42214) | [Pin Image property](https://wiki.genexus.com/commwiki/wiki?42212) | [Pin Image property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54382) |
| [Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863) | [Refresh command in Panels](https://wiki.genexus.com/commwiki/wiki?25060) | [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076) |
| [Server-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24234) | [Web Panels events](https://wiki.genexus.com/commwiki/wiki?8178) |

---
