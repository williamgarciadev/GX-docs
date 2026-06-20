---
title: "DesignOps - Best practices for designers"
source_id: 46874
source_url: https://wiki.genexus.com/commwiki/wiki?46874
genexus_version: "18"
---

# DesignOps - Best practices for designers

This article intends to be a guideline of best practices when designing apps for the GeneXus ecosystem. Following these design practices from the beginning increases the chance of achieving a good-looking result on the first try and promotes a smooth collaboration between designers and developers.

**Content**  

* [**Best practices**](#Best+practices)

+ [General](#General)
+ [Semantic naming](#Semantic+naming)
+ [Consistent naming](#Consistent+naming)
+ [Semantic grouping](#Semantic+grouping)
+ [Static content](#Static+content)
+ [Input content](#Input+content)
+ [Reuse components](#Reuse+components)
+ [Reuse styles](#Reuse+styles)
+ [Ignore platform elements](#Ignore+platform+elements)
+ [Export shapes](#Export+shapes)
+ [Optimize images](#Optimize+images)
+ [Avoid overlaps](#Avoid+overlaps)
+ [Text box spacing](#Text+box+spacing)
+ [Touch targets](#Touch+targets)
+ [Smooth horizontal grid scrolling](#Smooth+horizontal+grid+scrolling)

* [**Icon References**](#Icon+References)
* [**Availability**](#Availability)
* [**Scope**](#Scope)
* [**See also**](#See+also)

## [**Best practices**](#Best+practices)

### [General](#General)

To ensure a seamless integration between design and development, follow these best practices when structuring your design files:

* **Keep content within boundaries**  
  Verify that no content extends beyond the Artboard or Main Frame to prevent unintended cropping, misalignment, or rendering issues.
* **Test responsiveness**  
  Stretch and compress your Artboards or Main Frames to ensure the layout adapts as expected without breaking the design. Ensure that elements maintain their positions or scale properly when necessary. For scrollable content, verify that overflowing elements are contained within a fixed height to preserve the intended behavior.
* **Beware of reserved words**  
  Do not use reserved words ([Conventions](https://wiki.genexus.com/commwiki/wiki?46872)) for unintended elements to prevent naming conflicts or undesired behavior.

### [Semantic naming](#Semantic+naming)

Avoid default layer naming. Instead, describe what it is representing and collaborate with the developer to establish a naming convention (e.g. for naming attributes that come from the database).

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ Frame 1   ├─т Text 1   └─□ Rectangle 1 ``` | ``` ⌗ Home Panel   ├─т Title Text   └─□ Panel Background ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | Use alphanumeric characters for layer names, always start with a letter and remove any leading or trailing spaces. |
|  | 2) | Keep layer names concise yet meaningful, with a maximum length of 128 characters. |
|  | 3) | Avoid duplicate names in artboards and symbols. |
|  | 4) | Ensure unique layer names within the same artboard or symbol. |
|  | 5) | In case of duplication, the tool will automatically append numerical suffixes (e.g. Button, Button1, Button2, etc.) compromising the maintainability of the application. |

### [Consistent naming](#Consistent+naming)

Maintain a consistent and standardized naming convention across all layers, following the guidelines defined with the development team. Ensure that casing and formatting remain uniform, and avoid mixing different naming styles within the same design.

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ Home panel   ├─т titleText   └─□ panel BackGround ``` | ``` ⌗ Home Panel   ├─т Title Text   └─□ Panel Background ``` |

### [Semantic grouping](#Semantic+grouping)

Group everything that should be together. By default, a group or frame layer will represent a canvas or a table control, depending on whether there is overlapping or not. However, you can define a different control for a group by specifying a [Control convention](https://wiki.genexus.com/commwiki/wiki?46872).

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ User Panel   ├─т Title Text   ├─т User Name Label   ├─т User Name Value   ├─т Confirm Caption   ├─□ Confirm Background   └─□ Panel Background ``` | ``` ⌗ User Panel   ├─т Title Text   ├─⌗ User Name Box   │   ├─т User Name Label   │   └─т User Name Value   ├─⌗ Button Confirm (*)   │   ├─т Confirm Caption   │   └─□ Confirm Background   └─□ Panel Background ```  **(\*)** Defined by convention |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | There are several ways to group elements in the design, each serving different purposes. Below are visual general examples illustrating how elements can be grouped based on different criteria.  ``` ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │┌┄┄┄┄┄┄┄┄┐│ │          │ │┌┄┄┬┄┄┄┄┄┐│ │          │ │┆██ █████┆│ │ ████████ │ │┆██┆██ ██┆│ │ ████████ │ │┆██ █████┆│ │┌┄┄┄┄┄┄┄┄┐│ │┆██┆     ┆│ │┌┄┄┄┄┄┄┄┄┐│ │└┄┄┄┄┄┄┄┄┘│ │┆██ █████┆│ │┆██┆██ ██┆│ │┆██ ██ ██┆│ │ ████████ │ │└┄┄┄┄┄┄┄┄┘│ │└┄┄┴┄┄┄┄┄┘│ │├┄┄┄┄┄┄┄┄┤│ │ ████████ │ │ ████████ │ │ ████████ │ │┆████ ███┆│ │          │ │          │ │          │ │└┄┄┄┄┄┄┄┄┘│ └──────────┘ └──────────┘ └──────────┘ └──────────┘ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │┌┄┄┄┄┄┄┄┄┐│ │   ┌┄┄┄┄┄┐│ │   ┌┄┄┬┄┄┐│ │   ┌┄┄┄┄┄┐│ │┆█████ ██┆│ │ ██┆█████┆│ │ ██┆██┆██┆│ │ ██┆██ ██┆│ │├┄┄┄┄┄┄┄┄┤│ │ ██├┄┄┄┄┄┤│ │ ██┆  ┆  ┆│ │ ██├┄┄┄┄┄┤│ │┆██ █████┆│ │ ██┆██ ██┆│ │ ██┆██┆██┆│ │ ██┆██ ██┆│ │├┄┄┄┄┄┄┄┄┤│ │ ██├┄┄┄┄┄┤│ │ ██┆  ┆██┆│ │ ██┆██   ┆│ │┆█████ ██┆│ │ ██┆███ █┆│ │ ██┆██┆██┆│ │ ██┆██ ██┆│ │└┄┄┄┄┄┄┄┄┘│ │   └┄┄┄┄┄┘│ │   └┄┄┴┄┄┘│ │   └┄┄┄┄┄┘│ └──────────┘ └──────────┘ └──────────┘ └──────────┘ ```  If semantic grouping is not applied, GeneXus will attempt to infer a grouping structure by automatically assigning a generic name to the group, prefixing the table name with "Wrap". However, this may not always align with the intended design, making explicit grouping a recommended best practice. |

### [Static content](#Static+content)

Identify text or bitmap layers whose content does not change (e.g. app title, banners, icons) and apply the [Static convention](https://wiki.genexus.com/commwiki/wiki?46872).

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ Login Panel   ├─т Title Text   ├─⌗ User Name Box   │   ├─т User Name Label   │   └─т User Name Value   ├─⌗ Button Confirm   │   ├─т Confirm Caption   │   └─□ Confirm Background   └─□ Panel Background ``` | ``` ⌗ Login Panel   ├─т Static Title Text   ├─⌗ User Name Box   │   ├─т Static User Name Label   │   └─т User Name Value   ├─⌗ Button Confirm   │   ├─т Confirm Caption   │   └─□ Confirm Background   └─□ Panel Background ``` |

### [Input content](#Input+content)

Identify text layers with the purpose of being editable by the end user and apply the [Input convention](https://wiki.genexus.com/commwiki/wiki?46872).

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ Login Panel   ├─т Static Title Text   ├─⌗ User Name Box   │   ├─т User Name Label   │   └─т User Name Value   ├─⌗ Button Confirm   │   ├─т Confirm Caption   │   └─□ Confirm Background   └─□ Panel Background ``` | ``` ⌗ Login Panel   ├─т Static Title Text   ├─⌗ User Name Box   │   ├─т Static User Name Label   │   └─т Input User Name Value   ├─⌗ Button Confirm   │   ├─т Confirm Caption   │   └─□ Confirm Background   └─□ Panel Background ``` |

### [Reuse components](#Reuse+components)

Avoid making multiple copies of a group of elements in different [Artboards / Top-Level Frames](https://wiki.genexus.com/commwiki/wiki?46871). Instead, conceptualize your groups and define [Symbols / Components](https://wiki.genexus.com/commwiki/wiki?46871) for them. Use generic values or placeholders in the main component/symbol to make it as broadly applicable as possible, and override these values with specific examples in their instances.

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ Login Panel   ├─т Static Title Text   ├─⌗ User Name Box   │   ├─т Static User Name Label   │   │   • value: Username   │   │   │   └─т Input User Name Value   │       • value: jhon.doe   │   ├─⌗ User Password Box   │   ├─т Static Password Label   │   │   • value: Password   │   │   │   └─т Input Password Value   │       • value: ****   │   ├─⌗ Button Login   │   ├─т Confirm Caption   │   │   • value: Login   │   │   │   └─□ Confirm Background   │   └─□ Panel Background ``` | ``` ❖ Field (Symbol/Component)   ├─т Static Label   │   • value: Label Name   │   ├─т Input Value   │   • value: Invite Message...   │   └─⌗ Error Box       ├─☆ Error Icon       └─т Error Message           • value: An error has ocurred ```  ``` ❖ Button (Symbol/Component)   ├─т Caption Text   │   • value: Caption   │   └─□ Background Shape ```  ``` ⌗ Login panel   ├─т Static Title Text   ├─◇ User Name Field ┄┄┄┄┄> Instance of Field   │   ├─т Static Label   │   │   ◦ value: Username   │   │   │   ├─т Input Value    │   │   ◦ value: jhon.doe   │   │   │   └─⌗ Error Box   │       ◦ visible: NO   │   ├─◇ Password Field ┄┄┄┄┄> Instance of Field   │   ├─т Static Label   │   │   ◦ value: Password   │   │   │   ├─т Input Value   │   │   ◦ value: ****   │   │   │   └─⌗ Error Box   │       ◦ visible: NO   │   ├─◇ Button Login ┄┄┄┄┄┄┄> Instance of Button   │   ├─т Caption Text   │   │   ◦ value: Login   │   │    │   └─□ Background Shape   │   └─□ Panel Background ``` |

### [Reuse styles](#Reuse+styles)

Avoid defining the appearance of each element in your design. Instead, try to define [Styles](https://wiki.genexus.com/commwiki/wiki?46871) and [Colors](https://wiki.genexus.com/commwiki/wiki?46871) for reusing them on multiple elements.

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ Home Panel   ├─т Static Title Text   │   • font: Roboto   │   • size: 18   │   • color: #D6DCD6   │   └─⌗ Panel Background       • color: #24695C ``` | ``` ⌗ Home Panel   ├─т Static Title Text   │   • text-style: H1   │   └─⌗ Panel Background       • color: Primary ```  ``` α Text-Styles   ├─ H1   │  • font: Roboto   │  • size: 18   │  • color: Neutral   ├─ H2   └─ ...  ◐ Colors   ├─ Neutral: #D6DCD6   ├─ Primary: #24695C   └─ ... ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | Use meaningful names (e.g., H1, Primary) rather than based on appearance (e.g Bold 18px, Red). |
|  | 2) | Never override defined styles with manual adjustments unless necessary for a specific case. |

### [Ignore platform elements](#Ignore+platform+elements)

Exclude platform-specific UI elements that are not part of the actual app design. These elements are automatically provided by the operating system or the browser, and should neither be designed nor included in design files.

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ User Panel   ├─⌗ Status Bar   │   ├─☆ Signal Icon   │   ├─☆ WiFi Icon   │   └─т Time Value   ├─т Static Title Text   ├─□ Scroll Bar   └─□ Panel Background ``` | ``` ⌗ User Panel   ├─т Static Title Text   ├─□ _ Scroll Bar   └─□ Panel Background ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | If these platform-specific elements cannot be removed for some reason, consider hiding them or applying the [Ignore convention](https://wiki.genexus.com/commwiki/wiki?46872) to ensure they are excluded when GeneXus generates objects in the Knowledge Base. |
|  | 2) | Common platform elements include, but are not limited to:   * **Scroll Bars** – Automatic system behavior. * **Status Bar** – Displays battery status, signal strength, current time, and other system indicators. * **Keyboard** – Dinamically displayed when the user selects an input. * **Navigation Menu** – Displays back, home and menu icons in Android. * **Notch** or **Dynamic Island** – Specific for Apple devices. * **Home Indicator**– Exclusive to Apple devices, allowing users to swipe up to exit the app or switch between applications. * **Floating Assistive Buttons** – System-provided shortcuts, primarily for accessibility. * **Address Bar** – Common in browsers for entering a URL address. * **Device Frame Layout** – Includes phone bezels and borders of iOS and Android devices, as well as browser components like tabs, toolbars, and window controls that are not part of the actual app or web design. |

### [Export shapes](#Export+shapes)

Ensure that you export as an image any shapes that GeneXus cannot handle (e.g., stars, polygons, vectors, lines, etc.).

These shapes are often used as individual elements within an icon. In such cases, it is sufficient to export the entire group for the icon instead of exporting each element separately. Additionally, make sure to include margins between the group and the icon itself (usually that group will be a square box).

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ User Panel   ├─т User Name   ├─⌗ User Icon   │   │ • width: 20   │   │ • height: 25   │   │   │   ├─○ Oval 1   │   └─☈ Path 1   └─□ Panel Background ``` | ``` ⌗ User Panel   ├─т User Name   ├─⌗ User Icon   │   │ • width: 25   │   │ • height: 25   │   │ • export:    │   │   - png @1x   │   │   - png @2x   │   │   - png @3x   │   │   │   ├─○ Oval 1   │   └─☈ Path 1   └─□ Panel Background ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | Since GeneXus cannot interpret Line shapes, it is recommended to use Rectangle shapes with a height of 1 instead in order to avoid exporting them as images. |
|  | 2) | If a shape is defined as a Symbol or Component, any overridden colors in its instances will be ignored. In this case, GeneXus treats the entire Symbol/Component as an image rather than a dynamic element. To retain color variations, create separate image exports for each variation and replace the instances where needed. |
|  | 3) | Ensure that exported images have unique names to avoid conflicts or overwrites during development. As every other layer, use descriptive names that reflect the asset’s purpose, avoiding generic terms like "icon", "image" or "logo". |

### [Optimize images](#Optimize+images)

Ensure you optimize the size and resolution of the images before incorporating them into the design.

Unoptimized images can impact the performance of the application. Additionally, fill images (those added by the "Choose Image" option) should not be marked for export as images as they are images themselves. Doing so would result in duplicate images in the Knowledge Base.

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ Home Panel   ├─⌗ Header Row   │   ├─т Header Row Title   │   └─▣ Header Row Background   │       • fill: image.png    │               (2000x3500)   │       • export:   │         - png @1x   │         - png @2x   │         - png @3x   │   ├─  ...   └─□ Panel Background ``` | ``` ⌗ Home Panel   ├─⌗ Header Row   │   ├─т Header Row Title   │   └─▣ Header Row Background   │       • fill: image.png   │               (500x875)   │   ├─  ...   └─□ Panel Background ``` |

### [Avoid overlaps](#Avoid+overlaps)

Avoid layer overlapping when you can. When designing, imagine your design layers arranged as if they were placed in the cells of a table. When overlap cannot be avoided, consider the best way to group the layers.

For instance, if you have a floating button, group the scrollable area first and place the button outside of that group. Similarly, when dealing with two or more elements that unavoidably overlap, it is recommended to group them together as a single unit

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ Home Panel   ├─◇ Header Row   │   • x: 0   │   • y: 0   │   • width: 1440   │   • height: 695 <╌╌╌┐   │                     ┆   ├─◇ Button Chat       ┆(*)   │   • x: 1280         ┆   │   • y: 660 ╌╌╌╌╌╌┐  ┆   │   • width: 120   ├╌╌┘   │   • height: 120 ╌┘   │   ├─  ...   └─□ Panel Background ```  ``` ❖ Header Row (Symbol/Component)   ├─т Header Row Title   └─□ Header Row Background  ❖ Button (Symbol/Component)   ├─т Chat Icon   └─□ Chat Rounded Background ```   **(\*)** Overlap required. The Button Chat layer starts above and extends below the bottom edge of the Header Row layer. | ``` ⌗ Home Panel   ├─⌗ Header Row Group   │   │ • x: 0   │   │ • y: 0   │   │ • width: 1440   │   │ • height: 780   │   │    │   ├─◇ Header Row   │   │   • x: 0   │   │   • y: 0   │   │   • width: 1440   │   │   • height: 695   │   │   • z-index: 0   │   │   │   └─◇ Button Chat   │       • x: 1280   │       • y: 660   │       • width: 120   │       • height: 120   │       • z-index: 1   │   ├─  ...   └─□ Panel Background ```  ``` ❖ Header Row (Symbol/Component)   ├─т Header Row Title   └─□ Header Row Background  ❖ Button (Symbol/Component)   ├─☆ Chat Icon   └─□ Chat Rounded Background ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | Rectangles and images acting as the frame's background are excluded from the required overlapping concept because GeneXus will interpret them in terms of background-color, background-image, border-radius, etc. |

### [Text box spacing](#Text+box+spacing)

Ensuring enough space in text boxes prevents line breaks or clipped elements.

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ User Panel   ├─т User Name   │   • caption: Jhon   │   • font-size: 20   │   • line-height: 25   │   • width: 80   │   • height: 18   │   ├─  ...   └─□ Panel Background ``` | ``` ⌗ User Panel   ├─т User Name   │   • caption: Jhon   │   • font-size: 20   │   • line-height: 25   │   • width: 100   │   • height: 30   │   ├─  ...   └─□ Panel Background ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | Ensure text boxes are large enough to accommodate the font size and line height, preventing text from being truncated or clipped that may lead in illegible content. |
|  | 2) | Text boxes should be wider than the text inside them to avoid undesired newlines; especially when the text is defined in a component and then overridden by other values during instantiation. |

### [Touch targets](#Touch+targets)

For mobile designs, every layer that can be touched by the end-user (e.g. buttons, edits, icons, etc.) must have at least **48x48 dp** of tappable area.

Check [Android Material Design](https://material.io/design/usability/accessibility.html#layout-and-typography) and [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/accessibility#Buttons-and-controls).

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ Update User Panel   ├─т Input User Name (*)   │   • caption: Username...   │   • font-style: italics   │   • font-size: 20   │   • line-height: 25   │   • width: 100   │   • height: 30   │   ├─  ...   └─□ Panel Background ```   **(\*)** Tappable area | ``` ⌗ Update User Panel   ├─т Input User Name   │   • caption: Username...   │   • font-style: italics    │   • font-size: 20   │   • line-height: 25   │   • width: 100   │   • height: 48   │   ├─  ...   └─□ Panel Background ``` |

|  |  |  |
| --- | --- | --- |
| **Notes** | 1) | Maintain the minimum required dimensions to ensure proper usability and accessibility in interactive elements. |
|  | 2) | If the minimum tappable area is not met, elements within the control may be clipped or partially obscured, compromising both visual clarity and user interaction. |

### [Smooth horizontal grid scrolling](#Smooth+horizontal+grid+scrolling)

Ensure smooth horizontal scrolling in Group or Frame layers that follow [Horizontal Grid convention](https://wiki.genexus.com/commwiki/wiki?46872) by extending the grid to the full width of the screen. Any remaining space should be managed using one or a combination of the following methods:  
1) Adding filler cells (transparent columns) at the begining and end of the grid group.  
2) Adding spacing in the Symbol or Component that represents a grid item.

|  |  |
| --- | --- |
| ✘ **DON'T** | ✔ **DO** |
| ``` ⌗ Home Panel   ├─ ...   ├─⌗ Grid Horizontal Attractions   │   ├─◇ Attraction Card   │   │   ...   │   └─◇ Attraction Card   ├─  ...   └─□ Panel Background ```  ``` ❖ Attraction Card (Symbol/Component)   ├─т Attraction Name   ├─▣ Attraction Image   └─□ Attraction Background ``` | ``` ⌗ Home Panel   ├─ ...   ├─⌗ Grid Horizontal Attractions   │   ├─□ Filler Cell   │   │   • width: 10   │   │   │   ├─◇ Attraction Card   │   │   ...   │   ├─◇ Attraction Card   │   │   │   └─□ Filler Cell   │       • width: 10   │   ├─  ...   └─□ Panel Background ```   or   ``` ❖ Attraction Card (Symbol/Component)   │ • padding-left: 10   │ • padding-right: 10   │   ├─т Attraction Name   ├─▣ Attraction Image   └─□ Attraction Background ``` |

|  |  |  |
| --- | --- | --- |
| **Notes:** | 1) | The scrollable area is defined over the grid area. In the following visual representation, without any adjustment, the items will never reach out the left edge of the layout because the grid area does not fill the layout width.  ``` ┏━━━━━━━━━┓Layout ┃         ┃  ┃         ┃  ┃┌┄┄┄┄┄┄┄┄╂┄┄┄┄┄┄┐Grid  ┃┊┏━━━┓┏━━┻┓┏━━━┓┊  ┃┊┃   ┃┃   ┃┃   ┃┊  ┃┊┗━━━┛┗━━┳┛┗━━━┛┊  ┃└┄┄┄┄┄┄┄┄╂┄┄┄┄┄┄┘  ┗━━━━━━━━━┛ ```    This issue can be avoided ensuring the grid extends to the layout edges, applying one or a combination of the following methods:    1. Adding filler cells at the begining and the end:  ```  ┏━━━━━━━━━┓Layout  ┃         ┃   ┃         ┃   ┠┄┄┄┄┄┄┄┄┄╂┄┄┄┄┄┄┄┐Grid   ┃▒┏━━━┓┏━━┻┓┏━━━┓▒┊   ┃▒┃   ┃┃   ┃┃   ┃▒┊   ┃▒┗━━━┛┗━━┳┛┗━━━┛▒┊   ┠┄┄┄┄┄┄┄┄┄╂┄┄┄┄┄┄┄┘   ┗━━━━━━━━━┛ ```    2. Adding spacing inside the grid items:  ```  ┏━━━━━━━━━┓Layout  ┃         ┃   ┃         ┃   ┠┄┄┄┄┄┄┄┄┄╂┄┄┄┄┄┄┄┐Grid   ┠┲━━━┱┬┲━━┻┱┬┲━━━┱┤   ┃┨   ┠│┨   ┠│┨   ┠│   ┠┺━━━┹┴┺━━┳┹┴┺━━━┹┤   ┠┄┄┄┄┄┄┄┄┄╂┄┄┄┄┄┄┄┘   ┗━━━━━━━━━┛ ``` |

## [**Icon References**](#Icon+References)

Refer to [Conventions: Icon References](https://wiki.genexus.com/commwiki/wiki?46872).

## [**Availability**](#Availability)

These sections apply as of [GeneXus 17](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46873,,).

* As of [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46852,,):  
  - Color Variables are supported.
* As of [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066):  
  - Scalable Vector Graphics (SVG) images are supported.  
  - Static definition for bitmap and layers exported as images are supported

## [**Scope**](#Scope)

|  |  |
| --- | --- |
| **Generators** | .NET, .NET Core, Java, Android, Apple, Angular |

## [**See also**](#See+also)

* [Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871)
* [DesignOps - Conventions](https://wiki.genexus.com/commwiki/wiki?46872)


|  |
| --- |
| **Backlinks** |
| [DesignOps - Conventions](https://wiki.genexus.com/commwiki/wiki?46872) | [DesignOps - Conventions (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55465) |
| [DesignOps - FAQ and Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46880) | [DesignOps - Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877) | [DesignOps - Overview](https://wiki.genexus.com/commwiki/wiki?47020) | [Table of contents:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) |
| [GeneXus Design Prototyper for Figma](https://wiki.genexus.com/commwiki/wiki?56683) |

---
