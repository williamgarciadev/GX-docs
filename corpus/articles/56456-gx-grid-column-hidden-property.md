---
title: "gx-grid-column-hidden property"
source_id: 56456
source_url: https://wiki.genexus.com/commwiki/wiki?56456
genexus_version: "18"
---

# gx-grid-column-hidden property

Indicates whether the column is hidden or not (for example, depending on screen size or other conditions). In addition, the end user can hide/show the column at runtime.

### [Values](#Values)

|  |
| --- |
| **True** |
| **False** |

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

The behavior of this property is equivalent to the [Column Hidden property for Tabular Grid Columns](https://wiki.genexus.com/commwiki/wiki?55816). However, when using the **gx-grid-column-hidden property**, you have the advantage of being able to show/hide a column based on a certain condition.

So, if you do not have to consider conditions to show/hide a column, configure the [Column Hidden property for Tabular Grid Columns](https://wiki.genexus.com/commwiki/wiki?55816). Otherwise, solve it using a [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) and the **gx-grid-column-hidden property**.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Suppose your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is named "BillingSystem", and therefore a predefined [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) is created with the same name.

Below is the default **Styles tab** of the "BillingSystem" Design System object:

```
styles BillingSystem {
@import GeneXusUnanimo.UnanimoWeb;
}
```

There you can define, for example, a class named .GridColumnHidden and set its "gx-grid-column-hidden" property as follows:

```
styles BillingSystem {
@import GeneXusUnanimo.UnanimoWeb;
     .GridColumnHidden {
        gx-grid-column-hidden: false;
    }

    @media (max-width: 960px) {
        .GridColumnHidden {
            gx-grid-column-hidden: true;
        }
    }
}
```

Note that by using the [media rule](https://wiki.genexus.com/commwiki/wiki?49344) you define that if the screen size is smaller than 960 px the column is hidden.  
  
Finally, you can create a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) and include a [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) in its Layout.

`[imagen omitida: wiki id 56455]`

Click on the CustomerId column. Check that its [Column Class property](https://wiki.genexus.com/commwiki/wiki?24908) is set to .GridColumnHidden.

Build the Panel and run it. The CustomerId column will be hidden in the Tabular Grid, but the end user will be able to show it from the Tabular Grid configuration using the "Settings" button at runtime.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241) |

---
