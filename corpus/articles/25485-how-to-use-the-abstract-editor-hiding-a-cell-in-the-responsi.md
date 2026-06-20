---
title: "How to use the Abstract Editor: Hiding a cell in the Responsive Table"
source_id: 25485
source_url: https://wiki.genexus.com/commwiki/wiki?25485
genexus_version: "18"
---

# How to use the Abstract Editor: Hiding a cell in the Responsive Table

In a [Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159) the columns of a [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961) are not fixed and they may vary depending on the size of the screen.

Sometimes on phone screens only one column has to be shown, whereas on tablets and desktops more information can be presented to the user.

This can be configured using the [Web Abstract Editor](https://wiki.genexus.com/commwiki/wiki?24795) which is opened through the [Responsive Sizes property (X Evolution 3)](https://wiki.genexus.com/commwiki/wiki?25478,,) of the Responsive Table.

## [Example](#Example)

Consider the following example, where only one column will be displayed on phone screens, and two columns will be displayed to the user on tablets and desktop screens.

|  |  |
| --- | --- |
|  |  |

#### [The left menu is only shown when the screen size is not extra small.](#The+left+menu+is+only+shown+when+the+screen+size+is+not+extra+small.)

#### [How is it designed?](#How+is+it+designed%3F)

You can set it by pressing the "Responsive Sizes" button in the Responsive Table properties.

The screen size is selected in the "Size" combo box. When selecting the cell that belongs to the column which is going to be hidden, you have to configure the visible property.

In this case, the configuration is available only for Extra Small Sizes, as shown in the figure below:

`[imagen omitida: wiki id 25483]`

In the example, the menu is displayed using a grid, and it is configured to be hidden for extra small devices.

For small screens and wider screens, the visible property has to be set to TRUE; otherwise, its value will be inherited from the smaller size.

`[imagen omitida: wiki id 25484]`

## [See Also](#See+Also)

[How to design a responsive web application: Hiding an element of the form](https://wiki.genexus.com/commwiki/wiki?25490)  
[How to design a Responsive Web Application: Hiding a column in a grid](https://wiki.genexus.com/commwiki/wiki?25495)  
[Arranging the layout in a RWA](https://wiki.genexus.com/commwiki/wiki?25514)


|  |
| --- |
| **Backlinks** |
| [Arranging the layout in a RWA](https://wiki.genexus.com/commwiki/wiki?25514) | [How to design a Responsive Web Application: Hiding a column in a grid](https://wiki.genexus.com/commwiki/wiki?25495) | [How to design a responsive web application: Hiding an element of the form](https://wiki.genexus.com/commwiki/wiki?25490) |
| [Responsive Sizes property](https://wiki.genexus.com/commwiki/wiki?29125) | [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961) |

---
