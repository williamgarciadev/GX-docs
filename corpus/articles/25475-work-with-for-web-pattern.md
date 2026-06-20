---
title: "Work With for Web pattern"
source_id: 25475
source_url: https://wiki.genexus.com/commwiki/wiki?25475
genexus_version: "18"
---

# Work With for Web pattern

To apply the Work With for Web [pattern](https://wiki.genexus.com/commwiki/wiki?2814) to a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) select the **Patterns** tab and then choose the **Work With for Web** tab.

You only have to click on the **Apply this pattern on save** checkbox and save.

After that, if you look for the Transaction in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210), you can see that several objects are located below the Transaction. They are created by GeneXus when the Work With for Web pattern is applied.

## [Instance Nodes](#Instance+Nodes)

 The following nodes are present in every Work With for Web pattern instance (and their properties by default are set with the values indicated in the [Work With for Web Pattern Settings](https://wiki.genexus.com/commwiki/wiki?5642)):

### [1) Root Node](#1%29+Root+Node)

`[imagen omitida: wiki id 31406]`

It has the following properties (accessed through the Properties window):

`[imagen omitida: wiki id 31407]`

* [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135)
* [Update Transaction property](https://wiki.genexus.com/commwiki/wiki?51941)
* Navigation Group: It has the following properties:
  + AfterInsert
  + AfterUpdate
  + AfterDelete

These properties allow indicating the layout to which you want to go to after performing an insertion, an update, or a deletion, respectively. For each of these properties, there is a combo box that offers the values:

 <default>  
 <return to caller>  
 <go to view>  
 <go to selection>

### [2) Level Node](#2%29+Level+Node)

The instance will have one **Level node** for each [Transaction level](https://wiki.genexus.com/commwiki/wiki?42569):

`[imagen omitida: wiki id 31410]`  
  
Each of these nodes has the following properties:

* **Name:** The default value of this property is the level's base table.
* **Description:** Describes the node.

And the following sub-nodes:

#### [**2.1) Description Attribute**](#2.1%29+Description+Attribute)

It defines the Transaction's [Description attribute](https://wiki.genexus.com/commwiki/wiki?2154).  
Since this attribute will have a link, it can only be an Edit type attribute (that is, it cannot be a Combo or checkbox).

#### [**2.2) Selection**](#2.2%29+Selection)

See [Work With for Web Selection Node](https://wiki.genexus.com/commwiki/wiki?5640).

#### [**2.3) View**](#2.3%29+View)

See [Work With for Web View node](https://wiki.genexus.com/commwiki/wiki?5646).

## [Objects generated by the Work With for Web pattern](#Objects+generated+by+the+Work+With+for+Web+pattern)

The Work With for Web pattern will generate the following objects for each Transaction to which is applied:

### [1) Work With Web Panel](#1%29+Work+With+Web+Panel)

It's a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) with a grid that lists all the records in a table and includes the following features:

* Paging
* Conditional Filters
* Multiple Orders
* Control Info for Filter Attributes
* Standard Actions
* Export to Excel
* Save Grid State

### [2) View Web Panel](#2%29+View+Web+Panel)

It's a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) that shows all the information of a record that has been selected in the grid of a Work With Web Panel. It shows the record's data in a tab, and also shows one tab for each subordinated table, containing a grid with the related information.

### 3) Optional Features

* Context management
* Object level security

The generated objects are automatically generated and called as follows:

* **WW<TransactionName>**
  + Sample: WWCategory.
  + It's the [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) with a grid generated from the **first Level node** definition.
* **View<TransactionName>**
  + Sample: ViewCategory.
  + It's the [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) that shows all the information of a record that has been selected in the grid of the **WW<TransactionName>** Web Panel.
* **<TransactionName>General**
  + Sample: CategoryGeneral.
  + Is a [WebComponent](https://wiki.genexus.com/commwiki/wiki?1864) associated to the **View<TransactionName>**General Tab.
* **<XXX>WC**
  + Sample: CustomerWC.
  + A [WebComponent](https://wiki.genexus.com/commwiki/wiki?1864) with this name is generated for each Grid-type Tab.

## Work With for Web pattern features

The Work With for Web pattern features are the following:

* A [Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159) is automatically generated for [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s and [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s for listing, searching and ordering data.
* Web objects comply with the [Web Smooth UX](https://wiki.genexus.com/commwiki/wiki?25801,,).
* Controls supported by the [Web Abstract Editor](https://wiki.genexus.com/commwiki/wiki?24795) such as [Action Group Control for the Web](https://wiki.genexus.com/commwiki/wiki?25631) and [Tab control for Web Panels](https://wiki.genexus.com/commwiki/wiki?25623).
* The design proposed by [Unanimo](https://wiki.genexus.com/commwiki/wiki?48382) Design System is applied.
* [Responsive Web Design](https://wiki.genexus.com/commwiki/wiki?29134) apps are generated.

The [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) should be set to Responsive Web Design. Otherwise, check the compatibility notes below.

## Compatibility Notes

For compatibility reasons, the Work With pattern template generates different layouts depending on the Theme / Design System configured.

* If [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) is set to Responsive Web Design and [Default Form Layout property](https://wiki.genexus.com/commwiki/wiki?51685) = Unanimo Template, the default layouts use the [Unanimo](https://wiki.genexus.com/commwiki/wiki?48382) Design System. See Also [Default Master Page property](https://wiki.genexus.com/commwiki/wiki?11597).
* If [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) is set to Responsive Web Design and [Default Theme property](https://wiki.genexus.com/commwiki/wiki?48565,,) is Carmine (or a save as of it), the default forms use the [Carmine Theme](https://wiki.genexus.com/commwiki/wiki?32274) for [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,), [GeneXus 16](https://wiki.genexus.com/commwiki/wiki?35351,,), [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,) until [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,).
* If [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) is set to Responsive Web Design and [Default Theme property](https://wiki.genexus.com/commwiki/wiki?48565,,) is different than Carmine (or a save as of it), the default forms are equal to the ones generated for X Evolution 3.
* Otherwise, if [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) is set to "Previous Version Compatible", the generated objects won't be Responsive, and the layouts are equal to the forms generated for X Evolution 2.

## [See Also](#See+Also)

[Work With for Web Pattern Settings](https://wiki.genexus.com/commwiki/wiki?5642) (to see what the general settings related to all instances are).  
[LightCRM](https://wiki.genexus.com/commwiki/wiki?22592,,) sample for a [RWD](https://wiki.genexus.com/commwiki/wiki?25157,,) implementation of this pattern.


|  |
| --- |
| **Backlinks** |
| [Applying Carmine Template settings to old-model WW objects](https://wiki.genexus.com/commwiki/wiki?32274) | [Built-in Patterns](https://wiki.genexus.com/commwiki/wiki?6491) | [Caption property for the Selection Node of a Work With for Web Pattern instance](https://wiki.genexus.com/commwiki/wiki?52694) |
| [Custom Start Event Code property](https://wiki.genexus.com/commwiki/wiki?51459) | [Description property for the Selection Node of a Work With for Web Pattern instance](https://wiki.genexus.com/commwiki/wiki?52696) | [Dynamism between Transactions and Patterns](https://wiki.genexus.com/commwiki/wiki?6622) |
| [Executing From QR Codes](https://wiki.genexus.com/commwiki/wiki?18260) | [Form Template property](https://wiki.genexus.com/commwiki/wiki?51711) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |
| [How to design a Responsive Web Application: Hiding a column in a grid](https://wiki.genexus.com/commwiki/wiki?25495) | [How to use Unanimo](https://wiki.genexus.com/commwiki/wiki?52176) | [HowTo: Apply the Fiori for Web pattern for the first time](https://wiki.genexus.com/commwiki/wiki?38862) |
| [HowTo: apply the Fiori pattern for the first time (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54785) | [HowTo: Display a menu in a responsive application](https://wiki.genexus.com/commwiki/wiki?25778) | [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) | [HttpClient data type (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?55613) |
| [Is Main property for the Selection Node of a Work With for Web Pattern instance](https://wiki.genexus.com/commwiki/wiki?52699) | [Navigation external object](https://wiki.genexus.com/commwiki/wiki?32395) |
| [NewLine function](https://wiki.genexus.com/commwiki/wiki?8469) | [Notification Provider API](https://wiki.genexus.com/commwiki/wiki?33687) | [Style property in Work With for Web Pattern Settings](https://wiki.genexus.com/commwiki/wiki?52134) | [Style property in Work With for Web Pattern Settings (GeneXus 18)](https://wiki.genexus.com/commwiki/wiki?53343) |
| [Tab control for Web Panels](https://wiki.genexus.com/commwiki/wiki?25623) | [Update Transaction property](https://wiki.genexus.com/commwiki/wiki?51941) | [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) | [Work With for Web Selection Node](https://wiki.genexus.com/commwiki/wiki?5640) |
| [Work With for Web View node](https://wiki.genexus.com/commwiki/wiki?5646) | [Work With Patterns](https://wiki.genexus.com/commwiki/wiki?5636) |

---
