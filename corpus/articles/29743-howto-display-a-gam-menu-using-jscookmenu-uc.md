---
title: "HowTo: Display a GAM Menu using Jscookmenu UC"
source_id: 29743
source_url: https://wiki.genexus.com/commwiki/wiki?29743
genexus_version: "18"
---

# HowTo: Display a GAM Menu using Jscookmenu UC

If you need to include a Menu based on the [GAM Permissions](https://wiki.genexus.com/commwiki/wiki?15912) of the user in your application, the good news is that GAM dynamically creates the structure of the Menu with no need for any extra coding.

[GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) returns a Menu structure that can be displayed using any [User Control](https://wiki.genexus.com/commwiki/wiki?5273) that is appropriate for displaying a hierarchical structure.

To do so, follow the steps below:

### [Steps](#Steps)

**1.** Read [HowTo: Define a Menu using GAM](https://wiki.genexus.com/commwiki/wiki?29681) to create the Menu of your Web application.

**2.** After you have created the GAM Menu in step 1, you can display it using any appropriate User Control; for example, the [JScookMenu](https://marketplace.genexus.com/product.aspx?jscookmenu,en) could be a good choice. [Install](https://wiki.genexus.com/commwiki/wiki?5920) the JSCookMenu in your development machine and create a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) to include this User control in its form.

**3.** Enter the following code to populate the User Control with the Menu data returned by GAM.

```
Event Start   
    //&ApplicationGUID is the GUID of the GAM Application
    //&MenuGUID is the GUID of the Menu
    &MenuOptionList = GAMRepository.GetApplicationMenu(&ApplicationGUID,&MenuGUID, &Errors) //&MenuOptionList is 
//GAMMenuOptionList data type
    //The following data provider returns a collection of JSCookMenuItem given a GAMMenuOptionList collection
    &MenuDataCollection = TransformGAMMenuToJSCookMenu(&MenuOptionList.Nodes)
Endevent
```

`[imagen omitida: wiki id 29749]`

For more information about the GAM API for handling Menus, read [API for Menus](https://wiki.genexus.com/commwiki/wiki?29742).

**4.** The code of TransformGAMMenuToJSCookMenu is as follows:

```
JSCookMenuItem input &Menuitem in &Menu //&Menu is a collection of GAMMenuOptionList data type

{    
    Title = &Menuitem.Name
    Url = &Menuitem.Link
    Childs = TransformGAMMenuToJSCookMenu(&Menuitem.Nodes)        
}

parm(&Menu);
```

You can download the sample [here](https://wiki.genexus.com/commwiki/wiki?29746,,).

### [Using the TreeView User control](#Using+the+TreeView+User+control)

Following very similar steps, you can use the TreeView (which is distributed in the standard UCs toolbox) instead of the JSCookMenu.

You can download the TreeView sample [here](https://wiki.genexus.com/commwiki/wiki?29748,,).


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Define a Menu using GAM](https://wiki.genexus.com/commwiki/wiki?29681) |

---
