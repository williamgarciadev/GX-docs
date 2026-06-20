---
title: "BadgeText property"
source_id: 42041
source_url: https://wiki.genexus.com/commwiki/wiki?42041
genexus_version: "18"
---

# BadgeText property

This property sets a Badge text into controls in an application for Smart Devices. Badges texts usually include additional information into the action icons or button, i.e., in a shopping cart icon, displays how many products have been purchased so far.

### [Syntax](#Syntax)

**control**.BadgeText = Expression

**Where**:  
*Control*  
    Is the name of  a control inserted in the Application Bar

*Expression*  
    Is the text that will be displayed.

### [Description](#Description)

The assigned values will be displayed in the top-right corner of the control. For iOS applications, the property can be set for Buttons and Action Groups controls, in Android is only available for Buttons.

In order to reset the Badge value in the control, an empty text value must be assigned.

### [Run-time/Design-time](#Run-time%2FDesign-time)

This property applies only at run-time.

### [Samples](#Samples)

```
Button.BadgeText = !"1"
ActionGroup.BadgeText = "New"
Button.BadgeText = !"" // Reset badge
```

### [Scope](#Scope)

**Objects**: Panel for Smart Devices, Work With for Smart Devices  
**Platform**: Mobile (iOS, Android)  
**Controls**: Button, Action Group (only in iOS)


|  |
| --- |
| **Backlinks** |
| [Action Group Control for Panels](https://wiki.genexus.com/commwiki/wiki?25106) | [Button control](https://wiki.genexus.com/commwiki/wiki?6011) |

---
