---
title: "Application Bar control in Native Mobile Applications"
source_id: 19486
source_url: https://wiki.genexus.com/commwiki/wiki?19486
genexus_version: "18"
---

# Application Bar control in Native Mobile Applications

The Application Bar is a common control included in all [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), and [Work With](https://wiki.genexus.com/commwiki/wiki?15974) objects.

It acts as a container of actions for the screen displayed to the end user.

## [Where can you find it?](#Where+can+you+find+it%3F)

For [Menu object](https://wiki.genexus.com/commwiki/wiki?16321)s, it is available in the Menu *node* of the working tree. In this particular case, the Application Bar cannot contain actions because its purpose is to display a title for the menu. Nevertheless, you can change the [Application Bars Class property](https://wiki.genexus.com/commwiki/wiki?37518) of the control and hide it by setting its [Show Application Bars property](https://wiki.genexus.com/commwiki/wiki?23305).

For [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s and [Work With](https://wiki.genexus.com/commwiki/wiki?15974) objects, the Layout tab includes a special zone at the top that allows you to customize the Application Bar. By clicking on it, you will be able to set properties associated with the object Application Bar.

`[imagen omitida: wiki id 37521]`

Note that the Application Bar section can contain buttons ([actions](https://wiki.genexus.com/commwiki/wiki?20623)) and by right-clicking on them you can insert more [Button control](https://wiki.genexus.com/commwiki/wiki?6011)s or [Action group controls](https://wiki.genexus.com/commwiki/wiki?25106). Also, they can be dragged from the toolbox once the Application Bar section is selected.

## [How can you customize actions?](#How+can+you+customize+actions%3F)

Actions on the Application Bar can be customized like the buttons on the layout that have a Button class, Image, Caption, and more. The default look & feel of the Application Bars depends on each platform.

* **Android devices**  
  Actions that fit in the Application Bar are displayed in the same order as in the GeneXus layout Application Bar, from left to right. Initially, you don't know which ones will fit; you only know their order. Those that are left out will be moved to an *overflow area* where low priority actions take place.
* **iOS devices**  
  The Application Bar's behavior depends on the priority of the actions and the order they appear on the Application Bar. High Priority actions are shown at the top or at the bottom depending on the type of device. On iPhone, if there is no standard action (insert, save, edit, logout, etc.) and there is a high priority action, it will be the first one to appear from left to right at the top of the Application Bar. On iPad, they will appear at the top, and if they don't fit the bottom side is used.

## [Properties](#Properties)

Both of them are located below the *Appearance properties group*.

* [Show Application Bars property](https://wiki.genexus.com/commwiki/wiki?23305)
* [Application Bars Class property](https://wiki.genexus.com/commwiki/wiki?37518)

## [Samples](#Samples)

Suppose you design the following layout.

`[imagen omitida: wiki id 37522]`

Also, consider the following configuration:

|  |  |
| --- | --- |
| **Action** | **Priority** |
| Insert | Hight |
| Delete All | Low |
| Refresh | High |
| Count | Normal |

The result on both platforms will be as follows:

**Android devices**  
`[imagen omitida: wiki id 37523]`  
`[imagen omitida: wiki id 37528]`

**iOS devices**  
`[imagen omitida: wiki id 37524]`  
`[imagen omitida: wiki id 37529]`

### [See Also](#See+Also)

* [Action Group Control for Panels](https://wiki.genexus.com/commwiki/wiki?25106)
* [Large Title Mode property](https://wiki.genexus.com/commwiki/wiki?40345)


|  |
| --- |
| **Backlinks** |
| [Action Group Control for Panels](https://wiki.genexus.com/commwiki/wiki?25106) |
| [Application Bars Class property](https://wiki.genexus.com/commwiki/wiki?37518) | [ApplicationBars Theme Class](https://wiki.genexus.com/commwiki/wiki?17879) | [ApplicationBars Theme Class (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56454) | [Calls to Elements in Work Withs from Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17160) |
| [DesignOps - Conventions](https://wiki.genexus.com/commwiki/wiki?46872) | [Enable Header Row Pattern property](https://wiki.genexus.com/commwiki/wiki?29843) | [Expand Bounds Limit property](https://wiki.genexus.com/commwiki/wiki?37137) |
| [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) | [Getting Started with tvOS](https://wiki.genexus.com/commwiki/wiki?40787) | [HowTo: Use the Cancel Method from Actions in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?18363) | [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
