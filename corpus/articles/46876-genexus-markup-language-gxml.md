---
title: "GeneXus Markup Language (GXML)"
source_id: 46876
source_url: https://wiki.genexus.com/commwiki/wiki?46876
genexus_version: "18"
---

# GeneXus Markup Language (GXML)

GeneXus Markup Language (GXML) is an XML-like descriptive language for describing GeneXus' layouts.

The drag-and-drop concept in GeneXus makes it far easier for the average user to understand how to design apps by describing their components in an abstract way, without worrying about the lines of code that it may entail. Either way, for those adventured users, the GXML syntax aims to be very simple to understand, providing views, controls, and layout structures for declaring your app's user interface. This document pretends to be a guideline for those intrigued users that wants to analyze a GeneXus object from another point of view.

## [Overview](#Overview)

The GXML is a standard for defining layouts GeneXus' objects such as Panels, Stencils, and Master Panels objects. The purpose of this format is to structure content in a way that is semantically meaningful and readable for both humans and machines The fact of being a markup language means that uses tags to describe the structure and semantics of a layout rather than focusing on how it should be visually presented. In this way, the key advantages of using an abstract representation of the user interface are as follows:

1. **Structure:** Organizes the content into logical sections to make it easier to understand how the user interface is defined.
2. **Accessibility:** Uses semantic elements to help readers and other assistive technologies interpret the content.
3. **Coss-Platform:** Encapsulates the user interface logic by being agnostic of the target platform and ensuring consistent user experience.

The structure of a GXML document consists of a series of elements represented by tags. The relationship between elements is defined by their nesting resulting in a hierarchical structure. The element that contains another element is called the "parent", while the contained element is referred to as the "child", and elements at that same level in the hierarchy are called "siblings".

For instance, the following layout and GXML document are equivalent:

|  |  |
| --- | --- |
|  | ```   <panel id="D034848F-DB64-4622-88CD-F93EF77DFC03"          name="MyPanel">     <smart name="MyPanel"             width="100%"             height="219px"             columnsStyle="100%"             rowsStyle="128px;91px"            class="my-panel-class">       <tr height="128px">         <td class="table-cell"             hAlign="Left"             vAlign="Top">           <smart name="MyTable"                  class="table-class"                   width="189px"                  height="24px"                  columnsStyle="165px;24px"                  rowsStyle="24px">             <tr height="24px">               <td class="table-cell"                   hAlign="Left"                   vAlign="Top">                 <input attribute="&amp;MyInputText"                        class="edit-class"                        labelPosition="None"                        inviteMessage="Placeholder...."                        readonly="False"/>               </td>               <td class="table-cell"                   hAlign="Right"                   vAlign="Middle">                 <img name="MyUserIcon"                      class="image-class"                      Image="UserIcon" />               </td>             </tr>           </smart>         </td>       </tr>       <tr height="91px">         <td class="table-cell"              hAlign="Left"             vAlign="Top">           <action controlName="MyButton"                   onClickEvent="'MyButton'"                   caption="Click me!"                   class="button-class" />         </td>       </tr>     </smart>   </panel> ``` |

## [Root elements](#Root+elements)

#### [<panel>](#%26lt%3Bpanel%26gt%3B)

Describes the beginning of a Layout definition for a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), or [Master Panel object](https://wiki.genexus.com/commwiki/wiki?46247).

|  |  |
| --- | --- |
| **Permitted parents:** | None |
| **Permitted content:** | Layout element ([<view>](https://wiki.genexus.com/commwiki/wiki?46876)). |
| **Permitted attributes:** |  |
| id | String  Unique identifier. |
| description | String| optional  Short description. |


## [Layout elements](#Layout+elements)

#### [<view>](#%26lt%3Bview%26gt%3B)

Describes a specific layout when defining [Multiple Layouts in Panels](https://wiki.genexus.com/commwiki/wiki?23489) or a [Web Layout](https://wiki.genexus.com/commwiki/wiki?8132)

|  |  |
| --- | --- |
| **Permitted parents:** | Panel element ([<panel>](https://wiki.genexus.com/commwiki/wiki?46876)). |
| **Permitted content:** | Any container element. |
| **Permitted attributes:** |  |
| platform | String| default: any  Target platform.  **Values**: any, android, ios, web. |
| device | String| default: any  Target device.  **Values**: any, tablet or phone, tv, watch. |
| size | String| default: any  Target size.  **Values**: any, small, medium, large. |
| orientation | String| default: any  Target orientation.  **Values**: any, landscape, portrait. |

---

## [Container elements](#Container+elements)

#### [<canvas>](#%26lt%3Bcanvas%26gt%3B)

Describes a [Canvas control](https://wiki.genexus.com/commwiki/wiki?22452).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | Any control or container element. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |
| width | String  Control width expressed in px, dip, or %. |
| height | String  Control height expressed in px, dip, or %. |
| isSlot | String| default: false  Defines if the container is a slot or not.  **Values**: false, true. |
| background | String  Background image object full name.  **Note:** This only applies to non-Web layout context. |

---

#### [<flex>](#%26lt%3Bflex%26gt%3B)

Describes a [Flex control](https://wiki.genexus.com/commwiki/wiki?40521).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | Any control or container element. |
| **Permitted attributes:** | Extends [<canvas>](https://wiki.genexus.com/commwiki/wiki?46876) element's attributes. |
| flexDirection | String| default: row  Establishes the main axis, thus defining the direction flex items are placed in the flex container.  **Values**: row, row-reverse, column, column-reverse. |
| flexWrap | String| default: nowrap  Controls whether the flex container is single-line or multi-line, and the direction of the cross axis.  **Values**: nowrap, wrap, wrap-reverse. |
| justifyContent | String| default: flex-start  Defines the alignment along the main axis.  **Values**: flex-start, flex-end, center, space-around, space-between. |
| alignItems | String| default: stretch  Defines the default behavior for how flex items are laid out along the cross-axis on the current line.  **Values**: stretch, flex-start, flex-end, center, baseline. |

---

#### [<responsive>](#%26lt%3Bresponsive%26gt%3B)

Describes a [Responsive Table control](https://wiki.genexus.com/commwiki/wiki?24961).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | Any control or container element. |
| **Permitted attributes:** | Extends [<canvas>](https://wiki.genexus.com/commwiki/wiki?46876) element's attributes. |
| heights | String  Row heights. |
| sizes | String  Responsive sizes. |

---

#### [<section>](#%26lt%3Bsection%26gt%3B)

Describes a [Section Control](https://wiki.genexus.com/commwiki/wiki?6112).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | Any control or container element. |
| **Permitted attributes:** | Extends [<canvas>](https://wiki.genexus.com/commwiki/wiki?46876) element's attributes. |
| semanticContent | String| default: general  Determines de HTML attribute generated for this content.  **Values**: general, address, footer, header, main, nav, article, aside, h1, h2, h3, h4, h5, h6. |

---

#### [<smart>](#%26lt%3Bsmart%26gt%3B)

Describes a [Smart Table control](https://wiki.genexus.com/commwiki/wiki?45577).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | Table row element ([<tr>](https://wiki.genexus.com/commwiki/wiki?46876)). |
| **Permitted attributes:** | Extends [<canvas>](https://wiki.genexus.com/commwiki/wiki?46876) element's attributes. |
| columnsStyle | String  Column widths expressed in px, dip, or %, separated by semi-colons.  **Note**: The number of columns must match the number of <td> elements in the <tr> element with the most elements. |
| rowsStyle | String  Row heights expressed in px, dip, or %, separated by semi-colons.  **Note**: The number of rows must match the number of <tr> elements. |

---

#### [<table>](#%26lt%3Btable%26gt%3B)

Describes a [Table control](https://wiki.genexus.com/commwiki/wiki?6001).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | Table row element ([<tr>](https://wiki.genexus.com/commwiki/wiki?46876)). |
| **Permitted attributes:** | Extends [<canvas>](https://wiki.genexus.com/commwiki/wiki?46876) element's attributes in a Web layout context; otherwise extends [<smart>](https://wiki.genexus.com/commwiki/wiki?46876). |
| header | String  Header displayed above the table.  **Note**: This only applies to Web layout context. |

---

#### [<htable>](#%26lt%3Bhtable%26gt%3B)

Shorthand a Table element ([<table>](https://wiki.genexus.com/commwiki/wiki?46876)) or Smart element ([<smart>](https://wiki.genexus.com/commwiki/wiki?46876)) when it has a single row.

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | Any control or container element. |
| **Permitted attributes:** | Extends [<canvas>](https://wiki.genexus.com/commwiki/wiki?46876) element's attributes. |
| columnsStyle | String  Column widths expressed in px, dip, or %, separated by semi-colons. |

---

#### [<vtable>](#%26lt%3Bvtable%26gt%3B)

Shorthand a Table element ([<table>](https://wiki.genexus.com/commwiki/wiki?46876)) or Smart element ([<smart>](https://wiki.genexus.com/commwiki/wiki?46876)) when it has a single column.

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | Any control or container element. |
| **Permitted attributes:** | Extends [<canvas>](https://wiki.genexus.com/commwiki/wiki?46876) element's attributes. |
| rowsStyle | String  Row heights expressed in px, dip, or %, separated by semi-colons. |

---

## [Container item elements](#Container+item+elements)

#### [<tr>](#%26lt%3Btr%26gt%3B)

Describes a table row.

|  |  |
| --- | --- |
| **Permitted parents:** | Table element ([<table>](https://wiki.genexus.com/commwiki/wiki?46876)) or Smart element ([<smart>](https://wiki.genexus.com/commwiki/wiki?46876)). |
| **Permitted content:** | Table cell element ([<td>](https://wiki.genexus.com/commwiki/wiki?46876)). |
| **Permitted attributes:** |  |
| height | String  Table row height. |

---

#### [<td>](#%26lt%3Btd%26gt%3B)

Describes a table cell.

|  |  |
| --- | --- |
| **Permitted parents:** | Table row element ([<tr>](https://wiki.genexus.com/commwiki/wiki?46876)). |
| **Permitted content:** | Any control or container element. |
| **Permitted attributes:** | None. |
| hAlign | String| default: left  Horizontal alignment.  **Values**: left, center, right, justify. |
| vAlign | String| default: top  Vertical alignment.  **Values**: top, middle, bottom. |

---

## [Control elements](#Control+elements)

#### [<a>](#%26lt%3Ba%26gt%3B)

Describes an [Hyperlink control](https://wiki.genexus.com/commwiki/wiki?6007).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |

---

#### [<action>](#%26lt%3Baction%26gt%3B)

Describes a [Button control](https://wiki.genexus.com/commwiki/wiki?6011).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |
| caption | String  Button caption. |
| onClickEvent | String  Button event action name. |
| image | String  Image object full name. |
| imagePosition | String| default: above-text  Image position.  **Values**: above-text, below-text, behind-text, before-text, after-text.  **Note**: This only applies to non-Web layout context. |

---

#### [<actions>](#%26lt%3Bactions%26gt%3B)

Describes a [Action Group Control for Panels](https://wiki.genexus.com/commwiki/wiki?25106) or [Action Group Control for the Web](https://wiki.genexus.com/commwiki/wiki?25631).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | Action element ([<action>](https://wiki.genexus.com/commwiki/wiki?46876)). |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |

---

#### [<audio>](#%26lt%3Baudio%26gt%3B)

Describes a [Attribute/Variable](https://wiki.genexus.com/commwiki/wiki?6911) based on [Audio data type](https://wiki.genexus.com/commwiki/wiki?16529).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |

---

#### [<checkbox>](#%26lt%3Bcheckbox%26gt%3B)

Describes a [Attribute/Variable](https://wiki.genexus.com/commwiki/wiki?6911) having [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) with 'Checkbox' value.

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |

---

#### [<combobox>](#%26lt%3Bcombobox%26gt%3B)

Describes a [Attribute/Variable](https://wiki.genexus.com/commwiki/wiki?6911) having [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) with 'Combobox' value.

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |

---

#### [<component>](#%26lt%3Bcomponent%26gt%3B)

Describes a [Component control](https://wiki.genexus.com/commwiki/wiki?29811).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |

---

#### [<contentholder>](#%26lt%3Bcontentholder%26gt%3B)

Describes a Content Holder control when the layout is defined for a [Master Panel object](https://wiki.genexus.com/commwiki/wiki?46247).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |

---

#### [<errors>](#%26lt%3Berrors%26gt%3B)

Describes an [Error Viewer control](https://wiki.genexus.com/commwiki/wiki?6073).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |

---

#### [<grid>](#%26lt%3Bgrid%26gt%3B)

Describes a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid control](https://wiki.genexus.com/commwiki/wiki?6058), or Flex Grid control.

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | Any container element. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |
| scrollDirection | String| default: vertical  Scroll direction.  **Values**: vertical, horizontal. |
| multipleItems | String| default: single  Multiple items.  **Values**: single, multiple-quantity, staggered-quantity, multiple-size. |
| itempsPerRow | String| default: 1  Items per row.  **Note**: This only applies when multipleItems attribute has any of multiple-\* values. |
| snapToGrid | String| default: false  Snap to grid.  **Values**: false, true. |
| flexDirection | String| default: row  Establishes the main axis, thus defining the direction flex items are placed in the flex container.  **Values**: row, row-reverse, column, column-reverse.  **Note**: This overrides scrollDirection attribute and defines a Flex Grid. |
| flexWrap | String| default: nowrap  Controls whether the flex container is single-line or multi-line, and the direction of the cross axis.  **Values**: nowrap, wrap, wrap-reverse.  **Note**: This defines a Flex Grid. |
| justifyContent | String| default: flex-start  Defines the alignment along the main axis.  **Values**: flex-start, flex-end, center, space-around, space-between.  **Note**: This defines a Flex Grid. |
| alignContent | String| default: stretch  Aligns a flex container's lines within when there is extra space in the cross-axis.  **Values**: stretch, flex-start, flex-end, center, baseline.  **Note**: This defines a Flex Grid. |
| alignItems | String| default: stretch  Defines the default behavior for how flex items are laid out along the cross-axis on the current line.  **Values**: stretch, flex-start, flex-end, center, space-around, space-between.  **Note**: This defines a Flex Grid. |

---

#### [<group>](#%26lt%3Bgroup%26gt%3B)

Describes a [Group control](https://wiki.genexus.com/commwiki/wiki?6570).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |

---

#### [<hr>](#%26lt%3Bhr%26gt%3B)

Describes an [Horizontal Rule Control](https://wiki.genexus.com/commwiki/wiki?6016).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |

---

#### [<img>](#%26lt%3Bimg%26gt%3B)

Describes a [Attribute/Variable](https://wiki.genexus.com/commwiki/wiki?6911) based on [Image data type](https://wiki.genexus.com/commwiki/wiki?15204) or an [Image control](https://wiki.genexus.com/commwiki/wiki?5939).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |

---

#### [<input>](#%26lt%3Binput%26gt%3B)

Describes a [Attribute/Variable](https://wiki.genexus.com/commwiki/wiki?6911) having [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) with 'Edit' value.

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |
| autogrow | String| default: false  Autogrow.  **Values**: false, true, |
| inviteMessage | String  Invite message. |
| isPassword | String| default: false  Maks the user input while typing.  **Values**: false, true, |
| labelPosition | String| default: none  Label position.  **Values**: none, top, left. |
| labelWidth | String| default: 25%  Label width, in percentage, for each screen size in a responsive web application. The remaining space will be given to the control itself.  **Values**: n%, being n a positive integer.  **Note**: This only applies to Web layouts. |
| readonly | String| default: false  Value is read-write (false) or read-only (true).  **Values**: false, true, |

---

#### [<label>](#%26lt%3Blabel%26gt%3B)

Describes a [Text Block control](https://wiki.genexus.com/commwiki/wiki?5948).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |
| caption | String  Label caption. |

---

#### [<map>](#%26lt%3Bmap%26gt%3B)

Describes a [Map User Control](https://wiki.genexus.com/commwiki/wiki?5029).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |

---

#### [<stencil>](#%26lt%3Bstencil%26gt%3B)

Describes a [Stencil object](https://wiki.genexus.com/commwiki/wiki?38418) instance.

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | Any element (representing overridden controls). |
| **Permitted attributes:** |  |
| name | String  Control name. |

---

#### [<switch>](#%26lt%3Bswitch%26gt%3B)

Describes a [Attribute/Variable](https://wiki.genexus.com/commwiki/wiki?6911) having [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) with 'Swtich' value.

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |
| onText | String  Text displayed when the switch is on. |
| offText | String  Text displayed when the switch is off. |
| checkedValue | String  Checked value. |
| uncheckedValue | String  Unchecked value. |

---

#### [<tab>](#%26lt%3Btab%26gt%3B)

Describes a [Tab control for Panels](https://wiki.genexus.com/commwiki/wiki?29986) or [Tab control for Web Panels](https://wiki.genexus.com/commwiki/wiki?25623).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |

---

#### [<tabPage>](#%26lt%3BtabPage%26gt%3B)

Describes a tab-page and must be defined as a direct child of the Tab tag.

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | Action element ([<action>](https://wiki.genexus.com/commwiki/wiki?46876)). |
| **Permitted attributes:** |  |
| name | String  Control name. |
| caption | String  TabPage caption. |
| class | String  Control style class. |
| selClass | String  Selected tab style class. |
| itemClass | String  Control's tab pages style class. |
| position | String| default: default  Position of the action element when it is child of an Application Bar element ([<actionBar>](https://wiki.genexus.com/commwiki/wiki?46876)). The custom custom is only valid for iOS and it is defined by hAligh and vAlign.  **Values**: default, custom. |
| priority | String| default: normal  Determines action visibility and style in the Application Bar element ([<actionBar>](https://wiki.genexus.com/commwiki/wiki?46876)) based on priority levels.  **Values**:  - high: Displayed with icon, distinguished by the OS.  - normal: Shown with text from the caption property.  - low: Displayed in overflow section with caption text. |
| hAlign | String| default: left  Horizontal alignment when position property is custom.  **Values**: left, center, right, justify. |
| vAlign | String| default: top  Vertical alignment when position property is custom.  **Values**: top, middle, bottom |

---

#### [<video>](#%26lt%3Bvideo%26gt%3B)

Describes a [Attribute/Variable](https://wiki.genexus.com/commwiki/wiki?6911) based on [Video data type](https://wiki.genexus.com/commwiki/wiki?16608).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | None. |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |

---

## [Miscellaneous elements](#Miscellaneous+elements)

#### [<actionBar>](#%26lt%3BactionBar%26gt%3B)

Describes the [Applicatin Bars section](https://wiki.genexus.com/commwiki/wiki?19486) for [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

|  |  |
| --- | --- |
| **Permitted parents:** | Any container element. |
| **Permitted content:** | TabPage element ([<tabPage>](https://wiki.genexus.com/commwiki/wiki?46876)) |
| **Permitted attributes:** |  |
| name | String  Control name. |
| class | String  Control style class. |

---

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | Panel, WebPanel, Stencil, MasterPanel. |

## [See also](#See+also)

* [Design Import option](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46882,,)

---

|  |
| --- |
| **Backlinks** |
| [Design Import option (GeneXus 18 latest upgrade or prior)](https://wiki.genexus.com/commwiki/wiki?59501) | [Design Import option (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55439) |
| [Table of contents:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) | [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) | [GXML (GeneXus Markup Language) (GeneXus 18 Upgrade 4)](https://wiki.genexus.com/commwiki/wiki?55385) |

---
