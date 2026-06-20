---
title: "HowTo: Create a Dynamic Form"
source_id: 25857
source_url: https://wiki.genexus.com/commwiki/wiki?25857
genexus_version: "18"
---

# HowTo: Create a Dynamic Form

This article explains how to create a new and simple [GXflow Dynamic Forms](https://wiki.genexus.com/commwiki/wiki?25809) in [GXflow Client](https://wiki.genexus.com/commwiki/wiki?17835).

### [Step 1 - Run the GXflow Standard Client](#Step+1+-+Run+the+GXflow+Standard+Client)

First, open your GXflow Standard Client application. To do so, right-click on one of your [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486) and select Run:

`[imagen omitida: wiki id 52516]`

### [Step 2 - Log in and give permission to the user](#Step+2+-+Log+in+and+give+permission+to+the+user)

Log in with a user that has the GXflow Backend Administrator role and add the GXflow Form Designer role —see [GXflow Management Console](https://wiki.genexus.com/commwiki/wiki?9340) for details on how to manage users and roles. If no user has the GXflow Backend Administrator role, log in with the WFADMINISTRATOR user in order to set this role to any user. Then log in with that user.

**Note**: when using [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) the [GAM Backoffice](https://wiki.genexus.com/commwiki/wiki?15935) must be used in order to manage users, roles and permissions.

### [Step 3 - Open the Form Definitions component](#Step+3+-+Open+the+Form+Definitions+component)

Open the [GXflow Form Definitions](https://wiki.genexus.com/commwiki/wiki?25811) component by selecting it. It is located under the [GXflow Dynamic Forms](https://wiki.genexus.com/commwiki/wiki?25809) node. Once opened, the [GXflow Form Definitions](https://wiki.genexus.com/commwiki/wiki?25811) dialog should look as follows:

`[imagen omitida: wiki id 52517]`

### [Step 4 - Create a new Form Definition](#Step+4+-+Create+a+new+Form+Definition)

Press the "NEW" button and write the form name:

`[imagen omitida: wiki id 52518]`

**Note**: when using GAM a permission will be created once the Form Definition is created, using the GAM Prefix property value. The GAM Prefix property will be ignored when GAM is not used.

### [Step 5 - Add elements to the Form Definition](#Step+5+-+Add+elements+to+the+Form+Definition)

Next, you need to add some [GXflow Elements](https://wiki.genexus.com/commwiki/wiki?25812) to the newly created [Form Definition](https://wiki.genexus.com/commwiki/wiki?25811).

To do so, select it from the grid and press the "ELEMENTS" button. A dialog box will be displayed for you to add and delete elements from the form:

`[imagen omitida: wiki id 52519]`

In order to add an element, press the "NEW" button. When the button is pressed, the element creation dialog will be displayed; add a new element called "User Name" as follows:

`[imagen omitida: wiki id 52520]`

**Note**: see [GXflow Elements](https://wiki.genexus.com/commwiki/wiki?25812) for details about the properties of an element.

Add two new elements called "Password" and "Password Confirmation" as shown below:

`[imagen omitida: wiki id 52521]`

The last element to be added will be "User Age"; create this element as numeric using Length = 2 and Decimals = 0.

The layout should look as follows:

`[imagen omitida: wiki id 52522]`

Add a rule in order to check that the "User Age" is not under 18.

To do so, edit the "User Age" element by hovering the mouse over the element and pressing the "RULES" button. Then in the Rules tab, and press the "NEW" button. Add an "Error" rule as follows:

`[imagen omitida: wiki id 52523]`

Next, add a condition over the Rule; to do so, select the Rule from the grid and press "CONDITIONS" and then "NEW". Select the "User Age" element and create a condition as follows:

`[imagen omitida: wiki id 52524]`

### [Step 6 - Associate the Form Definition to a User Task](#Step+6+-+Associate+the+Form+Definition+to+a+User+Task)

Once the dynamic form is defined, you need to associate it with a [User Task](https://wiki.genexus.com/commwiki/wiki?17499). To do so, open your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) and create a new [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486), drag a user task to the diagram and set the [Application form property](https://wiki.genexus.com/commwiki/wiki?25827,,) of the user task to the newly created [Form Definition](https://wiki.genexus.com/commwiki/wiki?25853) as shown below:

`[imagen omitida: wiki id 52525]`

In order to set the newly created [Form Definition](https://wiki.genexus.com/commwiki/wiki?25853) to the user task: open the [Application form property](https://wiki.genexus.com/commwiki/wiki?25827,,) options by clicking on the "..." in it.  
Then press the "..." of the "Form" property and select "MyNewDynForm" as follows:

`[imagen omitida: wiki id 52526]``[imagen omitida: wiki id 52527]`

Once the [Form Definition](https://wiki.genexus.com/commwiki/wiki?25853) is set to the [Application form property](https://wiki.genexus.com/commwiki/wiki?25827,,) deploy your [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486) and execute the [GXflow Client](https://wiki.genexus.com/commwiki/wiki?17835)—running the newly created [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486) is enough.

### [Step 7 - Done!](#Step+7+-+Done%21)

Finally, test your form. To do so, Create a new Process Instance and execute it.

`[imagen omitida: wiki id 52528]`

### [See Also](#See+Also)

[GXflow Dynamic Forms](https://wiki.genexus.com/commwiki/wiki?25809)  
[GXflow Form Definitions](https://wiki.genexus.com/commwiki/wiki?25811)


|  |
| --- |
| **Backlinks** |
| [GXflow Dynamic Forms](https://wiki.genexus.com/commwiki/wiki?25809) |

---
