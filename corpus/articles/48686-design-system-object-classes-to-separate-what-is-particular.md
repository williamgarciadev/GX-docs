---
title: "Design System Object - Classes to separate what is particular from what is shared"
source_id: 48686
source_url: https://wiki.genexus.com/commwiki/wiki?48686
genexus_version: "18"
---

# Design System Object - Classes to separate what is particular from what is shared

To make this distinction and allow for abstraction, value assignments to design properties can be grouped into [Classes](https://wiki.genexus.com/commwiki/wiki?49309). These **classes** will suit the semantics of the design in question, so that they can be reused in other controls corresponding to the same concept. In this example, being the main title on a dark background.

If for all the [Text Block](https://wiki.genexus.com/commwiki/wiki?5948) that will be placed on the dark hero images you define a class named H1\_Negative, where you declare the following properties defined by the designer:

```
.H1_Negative {
      color: rgb(255,255,255);
      font-family: AbhayaLibre-Bold;
      font-size: 95px;
      font-weight: bold;
      letter-spacing: -1.72px;
      line-height: 75px;
      text-align: center;
}
```

It will be enough to associate it with the control in its Class property (both statically, as shown in the image, and dynamically):

`[imagen omitida: wiki id 48608]`

Then to all other controls that meet that conceptualization: being a main title on a dark background.

Thus, the particular characteristics of a certain control, such as Caption, are separated from those that belong to the design and can be shared with other controls. Some are attached to the control, and the others are separated because they are defined in its class (below you will see in which centralized place it is declared, but we can already anticipate that it will be the [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375)).

Later on, if the designer changes his or her mind and tells you to change the font color, size, or family of the texts used on the hero images, you will only have to change them in one place: the class. This change will affect all the controls associated with it. At the control level, you only have to associate the classes, and that’s the abstraction. Also, the class defines the particular values of its properties.

All this can be thought of as similar to what happens with the HTML elements of a page, and their classes defined in the CSS.

Where are all these classes declared?

To define all the [Classes](https://wiki.genexus.com/commwiki/wiki?49309) that will be used to style the controls of your application, you can use the [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375).

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See Also](#See+Also)

[Design System Object - Declaring the classes of the application's Design System](https://wiki.genexus.com/commwiki/wiki?48687)


|  |
| --- |
| **Backlinks** |
| [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |

---
