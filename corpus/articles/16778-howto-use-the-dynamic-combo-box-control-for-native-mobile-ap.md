---
title: "HowTo: Use the Dynamic Combo Box Control for Native Mobile Applications"
source_id: 16778
source_url: https://wiki.genexus.com/commwiki/wiki?16778
genexus_version: "18"
---

# HowTo: Use the Dynamic Combo Box Control for Native Mobile Applications

[Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598) is a control applied for Win, Web and Native Mobile applications. It is used to relate two different [Transactions](https://wiki.genexus.com/commwiki/wiki?1908).

In this tutorial, you will learn how to use a dynamic combo box in Native Mobile.

### [Properties](#Properties)

|  |  |
| --- | --- |
| **AutoGrow** | If this property is true then the field will adjust the length of the attribute. |
| **Data Source From** | Indicates where the data is loaded from (a table, a Data Provider or from fixed values) |
| **ItemValues** | When selecting an item from a dynamic combo box, this property specifies the value that will be used in this field. |
| **ItemDescriptions** | Specifies the attribute values that will be listed by the Dynamic Combo Box. |
| **SortDescriptions** | If this property is true, then the descriptions will be sorted. |
| **Conditions** | You can set conditions on the list that will be deployed (it is unavailable until RC). |
| **InstantiatedAttribute** | Specifies a list of attribute names whose values ​​will be assumed instantiated when navigation is being calculated. |
| **EmptyItem** | It enables to set an empty option for this field. |

### [Samples](#Samples)

For this example, you will create two Transactions: Country and Hostel. These Transactions are related 1 to N: a Hostel belongs to one Country and a Country has many Hostels.

`[imagen omitida: wiki id 16779]`

You will have to apply the [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) (WWSD) to Hostel Transaction (for further information, see [Applying Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975)).

`[imagen omitida: wiki id 16785]`

To set Dynamic Combo Box to CountryId you must set the [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) for the [WW](https://wiki.genexus.com/commwiki/wiki?20840).

You will set the properties like the image shows:

#### [**Pattern Work With for Native Mobile**](#Pattern+Work+With+for+Native+Mobile)

#### 

**Item Value:** CountryId  
**Item Descriptions:** CountryName

You want to see the names of the countries, but the value that you need to store is CountryId. Finally, create a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) and add the item "WorkWithDevicesHostel"

`[imagen omitida: wiki id 16780]`

Done! You have your application ready to deploy on the device.

#### [**Android Snapshots**](#Android+Snapshots)

`[imagen omitida: wiki id 16786]`

`[imagen omitida: wiki id 16787]`

`[imagen omitida: wiki id 16788]`

`[imagen omitida: wiki id 16789]`

### [See Also](#See+Also)

[Smart Devices Applications Overview](https://wiki.genexus.com/commwiki/wiki?20670,,)


|  |
| --- |
| **Backlinks** |
| [Data Source From property](https://wiki.genexus.com/commwiki/wiki?22945) | [Data Source From property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55489) | [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598) |
| [HowTo: Use the Data Source From property](https://wiki.genexus.com/commwiki/wiki?22948) | [HowTo: Using the Data Source From property (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55521) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Sort Descriptions Property](https://wiki.genexus.com/commwiki/wiki?8839) |

---
