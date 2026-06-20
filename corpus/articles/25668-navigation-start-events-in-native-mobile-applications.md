---
title: "Navigation Start Events in Native Mobile Applications"
source_id: 25668
source_url: https://wiki.genexus.com/commwiki/wiki?25668
genexus_version: "18"
---

# Navigation Start Events in Native Mobile Applications

One of the most important aspects of GeneXus is the possibility to build multi-platform applications in order to achieve a variety of features.

For example, the possibility to define different types of navigation depending on the platform where the application is running. To define this, you can configure the [Navigation Style property](https://wiki.genexus.com/commwiki/wiki?16229).

To add even more flexibility, GeneXus offers the **Navigation Start Events** to initialize the different layouts displayed when the application starts running, depending on the [Navigation Style property](https://wiki.genexus.com/commwiki/wiki?16229) set for that platform.

|  |  |
| --- | --- |
| **[Slide.Start](https://wiki.genexus.com/commwiki/wiki?25585)** | This event is executed when the Navigation Style selected is Slide, for the Platform where the application is running. |
| **[Split.Start](https://wiki.genexus.com/commwiki/wiki?25586)** | This event is executed when the Navigation Style selected is Split, for the Platform where the application is running. |
| **[Cascade.Start](https://wiki.genexus.com/commwiki/wiki?25587)** | This event is executed when the Navigation Style selected is Cascade, for the Platform where the application is running. |
| **[Flip.Start](https://wiki.genexus.com/commwiki/wiki?25571)** | This event will be executed if the Navigation Style selected is Flip, for the Platform where the application is running. |
| **[Tabs.Start](https://wiki.genexus.com/commwiki/wiki?25596)** | This event is executed when the [Control property](https://wiki.genexus.com/commwiki/wiki?55318) of the [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) is set to Tabs. |

### [Considerations](#Considerations)

* These Events only apply to [Main objects](https://wiki.genexus.com/commwiki/wiki?5770) of your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).
* It is important to note that in [Menu objects](https://wiki.genexus.com/commwiki/wiki?16321), when you have the [Control property](https://wiki.genexus.com/commwiki/wiki?55318) set to **Tabs**, the only Navigation Event executed is the [Tabs.Start event](https://wiki.genexus.com/commwiki/wiki?25596).

### [Samples](#Samples)

* When you need to display a **Welcome** Panel.
* When the [Navigation Style property](https://wiki.genexus.com/commwiki/wiki?16229) is set to Slide / Split, the corresponding Slide.Start Event / Split.Start Event (in a main Menu or Panel) allows you to set the right and left layouts to be displayed.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects:** | [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Menu](https://wiki.genexus.com/commwiki/wiki?16321) |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |


|  |
| --- |
| **Backlinks** |
| [Cascade.Start event](https://wiki.genexus.com/commwiki/wiki?25587) | [Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332) | [ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044) |
| [Flip.Start event](https://wiki.genexus.com/commwiki/wiki?25571) | [Flip.Start event (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55467) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [Navigation Style property](https://wiki.genexus.com/commwiki/wiki?16229) | [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076) | [Slide.Start event](https://wiki.genexus.com/commwiki/wiki?25585) | [Split.Start event](https://wiki.genexus.com/commwiki/wiki?25586) |
| [Tabs.Start event](https://wiki.genexus.com/commwiki/wiki?25596) |

---
