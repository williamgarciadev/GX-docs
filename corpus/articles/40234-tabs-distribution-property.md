---
title: "Tabs Distribution property"
source_id: 40234
source_url: https://wiki.genexus.com/commwiki/wiki?40234
genexus_version: "18"
---

# Tabs Distribution property

Defines how the tabs will be distributed in the container.

### [Values](#Values)

|  |  |
| --- | --- |
| **Fixed Size** | Tabs are fixed size, used when the control has at most four tabs. |
| **Platform Default** | Scroll for Android when there isn’t enough space, and Fixed for iOS. |
| **Scroll** | Allows scrolling the tab control when the number of tabs exceeds the screen width. |

### [Scope](#Scope)

**Objects:** Panel for Smart Devices  
**Platforms:** Smart Devices(Android, IOS)

### [Description](#Description)

Defines how the tab controls will be distributed within the container.

According to the standards, it means *Scroll* for Android when it does not have space, and *Fixed* for iOS.

The *Fixed* value is used when the control has few tabs (at most four). On the other hand, the *Scroll* value allows scrolling the tab control when the number of tabs exceeds the screen width.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a Build with this Only of the object.

### [See Also](#See+Also)

[Tab control for Panels](https://wiki.genexus.com/commwiki/wiki?29986)


|  |
| --- |
| **Backlinks** |
| [Tab control for Panels](https://wiki.genexus.com/commwiki/wiki?29986) |

---
