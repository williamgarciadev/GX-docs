---
title: "Design System Object - Untyped classes"
source_id: 48689
source_url: https://wiki.genexus.com/commwiki/wiki?48689
genexus_version: "18"
---

# Design System Object - Untyped classes

[Classes](https://wiki.genexus.com/commwiki/wiki?49309) are not restricted to be applied to a single type of control. They can be applied to any type. Of course, depending on the type of control, some class properties may be meaningless, and therefore they will have no effect on it.

In the example, it will make sense to assign the class H1\_Negative to any control containing text, without requiring it to be a [Text Block control](https://wiki.genexus.com/commwiki/wiki?5948). For example, it could be a [control of Variable or Attribute](https://wiki.genexus.com/commwiki/wiki?8133) type, or it could also be applied to control labels, column headings, and so on.

Thus, if in another Panel you use a Variable for the text on the hero image instead of the Text Block, or an Attribute (since its content will be searched for in the database), there is no difference: the Attribute/Variable control is associated with the same class, H1\_Negative, as the Text Block.

`[imagen omitida: wiki id 48612]`

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).


|  |
| --- |
| **Backlinks** |
| [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |

---
