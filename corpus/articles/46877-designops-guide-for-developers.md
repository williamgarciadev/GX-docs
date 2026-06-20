---
title: "DesignOps - Guide for developers"
source_id: 46877
source_url: https://wiki.genexus.com/commwiki/wiki?46877
genexus_version: "18"
---

# DesignOps - Guide for developers

This article aims to be a guide for those developers who start their application development by importing a design file. Also, it provides tips and good practices.

In the early stages of a Design Integration cycle, it is recommended that you (as developer) start importing a design with just a few panels at a time. Following this mechanism, developers and designers can not only learn from each other but they can also see how the application starts growing. On the other hand, while a developer starts coding the designer can start drawing a new panel for the next iteration, repeating this cycle until you have a fully functional application.

Remember that you (as a developer) have a powerful tool for inspecting the UI at runtime: [Live Editing](https://wiki.genexus.com/commwiki/wiki?27805). This tool will help you to find design mismatches that you can easily fix for achieving a great looking app. Also, do not forget to check the [Native Mobile Applications Prototyping](https://wiki.genexus.com/commwiki/wiki?20538) article in case you desire to import a mobile design.

## [Understanding Design Elements](#Understanding+Design+Elements)

The Import Design tool can identify and interpret elements in the design file as the objects listed below. Take into account that for achiving a good-looking result the designer should have followed the guidelines provided in the [guide for designers](https://wiki.genexus.com/commwiki/wiki?46871), [conventions](https://wiki.genexus.com/commwiki/wiki?46872), and [best practices](https://wiki.genexus.com/commwiki/wiki?46874).

### [Stencils](#Stencils)

[Stencil objects](https://wiki.genexus.com/commwiki/wiki?38418) are generated from [Symbols / Components](https://wiki.genexus.com/commwiki/wiki?46871) defined by the designer.

Remember that these objects aim to be reusable in multiple panels, so check if you can identify components in your application that should be reusable, and tell your designer to make a new Symbol. Also, check if their instances are correctly applied (overridden values, theme-class applied, etc.) -- you can find those instances by looking at the [References](https://wiki.genexus.com/commwiki/wiki?24910) of the target stencil.

### [Panels](#Panels)

[Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s or [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)s are generated from [Artboards / Top-Level Frames](https://wiki.genexus.com/commwiki/wiki?46871) defined by the designer depending on whether you checked the [Import as Web Panel option](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46882,,) or not.

The Layout tab of these objects will be generated from those Groups that the designer defined, and controls will be generated through the [conventions](https://wiki.genexus.com/commwiki/wiki?46872) applied. In every table, the cell sizes (width/height, absolute or relative) and positions will be generated from [Resizing Constraints](https://wiki.genexus.com/commwiki/wiki?46871) defined by the designer. Take this into account when importing in case the designer forgot to apply some rules in the design for achieving a good result. Also, if the designer [has linked its panels](https://wiki.genexus.com/commwiki/wiki?46871), the Code tab will have the corresponding Call event, and a [Form Enter/Exit effect transition](https://wiki.genexus.com/commwiki/wiki?20961) is applied if the designer included animations.

### [Images](#Images)

[Image objects](https://wiki.genexus.com/commwiki/wiki?23387) are generated from the [images included in the design](https://wiki.genexus.com/commwiki/wiki?46871) (and preserving their internal name, usually a GUID-like string) and also from the layers marked as 'Exportable' (e.g. logos drawn by the designer). These images should have been exported by the designer with the correct densities (1x, 2x, 3x, etc.) in order to display them correctly in the target platform; otherwise, a black image is displayed as a placeholder.

### [Fonts](#Fonts)

A set of [File objects](https://wiki.genexus.com/commwiki/wiki?5852) (.otf, .ttf) will be generated for all [embedded Fonts](https://wiki.genexus.com/commwiki/wiki?46871) in the design file. Then, those Files will be referenced as [@font-face rule](https://wiki.genexus.com/commwiki/wiki?49338) in the [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) section. Finally, set them in the corresponding theme-class (the [Class property](https://wiki.genexus.com/commwiki/wiki?8741) value of the target control).

### [Design System Colors](#Design+System+Colors)

A #color group will be generated in the [Design System Tokens](https://wiki.genexus.com/commwiki/wiki?47378) section and will include those colors defined by the designer as [Sytles](https://wiki.genexus.com/commwiki/wiki?46871), especially as *Fill*, *Border*, or *Text* styles (every color will be suffixed with one of these three categories), and also will include every color defined as [Colors Variable / Style](https://wiki.genexus.com/commwiki/wiki?46871) in your design.

### [Design System Styles](#Design+System+Styles)

A set of style-classes will be generated in the [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) section. Every control will have its own style-class unless the designer has defined [Styles](https://wiki.genexus.com/commwiki/wiki?46871) for it. In case you reimport a design file, remember that the properties will be overridden if you modified them by hand.

Each style-class will inherit from a parent prefixed with a "ExternalDesign" string. For example, if GeneXus infers the style-class of a Variable, it will generate a theme-class of an Attribute class that inherits from a "ExternalDesignAttribute" class (similarly to other theme-class categories).

## [Workflow Strategies](#Workflow+Strategies)

Depending on your project requirements, you can adopt different strategies when using the Import Design tool (or even hybrid strategies) taking into account their pros/cons and considerations.

### [Designing the Complete App](#Designing+the+Complete+App)

In this approach, the designer defines each main frame of your app along with its elements, ready for import. While this process may take time iterating with your designer to achieve the best result, it ensures that the front end is fully prepared, leaving no room for ambiguity during development.

### [Iterative App Design](#Iterative+App+Design)

Similar to the previous approach, but with shorter exchange cycles with development. Keep in mind that the Import Design tool will override objects without merging. In that terms, it is highly recommended to import a new iteration of a design in a predefined module for that purpose (using the [Module option](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46882,,)) and then manually merge it into the main branch. Evaluate iterations carefully and consider manual adjustments to avoid a new import if that implies minor changes.

### [Defining App Components](#Defining+App+Components)

Focus on defining individual components such as icons, buttons, and cards. Create a Main Frame containing instances of these components as a reference for developers, and provide clear instructions to follow on how every component should behave (e.g. when focusing, hovering, etc.). Be aware of any known limitation (described in [FAQ and Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46880) section) and try alternatives when something cannot be modeled as you design it.

## [Availability](#Availability)

These sections apply as of [GeneXus 17](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46873,,).

* As of [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46852,,):  
  - Color Variables are supported.
* As of [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48684,,):  
  - Design System object is the default style object.

## [See also](#See+also)

* [Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871)
* [Conventions](https://wiki.genexus.com/commwiki/wiki?46872)
* [Live Editing](https://wiki.genexus.com/commwiki/wiki?27805)
* [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974)


|  |
| --- |
| **Backlinks** |
| [Design Import option (GeneXus 18 latest upgrade or prior)](https://wiki.genexus.com/commwiki/wiki?59501) | [Design Import option (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55439) |
| [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [DesignOps - Other samples](https://wiki.genexus.com/commwiki/wiki?47103) | [DesignOps - Sample - Home Decor](https://wiki.genexus.com/commwiki/wiki?50970) | [DesignOps - Sample - Travel Agency mobile front-end](https://wiki.genexus.com/commwiki/wiki?47029) |
| [DesignOps - Sample - Travel Agency web back-office](https://wiki.genexus.com/commwiki/wiki?47052) | [DesignOps - Sample - Travel Agency web front-end](https://wiki.genexus.com/commwiki/wiki?49441) | [Table of contents:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) | [GXML (GeneXus Markup Language) (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55385) |

---
