---
title: "Invisible Mode property"
source_id: 22743
source_url: https://wiki.genexus.com/commwiki/wiki?22743
genexus_version: "18"
---

# Invisible Mode property

Applies to controls displayed on layouts of [Smart Devices object](https://wiki.genexus.com/commwiki/wiki?20087)s. The property specifies whether the control occupies space or not when its [Visible property](https://wiki.genexus.com/commwiki/wiki?8849) is set to false.

### [Scenarios](#Scenarios)

There is a need to provide a more beautiful and polished UX on Smart Device's apps. GeneXus is adding flexibility and power to the developer to do more dynamic screens, adapt to all states of the application, and do better UI being able to customize more elements.

This property enables the developer to add hidden information on the screen that does not occupy space and when the user triggers an event it can make this hidden info appear and disappear moving the rest of the elements so the UI keeps looking good.

### [Values](#Values)

|  |  |
| --- | --- |
| **Keep Space** | The layout maintains the control's space even though the control is not visible. This is the default value. |
| **Collapse Space** | The layout collapses the space, letting other controls use the space. Also, when the [Animated property](https://wiki.genexus.com/commwiki/wiki?34111) is enabled at theme level, there will be a smooth(1) transition between the both states (visible and invisible, and vice versa).  ***Note:*** (1) Available as of [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?33798,,)    (2)This "Collapse Space" option only works for collapsing row information (horizontal collapse), not column (vertical collapse). |

### [Description](#Description)

When a control is not visible there can be two possible behaviors. One is to reserve the space that the control should occupy even though it is not visible and the second is when other controls of the layout can copy the space of a control that is not visible.

### [[How to Apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+Apply+changes)

The object has to be built.

### [Example](#Example)

You can see a working example on [this sample](https://wiki.genexus.com/commwiki/wiki?21779,,).

Or you can follow the steps of the following [HowTo document.](https://wiki.genexus.com/commwiki/wiki?22838)

### [Availability](#Availability)

[GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?33798,,)


|  |
| --- |
| **Backlinks** |
| [Animated property](https://wiki.genexus.com/commwiki/wiki?34111) | [Animation Duration property (for Animation Theme class)](https://wiki.genexus.com/commwiki/wiki?34112) |
| [HowTo: Use the Invisible Mode property](https://wiki.genexus.com/commwiki/wiki?22838) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
