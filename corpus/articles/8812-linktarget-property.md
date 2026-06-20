---
title: "LinkTarget property"
source_id: 8812
source_url: https://wiki.genexus.com/commwiki/wiki?8812
genexus_version: "18"
---

# LinkTarget property

Establishes the window (or instance) of the Browser in which a Link will be shown when it is selected (associated with the Link property of the control).

### [Scope](#Scope)

**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), .NET, [.NET Core](https://wiki.genexus.com/commwiki/wiki?38604)  
**Controls:** Attribute/Variable, [Text Block](https://wiki.genexus.com/commwiki/wiki?5948), [Image](https://wiki.genexus.com/commwiki/wiki?5939)

### [Description](#Description)

It is oriented to the management of Frames and/or the Browser's windows and makes sense when the control's Link property has a value that is different from the empty string.

All the links that have their LinkTarget with the same value will be shown in the same window (or instance), except for the '\_blank' value of the LinkTarget property. This is a special value that forces the Browser to create a new window or tab (depending on the browser you are using and how it is configured) each time that a Link is selected.

#### [Notes:](#Notes%3A)

* This property applies only at execution time and its value is case-sensitive.
* This property is available for variables based on the [Bitmap data type](https://wiki.genexus.com/commwiki/wiki?7701,,), attributes based on the [Blob data type](https://wiki.genexus.com/commwiki/wiki?6704), [Text Block controls](https://wiki.genexus.com/commwiki/wiki?5948) and [Image controls](https://wiki.genexus.com/commwiki/wiki?5939).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at run-time.

### [See Also](#See+Also)

[Link property](https://wiki.genexus.com/commwiki/wiki?8811)


|  |
| --- |
| **Backlinks** |
| [Link property](https://wiki.genexus.com/commwiki/wiki?8811) |

---
