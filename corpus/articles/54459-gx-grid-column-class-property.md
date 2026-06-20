---
title: "gx-grid-column-class property"
source_id: 54459
source_url: https://wiki.genexus.com/commwiki/wiki?54459
genexus_version: "18"
---

# gx-grid-column-class property

Sets the class that styles all the Grid's / Tabular Grid's columns.

### [Scope](#Scope)

**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

You have to configure this property in the [Styles](https://wiki.genexus.com/commwiki/wiki?47379) tab of a [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) with a class defined by you.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Suppose your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is named "KBTest", and therefore a predefined [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) is created with the same name.

In the Styles tab of your "KBTest" Design System object, you define a class named .GridProduct.

```
styles KBTest {
@import GeneXusUnanimo.UnanimoWeb;
.GridProduct
    {
     gx-grid-column-class: GridProductColumn;
    }
.GridProductColumn 
    {
     background-color: #0F0;
    }
}
```

For the .GridProduct class, you have to configure the **gx-grid-column-class** property with a class defined by you. So, for example, define the .GridProductColumn class, set its background-color property to a specific color, and finally assign the .GridProductColumn class to the **gx-grid-column-class** property as explained before.

Finally, to add style to an entire Grid (included in a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)) or an entire [Tabular Grid](https://wiki.genexus.com/commwiki/wiki?54449) (included in a [Panel](https://wiki.genexus.com/commwiki/wiki?24829)), you have to assign the .GridProduct class to the Class propertyof the control you are working with.

The following image shows a Web Panel Grid with its Class property set to .GridProduct:

`[imagen omitida: wiki id 55783]`

When you run the Web Panel, its entire Grid is shown as follows:

`[imagen omitida: wiki id 55784]`

### [Compatibility](#Compatibility)

Angular supports the Tabular Grid as from GeneXus 18 Upgrade 3. Therefore, this property is available for Angular as from the same version.

### [See Also](#See+Also)

[DSO properties that begin with gx- and end with class](https://wiki.genexus.com/commwiki/wiki?55707)


|  |
| --- |
| **Backlinks** |
| [Column Class property in Grid and Tabular Grid](https://wiki.genexus.com/commwiki/wiki?24908) | [Column Class property in Theme Class (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54472) | [Tabular Grid control](https://wiki.genexus.com/commwiki/wiki?54449) |

---
