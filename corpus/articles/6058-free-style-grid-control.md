---
title: "Free Style Grid control"
source_id: 6058
source_url: https://wiki.genexus.com/commwiki/wiki?6058
genexus_version: "18"
---

# Free Style Grid control

The Free Style grid, which can be used in Web interface objects ([Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s and [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s), allows you to design one line with a free design (not containing structured columns) and that line will be repeated showing that design for every record browsed.

It can contain attributes, variables, [text blocks](https://wiki.genexus.com/commwiki/wiki?5948), [images](https://wiki.genexus.com/commwiki/wiki?5939), [buttons](https://wiki.genexus.com/commwiki/wiki?6011), [web components](https://wiki.genexus.com/commwiki/wiki?31172), [embedded pages](https://wiki.genexus.com/commwiki/wiki?6070), other Free Style grids and/or [Grid controls for Web objects](https://wiki.genexus.com/commwiki/wiki?24817) to be displayed.

This type of grid does not have column titles and provides design freedom.

To add a Free Style grid control to the desired location, drag the corresponding icon from the [GeneXus IDE Toolbox](https://wiki.genexus.com/commwiki/wiki?10000) to the Web Layout.

At runtime, the grid is an HTML table.

### [Sample](#Sample)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s:

```
Country
{
   CountryId*
   CountryName
   City
   {
      CityId*
      CityName
   }
}

Attraction
{
   AttractionId*
   AttractionName
   CountryId
   CityId
   AttractionPhoto
   AttractionDescription
}
```

Suppose you need to define a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) that displays all the attractions showing their data in a specific way (not in structured columns).

To solve it, you can add a Free Style grid control in the [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132) and distribute the attributes as you wish. For example:

`[imagen omitida: wiki id 55637]`

At runtime, the Web Panel is displayed as follows:

`[imagen omitida: wiki id 6061]`

Of course, you can set several properties for the Free Style Grid, such as:

* Conditions (Filters)
* Order
* Base Trn
* etc.

The following image shows the same Web Panel displayed above with two more variables added. Also, the corresponding Conditions have been defined for the Free Style grid:

`[imagen omitida: wiki id 55642]``[imagen omitida: wiki id 55643]`

At runtime, the Web Panel is displayed as follows:

`[imagen omitida: wiki id 55644]`

Inside the Free Style grid, you can include another Free Style grid or Grid (to show several records for each attraction record).

For example, if the Attraction Transaction is defined as follows:

```
Attraction
{
   AttractionId*
   AttractionName
   CountryId
   CityId
   AttractionPhoto
   AttractionDescription
   Schedule
   {
      ScheduleDayOfWeek*
      ScheduleOpeningTime
      ScheduleClosingTime
   }
}
```

You may include a Grid inside the Free Style Grid to show, for each attraction, the days of the week and their opening and closing times. Read more in [Nested Grids in Web Panels](https://wiki.genexus.com/commwiki/wiki?6062).


|  |
| --- |
| **Pages** |
| [Allow Drag property](https://wiki.genexus.com/commwiki/wiki?9766) | [Allow Drop property](https://wiki.genexus.com/commwiki/wiki?9765) | [BorderColor property](https://wiki.genexus.com/commwiki/wiki?8725) |
| [BorderWidth property](https://wiki.genexus.com/commwiki/wiki?8727) | [Cell Padding property](https://wiki.genexus.com/commwiki/wiki?8732) | [Cell Spacing property](https://wiki.genexus.com/commwiki/wiki?8733) |
| [Conditions property](https://wiki.genexus.com/commwiki/wiki?9763) | [Conditions property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55966) | [Drag event in Web](https://wiki.genexus.com/commwiki/wiki?9642) |
| [Drop event in Web](https://wiki.genexus.com/commwiki/wiki?9643) | [Order property](https://wiki.genexus.com/commwiki/wiki?9842) |

---
