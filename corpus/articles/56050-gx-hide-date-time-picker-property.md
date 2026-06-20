---
title: "gx-hide-date-time-picker property"
source_id: 56050
source_url: https://wiki.genexus.com/commwiki/wiki?56050
genexus_version: "18"
---

# gx-hide-date-time-picker property

Shows or hides a picker icon for the Date / DateTime control.

### [Values](#Values)

|  |
| --- |
| **True** |
| **False** |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

Consider a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) that contains a &DateOfBirth variable.

By default, a date picker for the Date or DateTime field will be displayed at runtime:

`[imagen omitida: wiki id 56290]`

The &DateOfBirth variable class property is set to a certain [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) class.

To hide the icon, in the [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) class assigned to the &DateOfBirth variable, configure its gx-hide-date-time-picker property = True.

Suppose your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is named "BillingSystem". Therefore, a predefined Design System object is created with the same name.

The Style tab of the "BillingSystem" Design System object contains the following code:

```
styles BillingSystem {
@import GeneXusUnanimo.UnanimoWeb;
}
```

Define there a class named "YourProfile" with its "gx-hide-date-time-picker" property set to True.

```
styles BillingSystem {
@import GeneXusUnanimo.UnanimoWeb;
   .YourProfile
    {
        gx-hide-date-time-picker: True;
    }
}
```

Check that the &DateOfBirth variable class property is set to .YourProfile.

Build the Panel and run it; after that, the icon for the Date field should no longer be displayed.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).
