---
title: "Work With for Web Selection Node"
source_id: 5640
source_url: https://wiki.genexus.com/commwiki/wiki?5640
genexus_version: "18"
---

# Work With for Web Selection Node

The Selection node, contained in every [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) instance, allows you to define and configure everything related to what will be generated in the corresponding WW<TransactionName> [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916).

`[imagen omitida: wiki id 52587]`.

This node has certain properties and subnodes that are explained below. All changes will generate code in the corresponding object. For example, if you change some property related to the Selection node, code will be written in the WW<TransactionName> Web Panel.

### [Properties](#Properties)

* [Caption](https://wiki.genexus.com/commwiki/wiki?52694)
* [Description](https://wiki.genexus.com/commwiki/wiki?52696)
* [Is Main](https://wiki.genexus.com/commwiki/wiki?52699)
* [Master Page](https://wiki.genexus.com/commwiki/wiki?52701,,)
* [Rows per page](https://wiki.genexus.com/commwiki/wiki?52700)
* [Custom Start Event Code](https://wiki.genexus.com/commwiki/wiki?51459)

### [Subnodes](#Subnodes+)

#### [**1)** **Modes (Insert, Update, Delete)**](#1%29+Modes+%28Insert%2C+Update%2C+Delete%29)

This node allows you to define which modes will be offered to invoke the [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908).

* Insert: Default | True | False
* Update: Default | True | False
* Delete: Default | True | False
* Display: Default | True | False
* Export: Default | True | False

The *Default* value means using the [Work With for Web Pattern Settings](https://wiki.genexus.com/commwiki/wiki?5642).

For each mode, a condition can be specified. To do so, the following properties are available:

* Insert Condition
* Update Condition
* Delete Condition
* Display Condition
* Export Condition

If a condition is defined, the associated action will be enabled only if its evaluation is True.

For the Update, Delete, and Display actions (which apply to a particular record) the condition can refer to the row values (e.g. CountryId= 10).

The condition can be anything that can be written inside an "if" statement in [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756), and often contains references to the context (current user, user level, etc), object parameters, the like operator, etc.

#### [**2)** **Attributes**](#2%29+Attributes)

This node includes the attributes and/or variables to be shown in the grid.

When right-clicking on the Attributes node, a [contextual menu](https://wiki.genexus.com/commwiki/wiki?16954,,) will appear allowing you to add new Attributes or variables.

Attribute properties:

* **Attribute:**Attribute name.
* **Description:**Text that will be shown as a label in tabs, or as a column title in grid tabs. The default value is taken from the Attribute's [ContextualTitle property](https://wiki.genexus.com/commwiki/wiki?4842).
* **Autolink:**If the attribute is a [Description attribute](https://wiki.genexus.com/commwiki/wiki?2154) and this property is set to True, a link to the corresponding View Web Panel will be placed wherever the Attribute is used.
* **Visible:** True (default value) or False.
* **Class:**Defines the Web Theme class-based Attribute, according to the classes of the selected Theme.
* **Column Class:**It is a Dynamic Combo Box to select the Theme class for the column.
* **Format:** Defines the [Format](https://wiki.genexus.com/commwiki/wiki?9083) used.

Variable properties:

* **Name:** Variable name.
* **Description:** Variable description.
* **Domain:** Variable [domain](https://wiki.genexus.com/commwiki/wiki?7221).
* **Load Code:** Code to be added in the Load event to load the variable.
* **Form**
  + **Visible:** True | False value.
  + **Class:** WebTheme class associated with the control.
  + **Format:** Text | HTML | Raw HTML | Text with meaningful spaces.

#### [**3) Orders**](#3%29+Orders)

Many orders can be offered in the Web Panel to be generated in order to sort the Grid rows. By right-clicking on the Orders node, you can add a new order, its name, and its composition. Each Order can be composed of many attributes and each attribute can be set as ascending or descending. For example, having defined the following Transactions:

```
Continent
{
    ContinentId*
    ContinentName
}

Country
{
      CountryId*
      CountryName
      ContinentId
      ContinentName
      City
     {
         CityId*
         CityName
     }
}
```

Suppose you apply the Work With for Web pattern to the Country Transaction and you define that Countries can be sorted by Name (*CountryName*) or Continent (*ContinentName*) or Both.

If there are many Orders, a combo will be presented (the shown values in the Combo are the names of the Orders).

`[imagen omitida: wiki id 52606]`

#### [**4) Filters**](#4%29+Filters)

Defines the conditions to filter the rows.  
  
Its subnodes are as follows:

* **Attributes:** Defines the Attributes/Variables in the plain level form that will be evaluated in the conditions.
* **Conditions:**For Attributes/Variables added in the Attributes Node, you can add conditions to filter the data to be shown in the Grid.

Following the example above, the filter Attributes are CountryName and ContinentName, and there are two conditions:

`[imagen omitida: wiki id 52611]`

#### [**5) Actions**](#5%29+Actions)

In addition to the predefined nodes that have been described, it is possible to add to the Selection node a node called 'Actions'. To do so, right-click on the Selection node and select **Add > Actions**. This node allows you to define actions so that the user can execute them when working with the Work With Web Panel.  
  
To create an Action, right-click on the **Actions** node, and select **Add > Action**.

Each action will be generated as an event in the Work With Web Panel.  
  
Action properties:

* **Name:**Action name (the associated event call will be generated as 'Do<action name>').
* **Caption:**This is the caption of the Action. For example: if the Action is associated with a button, this property applies to the button.
* **GXObject:** Name of the invoked object when performing the action.
* **Condition:** Determines when the action will be enabled.
* **ButtonClass:**It's the Web Theme class assigned to the button associated with the Action.
* **Grid Group**
  + **In Grid:** Defines if you want the action to be added as a Grid column (so that the action can be applied to a particular row) or as an independent action (outside the Grid). In this last case, a button will be added with a user event associated with it, named with the Caption property value. Use the True value to set the action must be inside the Grid. Select False to set the action must be outside the Grid. When selecting the True value, the action is displayed at the beginning of the Grid. When using the False value, the action button is included at the bottom of the Web Panel.
  + **MultiRowSelection:** By setting this property to True, a column with a checkbox will be added as the first column of the Grid (from left to right), and the action will be available out of the grid. In this way, at runtime, the action can be applied to multiple rows (the end user will be able to check the desired lines and execute the action to the selected lines). The default value for this property is False. When the MultiRowSelection property is set to True, an [SDT](https://wiki.genexus.com/commwiki/wiki?10021) collection with all the Attributes of the selected rows is added to the event code associated with the button. Then, the [GeneXus object](https://wiki.genexus.com/commwiki/wiki?1866) that was specified in the GXObject property is called, and the SDT is transferred as the first parameter as well as the additional parameters.
  + **Image:**Image to be associated with the Action in the Work With Web Panel when the Action is enabled (depending on the Condition property).
  + **Disabled Image:**Image to be associated with the Action in the Work With Web Panel when the Action is disabled (depending on the Condition property).
  + **Disabled Class:**Defines the Class to be used in the Grid when the action is not enabled.
  + **Tooltip:**Is the tooltip that appears when the mouse is positioned over the Action.
  + **In Grid Class:**Defines the Web Theme class for the variable that represents the action in the Grid.
  + **Column Class:**It is a Dynamic Combo Box that lets you define the Theme class for the column.
  + **Call Type:** Indicates the Call type for the object in Grid actions. When the value is "Auto", the invokation will be done with "Link" for all objects except non-main Procedures. When using the Call value, an event will be generated to call the [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908). When using the "Link" value, the Grid load logic will use the link method to call the object (&Control.Link = TransactionName.Link(Mode, parameters)).
* **Custom Group**
  + **Custom Code.** Procedural GeneXus code used to execute the action. Custom code cannot be used in conjunction with "MultiRowSelection" Actions.

You can indicate parameters to be sent to the called object. To do so, right-click on the Action, a [contextual menu](https://wiki.genexus.com/commwiki/wiki?16954,,) will appear and select **Add > Parameters**.

For example, imagine that you want to add an Action to let the user open another Web Panel that displays a list of all the countries that belong to the same continent as the selected country in the Grid.

The name of the Web Panel to be called is "ShowCountriesSameContinent" and contains the following [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862):

```
Parm(ContinentId);  // This attribute acts as a filter
```

And its Web Layout is:

`[imagen omitida: wiki id 52607]`

Look at the GXObject property and its parameters in the instance:

`[imagen omitida: wiki id 52608]`

The following event will be generated in the Work With Web Panel:

```
Event 'DoShowCountriesSameContinent'
    ShowCountriesSameContinent(ContinentId)
EndEvent
```

####


|  |
| --- |
| **Backlinks** |
| [Caption property for the Selection Node of a Work With for Web Pattern instance](https://wiki.genexus.com/commwiki/wiki?52694) | [Custom Start Event Code property](https://wiki.genexus.com/commwiki/wiki?51459) | [Description property for the Selection Node of a Work With for Web Pattern instance](https://wiki.genexus.com/commwiki/wiki?52696) |
| [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) |

---
