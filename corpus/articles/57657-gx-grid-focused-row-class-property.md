---
title: "gx-grid-focused-row-class property"
source_id: 57657
source_url: https://wiki.genexus.com/commwiki/wiki?57657
genexus_version: "18"
---

# gx-grid-focused-row-class property

Applies a style to a focused row while navigating a Tabular Grid using the keyboard.

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Samples](#Samples)

Suppose your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is named "KBTest", and therefore a predefined [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) (DSO) is created with the same name.

In the Styles tab of your "KBTest" DSO, you define the following classes:

```
styles KBTest
{
    .Grid {
        gx-grid-row-class:GridRow;
        gx-grid-selected-row-class: GridRowSelected;
        gx-grid-hover-row-class: GridRowHover;
        gx-grid-focused-row-class: GridRowFocused;
    }
    .GridRow {
        padding: 5px;
        border: 1px solid transparent;
    }
    .GridRowSelected {
        background-color: #32CD32;
    }
    .GridRowHover {
        background-color: #30CCC1;
    }
    .GridRowFocused {
        border: 1px dotted red;
    }
}
```

Note the **gx-grid-focused-row-class property** configured inside the Grid class. It is set to the **GridRowFocused** class defined by you (which has its border property set to a specific style).

**Note:** Make sure that in **KB Explorer > Customization > Platforms > Any Web Screen**, the [Style property](https://wiki.genexus.com/commwiki/wiki?43966) is set to the KBTestDSO [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375).

Create a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) (named KBTestPanel) with its [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) set to True.  
Next, drag a [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449) to its Layout and include inside it, for example, the CustomerName attribute to query all the customer names.

`[imagen omitida: wiki id 57702]`

When running the KBTestPanel, the behavior will be as follows:

`[imagen omitida: wiki id 57703]`

The currently selected row is highlighted in green. On the other hand, while you navigate through the rows using the keyboard, the focused row is underlined by a border style defined as 1px dotted red (because you gave it that style when setting the **gx-grid-focused-row-class property** for the Grid class of the DSO).

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243).

### [See Also](#See+Also)

[gx-grid-row-class property](https://wiki.genexus.com/commwiki/wiki?32772)  
[gx-grid-selected-row-class property](https://wiki.genexus.com/commwiki/wiki?54462)  
[gx-grid-hover-row-class property](https://wiki.genexus.com/commwiki/wiki?54463)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?54243) | [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) |

---
