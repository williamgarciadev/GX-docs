---
title: "How to design a responsive web application: Hiding an element of the form"
source_id: 25490
source_url: https://wiki.genexus.com/commwiki/wiki?25490
genexus_version: "18"
---

# How to design a responsive web application: Hiding an element of the form

In [Responsive Web Applications](https://wiki.genexus.com/commwiki/wiki?25159)s only the relevant information is shown for mobile applications. This implies that some elements which are present in desktop screens will not be included in phone screens.

### [Example](#Example)

Consider the following example where a list of tourist attractions is displayed. In small screens and wider screens (> 768px), each element of the list is displayed with its photo. On the other hand, in extra small screen devices the photo is not shown.

|  |  |
| --- | --- |
|  |  |

#### [How to design it](#How+to+design+it)

In this case the list of tourist attractions is loaded in a [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?9760) that includes a photo of each tourist attraction.

The photo and other elements of the grid (&AttractionName, &AttractionId, and &AttractionDescription variables) are inside a [Table control](https://wiki.genexus.com/commwiki/wiki?6001) nested into the Free Style Grid.

Since the element that is going to be hidden is not inside a cell of the Responsive Table, but inside a common table, we use [Conditional Class Properties for Themes](https://wiki.genexus.com/commwiki/wiki?25116) to solve this problem.

To do so:

First, assign a class to the image control:

`[imagen omitida: wiki id 25493]`

Next, edit the Theme and define a conditional rule. For that conditional rule and the class you've just defined, configure the class property "display = none", as shown below:

`[imagen omitida: wiki id 25494]`

And that's all! The reason is that the conditional class rule will be triggered and its settings will be applied depending on the size of the screen.

### [See Also](#See+Also)

[How to use the Abstract Editor: Hiding a cell in the Responsive Table](https://wiki.genexus.com/commwiki/wiki?25485)  
[How to design a Responsive Web Application: Hiding a column in a grid](https://wiki.genexus.com/commwiki/wiki?25495)


|  |
| --- |
| **Backlinks** |
| [Arranging the layout in a RWA](https://wiki.genexus.com/commwiki/wiki?25514) | [How to design a Responsive Web Application: Hiding a column in a grid](https://wiki.genexus.com/commwiki/wiki?25495) | [How to use the Abstract Editor: Hiding a cell in the Responsive Table](https://wiki.genexus.com/commwiki/wiki?25485) |
| [Responsive Sizes property](https://wiki.genexus.com/commwiki/wiki?29125) | [Responsive Table](https://wiki.genexus.com/commwiki/wiki?24961) |

---
