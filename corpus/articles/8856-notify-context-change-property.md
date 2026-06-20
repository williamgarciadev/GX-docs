---
title: "Notify Context Change property"
source_id: 8856
source_url: https://wiki.genexus.com/commwiki/wiki?8856
genexus_version: "18"
---

# Notify Context Change property

Saves the control context by default with the corresponding information.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Controls:** Attribute/Variable, [Grid](https://wiki.genexus.com/commwiki/wiki?24817), [Free Style Grid](https://wiki.genexus.com/commwiki/wiki?6058)

### [Description](#Description)

Default value: False.

Consider a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) with a [Grid](https://wiki.genexus.com/commwiki/wiki?24817). This Grid has the Notify Context Change property = True. What does this mean? It allows you to monitor a change made in a context related to the Grid; that is, if the user selects a line, the application will detect it and save this line selected as context.

`[imagen omitida: wiki id 28524]`

'Context' refers to the specific state or focus within an application's form. When accessing the CustomerId textbox, the context is CustomerId; when accessing the invoice lines Grid, the context is the invoice line, and so on.

When moving inside a screen, the context of attributes and variables changes. Understanding these context changes is essential for creating an intent-oriented interface.

This approach allows for the triggering of events and the execution of actions based on the context information of the application; more specifically, where the cursor is positioned.

This is why it is said that the [User Interface (UI) is context-sensitive](https://wiki.genexus.com/commwiki/wiki?5285): it gives more power to the final applications.

For attributes and variables, it only applies to non-read-only fields (with these possible controls: Combo Box, Radio Button, Edit, Check Box, [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598), List Box, Dynamic List Box). When the Attribute/Variable gets the focus, the context is saved with that information. Value changes in the Attribute/Variable are not detected, only the cursor's focus on it. The same happens for attributes or variables in [Free Style Grids](https://wiki.genexus.com/commwiki/wiki?6058).

In the case of a standard Grid:

* By selecting a row, the entire row is saved in the context.

In the case of standard/Free Style Grids:

* For Grids bound to SDT collections, by selecting the Grid title all the Grid information is tracked in the context.

The information tracked can be changed by programming the SetContext event.

*Note*: This property is not available when the attribute is a formula.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies both at runtime and at design time.

### [See Also](#See+Also)

[Context Sensitive User Interfaces](https://wiki.genexus.com/commwiki/wiki?5285)


|  |
| --- |
| **Backlinks** |
| [Attribute/Variable control properties in Web Forms](https://wiki.genexus.com/commwiki/wiki?8133) | [Free Style Grid Properties](https://wiki.genexus.com/commwiki/wiki?9760) |

---
