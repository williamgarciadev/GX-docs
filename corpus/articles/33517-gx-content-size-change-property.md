---
title: "gx-content-size-change property"
source_id: 33517
source_url: https://wiki.genexus.com/commwiki/wiki?33517
genexus_version: "18"
---

# gx-content-size-change property

Controls the behavior of the Form's layout when the virtual keyboard is displayed in the app, by maintaining the previous Form dimensions or by adapting the Form to the newly available space.

### [Values](#Values)

|  |  |
| --- | --- |
| **Default** | In Apple, it behaves as Resize. In Android, it behaves as Resize if there are no scrollable components on screen; otherwise, it behaves as Scroll. |
| **Resize** | Resizes the screen content as the keyboard appears and disappears. |
| **Scroll** | Adds scroll to the content to display the keyboard without resizing the elements on the screen. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** [Design System Style Class](https://wiki.genexus.com/commwiki/wiki?49309)

### [Description](#Description)

When the virtual keyboard appears on the screen, the space available for on-screen controls changes. In this case, there are two possible options:

* Change the screen size according to the space left available by the keyboard (Resize option), or
* Keep the screen size unchanged and add a scroll bar to access the content behind the keyboard (Scroll option).

Note that this only affects those Rows in the Layout with a height expressed as a percentage. If the row height is expressed in device-independent pixels (dips), the space available for that control does not change.

Also, note that even when the Resize option is selected, it is possible that showing the virtual keyboard will add a scroll. This can happen when the sum of the fixed-size rows is greater than the space left available by the keyboard (or there is a control with Auto Grow).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See Also](#See+Also)

[Design System Object](https://wiki.genexus.com/commwiki/wiki?47375)


|  |
| --- |
| **Backlinks** |
| [Form theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?37648) |

---
