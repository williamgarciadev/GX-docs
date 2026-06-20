---
title: "Design System Object - Token, design constant options"
source_id: 48692
source_url: https://wiki.genexus.com/commwiki/wiki?48692
genexus_version: "18"
---

# Design System Object - Token, design constant options

It is increasingly common for applications to provide one design for a Light color scheme and another for a Dark scheme.

For this reason, the designers have created both options for the home page:

`[imagen omitida: wiki id 48635]`

And for the Attractions screen:

`[imagen omitida: wiki id 48637]`

As you can see, the color of the surface or background is modified from a type of white to a type of black. Also, in the Dark mode the texts on the surface become their negative equivalent, and the texts that were highlighted in red will change to a type of yellow.

To represent these changes in the token values without having to duplicate anything, it is possible to define options for the tokens.

To do this, parameterize the set of tokens according to a parameter that you can name as you wish – in this case, "color-scheme” – and for which you define the two values that it can take:

`[imagen omitida: wiki id 48638]`

Then, it will be enough to set that when using the [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) with Light color-scheme option, certain values should be assigned to the color tokens, and when using the Dark color-scheme option, other values should be assigned to the color tokens:

`[imagen omitida: wiki id 48639]`

Boolean conditions are written with the "@" symbol.

Here you are only varying the color tokens, but it could be all of them.

In addition, here you are defining a single option, the color-scheme, but it could be platforms, for example, or any other that you can think of.

Now you only need to know how to apply one option or the other at runtime to the objects that use this DSO.

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |

---
