---
title: "DesignOps - Sample - Home Decor"
source_id: 50970
source_url: https://wiki.genexus.com/commwiki/wiki?50970
genexus_version: "18"
---

# DesignOps - Sample - Home Decor

This article is about a design file for a Home Deco mobile front end made with the [Figma design tool](https://www.figma.com/).  
The example presents a mobile design for a simple e-commerce application.

## [Sample resource](#Sample+resource)

`[imagen omitida: wiki id 40856]` [Home Decor](https://www.figma.com/community/file/1136023550177073361)

First, save a local copy to your Figma account as follows:

1. Open the Plant Care sample provided (you have a read-only view).
2. Click on the "Open in Figma" button. This action will create a copy of the sample in your drafts.
3. Next, follow the instructions of [HowTo: Export a Figma design](https://wiki.genexus.com/commwiki/wiki?50578) with your local copy.

## [Importing Figma file](#Importing+Figma+file)

Basically, you must follow the instructions described in the [Design Import option](https://wiki.genexus.com/commwiki/wiki?46882) article.

Once you paste your Figma URL in the File field of the Design Import option, you can start the inspection process by clicking on the Load button (it will ask you for the Figma Token). After processing every file retrieved from Figma, the Design Import dialog will display a preview as follows:

|  |
| --- |
|  |

You can inspect every node in the left-side tree. Every type of node will show context information; for example, preview (image and layout tree) and GXML code in case of Panels; only GXML code in case of a Design System for describing tokens and styles; a preview for Images and Fonts, etc. Also, you can select/unselect the nodes depending on whether or not you want to import them.

**Warning**: When you select/unselect nodes, there is no dependency check between nodes. So, for example, if you unselect a node, make sure there is no dependency with another node (for example, an image used in a panel). Otherwise, some import errors may occur.

Once the import has finished, check the generated panels and how they look. Also, check the tokens/styles in the Design System object, Image objects, and File objects (fonts) imported.

Finally, if you agree with the objects to be generated, you can click on the OK button and start importing the design into the Knowledge Base.

## [Runtime execution](#Runtime+execution)

Lastly, run the generated Main menu object to view the generated panels.

**Warning**: Do not expect it to be perfect. It is highly likely that you or your designer will have to fix something in the design file or the generated objects (abstract layout or style-classes).

Here is a preview of all three panels, showing how they were designed (Top-Level Frame column) and how they look at runtime without making any changes (Android/iOS columns).

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Designer** | | **Developer** | | |
| **Figma** | **Main-Frame** | **GeneXus** | **Android** | **iOS** |
| *Home Decor* |  | *ViewHomeDecor* |  |  |
| *Category Page Decor* |  | *ViewCategoryPageDecor* |  |  |
| *Product Page Decor* |  | *ViewProductPageDecor* |  |  |

You may notice a few differences between the design and how it looks at runtime, but you as a developer can make adjustments and achieve a perfect result.

Anyway, all panels were almost perfect on the first try!

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators** | Android, Apple |

## [See also](#See+also)

* [Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871)
* [Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877)
* [Export design from Figma](https://wiki.genexus.com/commwiki/wiki?50578)
* [Keep improving your Design Workflow with the new Import from Figma (Webinar)](https://wiki.genexus.com/commwiki/wiki?46881,,)

## [Availability](#Availability)

This sample has been made for [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?49971,,) and above.


|  |
| --- |
| **Backlinks** |
| [Toc:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) | [Toc:GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | [GeneXus 18 Samples](https://wiki.genexus.com/commwiki/wiki?52693) |

---
