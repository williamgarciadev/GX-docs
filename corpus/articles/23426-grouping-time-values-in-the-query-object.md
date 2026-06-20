---
title: "Grouping time values in the Query object"
source_id: 23426
source_url: https://wiki.genexus.com/commwiki/wiki?23426
genexus_version: "18"
---

# Grouping time values in the Query object

GXquery allows grouping values according to certain predefined criteria, only for elements of Date and DateTime type. This way of grouping values is especially useful when the output type is Pivot table.

The values that can be used for grouping other values are as follows:

* Year
* Semester
* Quarter
* Month
* Day of week

To do so, there is a new category in the properties of a QueryElement called "Grouping" (visible only for elements of Date and Datetime type) with the following properties.

|  |  |
| --- | --- |
| **Group by year** | Indicates whether to group by year. |
| **Year title** | Character; indicates the title of the field created when grouping by year if the previous property is True. |
| **Group by semester** | Indicates whether to group by semester. |
| **Semester title** | Indicates the title of the field created when grouping by semester if the previous property is True. |
| **Group by quarter** | Indicates whether to group by quarter. |
| **Quarter title** | Indicates the title of the field created when grouping by quarter if the previous property is True. |
| **Group by month** | Indicates whether to group by month. |
| **Month title** | Indicates the title of the field created when grouping by month if the previous property is True. |
| **Group by day of week** | Indicates whether to group by day of the week. |
| **Day of week title** | Indicates the title of the field created when grouping by day of the week if the previous property is True. |
| **Hide value** | Indicates whether to hide the Date or Datetime value if a grouping is set. |

A list is needed with the sales made to the company's clients. To do so, we build the Query object with the attributes Customer name, Invoice date, Invoice amount and Final price (for more details about how to create a Query object, read [Query object](https://wiki.genexus.com/commwiki/wiki?9026)).

After building the Query object with the above attributes, select the [Query Element](https://wiki.genexus.com/commwiki/wiki?19788) Invoice Date and change the value of the “Group by year” property to True.

`[imagen omitida: wiki id 23427]`

Because it was set to True, the “Year title” property that has the “Year” value by default is enabled. Click on the property and change the value to “Grouping by year”.

At runtime, the result will be as follows:

`[imagen omitida: wiki id 23435]`

As you can see, it is made up of the client’s name, the invoice date, subtotal, total, and the year that we’ve just entered in the property, in the column before the date column.

We pivot the year column by dragging it to the first column. The image below shows the Pivot table after it has been reordered.

`[imagen omitida: wiki id 23436]`

It is also possible to combine more than one criterion at the same time. Suppose that we set the “Year” and “Semester” properties to True. The result would be as shown below.

`[imagen omitida: wiki id 23430]`

### [Hiding the selected column](#Hiding+the+selected+column)

It may happen that we don’t want to show the column selected as indicated above. To do so, we need to change the value of the “Hide value” property to True.

Continuing with the previous example, we set the property to True. The image below shows the new format.

`[imagen omitida: wiki id 23431]`


|  |
| --- |
| **Backlinks** |
| [Day of week title property](https://wiki.genexus.com/commwiki/wiki?40162) | [Group by day of week property](https://wiki.genexus.com/commwiki/wiki?40428) |
| [Group by month property](https://wiki.genexus.com/commwiki/wiki?40429) | [Group by quarter property](https://wiki.genexus.com/commwiki/wiki?40432) | [Group by semester property](https://wiki.genexus.com/commwiki/wiki?40433) | [Group by year property](https://wiki.genexus.com/commwiki/wiki?40434) |
| [Hide value property](https://wiki.genexus.com/commwiki/wiki?40163) | [Month title property](https://wiki.genexus.com/commwiki/wiki?40161) | [Quarter title property](https://wiki.genexus.com/commwiki/wiki?40160) |
| [Semester title property](https://wiki.genexus.com/commwiki/wiki?40159) | [Year title property](https://wiki.genexus.com/commwiki/wiki?40158) |

---
