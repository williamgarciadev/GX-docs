---
title: "Web Component object"
source_id: 1864
source_url: https://wiki.genexus.com/commwiki/wiki?1864
genexus_version: "18"
---

# Web Component object

Defines a reusable Web Panel that can be embedded inside another Web Panel or Master Page or can be executed independently.

### [Description](#Description)

A Web Component is a web object that can be executed independently (like any other web object), or it can be part of another web object. This gives you a high degree of reusability.

The most common examples of use are menus, logins, customization areas, and so on. For example, instead of defining the menu load in every web object that uses it, the idea is to develop it in a Web Component and reuse it in every object that requires a menu.

You have two ways to create a Web Component:

1) By selecting in the main GeneXus menu [File > New Object](https://wiki.genexus.com/commwiki/wiki?9931), the [New Object Dialog](https://wiki.genexus.com/commwiki/wiki?1866) is opened. There, you have to select the Web category, and you are offered to create a Web Component.

2) By selecting the in the main GeneXus menu [File > New Object](https://wiki.genexus.com/commwiki/wiki?9931), and after that, by creating a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) or a [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) and setting their [Type property](https://wiki.genexus.com/commwiki/wiki?10444) with the **Component** value.

After having the Web Component defined, in order to use it inside another web object form, you have to insert a [Web Component control](https://wiki.genexus.com/commwiki/wiki?31172) over the desired web object form and set the corresponding [Web Component Control Properties](https://wiki.genexus.com/commwiki/wiki?10044).

### See also

[Type property (in Web Panels and Transactions)](https://wiki.genexus.com/commwiki/wiki?10444)
