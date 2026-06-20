---
title: "Enter Key Behavior"
source_id: 6761
source_url: https://wiki.genexus.com/commwiki/wiki?6761
genexus_version: "18"
---

# Enter Key Behavior

The following describes the effect of pressing the Enter key.

1. If the Enter event exists but is not associated to any web control in the form, the effect of pressing the Enter key is that the Enter Event will be executed.
2. If the Enter event exists and is associated to a control in the form, the effect of pressing the Enter key when the focus is on a control with no event associated to it, or the focus isn't on any control, is that the Enter Event is executed.
3. If the Enter event exists and is associated to a control in the form, the effect of pressing the Enter key when the focus is on a control with another event associated to it ('x' Event), is that the X Event is executed.

If you have a grid and filters associated to conditions in the grid, the effect of pressing the Enter key immediately after entering any filter is explained in the following document:

[Enter Key behavior when entering grid filters](https://wiki.genexus.com/commwiki/wiki?6760).


|  |
| --- |
| **Backlinks** |
| [Refresh Behavior in grids](https://wiki.genexus.com/commwiki/wiki?6760) |

---
