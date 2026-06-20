---
title: "GXflow Actions"
source_id: 25711
source_url: https://wiki.genexus.com/commwiki/wiki?25711
genexus_version: "18"
---

# GXflow Actions

The Actions component allows the user to view all the existing actions and manage all their properties. Actions are buttons that can be available on each component, for example the Inbox component has the "New", "Execute" and "Send" actions—among others. These actions are represented by buttons on the component interface, as shown below:

`[imagen omitida: wiki id 52304]`

In the following sections you will find the description of the different components.

### [Actions](#Actions)

The following toolbar buttons allow you to make changes to the Actions in the grid.

* **New**: the New button allows the user to create a new action. The user will view the following dialog where he can set the action properties:  
  `[imagen omitida: wiki id 52305]``[imagen omitida: wiki id 52306]`

1. General tab:
   * **Id**: a string identifying the action.
   * **Name**: a string to be used in the tree to identify the action.
   * **Description**: a string with a description of the action.
2. Application tab:
   * **Class Name**: name of the object to be called when the component is opened. For example, if a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) named "SendEmail" is to be called, the "SendEmail" string is set to the **Object** property.
   * **Is batch?**: whether the action is batch. If the action is not set as batch it will be called as a pop up window.
   * **Apply on selection**: whether the action applies over a selection. If this property is enabled, the object assigned in the **Class Name** property will be called using a string as parameter. This string will contain the ID of the item selected in the row.
   * **Multiple selection**: whether the action applies over a multiple selection. If this property is enabled the object assigned in the **Class Name** property will be called using a string as parameter. The string will contain the IDs of the items selected in the grid, separated by a comma—','.

* **Edit**: allows editing any property of an action. This option is not allowed for default actions; the error "This operation is not allowed" will be displayed if used when selecting a default action.
* **Display**: displays all the properties of the action.
* **Remove**: removes/deletes the action. This option is not allowed for default actions; the error "This operation is not allowed" will be displayed if used when selecting a default action.

### [Actions Grid](#Actions+Grid)

This grid has the following options:

`[imagen omitida: wiki id 52012]` It allows selecting the columns wanted to be visible.

`[imagen omitida: wiki id 52013]` It allows refreshing the grid.

It is possible to sort some columns by clicking on their title.

This grid consists of the following columns:

* **Id**: displays the ID property of the action.
* **Name**: displays the name property of the action.
* **Description**: displays the description of the action.

### [See Also](#See+Also)

* [HowTo: Create an Action in the GXflow Client](https://wiki.genexus.com/commwiki/wiki?25737,,)
* [GXflow Menus](https://wiki.genexus.com/commwiki/wiki?25709)
* [GXflow Components](https://wiki.genexus.com/commwiki/wiki?25710)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [GXflow - Access Level property](https://wiki.genexus.com/commwiki/wiki?25723) | [GXflow Backend](https://wiki.genexus.com/commwiki/wiki?25704) |
| [GXflow Components](https://wiki.genexus.com/commwiki/wiki?25710) | [GXflow Menus](https://wiki.genexus.com/commwiki/wiki?25709) | [HowTo: Create a menu in GXflow Client](https://wiki.genexus.com/commwiki/wiki?25755) |
|

---
