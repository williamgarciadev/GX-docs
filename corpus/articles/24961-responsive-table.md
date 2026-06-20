---
title: "Responsive Table"
source_id: 24961
source_url: https://wiki.genexus.com/commwiki/wiki?24961
genexus_version: "18"
---

# Responsive Table

The control used in GeneXus to design a [Responsive Web Application](https://wiki.genexus.com/commwiki/wiki?25159) is called Responsive Table, and it is the main control of the [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209).

Frameworks like [BootStrap](http://getbootstrap.com/2.3.2/#fluidGridSystem) provide a container that they call Grid. It is similar to a table, but it adapts to the width of the screen to allow for a [RWD](https://wiki.genexus.com/commwiki/wiki?25157,,). Therefore, this container makes it possible to display the information in a way that is readable to the user regardless of the device or screen size.

The GeneXus Responsive Table is generated as a Bootstrap fluid grid.

Unlike the traditional [Table control](https://wiki.genexus.com/commwiki/wiki?6001), responsive tables allow working with percentage-based designs that guarantee that the elements inside them will always adapt to the device screen. 

## [Responsive Table control](#Responsive+Table+control)

1. It looks like a table, but the width of the cells is specified using percentages.

`[imagen omitida: wiki id 25477]`

The percentages are specified for four different screen sizes (according to the width of the screen).

* Extra small devices (xs)       (Phone < 768px)
* Small devices (sm)              (Tablets >= 768px)
* Medium devices (md)            (Desktops >= 992px)
* Large devices (lg)               (Desktops >= 1200px)

The [Responsive Sizes property (X Evolution 3)](https://wiki.genexus.com/commwiki/wiki?25478,,) allows making this configuration for the different screens.

2. The cells cannot be spanned to more than one row - row span is always 1, so this property is not available for the control.

3. For each size (xs, sm, md, lg) a value can be specified for the offset of each column. Besides, the columns can be interchanged depending on the screen size (Move).

4. The aesthetic properties of the controls inside the cells of the Responsive Table have to be managed using [Theme](https://wiki.genexus.com/commwiki/wiki?6420) Classes.

## [Features of a Responsive Table](#Features+of+a+Responsive+Table)

### [1. Generated as div elements](#1.+Generated+as+div+elements)

It is generated as div HTML elements, so the columns are not fixed. They may vary according to the screen size, and this can be set using the [Responsive Sizes property (X Evolution 3)](https://wiki.genexus.com/commwiki/wiki?25478,,). 

### [2. Differences in behavior between Responsive Table and Table control](#2.+Differences+in+behavior+between+Responsive+Table+and+Table+control)

There are differences in the behavior of the responsive table and the [Table control](https://wiki.genexus.com/commwiki/wiki?6001). If the width of a cell of a responsive table (which is determined in percentages) is not wide enough to contain the control inside, the information of the control can be overlapped. On the contrary, when the common [Table control](https://wiki.genexus.com/commwiki/wiki?6001) has no fixed width, it expands to occupy all the necessary horizontal space for its content to be displayed without wrapping or overlapping.

### [3. Different parts of the screen can be hidden or shown depending on the screen size](#3.+Different+parts+of+the+screen+can+be+hidden+or+shown+depending+on+the+screen+size)

This can be achieved by using the [Conditional Class Properties for Themes](https://wiki.genexus.com/commwiki/wiki?25116).

The form can be arranged in a different way depending on the screen size of the device also.

## [Layout issues of the responsive table](#Layout+issues+of+the+responsive+table)

The cells of a row in the responsive table can be set to any width, regardless that the sum of all the widths is greater than 100%. In such case, the cells remaining - which exceed the width - will wrap to a new line.

Example:

`[imagen omitida: wiki id 31547]`

Then, the cells of the same row can be interchanged, hidden, or dropped down to another row for any of the screen sizes.

Nevertheless, cells that are displayed in a different row, cannot move up to the row which is above of it.

For example, if you need to design the following form, where two controls are one beside to the other in the large screen, you need to design the following layout. This, although, in the other screens (extra small, small, medium), the controls are one at the top of the other.

`[imagen omitida: wiki id 31548]`

### [Use default values for all screen sizes button](#Use+default+values+for+all+screen+sizes+button)

This button allows setting the defaults for all the controls and for all the screen sizes (extra small, small, medium, and large), not only for selected screen size in the "Size" combo box. See [Responsive Sizes property](https://wiki.genexus.com/commwiki/wiki?29125) to understand the defaults criteria.

### [Default checkbox](#Default+checkbox+)

When checked, the selected control is set to its default values. See [Responsive Sizes property](https://wiki.genexus.com/commwiki/wiki?29125) to understand the defaults criteria.

### [See Also](#See+Also)

[Arranging the layout in a RWA](https://wiki.genexus.com/commwiki/wiki?25514)  
[How to use the Abstract Editor: Hiding a cell in the Responsive Table](https://wiki.genexus.com/commwiki/wiki?25485)  
[How to design a responsive web application: Hiding an element of the form](https://wiki.genexus.com/commwiki/wiki?25490)  
[How to design a Responsive Web Application: Hiding a column in a grid](https://wiki.genexus.com/commwiki/wiki?25495)


|  |
| --- |
| **Backlinks** |
| [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209) | [Action Group Control for the Web](https://wiki.genexus.com/commwiki/wiki?25631) | [Arranging the layout in a RWA](https://wiki.genexus.com/commwiki/wiki?25514) |
| [Category:Common Controls](https://wiki.genexus.com/commwiki/wiki?5928) | [Container Theme Class for RWA](https://wiki.genexus.com/commwiki/wiki?25962) | [Convert to Abstract Layout menu option](https://wiki.genexus.com/commwiki/wiki?29297) | [Designing a Responsive web form: alignment of labels and controls](https://wiki.genexus.com/commwiki/wiki?28275) |
| [Flex control](https://wiki.genexus.com/commwiki/wiki?40521) | [GeneXus Markup Language (GXML)](https://wiki.genexus.com/commwiki/wiki?46876) | [Getting started with RWD: Understanding default forms](https://wiki.genexus.com/commwiki/wiki?29098) |
| [Header property](https://wiki.genexus.com/commwiki/wiki?17942) | [Horizontal Alignment property](https://wiki.genexus.com/commwiki/wiki?28263) | [How to change cell width in RWA](https://wiki.genexus.com/commwiki/wiki?26077) | [How to configure Table control styles in web apps](https://wiki.genexus.com/commwiki/wiki?32687) |
| [How to use the Abstract Editor: designing a Web Transaction Form](https://wiki.genexus.com/commwiki/wiki?25250) | [How to use the Abstract Editor: Hiding a cell in the Responsive Table](https://wiki.genexus.com/commwiki/wiki?25485) |
| [HowTo: Display a menu in a responsive application](https://wiki.genexus.com/commwiki/wiki?25778) | [HowTo: Responsive vertical centering](https://wiki.genexus.com/commwiki/wiki?30650) | [HowTo: Take up the full height of a page](https://wiki.genexus.com/commwiki/wiki?30640) | [Is Slot property](https://wiki.genexus.com/commwiki/wiki?51306) |
| [Responsive Sizes property](https://wiki.genexus.com/commwiki/wiki?29125) | [Toc:Responsive Web Design in GeneXus](https://wiki.genexus.com/commwiki/wiki?29134) |
| [Section Control](https://wiki.genexus.com/commwiki/wiki?6112) | [Smart Table control](https://wiki.genexus.com/commwiki/wiki?45577) | [Tab control for Web Panels](https://wiki.genexus.com/commwiki/wiki?25623) | [Web Abstract Editor](https://wiki.genexus.com/commwiki/wiki?24795) |
| [Category:Web Master Panel object](https://wiki.genexus.com/commwiki/wiki?10348) |

---
