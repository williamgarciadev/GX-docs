---
title: "text-transform property"
source_id: 40682
source_url: https://wiki.genexus.com/commwiki/wiki?40682
genexus_version: "18"
---

# text-transform property

Shows text in All Caps.

### [Values](#Values)

|  |
| --- |
| **none** |
| **uppercase** |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

It sets whether the text is shown using all capital letters or not. Therefore, when the property is set to "uppercase", all letters are capitalized, and when the property is set to "none", the text appears as it was written or stored.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) that contains a button with its [Caption property](https://wiki.genexus.com/commwiki/wiki?4633) = “All Caps”.

The button [Class property](https://wiki.genexus.com/commwiki/wiki?8741) is set to a certain [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) class (Button).

`[imagen omitida: wiki id 56519]`

Suppose your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is named "BillingSystem". Therefore, a predefined Design System object (DSO) is created with the same name.

The Styles tab of the "BillingSystem" DSO contains code as follows:

```
styles BillingSystem {
@import GeneXusUnanimo.UnanimoWeb;
}
```

Define there a class named "Button" with its text-transform property set to uppercase.

```
styles BillingSystem {
@import GeneXusUnanimo.UnanimoWeb;
   .Button
    {
        text-transform: uppercase;
    }
}
```

Build the Panel and run it to see the button's caption shown in capital letters.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).


|  |
| --- |
| **Backlinks** |
| [Font All Caps property (GeneXus 18 Upgrade 6 or prior)](https://wiki.genexus.com/commwiki/wiki?56518) | [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241) |

---
