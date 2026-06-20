---
title: "HowTo: Customize Map visualization in QueryViewer control"
source_id: 48467
source_url: https://wiki.genexus.com/commwiki/wiki?48467
genexus_version: "18"
---

# HowTo: Customize Map visualization in QueryViewer control

The purpose of this article is to explain the necessary steps to customize Map visualization in QueryViewer control.

### [Step 1](#Step+1)

To customize how maps are displayed in the [QueryViewer control](https://wiki.genexus.com/commwiki/wiki?9075), you have to associate a class with it (below the Appearance group):

`[imagen omitida: wiki id 52507]`

### [Step 2](#Step+2)

Open the associated [Web Theme object](https://wiki.genexus.com/commwiki/wiki?6420):

`[imagen omitida: wiki id 48475]`

### [Step 3](#Step+3)

Select the class that matches the one associated with the QueryViewer control:

`[imagen omitida: wiki id 48476]`

Below the Map Specific group, you will find the properties that allow you to configure the desired user interface for the map:

`[imagen omitida: wiki id 48477]`

For example, you will see the *Selection Color* property and several groups of properties:

`[imagen omitida: wiki id 48478]`

* **Selection Color property**: Allows you to change the color of the selected area.

`[imagen omitida: wiki id 48497]`

**Example:** If you define the *Selection Color* property as follows:

`[imagen omitida: wiki id 48498]`

The map will be displayed as shown below:

`[imagen omitida: wiki id 48499]`

* **Background group**: Provides the *Color* and *Opacity* properties of the map’s background.

`[imagen omitida: wiki id 48479]`

**Example:** If you make these configurations:

`[imagen omitida: wiki id 48480]`

The map will be displayed as shown below:

`[imagen omitida: wiki id 48481]`

* **Title group**: Below *Font*, the following properties are available:

`[imagen omitida: wiki id 48482]`

**Example:** If you define the properties of the *Title* group as follows:

`[imagen omitida: wiki id 48483]`

The map will be displayed as shown below:

`[imagen omitida: wiki id 48484]`

* **Series group:**

  + The Box subgroup allows you to modify the Color, Opacity, Border color, and Border width properties of the box that will contain the label of the defined series.
  + The Text subgroup allows you to modify the properties related to the fonts of these labels. Properties include Font, Font Family, Font size, Font style, and Font weight. You can also modify the Foreground color property that allows you to change the color of the label text.

`[imagen omitida: wiki id 48485]`

**Example:** If you define the *Series* group as follows:

`[imagen omitida: wiki id 48486]`

The map will be displayed as shown below:

`[imagen omitida: wiki id 48487]`

* **Tooltip group**:

  + The *Box* subgroup allows you to modify the properties of the box that will contain the defined tooltip.
  + The *Text* subgroup allows you to modify the properties related to the tooltip fonts. The properties you can configure include *Font*, *Font Family*, *Font size*, *Font style,* and *Font weight*. In addition, within this subgroup you can also modify the *Foreground color* property that allows you to change the color of the tooltip text.

`[imagen omitida: wiki id 48488]`

**Example:** If you define the *Tooltip* subcategory as follows:

`[imagen omitida: wiki id 48490]`

The map’s tooltip will be displayed as shown below:

`[imagen omitida: wiki id 48491]`

* **Legend group**:

  + The *Box* group allows you to modify the properties of the box that will contain the corresponding map legend.
  + The *Text* subgroup allows you to modify the properties related to the legend fonts. Among the properties in this group are: *Font, Font Family, Font size, Font style, and Font weight*. You can also modify the *Foreground color* property that allows you to change the color of the legend text.

`[imagen omitida: wiki id 48489]`

**Example:** If you define the *Legend* subcategory as follows:

`[imagen omitida: wiki id 48495]`

The maps’s legend will be displayed as shown below:

`[imagen omitida: wiki id 48496]`

### [Availability](#Availability)

This customization in Maps is available since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).


|  |
| --- |
| **Backlinks** |
| [HowTo: Customize the QueryViewer control](https://wiki.genexus.com/commwiki/wiki?40026) | [Toc:Reporting in GeneXus](https://wiki.genexus.com/commwiki/wiki?25314) |

---
