---
title: "Grid control"
source_id: 24817
source_url: https://wiki.genexus.com/commwiki/wiki?24817
genexus_version: "18"
---

# Grid control

The Grid control displays data associated with many records. In some cases, it also allows entering, updating, and deleting data.

You can include a Grid control in GeneXus objects with UI (User Interface/screen).

The Grid control has different capabilities depending on the object in which it is located. It is important to understand them.

## [Grids in Web Panels and Transactions](#Grids+in+Web+Panels+and+Transactions)

Grids in [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s and [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s contain structured columns (each one containing an attribute or a variable) and each column has a title.

They are usually called Standard Grids.

To design a more flexible distribution of the attributes/variables for the lines of the Grid (or to add another Grid or other controls inside a Grid), use the [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058).

## [Grids in Panels](#Grids+in+Panels)

When you add a Grid control in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) and select the attributes/variables to be included inside it, by default, they are placed one next to the other.

`[imagen omitida: wiki id 55827]`

If you leave this kind of distribution, at runtime you will see a result very similar to a Grid that contains columns, but, strictly speaking, they are not columns.

You can move those attributes/variables freely. For example, instead of displaying each attraction's attribute/variable values one next to the other, you can place the attributes/variables as you wish them to be displayed for each attraction.

`[imagen omitida: wiki id 55828]`

In addition, you can include another Grid (or other controls) inside a Grid present in a Panel.

That is to say, the Grid control in Panels offers the same behavior as the [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058) in Web Panels and Transactions.

Moreover, Grids included in Panel objects have the [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) which allows presenting the data with interesting formats.

**Note**: If you want to include a Grid with structured columns in a Panel, the [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) is available since [GeneXus 18 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?53853) when using the [GeneXus Angular Generator](https://wiki.genexus.com/commwiki/wiki?42550).

## [How to add a Grid](#How+to+add+a+Grid)

There are different ways to add a Grid:

1. Drag the Grid icon from the [Toolbox](https://wiki.genexus.com/commwiki/wiki?10000) to the desired location on the Web Layout of the Web Panel / Layout of the Panel.
2. Select **Insert > Grid** from the GeneXus main menu.

Next, a Selector window will be opened to select which attributes/variables you want to include in the Grid.

## [Behavior according to the object in which the Grid is located](#Behavior+according+to+the+object+in+which+the+Grid+is+located)

|  |  |
| --- | --- |
| **Web Panel / Panel** | **Transaction** |
| Attributes included in the Grid are always read-only. They are queried and displayed. You can't change this behavior. | * Not inferred attributes included in the Grid are editable by default. You can change this behavior if needed. See [NoAccept rule](https://wiki.genexus.com/commwiki/wiki?6856). * Inferred attributes included in the Grid are read-only. You can change this behavior if needed. See [Update rule](https://wiki.genexus.com/commwiki/wiki?21430). |
| Variables included in the Grid are, by default, read-only.  However, data can be accepted in Grid variables depending on the events programmed in the object:  1. If you are using the [For Each Line command](https://wiki.genexus.com/commwiki/wiki?8605) inside an event.  2. If the Grid includes a control with an associated [Click event](https://wiki.genexus.com/commwiki/wiki?8177).  When one of these cases occurs, all variables inside the Grid become input variables. You can define which variables can't be modified by using the [NoAccept rule](https://wiki.genexus.com/commwiki/wiki?6856) or by setting the variable Read Only property to True. | Variables included in the Grid are read-only by default. You can change this behavior if needed. See [Accept rule](https://wiki.genexus.com/commwiki/wiki?6844). |
| The main objective of the Grid control in these objects is to query data. | The main objective of the Grid control in Transactions is to insert, update, and/or delete records in the corresponding associated table. |
| The Grid control's behavior is different in other use cases, such as when including variables based on [SDT](https://wiki.genexus.com/commwiki/wiki?2427)s. See [SDTs on Forms](https://wiki.genexus.com/commwiki/wiki?2090,,). | The Grid control's behavior is different when used in [Dynamic Transactions](https://wiki.genexus.com/commwiki/wiki?28062). |

## [Runtime features of Grids](#Runtime+features+of+Grids)

* Grids allow for [automatic paging](https://wiki.genexus.com/commwiki/wiki?6086).
* Grids with structured columns (those included in Web Panels and Transactions) allow users to order the column's contents (in ascending or descending order) by clicking on their titles.

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Web panel object. First steps](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/web-panel-object-first-steps-6104784)


|  |
| --- |
| **Pages** |
| [Allow Drag property](https://wiki.genexus.com/commwiki/wiki?9766) | [Allow Drop property](https://wiki.genexus.com/commwiki/wiki?9765) | [Allow Hovering property](https://wiki.genexus.com/commwiki/wiki?43237) |
| [Allow Selection property](https://wiki.genexus.com/commwiki/wiki?8680) | [Arrange Columns](https://wiki.genexus.com/commwiki/wiki?9637) | [Attribute/Variable control properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8133) |
| [Average length property](https://wiki.genexus.com/commwiki/wiki?7237) | [BorderColor property](https://wiki.genexus.com/commwiki/wiki?8725) | [BorderWidth property](https://wiki.genexus.com/commwiki/wiki?8727) |
| [Cell Padding property](https://wiki.genexus.com/commwiki/wiki?8732) | [Cell Spacing property](https://wiki.genexus.com/commwiki/wiki?8733) | [Conditions property](https://wiki.genexus.com/commwiki/wiki?9763) |
| [Conditions property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55966) | [Dimensions property](https://wiki.genexus.com/commwiki/wiki?7380) | [Fixed Grid header with vertical scroll](https://wiki.genexus.com/commwiki/wiki?36036) |
| [Grid paging on the Web](https://wiki.genexus.com/commwiki/wiki?6064) | [HowTo: Work with rows in a Transaction Grid](https://wiki.genexus.com/commwiki/wiki?6816) | [Maximum length property](https://wiki.genexus.com/commwiki/wiki?7236) |
| [Nested Grids in Web Panels](https://wiki.genexus.com/commwiki/wiki?6062) | [Order property](https://wiki.genexus.com/commwiki/wiki?9842) | [Refresh Behavior in grids](https://wiki.genexus.com/commwiki/wiki?6760) |
| [Sortable property](https://wiki.genexus.com/commwiki/wiki?14173) | [Working with Grids in Web Panels](https://wiki.genexus.com/commwiki/wiki?6093) |

---
