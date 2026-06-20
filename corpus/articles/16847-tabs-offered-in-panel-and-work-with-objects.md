---
title: "Tabs offered in Panel and Work With objects"
source_id: 16847
source_url: https://wiki.genexus.com/commwiki/wiki?16847
genexus_version: "18"
---

# Tabs offered in Panel and Work With objects

For each [Work With List Node](https://wiki.genexus.com/commwiki/wiki?15984), and [Work With Detail Node](https://wiki.genexus.com/commwiki/wiki?15985) defined in the [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) instance, a window is generated to the right containing five Selectors or Tabs.

`[imagen omitida: wiki id 52426]`

### [Layout tab](#Layout+tab)

Includes the attributes/variables among other controls that will be displayed and how they will be shown.

In the example above, the attributes *PropertyFrontImage and* *PropertyName* that belong to the Property [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) (handled by a [real estate agency](https://wiki.genexus.com/commwiki/wiki?23631,,)) are listed inside a grid control.

Although you can see only one layout at a time (e.g. the "*Any Platform, Default Orientation*" one) for the List node. Note the possibility to **Add** a new one, or **Delete** the current. This lets you design different layouts depending on the *Platform* (i.e. Android, iOS, Angular), the *Device Kind* (i.e. Phone, Tablet, Watch, TV), the *Size* (i.e. Phone, Tablet 7'', Tablet 10'') and/or the *Orientation* (i.e. Landscape, Portrait). For the [Work With Section Node](https://wiki.genexus.com/commwiki/wiki?20624) it also offers the *Mode* (i.e. View or Edit) to differentiate the layout displayed to insert, update or delete, from the layout displayed to just view the information.

### [Rules tab](#Rules+tab)

As the [Web Panel rules](https://wiki.genexus.com/commwiki/wiki?8288), specify some kind of behavior of the corresponding WW node (List, Detail or Sections).

Rules provide a generic language to enforce the controls in these programs.

`[imagen omitida: wiki id 36891]`

For example, specify the parameters received and/or returned by the node. Do not confuse the rules of the node, with the [rules of the Transaction](https://wiki.genexus.com/commwiki/wiki?16843), which will run when you insert, delete or modify the element corresponding to detail.

### [Events tab](#Events+tab)

The objective of Events is to provide behavior and interaction between clients and services. Note in the layout shown above the "Insert" button on the List node **Application Bar**. An 'Insert' event is automatically associated, calling the **Detail** node of that WW, in **Insert** mode:

`[imagen omitida: wiki id 52432]`

As usual, other events could be created. Examples of this could be an action to show the real estate properties on a map, an action to call certain data, an action to schedule items, and so on. The actions available on the User Interface usually have a graphic element associated with them, such as a button, an option in a global menu, a link, and so on.

In the [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974), the user can add actions in the [List node](https://wiki.genexus.com/commwiki/wiki?15984) and in the [Detail and Sections nodes](https://wiki.genexus.com/commwiki/wiki?15985). These actions can be placed on screen -besides associating them to controls- using the Application Bar of the pattern layouts.

In addition to the actions included by default ("Insert" Action for List, "Save", "Cancel", "Update" and "Delete" for Section), new actions can be defined.

The grammar of events running on the device has its peculiarities regarding the events that run on the server. This is due to the [architecture](https://wiki.genexus.com/commwiki/wiki?14981). For example, to invoke two or more objects within an event sequence, you have to use the [Composite command](https://wiki.genexus.com/commwiki/wiki?17389) inside an event executed on the client (device).

To go deeper into this topic: [Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042).

### [Conditions tab](#Conditions+tab)

This section allows the developer to specify free and global **conditions** over the whole object. This condition aims to filter the displayed data.

`[imagen omitida: wiki id 36893]`

For conditions and fine-grained searches over a specific grid, controls refer to [Orders and Filters in Grids of Panels](https://wiki.genexus.com/commwiki/wiki?24805).

### [Variables tab](#Variables+tab)

Displays every variable defined on the object (List, Detail, and Section are independent), including standard pre-defined variables ([Pgmdesc](https://wiki.genexus.com/commwiki/wiki?7672), [Pgmname](https://wiki.genexus.com/commwiki/wiki?8870), [Time](https://wiki.genexus.com/commwiki/wiki?8102), [Today](https://wiki.genexus.com/commwiki/wiki?8873) and [Mode](https://wiki.genexus.com/commwiki/wiki?31225) variable in Section node).

`[imagen omitida: wiki id 36899]`

## [Related information](#Related+information)

Relations among Transactions are also strictly generated in the Work With. Note the following Transactions:

`[imagen omitida: wiki id 36896]`

As you can see, the Neighborhood Transaction has a 1-N relation with the Property Transaction, that is, for one neighborhood there can be N properties.

So, when you select one neighborhood, the relations tab will be displayed on top of its properties.

`[imagen omitida: wiki id 52433]`

In the image above, the Coral Gables neighborhood was selected and the Level/Detail/Section (General)/View node was opened. Note that the General tab located in the upper section is selected. To the right is the Property tab, thus closing the relationships among entities. So, if you select the Property tab, you can access the list of all the properties of the selected neighborhood.

## [See Also](#See+Also)

[Composite examples](https://wiki.genexus.com/commwiki/wiki?15551)

## [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Container of sections in the Detail screen of the Work With](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/container-of-sections-in-the-detail-screen-of-the-work-with?p=3658)


|  |
| --- |
| **Backlinks** |
|
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Transaction Rules in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?16843) | [Work With Detail Node](https://wiki.genexus.com/commwiki/wiki?15985) | [Work With List Node](https://wiki.genexus.com/commwiki/wiki?15984) |
| [Work With Section Node](https://wiki.genexus.com/commwiki/wiki?20624) |

---
