---
title: "What is a Master Page"
source_id: 17088
source_url: https://wiki.genexus.com/commwiki/wiki?17088
genexus_version: "18"
---

# What is a Master Page

A Master Page is a panel that defines the layout and behavior common to the referenced application UI screens.

In other words, it specifies the framework or context and the behavior of the application UI screens that reference it.

`[imagen omitida: wiki id 43313]`

### [Benefits offered by Master Pages](#Benefits+offered+by+Master+Pages)

* Centralize the design of your application, providing coherence and consistency.
* Less Coding.
* Better Performance (less generated code).
* Incremental Development (just changing a Master Page changes all the application UI screens that reference it).

### [Restrictions](#Restrictions)

* Each Master Page can include only one Content Placeholder control (otherwise, when saving the following error will be displayed: "Error: Only one Content Placeholder control is allowed").
* A Master Page can't contain a [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) (otherwise, at specification time the following message will be displayed: "spc0092: Master Pages do not support the parm() rule").
* A Master Page cannot be Main (the [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) disappears for Master Pages).
* You can't call a Master Page from another object like from any GeneXus object (otherwise, at specification time the following message will be displayed: "spc0008 Events(6): Call to program Master Web Panel that cannot be generated."). To assign a Master Page, you have to set a property of an object with UI with the name of the desired Master Page.

### [Compatibility](#Compatibility+)

Since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,) the Master Page concept was divided into two types of objects:

* [Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348): It can be assigned to Web objects.
* [Master Panel object](https://wiki.genexus.com/commwiki/wiki?46247): It can be assigned to [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s.


|  |
| --- |
| **Backlinks** |
| [Design System Class Properties List (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55680) |
| [Design System Object - Design abstractions for your screens](https://wiki.genexus.com/commwiki/wiki?48681) | [Design System Object - Design and Behavior Abstractions](https://wiki.genexus.com/commwiki/wiki?48930) | [How to convert my application to make it responsive](https://wiki.genexus.com/commwiki/wiki?25214) | [How to create a dynamic menu for WEB applications](https://wiki.genexus.com/commwiki/wiki?33589) |
| [HowTo: Use an external CSS file on a Web Panel](https://wiki.genexus.com/commwiki/wiki?24387) | [Prompts Master Page property](https://wiki.genexus.com/commwiki/wiki?51714) | [Security considerations in Smooth models](https://wiki.genexus.com/commwiki/wiki?25356) | [Category:Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348) |

---
