---
title: "DesignOps - Conventions (GeneXus 18 Upgrade 4)"
source_id: 55465
source_url: https://wiki.genexus.com/commwiki/wiki?55465
genexus_version: "18"
---

# DesignOps - Conventions (GeneXus 18 Upgrade 4)

Conventions are useful for the essential difference between a designer profile and a developer profile.

In some cases, designers are creating and drawing without considering abstractions. Some of these drawings in the implementation must be, for example, an image. Therefore, the internal details of those components are not imported to GeneXus.

The freedom while designing is so great that there is no single heuristic that allows us to understand today the true meaning of what is drawn. This is why there are conventions to allow the design to be transmitted unambiguously to implementation.

## [Conventions](#Conventions)

Conventions are **prefixes** used by designers to label layers, providing a standardized approach for communicating the intended control type and behavior within the design, ensuring cohesion and consistency throughout the development process. These prefixes are **case-insensitive** and should be treated as **keywords** (without translating them into other languages).

### [Ignore layer](#Ignore+layer)

Used when you draw a draft that you do not want to be imported by GeneXus.

|  |  |
| --- | --- |
| **Prefix** | **\_** (underscore) |
| **Applies to** | Any element |
| **Example** | ```  Root/Group/Frame layer  └─ _ Ignore this layer ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | Since some elements in the application are intended to be standard, the following set of keywords also ignores a layer: 'keyboard', 'status bar' |

### [Static content](#Static+content)

Used for defining static content (e.g. a section title or static image) that will be interpreted by GeneXus as a TextBlock in case of text layers and as an Image control for bitmaps layers or layers exported as images.

|  |  |
| --- | --- |
| **Prefix** | **static** |
| **Applies to** | Text element |
| **Example** | ```  Root/Group/Frame layer  └─ Static Header title ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | As of [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) this convention is supported for bitmaps and layers exported as images for generating an Image control instead of an Image variable. |

### [Dynamic content](#Dynamic+content)

Used for defining dynamic content (e.g. a customer name) that will be interpreted by GeneXus as a read-only Variable.

|  |  |
| --- | --- |
| **Prefix** | **(none)** |
| **Applies to** | Text element |
| **Example** | ```  Root/Group/Frame layer  └─ Customer Name ``` |

### [Editable content](#Editable+content)

Used for defining editable content (i.e. user input) that will be interpreted by GeneXus as an editable Variable.

|  |  |
| --- | --- |
| **Prefix** | **input** |
| **Applies to** | Text element |
| **Example** | ```  Root/Group/Frame layer  └─ Input Customer Name ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | The import process cannot infer if the value associated with an input field is a preset value or if it is an invite message. Let your developer know which case is being displayed, so he/she can customize the appropriate colors for each case. GeneXus will not set a value associated to an input field; instead, it will use that value as an invite message. |

### [Button control](#Button+control)

Used for defining buttons that will be interpreted by GeneXus as a Button control. Also, if the layer defines a link, GeneXus will interpret a call action to the panel defined by the target artboard; otherwise, it will display a dummy message.

|  |  |
| --- | --- |
| **Prefix** | **button** |
| **Applies to** | Group / Frame |
| **Example** | ```  Root/Group/Frame layer ​​​​​​ └─ Button Cancel     ├─ Caption     ─> caption     └─ Background  ─> background and shape ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | If you have multiple text-layers defining the button caption, only the first one will be taken into account. |

### [ComboBox control](#ComboBox+control)

Used for defining a combo-box control that will be interpreted by GeneXus as a Variable with Control Type = Combo Box.

|  |  |
| --- | --- |
| **Prefix** | **combobox** |
| **Applies to** | Group / Frame |
| **Example** | ```  Root/Group/Frame layer ​​​​​​  └─ ComboBox Country     ├─ Uruguay          ─> displayed value     ├─ Chevron Drawing  ─> chevron drawing     └─ Background       ─> background and shape ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | GeneXus will always use the default combo-box control, so custom chevron drawings will not be rendered. |

### [Check control](#Check+control)

Used for defining a check-box control that will be interpreted by GeneXus as a Variable with Control Type = Check Box.

|  |  |
| --- | --- |
| **Prefix** | **checkbox** |
| **Applies to** | Group / Frame |
| **Example** | ```  Root/Group/Frame layer ​​​​​​  └─ CheckBox Agree      ├─ Are you agree?  ─> checkbox label     ├─ Check Drawing   ─> check rectangle drawing     └─ Background      ─> background and shape ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | GeneXus will always use the default check-box control, so custom check drawings will not be rendered. |

### [Radio-button control](#Radio-button+control)

Used for defining a radio-button control that will be interpreted by GeneXus as a Variable with Control Type = Radio Button. The elements defined in the group will be the items of the radio-button.

|  |  |
| --- | --- |
| **Prefix** | **radiobutton** |
| **Applies to** | Group / Frame |
| **Example** | ```  Root/Group/Frame layer ​​​​​​  └─ RadioButton Payment Currency     ├─ USD Item      │  ├─ USD                ─> first radio label     │  └─ Radio Drawing      ─> first radio circle drawing     ┆ ...   ​​​​​​  ├─ UYU Item     │  ├─ UYU                ─> last radio label       │  └─ Radio Drawing      ─> last radio circle drawing   ​​​​​​  └─ Background      ─> background and shape ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | GeneXus will always use the default radio-button control, so custom radio button drawings will not be rendered. |

### [Tabs control](#Tabs+control)

Used for defining tabs controls that will be interpreted by GeneXus as a Tab control. The elements defined in the group are just two: a group for the tab-strip and a group for the tab-content.

|  |  |
| --- | --- |
| **Prefix** | **tabs** |
| **Applies to** | Group / Frame |
| **Example** | ```  Root/Group/Frame layer ​​​​​​  └─ Tabs Information      ├─ Tab Strip      │  ├─ About        ─> match this artboard's suffix / selected style applied      │  ┆ ...      │  └─ Directions   ─> match another artboard's suffix / unselected style applied      └─ Tab Content         └─ (tab content design for the 'about' section) ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | Selected tab-item in the tab-strip must be differentiated from other tab-items (e.g. by changing its font-color). |
|  | 2) | The tab-content variation must be designed in separated Artboards sharing the same prefix. For instance, if you want to design a panel "Attraction" containing a tab with "About" and "Directions" items, then you should design the two Artboards and name them "Attraction - About" and "Attraction - Directions", both of them will be equal except for the tab-content section and the tab-item style. |
|  | 3) | Scrollable tab strips are not allowed and it is recommended to have at most 4 tabs. |
|  | 4) | The tab-strip must be defined as a group (not as a symbol). |
|  | 5) | Each tab-item only allows text layers (no icons are allowed nor selector bar). |

### [List & Carousel](#List+%26+Carousel)

Used for defining a list (vertical scroll) or carousel (horizontal scroll) that will be interpreted by GeneXus as a Grid control with the appropriate item orientation.

|  |  |
| --- | --- |
| **Prefix** | **grid (vertical | horizontal)** |
| **Applies to** | Group / Frame |
| **Example** | ```  Root/Group/Frame layer ​​​​​​  └─ Grid Attractions     ├─ Attraction 1     │  ├─ Attraction Name   ─> first overridden value/style     │  └─ Attraction Image  ─> first overridden style     ┆ ...     └─ Attraction N        ├─ Attraction Name   ─> first overridden value/style        └─ Attraction Image  ─> first overridden style ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | When orientation is not indicated in the naming convention, GeneXus will try to infer it. |
|  | 2) | It is highly recommended that you use symbols/components as items of the list (reusability).    **Important**:  * Grid designs for Mobile admit instances of **multiple** symbols/components (displayed as different layouts) * Grid designs for Web admit instances of a **single** symbol/component (because they only admit a single layout). Other instances different from the first symbol/component instance will be ignored.  In both cases (mobile or web designs), text and image overrides are allowed, and style overrides are supported as of [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?49956,,). |

### [Navigation bar](#Navigation+bar)

Used for rendering the navigation bar for a mobile app panel that will be interpreted by GeneXus as the Application Bar of the target panel.

|  |  |
| --- | --- |
| **Prefix** | **navigation** |
| **Applies to** | Group / Frame |
| **Example** | ```  Root Layer ​​​​​​  └─ Navigation Bar     ├─ Back Icon       ─> optional left icon     ├─ Title           ─> title     ├─ Profile Icon    ╮     ┆   ...           ├> optional sequence of right icons     └─ Cart Icon       ╯ ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | Only applies to Mobile applications. For Web applications, this convention will be ignored and will be generated as is. |
|  | 2) | Only one left icon is admitted (e.g. for defining a back button). |
|  | 3) | Only one centered text is admitted as a title. |
|  | 4) | Multiple right-stacked icons are admitted (i.e. multiple options). |

### [Navigation tab](#Navigation+tab)

Used for rendering a navigation tab for mobile apps that will be interpreted by GeneXus as a Menu object referencing multiple target Panels.

|  |  |
| --- | --- |
| **Prefix** | **tabbar** |
| **Applies to** | Group / Frame |
| **Example** | ```  Root Layer ​​​​​​  └─ TabBar Menu     ├─ Attractions           ─> group's name references 'Attractions' artboard     │  ├─ Attractions Label     │  └─ Attractions Icon     ┆  ...     └─ Profile               ─> group's name references 'Profile' artboard        ├─ Profile Label        └─ Prifile Icon ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | Does not apply to web applications. For mobile applications, it is recommended to have at most 5 tabs. |
|  | 2) | Each tab-item must be grouped and each group name must match exactly with the Artboard's name being displayed (or the first one you linked with other Artboards). For instance, if the navigation tab has an item for displaying the Artboard named "User Profile", then that item (the layer-group) must be also named "User Profile" too. |
|  | 3) | Each tab-item must contain at least a text layer (representing the tab caption) or an image/exported layer (representing the tab icon). |

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators** | .NET, .NET Core, Java, Android, Apple, Angular |

## [See also](#See+also)

* [Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871)
* [DesignOps - Best practices for designers](https://wiki.genexus.com/commwiki/wiki?46874)

## [Availability](#Availability)

These conventions are available as of [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46873,,).

* [Tabs control](https://wiki.genexus.com/commwiki/wiki?46872) and [Navigation tab](https://wiki.genexus.com/commwiki/wiki?46872) conventions are available as of GeneXus 17 Upgrade 6.
