---
title: "Overflow Behavior property"
source_id: 46288
source_url: https://wiki.genexus.com/commwiki/wiki?46288
genexus_version: "18"
---

# Overflow Behavior property

Determines whether a control has a scroll or not when setting Auto Grow Property = false.

### [Values](#Values)

|  |  |
| --- | --- |
| **Add Scroll** | The table provides scrollable behavior. When the table height exceeds the space available, a scroll bar is shown. |
| **Clip Content** | The table doesn't provide scroll in any case; content is clipped at the bottom. |
| **Platform Default** | Default value. The platform default value is used: iOS will use Add Scroll and Android Clip Content. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Table](https://wiki.genexus.com/commwiki/wiki?6001)

### [Description](#Description)

The use of Scroll is recommended only when you know it will be necessary.

The support for nested scrolls has more limitations on Android than on iOS (due to the platform's internal limitations), so it is advisable to test your layouts in more detail in Android -when using this property- to avoid possible differences in behavior.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [Availability](#Availability)

This property is available since [GeneXus 17](https://wiki.genexus.com/commwiki/wiki?46066,,).


|  |
| --- |
| **Backlinks** |
| [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [gx-overflow-style property](https://wiki.genexus.com/commwiki/wiki?51796) |

---
