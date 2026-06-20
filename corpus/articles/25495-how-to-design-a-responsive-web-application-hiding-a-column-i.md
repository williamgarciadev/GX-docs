---
title: "How to design a Responsive Web Application: Hiding a column in a grid"
source_id: 25495
source_url: https://wiki.genexus.com/commwiki/wiki?25495
genexus_version: "18"
---

# How to design a Responsive Web Application: Hiding a column in a grid

In a [Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159) only the relevant information is shown for mobile applications; this implies that some elements which are displayed on desktop screens, are not displayed on phone screens.  
As for grids, in general they show more columns for wide screens than for extra small screens.

This is the case of the [Work With Pattern for web](https://wiki.genexus.com/commwiki/wiki?25475), whose default form generates the [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209) shown below - when the [Web Form Defaults property](https://wiki.genexus.com/commwiki/wiki?25135) is set to Responsive Web Design.

`[imagen omitida: wiki id 25498]`

### [At runtime...](#At+runtime...)

* Note that for extra small screen sizes the grid only shows three columns:

`[imagen omitida: wiki id 25496]`

* In small and wider screens, the grid displays all columns:

`[imagen omitida: wiki id 25497]`

### [How it is designed](#How+it+is+designed)

The user can decide, at design time, which columns will be visible and which won't.

In the example, select one grid column which is hidden at runtime for the extra small screen size and note that the WWOptionalColumn class is assigned to the [Column Class Property](https://wiki.genexus.com/commwiki/wiki?24908).

`[imagen omitida: wiki id 25499]`

The WWOptionalColumn class belongs to the "Flat" Theme, and has property values which depend on a conditional rule called "ExtraSmall". See [Conditional Class Properties for Themes](https://wiki.genexus.com/commwiki/wiki?25116) for more information about this topic.

`[imagen omitida: wiki id 25500]`

Note that the display property value for the WWOptionalColumn class is none, when the "ExtraSmall" rule evaluates to TRUE. The conditional rule is translated into a media query, which is transparent to the user, and this is what makes it possible to obtain the desired behavior and hide some of the grid columns.

### [See Also](#See+Also)

[How to design a responsive web application: Hiding an element of the form](https://wiki.genexus.com/commwiki/wiki?25490)  
[How to use the Abstract Editor: designing a Web Transaction Form](https://wiki.genexus.com/commwiki/wiki?25250)  
[How to use the Abstract Editor: Hiding a cell in the Responsive Table](https://wiki.genexus.com/commwiki/wiki?25485)  
[Arranging the layout in a RWA](https://wiki.genexus.com/commwiki/wiki?25514)


|  |
| --- |
| **Backlinks** |
| [Arranging the layout in a RWA](https://wiki.genexus.com/commwiki/wiki?25514) | [Column Class property in Grid (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55106) | [Column Class property in Grid and Tabular Grid](https://wiki.genexus.com/commwiki/wiki?24908) |
| [How to design a responsive web application: Hiding an element of the form](https://wiki.genexus.com/commwiki/wiki?25490) | [How to use the Abstract Editor: Hiding a cell in the Responsive Table](https://wiki.genexus.com/commwiki/wiki?25485) | [Responsive Sizes property](https://wiki.genexus.com/commwiki/wiki?29125) |
| [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961) |

---
