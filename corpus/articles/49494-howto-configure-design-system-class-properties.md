---
title: "HowTo: Configure Design System Class Properties"
source_id: 49494
source_url: https://wiki.genexus.com/commwiki/wiki?49494
genexus_version: "18"
---

# HowTo: Configure Design System Class Properties

The [Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49323) allow you to customize and configure styles and behaviors in user interfaces.  
  
To make it easier to edit these Class Properties (CSS and gx-properties), the [Properties Editor](https://wiki.genexus.com/commwiki/wiki?3160) can be used.  
  
The Properties Editor greatly simplifies the design process by providing a smooth experience for viewing, filtering, and synchronously editing properties.

You can filter and configure properties according to a specific control type and a certain user interface. To do so, use the **Filter by ControlType** and the [Filter by UI](https://wiki.genexus.com/commwiki/wiki?55701)properties to select the filter you want, and the related properties will be shown.

`[imagen omitida: wiki id 55697]`

In addition, when you use the Properties Editor to set a certain property, that configuration is shown (refreshed) directly in the Styles section of the [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) for the corresponding property of the Class where the cursor is positioned. Likewise, when the cursor is positioned over a class in the Design System Styles section, and you edit a property value, the Properties Editor is automatically updated.

`[imagen omitida: wiki id 55685]`

The Properties Editor also provides information about property inheritance. This means that, for example, if a class A uses the [Include style rule](https://wiki.genexus.com/commwiki/wiki?49353) to incorporate the settings of class B, and class B defines a background color: red, when the cursor is over class A, the Properties Editor will display background color: red as the "default" property.

To illustrate the above, the following image shows two classes defined in the Styles section of a Design System object: "HighlightInfo" and "LabelHighlightInfo".

`[imagen omitida: wiki id 55699]`

In the "HighlightInfo" class, the following properties have been defined:

* "font-family"
* "font-size"
* "color"

The "LabelHighlightInfo" class contains these properties:

* "color"
* "font-weight"

The @Include rule is used to incorporate the settings of the "HighlightInfo" class. When the cursor is positioned over the "LabelHighlightInfo" class, the "font-family" and "font-size" properties configured in the "HighlightInfo" class are displayed in the Properties Editor.

### [Availability](#Availability)

This functionality is available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).

### [See Also](#See+Also)

[Design System Class Properties List File](https://wiki.genexus.com/commwiki/wiki?49527,,)


|  |
| --- |
| **Backlinks** |
| [Design System Class Properties](https://wiki.genexus.com/commwiki/wiki?49323) | [Design System Class Properties List (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55680) | [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |
| [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239) | [gx-datepicker-image-class property](https://wiki.genexus.com/commwiki/wiki?50630) | [gx-multimedia-upload-change-class property](https://wiki.genexus.com/commwiki/wiki?50634) | [gx-multimedia-upload-class property](https://wiki.genexus.com/commwiki/wiki?50632) |
| [gx-multimedia-upload-clear-class property](https://wiki.genexus.com/commwiki/wiki?50633) | [gx-multimedia-upload-empty-class property](https://wiki.genexus.com/commwiki/wiki?50635) | [gx-prompt-image-class property](https://wiki.genexus.com/commwiki/wiki?50631) |

---
