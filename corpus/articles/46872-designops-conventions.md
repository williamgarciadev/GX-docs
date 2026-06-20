---
title: "DesignOps - Conventions"
source_id: 46872
source_url: https://wiki.genexus.com/commwiki/wiki?46872
genexus_version: "18"
---

# DesignOps - Conventions

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
| **Applies to** | Any layer |
| **Example** | ``` ⌗ Root/Group/Frame layer   ├─⌗ _ Status Bar ┄┄┄┄┄┄┄> ignores this layer and its content   │   ├─т Time Text   │   ├─☆ WiFi Icon   │   ├─☆ Signal Icon   │   └─☆ Battery Icon   ├─т Title Text   ├─□ _ Scroll Bar ┄┄┄┄┄┄┄> ignores this layer   └─□ Panel Background ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | Since some elements in the application are intended to be standard (managed by the operative system or the browser), the following set of keywords also ignores a layer: 'keyboard', 'status bar' |
|  | 2) | The ignore convention does not applies for main Symbol/Components because their instances could be referenced in other layers. |

### [Static content](#Static+content)

Used for defining static content (e.g. a section title or static image) that GeneXus will interpret as a [Text Block control](https://wiki.genexus.com/commwiki/wiki?5948) in case of text layers and as an [Image control](https://wiki.genexus.com/commwiki/wiki?5939) for bitmaps layers or layers exported as images.

|  |  |
| --- | --- |
| **Prefix** | **static** |
| **Applies to** | Text, Bitmap, or Exported-As-Image layers |
| **Example** | ``` ⌗ Root/Group/Frame layer   └─т Static Header Title ``` |

### [Dynamic content](#Dynamic+content)

Used for defining dynamic content (e.g. a customer name) GeneXus will interpret as a read-only [Variable definition](https://wiki.genexus.com/commwiki/wiki?7375).

|  |  |
| --- | --- |
| **Prefix** | **(none)** |
| **Applies to** | Text layer |
| **Example** | ``` ⌗ Root/Group/Frame layer   └─т Customer Name ``` |

### [Editable content](#Editable+content)

Used for defining editable content (i.e. user input) that GeneXus will interpret as an editable [Variable definition](https://wiki.genexus.com/commwiki/wiki?7375).

|  |  |
| --- | --- |
| **Prefix** | **input** |
| **Applies to** | Text layer |
| **Example** | ``` ⌗ Root/Group/Frame layer   └─т Input Customer Name ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | The import process cannot infer if the value associated with an input field is a preset value or if it is an invite message. Let your developer know which case is being displayed, so he/she can customize the appropriate colors for each case. GeneXus will not set a value associated with an input field; instead, it will use it as an invite message. |

### [Button control](#Button+control)

Used for defining buttons that GeneXus will interpret as a [Button control](https://wiki.genexus.com/commwiki/wiki?6011). Also, if the layer defines a link, GeneXus will interpret a call action to the panel defined by the target artboard; otherwise, it will display a dummy message.

|  |  |
| --- | --- |
| **Prefix** | **button** |
| **Applies to** | Group or Frame layers |
| **Example** | ``` ⌗ Root/Group/Frame layer ​​​​  └─⌗ Button Cancel       ├─т Caption ┄┄┄┄┄> caption text       └─□ Background ┄┄> background and shape ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | If you have multiple text-layers defining the button caption, only the first one will be taken into account. |
|  | 2) | By default a button will define an event with a [Msg command](https://wiki.genexus.com/commwiki/wiki?31635) prompting the control's name if the button does not define a link to a main-frame. |

### [ComboBox control](#ComboBox+control)

Used for defining a combo-box control that will be interpreted by GeneXus as a Variable with [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) set as Combo Box.

|  |  |
| --- | --- |
| **Prefix** | **combobox** |
| **Applies to** | Group or Frame layers |
| **Example** | ``` ⌗ Root/Group/Frame layer ​​​​​​   └─⌗ ComboBox Country       ├─т Uruguay ┄┄┄┄┄┄┄┄┄┄> displayed value       ├─☈ Chevron Drawing ┄┄> chevron drawing       └─□ Background ┄┄┄┄┄┄┄> background and shape ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | GeneXus will always use the default combo-box control, so custom chevron drawings will not be rendered. |
|  | 2) | By default, the combo-box will include the displayed value from the design (e.g., Uruguay) along with a default empty value (none). Developers can customize the available options dynamically by using the [AddItem method](https://wiki.genexus.com/commwiki/wiki?8668). |

### [Check control](#Check+control)

Used for defining a check-box control that will be interpreted by GeneXus as a Variable with [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) set as Check Box.

|  |  |
| --- | --- |
| **Prefix** | **checkbox** |
| **Applies to** | Group or Frame layers |
| **Example** | ``` ⌗ Root/Group/Frame layer ​​​​​​   ├─т Label Agreement ┄┄┄┄┄> checkbox label   └─⌗ CheckBox Agreement       ├─☈ Check Drawing ┄┄┄> check rectangle drawing       └─□ Background ┄┄┄┄┄┄> background and shape ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | GeneXus will always use the default check-box control on each platform, so custom check drawings will not be rendered. |

### [Switch control](#Switch+control)

Used for defining a switch control that will be interpreted by GeneXus as a Variable with [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) set as Switch.

|  |  |
| --- | --- |
| **Prefix** | **switch** |
| **Applies to** | Group or Frame layers |
| **Example** | ``` ⌗ Root/Group/Frame layer ​​​​​​   ├─т Label Agreement ┄┄┄┄┄> switch label   └─⌗ Switch Agreement        ├─☈ Switch Drawing ┄┄> switch drawing       └─□ Background ┄┄┄┄┄┄> background and shape ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | GeneXus will always use the default switch control on each platform, so custom switch drawings will not be rendered. |

### [Radio-button control](#Radio-button+control)

Used for defining a radio-button control that will be interpreted by GeneXus as a Variable with [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) set as Radio Button. The elements defined in the group will be the items of the radio-button.

|  |  |
| --- | --- |
| **Prefix** | **radiobutton** |
| **Applies to** | Group or Frame layers |
| **Example** | ``` ⌗ Root/Group/Frame layer ​​​​​​   └─⌗ RadioButton Payment Currency       ├─⌗ USD Item        │   ├─т USD ┄┄┄┄┄┄┄┄┄┄┄┄> first radio label       │   └─☈ Radio Drawing ┄┄> first radio circle drawing       ┆   ...     ​​​​​​  ├─⌗ UYU Item       │   ├─т UYU ┄┄┄┄┄┄┄┄┄┄┄┄> last radio label         │   └─☈ Radio Drawing ┄┄> last radio circle drawing     ​​​​​​  └─□ Background ┄┄┄┄┄┄┄┄┄> background and shape ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | GeneXus will always use the default radio-button control, so custom radio button drawings will not be rendered. |
|  | 2) | Only vertical radio-buttons are supported. |

### [Tabs control](#Tabs+control)

Used for defining tabs controls that GeneXus will interpret as a [Tab control for Web Panels](https://wiki.genexus.com/commwiki/wiki?25623) or [Tab control for Panels](https://wiki.genexus.com/commwiki/wiki?29986). The elements defined in the containers are just two: a container for the tab-strip and a container for the tab-content.

|  |  |
| --- | --- |
| **Prefix** | **tabs** |
| **Applies to** | Group or Frame layers |
| **Example** | ``` ⌗ Root Layer = Attraction - About ┄┄┄┄┄┐ suffix matching the   └─⌗ Tabs Information                 ┊ selected tab layer name       ├─⌗ Tab Strip                    ┊       │   ├─т About <┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘       │   └─т Directions       ├─⌗ Tab Content       │   └─ (About tab content)       └─□ Background  ⌗ Root Layer = Attraction - Direction ┄┐ suffix matching the ​​​  └─⌗ Tabs Information                 ┊ selected tab layer name       ├─⌗ Tab Strip                    ┊       │   ├─т About                    ┊       │   └─т Directions <┄┄┄┄┄┄┄┄┄┄┄┄┄┘       ├─⌗ Tab Content       │   └─ (Direction tab content)       └─□ Background ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | Selected tab-item in the tab-strip must be differentiated from other tab-items (e.g. by changing its font-color). |
|  | 2) | The tab-content variation must be designed in separated Artboards sharing the same prefix. For instance, if you want to design a panel "Attraction" containing a tab with "About" and "Directions" items, then you should design the two Artboards and name them "Attraction - About" and "Attraction - Directions", both of them will be equal except for the tab-content section and the tab-item style. |
|  | 3) | Scrollable tab strips are not allowed and it is recommended to have at most 4 tabs. |
|  | 4) | The tab-strip must be defined as a group (not as a symbol). |
|  | 5) | Each tab-item only allows text layers (no icons are allowed nor selector bar). |

### [List & Carousel](#List+%26+Carousel)

Used for defining a list (vertical scroll) or carousel (horizontal scroll) that will be interpreted by GeneXus as a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) with the appropriate item direction.

|  |  |
| --- | --- |
| **Prefix** | **grid (vertical | horizontal)** |
| **Applies to** | Group or Frame layers |
| **Example** | ``` ⌗ Root/Group/Frame layer ​​​​​​   └─⌗ Grid Attractions       ├─◇ Attraction       │   ├─т Attraction Name ┄┄┄> first overridden value/style       │   └─☆ Attraction Image ┄┄> first overridden style       ┆   ...       ├─◇ Attraction       │   ├─т Attraction Name ┄┄┄> last overridden value/style       │   └─☆ Attraction Image ┄┄> last overridden style       └─□ Background ```  ``` ❖ Attraction (Symbol/Component)   ├─т Attraction Name   └─☆ Attraction Image ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | When scroll direction is not indicated in the naming convention, GeneXus will try to infer it. However, in certain cases, the inference may lead to incorrect results due to ambiguity (e.g., multi-column grids with a single row may be incorrectly interpreted as an horizontal grid). To ensure the correct interpretation, specify the direction in the naming convention when the arrangement of items is unclear. |
|  | 2) | It is highly recommended to reuse the items on the list by using symbols/components. In fact, a grid is a sequence of repetitive elements where each item has the same semantic.  **Important:**  * Grid designs for Mobile admit instances of **multiple** symbols/components (displayed as different layouts) * Grid designs for Web admit instances of a **single** symbol/component (because they only admit a single layout). Other instances different from the first symbol/component instance will be ignored. |
|  | 3) | When the Grid layer is defined as an Auto Layout and the Layout Flow is defined as Wrap, the Grid control will be defined in GeneXus with [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) set as Flex (defining a Flex Grid). |
|  | 4) | When importing for web a [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058) is used. |

### [Navigation bar](#Navigation+bar)

Used for rendering the navigation bar for a mobile app panel that will be interpreted by GeneXus as the [Application Bar control](https://wiki.genexus.com/commwiki/wiki?19486) of the target panel.

|  |  |
| --- | --- |
| **Prefix** | **navbar** |
| **Applies to** | Group or Frame layers |
| **Example** | ``` ⌗ Root layer ​​​​​​   ├─⌗ NavBar App Header   │   ├─т Back Icon ┄┄┄┄┄┄┄> optional left icon   │   ├─т Title ┄┄┄┄┄┄┄┄┄┄┄> title   │   ├─т Profile Icon   ┐   ┆   ┆   ...            ├┄> optional sequence of right icons   │   ├─т Cart Icon      ┘   │   └─□ Background   └─ (body content) ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | Only applies to Mobile applications, and must be unique for each screen. For Web applications, this convention will be ignored and will be generated as is. |
|  | 2) | Only one left icon is admitted (e.g. for defining a back button). |
|  | 3) | Only one centered text is admitted as a title. |
|  | 4) | Multiple right-stacked icons are admitted (i.e. multiple options). |

### [Navigation tab](#Navigation+tab)

Used for rendering a navigation tab for mobile apps that will be interpreted by GeneXus as a [Menu object](https://wiki.genexus.com/commwiki/wiki?16321) referencing multiple target Panels.

|  |  |
| --- | --- |
| **Prefix** | **tabbar** |
| **Applies to** | Group or Frame layers |
| **Example** | ``` ⌗ Root Layer = Attractions ┄┄┄┄┄┐ panel's name matches the   ├─ (body content)             ┊ selected tab layer name   └─⌗ TabBar Menu Options       ┊       ├─⌗ Attractions <┄┄┄┄┄┄┄┄┄┘       │   ├─т Attractions Label       │   └─☆ Attractions Icon       ┆   ...       ├─⌗ Profile       │   ├─т Profile Label       │   └─☆ Prifile Icon       └─□ Background  ⌗ Root Layer = Profile ┄┄┄┄┄┄┄┄┄┐ panel's name matches the   ├─ (body content)             ┊ selected tab layer name   └─⌗ TabBar Menu Options       ┊       ├─⌗ Attractions           ┊       │   ├─т Attractions Label ┊       │   └─☆ Attractions Icon  ┊       ┆   ...                   ┊       ├─⌗ Profile <┄┄┄┄┄┄┄┄┄┄┄┄┄┘       │   ├─т Profile Label       │   └─☆ Profile Icon       └─□ Background ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | This convention is exclusive to mobile application designs and does not apply to web applications. It is highly recommended to include a maximum of five tabs, ensuring that each tab has a corresponding Artboard to prevent empty content when tapping a tab-item. |
|  | 2) | Each tab-item must be grouped and each group name must match exactly with the Artboard's name being displayed (or the first one you linked with other Artboards). For instance, if the navigation tab has an item for displaying the Artboard named "User Profile", then that item (the layer-group) must be also named "User Profile" too. |
|  | 3) | Each tab-item must contain at least a text layer (representing the tab caption) or an image/exported layer (representing the tab icon). |

### [Variable content](#Variable+content)

Used for rendering a common layout (shared by all screens) that will be interpreted by GeneXus as a [Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348) or [Master Panel object](https://wiki.genexus.com/commwiki/wiki?46247) containing a ContentHolder control. When designing the common layout, do so in a separate artboard and be sure to define the variable content placeholder as a slot (where the rest of your screens will be rendered). By using this strategy, each panel can be designed without the need to repeatedly include the same layout around them.

|  |  |
| --- | --- |
| **Prefix** | **slot** |
| **Applies to** | Group or Frame layers |
| **Example** | ``` ⌗ Root/Group/Frame layer ┄┄> the artboard or main-frame   ├─⌗ Header                 will be defined as Master Panel   │  ├─т Static Title   │  └─□ Background   │   ...   ├─⌗ Slot Body ┄┄┄┄┄┄┄┄​​​┄┄┄> defines the placeholder    │   ...                    where other panels will be placed   ├─⌗ Footer   │   ├─т Static Copyright   │   └─□ Background   └─□ Background ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | The convention applied to an artboard or main-frame is exclusively available for the Web or Angular platforms because it is related to the Mater Panel object. |
|  | 2) | When defining multiple layers with the Slot convention in an artboard or main-frame, only one will be considered because the Content Holder control must be unique in a Master Panel object. |
|  | 3) | When defining a container layer with the Slot convention in an artboard or main-frame, the content of that container will be ignored because the aim of the Content Holder control is to define a placeholder section. |

On the other hand, this convention can also be applied over multiple containers in Symbols or Components and GeneXus will interpret those containers as Table/Canvas controls with the [Is Slot property](https://wiki.genexus.com/commwiki/wiki?51306) set to True. The purpose of this other strategy is to allow developers to edit and relocate the controls defined within these slots as needed. This can be beneficial when aiming to use a single Stencil instance differently, depending on the screen on which it's being displayed.

|  |  |
| --- | --- |
| **Prefix** | **slot** |
| **Applies to** | Group or Frame layers |
| **Example** | ``` ❖ User Card ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄> the symbol or component   ├─▣ User Picture   ├─⌗ Slot Body ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄> defines a table with    │   ├─т User Name                 Is Slot property in True   │   ├─т User Lastname   │   ├─т User Company   │   └─□ Background ┄┄┄┄┄┄┄┄┄┄┄┄┄> will not be generated as a control   └─□ Line                          but defines table's style class ```  ``` ⌗ Root/Group/Frame layer ┄┄┄┄┄┄┄┄┄> the artboard or main-frame   ├─⌗ Header   ├─⌗ Body   │   ├─ ...   │   ├─◇ User Profile ┄┄┄┄┄┄┄​​​​​​​┄​​​​​​​┄​​​​​​​┄​​​​​​​┄​​​​​​​> instance of User Card   │   │   ├─▣ User Picture ┄┄┄┄┄┄┄> cannot be modified but can be overridden   │   │   ├─⌗ Slot Body   │   │   │   ├─т User Name     ┐   │   │   │   ├─т User Lastname ├┄> can be modified and overriden   │   │   │   ├─т User Company  ┘   │   │   │   └─□ Background   │   │   └─□ Line ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄> cannot be modified but can be overridden   │   └─ ...   ├─⌗ Footer   └─□ Background ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | The convention applied to symbol or component's containers is available on every platform because it is related to the Stencil control. |
|  | 2) | When defining a container layer with the Slot convention in a symbol or component, the slot content will be fully editable by the developer in the Stencil instances (e.g. change position, sizes, name, etc). However, since the control is a Stencil instance, both slot-contained and non-editable elements can still apply overrides (e.g. change value, style, visibility, etc.). |

## [Icon References](#Icon+References)

|  |  |
| --- | --- |
| ⌗ | Frame or Group layer |
| ❖ | Symbol or Component layer |
| ◇ | Symbol or Component Instance layer |
| т | Text layer |
| □ | Rectangle Shape layer |
| ▣ | Bitmap or Rectangle Shape layer (with fill image) |
| ○ | Oval Shape layer |
| ☆ | Poligon Shape layer |
| ☈ | Path Shape layer |
| ◐ | Color style |
| α | Text style |

## [Notes](#Notes)

* The **Background** layer described in every example is a rectangle shape that fits its container. This layer is optional if the background properties (such as background color, border width, border radius, etc.) are defined over a Frame layer. However, the layer is mandatory if the container is defined as a Group layer because a group does not allow background properties to be set. Therefore, in Sketch, the background shape is always required because Sketch only handles groups. In contrast, in Figma, the background shape can be omitted if a Frame layer is used, but it is required if a Group layer is used.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Generators** | .NET, .NET Core, Java, Android, Apple, Angular |

## [See also](#See+also)

* [Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871)
* [DesignOps - Best practices for designers](https://wiki.genexus.com/commwiki/wiki?46874)

## [Availability](#Availability)

These conventions are available as of [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066).


|  |
| --- |
| **Backlinks** |
| [DesignOps - Best practices for designers](https://wiki.genexus.com/commwiki/wiki?46874) | [DesignOps - Conventions (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55465) | [DesignOps - Conventions (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55465) |
| [DesignOps - Conventions - Multiple Layouts](https://wiki.genexus.com/commwiki/wiki?48697) | [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [DesignOps - Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877) | [Table of contents:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) |
| [GeneXus Design Prototyper for Figma](https://wiki.genexus.com/commwiki/wiki?56683) |
|

---
