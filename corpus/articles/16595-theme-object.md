---
title: "Theme object"
source_id: 16595
source_url: https://wiki.genexus.com/commwiki/wiki?16595
genexus_version: "18"
---

# Theme object

Defines graphic and functional design of controls for applications.

### [Description](#Description)

When you use the [Native Mobile Generator](https://wiki.genexus.com/commwiki/wiki?14451) (for example, when creating or importing the first object related to a mobile app into your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)), the 'CarmineSD'Theme object is automatically imported with two child-themes: 'CarmineIOS' and 'CarmineAndroid'.

The 'CarmineIOS' and the 'CarmineAndroid' [Theme](https://wiki.genexus.com/commwiki/wiki?4375) are automatically assigned under the [Platforms node](https://wiki.genexus.com/commwiki/wiki?24284) to the "Any iOS" subnode and the "Any Android" subnode respectively (in their [Theme property](https://wiki.genexus.com/commwiki/wiki?48569,,)). Each specific iOS platform (iPad, iPhone, iPhone 3.5", etc.) inherits the Theme configured for the "Any iOS" node and each specific Android platform inherits the Theme configured for the "Any Android" node. You could change all those Themes, to get different looks and feels depending on the device type.

`[imagen omitida: wiki id 46611]`

There also exist two more Themes (backward-compatible) that can be imported and set: [SimpleAndroid](https://wiki.genexus.com/commwiki/wiki?18324) and [SimpleiOS](https://wiki.genexus.com/commwiki/wiki?18325,,).

You can create your own Theme object based on one of the existing, or new at all (all classes with its default value) by selecting in the main GeneXus menu [File > New Object](https://wiki.genexus.com/commwiki/wiki?9931).

The created Theme automatically will contain a group of predefined [classes](https://wiki.genexus.com/commwiki/wiki?6246) corresponding to GeneXus controls (and also, other elements).  
  
`[imagen omitida: wiki id 32518]`

### [Styles tab](#Styles+tab)

Displays every component of a Theme object in a tree-like interface.

* **Classes node**
  + [Animation](https://wiki.genexus.com/commwiki/wiki?37939) (1)
  + [Application](https://wiki.genexus.com/commwiki/wiki?30887)
  + [ApplicationBars](https://wiki.genexus.com/commwiki/wiki?17879)
  + [Attribute](https://wiki.genexus.com/commwiki/wiki?37646)
  + [AudioController](https://wiki.genexus.com/commwiki/wiki?31046)
  + [Button](https://wiki.genexus.com/commwiki/wiki?37647)
  + Calendar
  + [Form](https://wiki.genexus.com/commwiki/wiki?37648)
  + [Grid](https://wiki.genexus.com/commwiki/wiki?37657)
  + GridRow
  + Group
  + GroupSeparator
  + [HorizontalLine](https://wiki.genexus.com/commwiki/wiki?18797)
  + [Image](https://wiki.genexus.com/commwiki/wiki?20460)
  + [Matrix](https://wiki.genexus.com/commwiki/wiki?25692)
  + MatrixAxisLabel
  + [Menu (ex Dashboard)](https://wiki.genexus.com/commwiki/wiki?37667)
  + MenuItem (ex DashboardOption)
  + [Progress](https://wiki.genexus.com/commwiki/wiki?37765) (2)
  + SDMapPinImage
  + SDPageController
  + Tab
  + Table
  + TabPage
  + TextBlock
* **[Transformations node](https://wiki.genexus.com/commwiki/wiki?23694)**
* **[Fonts node](https://wiki.genexus.com/commwiki/wiki?22781)**

**Notes**  
**(1)** Available as of [GeneXus 15 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?36778,,)  
**(2)** Available as of [GeneXus 15 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?37491,,)

### [Color tab](#Color+tab)

Allows you to select a [Color Palette object](https://wiki.genexus.com/commwiki/wiki?31262) that applies to the Theme object, displaying which colors are used (in the palette or not) for that theme. Also, for each color, will display a properties list with theme-class that uses such colors. That simplifies the developer task of discovering which color is applying to.  
`[imagen omitida: wiki id 37639]`  
For more information, refer to [Colors Tab of Theme Object](https://wiki.genexus.com/commwiki/wiki?22256).

### [Images tab](#Images+tab)

At this tab, all the images used by the Theme object will be displayed. When an image varies with a theme, only the corresponding to this theme is shown.  
`[imagen omitida: wiki id 37640]`

### [See also](#See+also)

* [My first Theme object](https://wiki.genexus.com/commwiki/wiki?16237)
* [Colors Tab of Theme Object](https://wiki.genexus.com/commwiki/wiki?22256)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Design Systems](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/design-systems-6103186?p=3637)  
`[imagen omitida: wiki id 20668]` [Images and Theme Object](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/images-and-theme-object?p=3640)


|  |
| --- |
| **Pages** |
| [Color Editor](https://wiki.genexus.com/commwiki/wiki?22241) | [Dark Theme property](https://wiki.genexus.com/commwiki/wiki?44354) | [Enable Preferred Color Scheme property](https://wiki.genexus.com/commwiki/wiki?44353) |
| [SimpleAndroid Theme for Smart Devices](https://wiki.genexus.com/commwiki/wiki?18324) | [Transformations](https://wiki.genexus.com/commwiki/wiki?23694) | [Using Custom Fonts](https://wiki.genexus.com/commwiki/wiki?22781) |

---
