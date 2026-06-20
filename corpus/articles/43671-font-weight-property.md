---
title: "font-weight property"
source_id: 43671
source_url: https://wiki.genexus.com/commwiki/wiki?43671
genexus_version: "18"
---

# font-weight property

Sets how thick or thin characters in text will be displayed.

### [Values](#Values)

|  |  |
| --- | --- |
|  | Property not set. |
| **900 (black)** | Text characters will be displayed in black color. |
| **700 (bold)** | Text characters will be displayed in bold. |
| **800 (extraBold)** | Text characters will be displayed in extra bold. |
| **200 (extraLight)** | Text characters will be displayed with extra light thickness. |
| **300 (light)** | Text characters will be displayed with light thickness. |
| **500 (medium)** | Text characters will be displayed with medium thickness. |
| **400 (normal)** | Text characters will be displayed with normal thickness. |
| **600 (semiBold)** | Text characters will be displayed in semi bold. |
| **100 (thin)** | Text characters will be displayed with thin thickness. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Suppose your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is named "BillingSystem", and therefore a predefined [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) is created with the same name.

Below is shown the default **Styles tab** of your "BillingSystem" Design System object:

```
styles BillingSystem {
@import GeneXusUnanimo.UnanimoWeb;
}
```

There you can define, for example, a class named .TextBlock and set its "font-weight" property as follows:

```
styles BillingSystem {
@import GeneXusUnanimo.UnanimoWeb;
    .TextBlock 
    {
      font-weight: medium;
    }
}
```

In this case, the font-weight property is defined with medium value (500).  
  
Remember that you can also set the desired value using the Properties Editor window:

`[imagen omitida: wiki id 56445]`

**Note**: You can set the property to 500 (instead of medium).

Finally, you can create a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) and include a Text Block with text in its Layout.  
Check that the Text Block **class property** is set to .TextBlock.

Build the Panel and run it. The thickness of the characters will be medium.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241) |

---
