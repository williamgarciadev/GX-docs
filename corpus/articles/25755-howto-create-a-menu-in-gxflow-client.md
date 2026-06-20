---
title: "HowTo: Create a menu in GXflow Client"
source_id: 25755
source_url: https://wiki.genexus.com/commwiki/wiki?25755
genexus_version: "18"
---

# HowTo: Create a menu in GXflow Client

This article explains how to create a new menu in [GXflow Client](https://wiki.genexus.com/commwiki/wiki?17835).

### [Step 1 - Run the GXflow Standard Client](#Step+1+-+Run+the+GXflow+Standard+Client)

First, open your GXflow Standard Client application. To do so, right-click on a [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486) and select Run:

`[imagen omitida: wiki id 52744]`

### [Step 2 - Login](#Step+2+-+Login)

Log in with a user that has the role GXflow Backend Administrator —see [GXflow Management Console](https://wiki.genexus.com/commwiki/wiki?9340) for details on how to manage users and roles— for example the WFADMINISTRATOR user.

**Note**: When using [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746), the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) must be used in order to manage users, roles and permissions.

### [Step 3 - Open the Menus component](#Step+3+-+Open+the+Menus+component)

Open the Menus component by selecting it —it is located under the [GXflow Backend](https://wiki.genexus.com/commwiki/wiki?25704) node.

`[imagen omitida: wiki id 52745]`

The [GXflow Menus](https://wiki.genexus.com/commwiki/wiki?25709) dialog will be opened.

### [Step 4 - Create a new Menu](#Step+4+-+Create+a+new+Menu)

Press the "NEW" button, and set the properties as follows:

`[imagen omitida: wiki id 52746]`

**Note**: When using GAM a permission will be created once the menu is created. The permission will be created with the name "{MENU\_ID}"; in this case: "MyMenu".

### [Step 5 - Add components to the Menu](#Step+5+-+Add+components+to+the+Menu)

Next, in order to use the newly created [GXflow Menu](https://wiki.genexus.com/commwiki/wiki?25709) you must add some components to it. For simplicity purposes, add to it some existing [GXflow Components](https://wiki.genexus.com/commwiki/wiki?25710).

To do so select the new menu and press the "COMPONENTS" button. A dialog will be displayed for you to select the component to be added or removed from the menu:

`[imagen omitida: wiki id 52747]`

**Note**: you can rearrange the components by selecting them and using the arrow buttons.

### [Step 6 - Done!](#Step+6+-+Done%21)

Lastly, test your menu. To do so, add permissions for the "MyMenu" menu to a role, and log in with a user that has permissions to use the newly created menu— for example use WFADMINISTRATOR. Then open it.

### [See Also](#See+Also)

[GXflow Backend](https://wiki.genexus.com/commwiki/wiki?25704)  
[GXflow Menus](https://wiki.genexus.com/commwiki/wiki?25709)  
[GXflow Components](https://wiki.genexus.com/commwiki/wiki?25710)  
[GXflow Actions](https://wiki.genexus.com/commwiki/wiki?25711)


|  |
| --- |
| **Backlinks** |
| [GXflow Backend](https://wiki.genexus.com/commwiki/wiki?25704) | [GXflow Menus](https://wiki.genexus.com/commwiki/wiki?25709) |

---
