---
title: "Query Object Usage Example"
source_id: 33991
source_url: https://wiki.genexus.com/commwiki/wiki?33991
genexus_version: "18"
---

# Query Object Usage Example

The objective of this document is to provide a detailed list of steps required to use the [Query object](https://wiki.genexus.com/commwiki/wiki?9026) and [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075).

This example is based on the reality of a Travel Agency and includes concepts such as Countries, Cities, Attractions, Tickets, Airports and more.

Many scenarios can be solved by using a [Query object](https://wiki.genexus.com/commwiki/wiki?9026), so let's focus on solving the following problem: knowing the number of attractions in France and Brazil.

**Note:** It is assumed that you have read the [Query object](https://wiki.genexus.com/commwiki/wiki?9026) and [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075) documents, and that you're familiar with basic concepts such as the query object structure.

Experience more QueryViewer functionalities with the [TestWebQueryViewer](https://wiki.genexus.com/commwiki/wiki?36747,,) KB sample.

### [Step-by-step guide](#Step-by-step+guide)

#### [1) Object creation](#1%29+Object+creation)

Create a [Query object](https://wiki.genexus.com/commwiki/wiki?9026) called *AttractionsByCountry*.

`[imagen omitida: wiki id 52637]`

#### [2) Object definition](#2%29+Object+definition)

To define the query's result, add attributes in the *Attributes* node under the *Structure* tab.

These attributes can be added in two ways: drag them from the *Work With Attributes* window to the query:

`[imagen omitida: wiki id 52638]`

Or, write the attribute names inline.

`[imagen omitida: wiki id 52639]`

Note that a suggested mechanism is available to make this task easier.

Use one method to include the following attributes in the query: *AttractionName* and *CountryName*.

#### [3) Descriptions](#3%29+Descriptions)

Once the attributes are under the *Attributes* node, check each *Description* column and set the descriptions: *Attractions* for *AttractionName* and *Countries* for *CountryName*.

Remember that descriptions are shown when the query is executed in the *Preview* tab or at runtime.

#### [4) Aggregations](#4%29+Aggregations)

To find out the number of attractions in each city, the *AttractionName* attribute must be defined as an aggregated formula.

Define the *Count*  aggregation function for the *AttractionName* attribute.

`[imagen omitida: wiki id 52640]`

#### [5) Preview](#5%29+Preview)

Sometimes, an early result of the query is very useful to find out if the desired result is displayed.

To do so, select the *Preview* tab and set the following property values:

* Output Type = Chart
* Chart Type = Pie

`[imagen omitida: wiki id 52642]`

#### [6) Filters](#6%29+Filters)

Suppose that we want to see only the values related to France and Brazil in the query result.

To achieve this, define the filter *CountryName* in (France, Brazil) under the *Filters* node.

The filter can be written inline or can be set using the right-click options available in each level. The new query structure will look as shown below:

`[imagen omitida: wiki id 52643]`

Return to the *Preview* section, and after a recalculation of the SQL statement needed, the new query result will be displayed.

#### [7) QueryViewer](#7%29+QueryViewer)

So far, we have defined the query to execute. Now, we need to include it in the application to be visible for the users.

For a Query object to be run at runtime, it needs a special control called [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075). This control needs to be dragged to a Web Panel object.

So, create a Web Panel object called *AttractionsQuantityByCountry.*

`[imagen omitida: wiki id 52644]`

And drag the QueryViewer control from the toolbar.

`[imagen omitida: wiki id 52645]`

Next, we need to set the control properties, so configure the *Object* property with the value *AttractionsByCountry*.

`[imagen omitida: wiki id 52646]`

#### [8) Execution](#8%29+Execution)

The final step is to display the query at runtime. To do so, run the application (F5) and open the Web Panel. At runtime, it will look as shown in the figure below:

`[imagen omitida: wiki id 52659]`


|  |
| --- |
| **Backlinks** |
| [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |

---
