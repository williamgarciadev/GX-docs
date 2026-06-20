---
title: "DesignOps - Guide for designers"
source_id: 46871
source_url: https://wiki.genexus.com/commwiki/wiki?46871
genexus_version: "18"
---

# DesignOps - Guide for designers

This article aims to be a guide for designers in order to understand how GeneXus will interpret what you draw when designing an application.

**Note**: Before reading the article, you must know that there are two main rules for achieving a good-looking application on the first try:  
**1. Keep your design simple.**  
**2. Be tidy when designing.**  
Adhering to these rules promotes a smooth collaboration, aligning designers and developers for an efficient workflow.

## [Symbols / Components](#Symbols+%2F+Components)

Used for reusing common elements in your design.

GeneXus will interpret these elements of your design as [Stencil objects](https://wiki.genexus.com/commwiki/wiki?38418), and they will be named as they were named in your design. These objects will be organized within a "Stencils" folder in the Knowledge Base.

**Related readings:**  
[Sketch Symbols](https://www.sketch.com/docs/symbols/), [Figma Components](https://help.figma.com/hc/en-us/sections/4403935997847-Components).

**Notes:**

* If the element name contains slashes ("/"), GeneXus will interpret the last segment as the stencil’s name, while the preceding segments will form a nested folder structure to represent the hierarchy suggested by the slashes
* Following the previous point, when two or more elements share the same final segment, GeneXus will automatically add a numeric suffix to each duplicated object name to prevent naming conflicts.
  + For example, if you have a symbol or component named "Cards/Product" and another named "Cards/Small/Product," GeneXus will create a stencil named Product under *Stencils > Cards* and another named Product1 under *Stencils > Cards > Small*.
  + To avoid enumeration, consider adjusting the symbol or component names. For instance, naming them "Cards/Product" and "Cards/ProductSmall" will generate Product and ProductSmall stencils both within the *Stencils > Cards* folder

## [Artboards / Top-Level Frames](#Artboards+%2F+Top-Level+Frames)

Define the area where a designer will draw every panel of the application.

GeneXus will interpret these elements of your design as [Panel objects](https://wiki.genexus.com/commwiki/wiki?24829) (if it is a mobile application) or [Web Panel objects](https://wiki.genexus.com/commwiki/wiki?6916) (if it is a web application), and they will be named as they were named in your design preceded by a "View" prefix.

**Related readings:**  
[Sketch Artboards](https://www.sketch.com/docs/designing/the-interface/the-canvas/#how-to-use-artboards), [Figma Top-Level Frames](https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma#Top-level_frames).

## [Links / Interactions](#Links+%2F+Interactions)

Allow the designer to define how the Artboards are related between them, including animations.

GeneXus will interpret these Links between Artboards as [Calls](https://wiki.genexus.com/commwiki/wiki?16224) between Panels or as a [Return command](https://wiki.genexus.com/commwiki/wiki?31353) in case of Back-Links, including a [Form Enter/Exit effect transition](https://wiki.genexus.com/commwiki/wiki?20961) when it has been set.

**Related readings:**  
[Sketch Links](https://www.sketch.com/docs/prototyping/), [Figma Interactions](https://help.figma.com/hc/en-us/articles/360040315773-Prototype-interactions-and-animations).

**Notes:**

* These interactions are modeled in GeneXus through the Event of the control that represents the layer with the link.
* Remember to avoid loops when designing the interaction through links between artboards.
* Animations are not supported for Figma files.

## [Group / Frames](#Group+%2F+Frames)

Allows the designer to organize and structure the design elements.

GeneXus will interpret these container elements in your design as a [Table control](https://wiki.genexus.com/commwiki/wiki?6001) when the contained elements are disjoint and can be positioned in a cell. On the other hand, when the elements overlap, GeneXus will interpret the container as a [Canvas control](https://wiki.genexus.com/commwiki/wiki?22452). Additionally, since containers can represent semantic structures (such as grids, buttons, check-boxes, combo-boxes, radio-buttons, etc.), GeneXus requires a [Convention](https://wiki.genexus.com/commwiki/wiki?46872) to interpret the appropriate control.

**Related readings:**  
[Sketch Grouping Layers](https://www.sketch.com/docs/designing/layer-basics/grouping-layers/), [Sketch Smart Layout](https://www.sketch.com/docs/designing/smart-layout/), [Figma Frames](https://help.figma.com/hc/en-us/articles/360041539473-Frames-in-Figma), [Figma Group vs Frame](https://help.figma.com/hc/en-us/articles/360039832054-The-difference-between-frames-and-groups), [Figma Autolayout](https://help.figma.com/hc/en-us/articles/5731482952599-Using-auto-layout).

## [Images](#Images)

Images, as every designer knows, are resources of vital importance in any application to easily improve the user experience and captivate your audience. Also, there could be complex controls (like calendars) or drawings (like icons) that should be marked as Exportable in order to generate an image for them, and then the developer can easily integrate the real control into the application.

GeneXus will interpret both of these resources as [Image objects](https://wiki.genexus.com/commwiki/wiki?23387) that will be stored in the Knowledge Base and they will be loaded in the target panel as:

* A [Variable definition](https://wiki.genexus.com/commwiki/wiki?7375) based on the [Image data type](https://wiki.genexus.com/commwiki/wiki?15204) (by default)
* An [Image control](https://wiki.genexus.com/commwiki/wiki?5939) if the image was defined by the [Static convention](https://wiki.genexus.com/commwiki/wiki?46872) in your design
* A background-image reference in the style class of the [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) if the image fits its container

**Related readings:**  
[Sketch Images](https://www.sketch.com/docs/images/), [Sketch Exportable Layer](https://www.sketch.com/docs/exporting/), [Figma Images](https://help.figma.com/hc/en-us/articles/360040028034-Add-images-to-design-files), [Figma Exportable Layer](https://help.figma.com/hc/en-us/articles/360040028114).

**Notes:**

* GeneXus supports .png, .jpg, .jpeg, .gif, and .svg image formats.
* Those layers exported as images for PNG/JPEG formats require at least 1x resolution for Android and Apple apps, or SVG for Web and Angular apps
* There is no need to download or package the exported images; you just have to mark them as Exportables (with their format and densiities) and GeneXus will do the rest
* In case you want an image variable definition that fits its container but you do not want it to be a background-image reference (static behavior), you have to create a group/frame with just that image
* The definitions of inner layers within a layer marked as Exportable will be ignored as they are contained in a container that will be treated as an inmutable Image object
* When [Symbols / Components](https://wiki.genexus.com/commwiki/wiki?46871) are marked as Exportable, the master is treated as an inmutable Image object. In consequence:  
  1. Their instances do not need to be marked as Exportable  
  2. The overrides in their instances will be ignored

## [Texts](#Texts)

Texts, as every designer knows, are fundamental elements in any design for the simple fact that they communicate information to the end-user, not only through the content itself but also in the way the information is presented, involving sizes, colors, distribution, typography, casing, anchoring (responsive behavior), etc. What's more, in order to reuse that 'pieces' of visual information you want to convey, it is highly recommended that you use text-styles.

GeneXus will interpret texts as Variables based on the [VarChar data type](https://wiki.genexus.com/commwiki/wiki?6778) that the developer can change if necessary. However, if the text layer is defined with the [Static convention](https://wiki.genexus.com/commwiki/wiki?46872), the text will be interpreted as a [Text Block control](https://wiki.genexus.com/commwiki/wiki?5948). On the other hand, every text will define a style-class in the [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) section unless you define Text Styles, in which case those text-layers that share the same Text Style will also share the same [Class property](https://wiki.genexus.com/commwiki/wiki?8741) value (i.e. same style-class). If your Text Style defines a color, it will be added to the #color group in the [Design System Tokens](https://wiki.genexus.com/commwiki/wiki?47378) section and referenced by the target style-class.

Also, if your text has custom fonts, GeneXus will import them as [File objects](https://wiki.genexus.com/commwiki/wiki?5852), include them in the [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) section as a [@font-face rule](https://wiki.genexus.com/commwiki/wiki?47472), and set them in the corresponding style-class.

**Related readings**:  
[Sketch Text Layer](https://www.sketch.com/docs/text/), [Sketch Text Styles](https://www.sketch.com/docs/styling/#text-styles), [Figma Text Layer](https://help.figma.com/hc/en-us/articles/360039956474), [Figma Text Style](https://help.figma.com/hc/en-us/articles/360039957034).

**Notes:**

* GeneXus support .ttf, .otf, .eot, and .woff font file formats.  
  If your design has .ttc or .otc font files, refer to [DesignOps - FAQ and Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46880).
* Ensure you provide sufficient horizontal and vertical space for the text-box when content may vary in length or size.

## [Styles](#Styles)

Styles are meant to be a way to reuse visual design, distinguishing two categories: Text Styles (described in the previous section) and Layer Styles. For this last category, a designer is able to define Fills and Border styles.

GeneXus will interpret Text and Layer Styles as style classes in the [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) section.

**Related readings:**  
[Sketch Styles](https://www.sketch.com/docs/styling/), [Figma Styles](https://help.figma.com/hc/en-us/articles/360039238753-Styles-in-Figma).

## [Colors](#Colors)

Colors aim to define a color scheme for your design. As you may know, colors can contribute to how your design is perceived by humans, helping them to understand better the application and how to interact with it.

GeneXus will interpret Colors Styles as elements of the #color group in the [Design System Tokens](https://wiki.genexus.com/commwiki/wiki?47378) section, which will be referenced by the target style classes defined in the [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379). On the other hand, raw color definitions (using the hex representation) will be preserved as-is within the [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) linked to the layer.

**Related readings:**  
[Sketch Color Variables](https://www.sketch.com/docs/styling/#color-variables), [Figma Color Paints](https://help.figma.com/hc/en-us/articles/360038746534#Colors_paints).

**Notes:**

* The interpretation of Fill Color varies based on the layer type:  
  - Frame layers and Rectangle shapes will define the background-color.  
  - Text layers will define the font color.

## [Responsive](#Responsive)

Resizing Constraint is a vital feature for manipulating responsiveness in your design. Take into account that your application may run on devices of different sizes and resolutions. So, use fixed sizes when your layer must not grow or shrink, and pin-to-edge those elements that must not change their position.

GeneXus will interpret Resizing Constraints when it generates the [Table control](https://wiki.genexus.com/commwiki/wiki?6001) that will contain the controls the designer has drawn. Every control will be placed in a cell in the Table that will have a relative (%) or absolute (dips/px) size and position depending on the constraint you set. In case you overlap controls, GeneXus will generate a [Canvas control](https://wiki.genexus.com/commwiki/wiki?22452) instead but it also applies a [Z-Order property](https://wiki.genexus.com/commwiki/wiki?22510) in order to define the overlapping order.

**Related readings:**  
[Sketch Resizing Constraints](https://www.sketch.com/docs/layer-basics/#resizing-constraints), [Figma Constraints](https://help.figma.com/hc/en-us/articles/360039957734-Apply-constraints-to-define-how-layers-resize), [Figma Auto-Layout Resizing](https://help.figma.com/hc/en-us/articles/360040451373-Create-dynamic-designs-with-auto-layout#resizing).

**Notes:**

* When the group/frame is defined as a table and the contained element has anchors, the remaining space between the cell and the control itself will be defined as margins.

## [Fix position when scrolling](#Fix+position+when+scrolling)

Fix position when scrolling is a design property that allows you to lock an object's position and make sure it stays in the same location, even as you scroll. For example, header, footer or floating button.

GeneXus will interpret every element of your design that have checked the Fix position when scrolling property as part of the MainTable (set as a Canvas control). The elements that do not have this property marked will be part of Table control (whose Control Name property will have the "Scrollable" suffix).

In Mobile, the Table containing the elements without Fix position when scrolling has the properties [Auto Grow property](https://wiki.genexus.com/commwiki/wiki?20204) in False and [Overflow Behavior property](https://wiki.genexus.com/commwiki/wiki?46288) with Add Scroll value.

In Web, the style of the elements with Fix position when scrolling defined in the [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) have set 'position: absolute' and their respective location/sizes in the top, left, bottom, right, width and height properties.

**Related readings:**  
[Creating fixed elements in Sketch](https://www.sketch.com/docs/prototyping/creating-fixed-elements/), [Creating fixed objects in Figma](https://help.figma.com/hc/en-us/articles/360039818734-Prototype-scrolling-with-overflow-behavior#Create_fixed_objects_in_a_prototype).

**Notes:**

* If the elements with Fix position when scrolling unchecked are overlapped, then the scrollable Table (whose Control Name property has "Scrollable" suffix) necessarily becomes a Canvas and a Table wrap is made over the Canvas.
* Avoid applying for the Fix position when scrolling property to symbols/components. The position is defined with respect to the symbol and not with respect to the Artboard (or Top-Level Frame) where it is instantiated.

## [Availability](#Availability)

These sections apply as of [GeneXus 17](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46873,,).

* As of [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46852,,):  
  - Color Variables are supported.
* As of [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49956,,):  
  - Fix position when scrolling property is supported.

## [See Also](#See+Also)

[Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877)


|  |
| --- |
| **Backlinks** |
| [Design Import option (GeneXus 18 latest upgrade or prior)](https://wiki.genexus.com/commwiki/wiki?59501) | [Design Import option (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55439) |
| [DesignOps - Best practices for designers](https://wiki.genexus.com/commwiki/wiki?46874) | [DesignOps - Conventions](https://wiki.genexus.com/commwiki/wiki?46872) | [DesignOps - Conventions (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55465) | [DesignOps - Conventions - Multiple Layouts](https://wiki.genexus.com/commwiki/wiki?48697) |
| [DesignOps - Export design - Figma](https://wiki.genexus.com/commwiki/wiki?50578) | [DesignOps - Export design - Sketch](https://wiki.genexus.com/commwiki/wiki?46875) | [DesignOps - FAQ and Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46880) | [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) |
| [DesignOps - Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877) | [DesignOps - Other samples](https://wiki.genexus.com/commwiki/wiki?47103) | [DesignOps - Overview](https://wiki.genexus.com/commwiki/wiki?47020) | [DesignOps - Sample - Home Decor](https://wiki.genexus.com/commwiki/wiki?50970) |
| [DesignOps - Sample - Travel Agency mobile front-end](https://wiki.genexus.com/commwiki/wiki?47029) | [DesignOps - Sample - Travel Agency web back-office](https://wiki.genexus.com/commwiki/wiki?47052) | [DesignOps - Sample - Travel Agency web front-end](https://wiki.genexus.com/commwiki/wiki?49441) | [Table of contents:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) |
| [GXML (GeneXus Markup Language) (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55385) |

---
