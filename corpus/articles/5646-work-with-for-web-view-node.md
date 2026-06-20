---
title: "Work With for Web View node"
source_id: 5646
source_url: https://wiki.genexus.com/commwiki/wiki?5646
genexus_version: "18"
---

# Work With for Web View node

Every [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) pattern instance contains a View node.

The following image shows the Work With for Web pattern instance that corresponds to a Transaction named "Category":

`[imagen omitida: wiki id 5647]`

Through this node (and subnodes), you can edit particularities you want GeneXus to consider when generating the **View** [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) that shows all the information of a record that in runtime has been selected in the grid of a [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) page.

The **View** generated Web Panel shows the record's data in a tab, and it has one tab for each subordinated table that contains a grid with the related information.

### [View subnodes](#View+subnodes)

#### Parameters

Declares the parameters that must be sent (and received) when calling the View object.

#### [Fixed Data](#Fixed+Data)

Attribute or ser of attributes shown as fixed data out of the Tabs. By default, It's the [Description Attribute](https://wiki.genexus.com/commwiki/wiki?2154).

`[imagen omitida: wiki id 52137]`

#### [Tabs](#Tabs)

Defines the Tabs that will be presented in the **View** Web Panel. Usually, the first Tab is labeled 'General' and displays information related to the first Transaction level.

There is also a Tab for each subordinate table.

The following properties can be configured for each Tab:

* **Condition**: Defines whether the Tab will be shown or not, depending on the condition. For instance, in this property, you can write CategoryId = 8 and the tab will be shown only if the condition is fulfilled. You can include in the condition a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) that returns a boolean value to be evaluated.
* **Type**: Defines how the data will be shown. The possible values are the following:
  + Tabular: This value is assigned for the property for the General tab. Data will be shown in text format.
  + Grid: Usually, this value is assigned for the property when the tab is used to present subordinated tables data.
  + UserDefined: In this case, a Web Component created by the developer will be called. It will be called with the same parameters as the View.
* **Rows per Page:** Number of rows to be shown in the grid.

**General** **Tab**

This tab displays the text data of the table. By default, it is Type = Tabular and contains the following data:

* Attributes - It indicates the attributes to be shown within it
* Actions - Actions executed on the database that can be performed with the information shown

**Related Tabs**

The rest of the Tabs display information corresponding to the tables related to the main table. By default, they are Type = Grid and have the following data:

* Name of the Transaction whose data will be shown
* Parameters to be used to call the Transaction
* Modes to be enabled for these parameters. In the InsertCondition, UpdateCondition, DeleteCondition and DisplayCondition properties, you can enter the condition that indicates whether the Mode will be shown or not. In these conditions you can use procedures (which are called using udp) as long as these procedures return a boolean value.

This structure of interrelated objects allows you to maintain consistency in the data viewed in the Tabs (browsing through the Transactions) after executing any action on any currently viewed data.


|  |
| --- |
| **Backlinks** |
| [Custom Start Event Code property](https://wiki.genexus.com/commwiki/wiki?51459) | [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) |

---
