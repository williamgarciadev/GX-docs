---
title: "Orders and Filters in Grids of Panels"
source_id: 24805
source_url: https://wiki.genexus.com/commwiki/wiki?24805
genexus_version: "18"
---

# Orders and Filters in Grids of Panels

When business data is displayed on a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), it is possible to present the information in a clear way pursuant to criteria applied by developers based on the contents of the attributes and variables included in the [Work With object](https://wiki.genexus.com/commwiki/wiki?15974) or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829). In order to achieve that aim the **Data properties group** offers some properties to set up different aspects.

### [Data properties group](#Data+properties+group)

|  |  |
| --- | --- |
| **Property** | **Description** |
| [Orders property](https://wiki.genexus.com/commwiki/wiki?25472) | Allows specifying the **orders** in which the information should be listed, grouping information according to a specific value (**break by**). |
| [Search property](https://wiki.genexus.com/commwiki/wiki?36833) | Allows defining filters for **search** (including **advanced search**) allowed in regard to the data. |
| [Conditions property](https://wiki.genexus.com/commwiki/wiki?9763) | Field (and section as well) for filtering data by **conditions** that can be used freely and independently from the interface. |
| [Base Trn property](https://wiki.genexus.com/commwiki/wiki?36811) | Specifies which **Transactions** have to be navigated by the grid control. |

### [Example](#Example)

Consider the PropertyRealState [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) to represent the properties handled by a real estate.

`[imagen omitida: wiki id 36825]`

After [applying the Work With pattern](https://wiki.genexus.com/commwiki/wiki?15975) in this Transaction, GeneXus offers by default on the [List node](https://wiki.genexus.com/commwiki/wiki?15984) an order, search and filter conditions for the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) based on the types of attributes contained in the structure of the Transaction.

`[imagen omitida: wiki id 36862]`

If you consider this default information offered by the pattern, you may conclude the following:

* The list will be sorted by property name.  
  `[imagen omitida: wiki id 36827]`
* Searches will be possible inside the fields PropertyName and PropertyAddress, meaning that what the user enters in the Search will be searched within that information:  
  `[imagen omitida: wiki id 36828]`
* There will be possibilities to filter by the attributes PropertyListingDate (in this case offering to select Date From and Date Up To), PropertyOperation (offering the elements of the Operation enumerated, namely: Sale and Rent), and NeighborhoodId, to filter by neighborhood (where something like a selection list will be opened since it is [FK](https://wiki.genexus.com/commwiki/wiki?22918)):  
  `[imagen omitida: wiki id 36829]`

### [Sample](#Sample)

This example is available on [RealEstate](https://wiki.genexus.com/commwiki/wiki?23631,,).


|  |
| --- |
| **Backlinks** |
| [ApplicationBars Theme Class](https://wiki.genexus.com/commwiki/wiki?17879) | [ApplicationBars Theme Class (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56454) | [Conditions property](https://wiki.genexus.com/commwiki/wiki?9763) |
| [Conditions property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55966) | [Determining the Base Table for the Form and Grid in Panels](https://wiki.genexus.com/commwiki/wiki?24807) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Orders property](https://wiki.genexus.com/commwiki/wiki?25472) |
| [Orders property (GeneXus 18 upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55997) | [Server-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24234) | [Tabs offered in Panel and Work With objects](https://wiki.genexus.com/commwiki/wiki?16847) |

---
